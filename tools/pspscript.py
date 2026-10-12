"""PSP-script variant: the English of the official PSP release (Shin Megami Tensei: Persona, ULUS10432) in place of
the project's own translation, for the story events (ADV/E0..E3.BIN) and the demon negotiations (TALK/*.BIN).

The repository holds no PSP text: it is read from the user's own PSP ISO at build time (build.py --psp ISO).

  python tools/pspscript.py extract ISO        pack/E0..E3.BIN + pack/talk/*.BIN of the PSP ISO -> original_psp/
  python tools/pspscript.py convert            -> psp_text/events/E?.tsv, psp_text/talk/*.tsv, psp_text/report.tsv
  python tools/pspscript.py show E0 77         the PSP boxes of one entry (debug)

PSP formats (same engine family as the PS1 game):
  E?.BIN   u32[512] (start, end) byte pairs per entry, 224/224/240/128 entries like the PS1 files. Text is a stream of
           big-endian u16 words: glyph codes (table CHARS) or FFxx control codes; FF05/FF06/FF0E/FF18/FF19/FF1A carry
           one parameter word. A box ends with FF01, pages with FF02 FF04, lines with FF03. FF1B name FF03 = nameplate
           (the PS1 text writes "Name: " instead). FF07/FF08/FF0F = player name (no parameter on the PSP).
  talk     header u32[6] ([0]=0x18), unit table at 0x18, text pool; same unit count as the PS1 files. Byte stream:
           FF xx control (FFFD + 1 parameter byte), otherwise a 2-byte big-endian glyph. FF03 = new line.

convert keeps the control-code skeleton of the Japanese PS1 box (pauses, name tokens, choices, profile styles) and
fills it with the PSP wording, re-wrapped to the PS1 box (239 px, 3 lines a page). A box / unit that cannot be
converted or fails the normal QA (tstatus.check / talktl.check) keeps the project's own English; every case is
listed in psp_text/report.tsv.
"""
import collections
import glob
import os
import re
import struct
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import etext      # noqa: E402
import tl_lib     # noqa: E402
import vwf_wrap   # noqa: E402

ROOT = etext.ROOT
SRC = os.environ.get('PERSONA_PSP_FILES') or os.path.join(ROOT, 'original_psp')     # extracted PSP files
OUT = os.environ.get('PERSONA_PSP_TEXT') or os.path.join(ROOT, 'psp_text')          # converted tables
TAB, NL = chr(9), chr(10)

# 0x43 / 0x44 frame headings ("[During play]") and start the profile cards ("] Masao Inaba ..."; dropped in
# psp_pages); 0x02 is a stray Japanese full stop. Not mapped on purpose (the box keeps the project's English):
# button icons 0x39 0x3A 0x3E 0x5B 0x60 0x62, card suits 0x204-0x207, yen 0x4F, kana / kanji.
CHARS = {0x00: ' ', 0x02: '', 0x03: ',', 0x04: '.', 0x06: ':', 0x07: ';', 0x08: '?', 0x09: '!', 0x1E: '/',
         0x26: "'", 0x28: '"', 0x29: '(', 0x2A: ')', 0x3C: '-', 0x43: '[', 0x44: ']', 0x53: '%', 0x54: '#',
         0x55: '&', 0x56: '*'}
CHARS.update({0xE0 + i: chr(65 + i) for i in range(26)})
CHARS.update({0x101 + i: chr(97 + i) for i in range(26)})
CHARS.update({0xCF + i: chr(48 + i) for i in range(10)})


# ---------------------------------------------------------------- ISO
def iso_files(iso):
    """{path: (lba, size)} of an ISO9660 image (2048-byte sectors)."""
    f = open(iso, 'rb')

    def rd(lba, n):
        f.seek(lba * 2048)
        return f.read(n)
    out = {}

    def walk(lba, size, path):
        d, i = rd(lba, size), 0
        while i < len(d):
            n = d[i]
            if n == 0:
                i = (i // 2048 + 1) * 2048
                continue
            rec = d[i:i + n]
            i += n
            name = rec[33:33 + rec[32]]
            if name in (b'\0', b'\1'):
                continue
            p = path + '/' + name.decode('ascii', 'replace').split(';')[0]
            elba, esz = struct.unpack_from('<I', rec, 2)[0], struct.unpack_from('<I', rec, 10)[0]
            if rec[25] & 2:
                walk(elba, esz, p)
            else:
                out[p] = (elba, esz)
    root = rd(16, 2048)[156:190]
    walk(struct.unpack_from('<I', root, 2)[0], struct.unpack_from('<I', root, 10)[0], '')
    return out, f


def cmd_extract(iso):
    files, f = iso_files(iso)
    if '/UMD_DATA.BIN' not in files or '/PSP_GAME/USRDIR/pack/E0.BIN' not in files:
        raise SystemExit(f'{iso}: not the PSP Shin Megami Tensei: Persona ISO')
    n = 0
    for p, (lba, size) in files.items():
        m = re.match(r'/PSP_GAME/USRDIR/pack/(E[0-3]\.BIN|talk/\w+\.BIN)$', p)
        if m:
            dst = os.path.join(SRC, *m.group(1).split('/'))
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            f.seek(lba * 2048)
            open(dst, 'wb').write(f.read(size))
            n += 1
    print(f'{n} PSP files -> {SRC}')


# ---------------------------------------------------------------- PSP events
E_PARAM = {0xFF05, 0xFF06, 0xFF0E, 0xFF18, 0xFF19, 0xFF1A}


def e_entries(name):
    d = open(os.path.join(SRC, name + '.BIN'), 'rb').read()
    w = struct.unpack_from('<512I', d, 0)
    out = []
    for i in range(0, 512, 2):
        if w[i] == 0 and w[i + 1] == 0:
            break
        out.append(d[w[i]:w[i + 1]])
    return out


def e_boxes(b):
    """[(offset, [words])] of the text boxes of a PSP entry (runs of text tokens ending with FF01)."""
    n = len(b) // 2
    w = struct.unpack('>%dH' % n, b[:n * 2])
    res, start, i = [], None, 0
    while i < n:
        v = w[i]
        if v < 0x0800 or 0xFF01 <= v <= 0xFF1F:
            if start is None:
                start = i
            if v in E_PARAM:
                i += 1
            elif v == 0xFF01:
                k = start                   # skip padding and stray command words before the text
                while k < i and w[k] < 0xFF00 and (w[k] == 0 or w[k] not in CHARS):
                    k += 1
                box = list(w[k:i + 1])
                if any(x not in (0, 0xFF02, 0xFF03, 0xFF04, 0xFF01) and x < 0xFF00 for x in box):
                    res.append((k * 2, box))
                start = None
        else:
            start = None
        i += 1
    return res


def e_show(words):
    out, i = [], 0
    while i < len(words):
        v = words[i]
        if v >= 0xFF00:
            out.append(f'<{v:04X}>')
            if v in E_PARAM and i + 1 < len(words):
                i += 1
                out.append(f'[{words[i]:04X}]')
        else:
            out.append(CHARS.get(v, f'{{{v:X}}}'))
        i += 1
    return ''.join(out)


# ---------------------------------------------------------------- conversion helpers
NAME_OPS, PAUSE, STYLE, CHOICE, VALUE = {0x07, 0x08, 0x0F}, 0x05, 0x06, 0x0E, {0x11, 0x12}
NAME_PH, PAUSE_PH, VALUE_PH = '\x01', '\x02', '\x03'
LINE = '\x07'            # a PSP line break inside a page


class Fail(Exception):
    pass


class ExtraPage(Exception):
    """a converted talk unit that needs more pages than the Japanese (args[0] = the English)"""


EXTRA_PAGES = True


def tok(op, params):
    """PS1 text form of a control code with its parameter bytes (name tokens as <FF0F>あ for the width table)."""
    t = etext.decode(bytes((0xFF, op)) + params) if op in NAME_OPS else \
        f'<FF{op:02X}>' + ''.join(f'<{b:02X}>' for b in params)
    return t


def psp_pages(words):
    """PSP box -> (pages [(speaker, text with placeholders)], counts {kind: n}, choice?, name codes in order)"""
    pages, spk, cur = [], '', []
    counts = collections.Counter()
    name_ops = []
    choice = False
    i = 0
    while i < len(words):
        v = words[i]
        if v < 0xFF00:
            c = CHARS.get(v)
            if c is None:
                raise Fail(f'glyph {v:04X}')
            cur.append(c)
        elif v == 0xFF1B:                                   # nameplate: FF1B name FF03
            j = i + 1
            nm = []
            while j < len(words) and words[j] != 0xFF03:
                if words[j] - 0xFF00 in NAME_OPS:          # "<player>'s voice"
                    nm.append(NAME_PH)
                    counts['name'] += 1
                    name_ops.append(words[j] - 0xFF00)
                    j += 1
                    continue
                c = CHARS.get(words[j])
                if c is None:
                    raise Fail(f'name glyph {words[j]:04X}')
                nm.append(c)
                j += 1
            spk = ''.join(nm).strip()
            i = j
        elif v == 0xFF03:
            if not (len(cur) > 1 and cur[-1] == '-' and cur[-2].isalpha()):   # "part-<br>time" stays one word
                cur.append(LINE)                              # a space, except under a heading card's title
        elif v in (0xFF02, 0xFF04, 0xFF01):
            if v == 0xFF04 or (v == 0xFF01 and ''.join(cur).strip()) or (v == 0xFF02 and i + 1 < len(words) and words[i + 1] != 0xFF04):
                if ''.join(cur).strip():
                    pages.append((spk, ''.join(cur)))
                cur, spk = [], ''
        elif v - 0xFF00 in NAME_OPS:
            cur.append(NAME_PH)
            counts['name'] += 1
            name_ops.append(v - 0xFF00)
        elif v == 0xFF05:
            cur.append(PAUSE_PH)
            counts['pause'] += 1
            i += 1
        elif v - 0xFF00 in VALUE:
            cur.append(VALUE_PH)
            counts['value'] += 1
        elif v == 0xFF0E:
            choice = True
            i += 1
        elif v in E_PARAM:                                 # FF06 style, FF18/19/1A colour: the PS1 codes come from the Japanese
            i += 1
        else:
            raise Fail(f'code {v:04X}')
        i += 1
    if ''.join(cur).strip():
        pages.append((spk, ''.join(cur)))
    clean = []
    for s, t in pages:
        t = re.sub(' *' + LINE + ' *', LINE, re.sub(r' +', ' ', t)).strip(' ' + LINE)
        t = re.sub(r'^\] ', '', t)                          # profile-card bullet
        t = re.sub(r' ([,.!?])', r'\1', t)
        clean.append((s, t))
    return clean, counts, choice, name_ops


ANCHOR = re.compile(r'<FF0[78F]>.|<FF1[12]>')


def place_by_fraction(text, fracs, token_for, before=None):
    """insert tokens at sentence ends nearest to the given fractions of the text length (pauses).
    before[k] = number of ANCHOR tokens (names / values) that must precede token k (keeps the Japanese code order)."""
    anchors = [(m.start(), m.end()) for m in ANCHOR.finditer(text)]
    sent = [m.end() for m in re.finditer(r'[.!?]+"?(?=[\s\x04]|$)', text)]
    space = [m.start() for m in re.finditer(r'[ \x04]', text)]
    ins = []
    for k, f in enumerate(fracs):
        lo, hi = 0, len(text)
        if before is not None:
            nb = before[k]
            lo = anchors[nb - 1][1] if nb > 0 else 0
            hi = anchors[nb][0] if nb < len(anchors) else len(text)
        target = min(max(f * len(text), lo), hi)
        cands = [b for b in sent if lo <= b <= hi] or [b for b in space if lo <= b <= hi] or [hi]
        ins.append((min(cands, key=lambda b: abs(b - target)), k))
    for pos, k in sorted(ins, key=lambda x: (-x[0], -x[1])):
        text = text[:pos] + token_for(k) + text[pos:]
    return text


def jp_fracs(ja_bytes, op):
    """positions (fraction of displayed text) of every `op` code in an encoded Japanese box."""
    import tstatus
    out, shown, i, b = [], 0, 0, ja_bytes
    total = len(tstatus.text_only(b)) or 1
    while i < len(b):
        c = b[i]
        if c == 0xFF and i + 1 < len(b):
            o = b[i + 1]
            if o == op:
                out.append(shown / total)
            i += 2 + tstatus.PARAM_LEN.get(o, 0)
        elif 0x80 <= c <= 0x87:
            shown += 2
            i += 2
        else:
            shown += 1
            i += 1
    return out


_LOWER = None


def lower_words():
    """every word the PSP event script writes in lowercase (used to tell common words from names)"""
    global _LOWER
    if _LOWER is None:
        _LOWER = set()
        for n in etext.FILES:
            for ent in e_entries(n):
                for off, w in e_boxes(ent):
                    _LOWER.update(re.findall(r"\b[a-z][a-z']*", ''.join(CHARS.get(v, ' ') for v in w if v < 0xFF00)))
    return _LOWER


def convert_box(ja, our, words):
    """PS1 English for one box from the PSP words, or raise Fail."""
    import tstatus
    jb = etext.encode(ja)
    seq = tstatus.code_seq(jb)
    jnames = [(o, p) for o, p in seq if o in NAME_OPS]
    pauses = [tok(o, p) for o, p in seq if o == PAUSE]
    values = [tok(o, p) for o, p in seq if o in VALUE]
    styles = [tok(o, p) for o, p in seq if o == STYLE]
    nchoice = sum(1 for o, p in seq if o == CHOICE)
    pages, counts, choice, name_ops = psp_pages(words)
    # player name: the PSP's choice of name (it often uses the given name where the Japanese uses the family
    # name: FF07 given, FF0F family, FF08 nickname, the same codes on both) with the Japanese parameter byte
    names = [tok(po, p) for po, (o, p) in zip(name_ops, jnames)]
    if not pages or not re.search('[A-Za-z]{2}', ' '.join(t for sp, t in pages)):
        raise Fail('no text')          # e.g. a box the PSP left in Japanese (only punctuation survives)
    if counts['name'] != len(jnames):
        raise Fail(f'name tokens {counts["name"]} vs {len(jnames)}')
    if counts['value'] != len(values):
        raise Fail(f'value tokens {counts["value"]} vs {len(values)}')
    if bool(nchoice) != choice or nchoice > 1:
        raise Fail('choice differs')
    # FF06 = style: either a profile card (first code at the very start of the box: kept there, a closing one goes
    # to the end) or an inline symbol at the end (Ayase's heart: the project's English already has that suffix)
    style_pre, style_suf = '', ''
    if styles:
        if jp_fracs(jb, STYLE)[0] == 0:
            style_pre, style_suf = styles[0], ''.join(styles[1:])
        else:
            m = re.search(r'(<FF06>.*)<FF02>$', our)
            if not m or len(plain(m.group(1))) > 3:
                raise Fail('style pattern')
            style_suf = m.group(1)
    # heading card (profile cards, info cards such as the Hiremon Stone): the first line is a title, not part of a
    # sentence. Both sides must say so: the PSP page starts with its bullet glyph 0x44 and the Japanese box starts
    # with a short line ended by a line break. (The PSP also uses the bullet for plain narration.)
    heading = bool(style_pre) or (0x44 in words[:3] and
                                  re.match(r'(?:<FF06><[0-9A-F]{2}>)?[^<：。、！？]{1,20}<FF03>', etext.decode(jb)) is not None)

    def fill(pause_mode):
        it_n, it_v, it_p = iter(names), iter(values), iter(pauses)
        sub = {NAME_PH: lambda: next(it_n), VALUE_PH: lambda: next(it_v),
               PAUSE_PH: lambda: next(it_p) if pause_mode else ''}
        out = []
        for k, (s, t) in enumerate(pages):
            t = ''.join(sub[c]() if c in sub else c for c in t)
            if heading and k == 0:                     # the title ("Name (Nickname: X)") stays on its own line
                head, sep, rest = t.partition(LINE)
                t = head + sep + rest.replace(LINE, ' ')
            else:
                t = t.replace(LINE, ' ')
            out.append([''.join(sub[c]() if c in sub else c for c in s), t])
        if pauses and not pause_mode:                  # the Japanese pauses at the nearest sentence ends, in code order
            ops = [o for o, p in seq if o in NAME_OPS or o in VALUE or o == PAUSE]
            before = [sum(1 for o in ops[:i] if o != PAUSE) for i, o in enumerate(ops) if o == PAUSE]
            joined = place_by_fraction('\x04'.join(t for s, t in out), jp_fracs(jb, PAUSE), lambda k: pauses[k], before)
            for k, t in enumerate(joined.split('\x04')):
                out[k][1] = t
        return [(f'{s}: ' if s else '') + t for s, t in out]

    tail = None
    if nchoice:
        m = re.search(r'((?:<FF0[234]>)*<FF0E>.*?)(?:<FF01>)?$', our)
        tail = m.group(1) if m else None
        if not tail:
            raise Fail('choice tail')

    def titled(texts):
        """heading card: the title on its own line as on the PSP, or "Title: description" when the own line would
        cost an extra page (the PS1 box is narrower); 3 lines a page. Later PSP pages are wrapped as usual."""
        def paged(lines):
            return ['<FF03>'.join(lines[i:i + 3]) for i in range(0, len(lines), 3)]
        head, _, rest = texts[0].partition(LINE)
        head, rest = head.strip(), rest.strip()
        own = vwf_wrap.wrap(head).split(vwf_wrap.NEWLINE) + (vwf_wrap.wrap(rest).split(vwf_wrap.NEWLINE) if rest else [])
        # inline: "Saeko Takami, homeroom teacher for ..." (a comma, not ':' which would read as speech); the first
        # word is lowercased only when the PSP script uses it in lowercase somewhere (keeps "Kandori's", "St.")
        w = re.match(r"[A-Za-z']+", rest)
        if w and w.group(0).lower() in lower_words() and w.group(0) != 'I':
            rest = rest[0].lower() + rest[1:]
        inline = vwf_wrap.wrap(f'{head}, {rest}' if rest else head).split(vwf_wrap.NEWLINE)
        first = paged(own) if len(paged(own)) <= len(paged(inline)) else paged(inline)
        later = [p for t in texts[1:] for p in paged(vwf_wrap.wrap(t.strip()).split(vwf_wrap.NEWLINE))]
        return '<FF02><FF04>'.join(first + later) + '<FF02>'

    def assemble(texts):
        en = titled(texts) if heading else tl_lib.build(texts)
        if tail and not tail.startswith('<FF02>'):     # the options share the last page: at most 2 text lines there
            last = en[:-len('<FF02>')].split('<FF02><FF04>')
            lines = last[-1].split('<FF03>')
            if len(lines) > 2:
                m = tl_lib._LABEL.match(lines[0])
                last[-1:] = ['<FF03>'.join(lines[:-1]), (m.group(1) if m else '') + lines[-1]]
                en = '<FF02><FF04>'.join(last) + '<FF02>'
        if styles:
            en = style_pre + en[:-len('<FF02>')] + style_suf + '<FF02>'
        if tail:
            en = en + tail[len('<FF02>'):] if tail.startswith('<FF02>') else en[:-len('<FF02>')] + tail
        return en

    err = None
    for mode in ([True, False] if counts['pause'] == len(pauses) else [False]):
        try:
            en = assemble(fill(mode))
        except ValueError as ex:
            err = f'wrap: {ex}'
            continue
        bad = [(k, msg) for k, msg in tstatus.check(ja, en) if k != 'label']
        if not bad:
            return en
        err = 'qa ' + '; '.join(f'[{k}] {msg}' for k, msg in bad)
    raise Fail(err)


# ---------------------------------------------------------------- alignment
def plain(s):
    return re.sub(r'<[^>]+>', '', s)


def spk_of(en):
    m = re.match(r"(?:<FF0[0-9A-F]>(?:<[0-9A-F]{2}>)?)*([A-Z][A-Za-z.' -]{0,30}): ", en)
    return m.group(1).lower() if m else ''


STOP = set('that this with have what your will just there they them then than were been from into about would '
           'could should know like well here when where which while because really right going something '
           'young ones'.split())


def stems(text):
    return {w[:5] for w in re.findall(r'[a-z]{4,}', text.lower())} - {w[:5] for w in STOP}


def psp_sig(words):
    try:
        pages, counts, choice, _ = psp_pages(words)
    except Fail:
        try:
            raw = e_show(words)
        except Exception:
            raw = ''
        return '', 0, '<FF0E>' in raw, 0, stems(re.sub(r'<[^>]+>|\{[^}]+\}|\[[^\]]+\]', ' ', raw))
    spk = pages[0][0].lower() if pages else ''
    body = ' '.join(t for s, t in pages)
    return spk, sum(len(t) for s, t in pages), choice, counts['name'], stems(body)


def align(ours, psp):
    """ours: [(ja, en)], psp: [words] -> {our index: psp index}: Needleman-Wunsch on speaker, choice, name tokens,
    length and shared word stems (the PSP sometimes adds one box and drops another, so equal counts prove nothing)."""
    A = [(spk_of(en), len(plain(en)), '<FF0E>' in en, len(re.findall(r'<FF0[78F]>', en)),
          stems(re.sub(r'(?m)\b[A-Z][\w.\' -]{0,30}: ', ' ', plain(en)))) for ja, en in ours]
    B = [psp_sig(w) for w in psp]

    def sim(a, b):
        s = 0.0
        if a[0] and b[0]:
            s += 2 if (a[0] == b[0] or a[0] in b[0] or b[0] in a[0]) else -0.5
        s += 1.5 if a[2] == b[2] else -2
        s += 1 if a[3] == b[3] else -1
        if a[1] and b[1]:
            r = min(a[1], b[1]) / max(a[1], b[1])
            s += 2 * r - 0.6
        if a[4] and b[4]:
            s += 4 * len(a[4] & b[4]) / min(len(a[4]), len(b[4]))
        return s
    gap = -1.2
    n, m = len(A), len(B)
    D = [[0.0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        D[i][0] = i * gap
    for j in range(1, m + 1):
        D[0][j] = j * gap
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = max(D[i - 1][j - 1] + sim(A[i - 1], B[j - 1]), D[i - 1][j] + gap, D[i][j - 1] + gap)
    res, i, j = {}, n, m
    while i > 0 and j > 0:
        if abs(D[i][j] - (D[i - 1][j - 1] + sim(A[i - 1], B[j - 1]))) < 1e-9:
            res[i - 1] = j - 1
            i, j = i - 1, j - 1
        elif abs(D[i][j] - (D[i - 1][j] + gap)) < 1e-9:
            i -= 1
        else:
            j -= 1
    return res


# ---------------------------------------------------------------- PSP talk
def talk_units(name):
    d = open(os.path.join(SRC, 'talk', name + '.BIN'), 'rb').read()
    h = struct.unpack_from('<6I', d, 0)
    first = struct.unpack_from('<I', d, h[0])[0]
    tab, i = [], h[0]
    while i < first:
        v = struct.unpack_from('<I', d, i)[0]
        if v == 0xFFFFFFFF:
            break
        tab.append(v)
        i += 4
    ends = tab[1:] + [h[1]]
    return [d[s:e] for s, e in zip(tab, ends)]


def talk_tokens(b):
    """[('t', char) | ('c', 'FFxx', param byte or None)] up to and including the first end code."""
    out, i = [], 0
    while i + 1 < len(b):
        if b[i] == 0xFF:
            op = b[i + 1]
            p = None
            if op == 0xFD:
                p = b[i + 2] if i + 2 < len(b) else 0
                i += 1
            out.append(('c', f'<FF{op:02X}>', p))
            i += 2
            if op in (0xF5, 0xEF):
                break
        else:
            v = (b[i] << 8) | b[i + 1]
            c = CHARS.get(v)
            if c is None:
                raise Fail(f'glyph {v:04X}')
            out.append(('t', c, None))
            i += 2
    return out


NBSP = '\x08'           # a space that must not break: "<race> <name>" ("Night Pairika")


def glue(text):
    return text.replace('<FFF0> <FFF3>', '<FFF0>' + NBSP + '<FFF3>')


def wrap_talk(text, maxw):
    """greedy wrap of one page (tokens kept) using talktl.width; -> lines"""
    import talktl
    words, lines, cur = glue(text).split(' '), [], ''
    for w in words:
        cand = (cur + ' ' + w) if cur else w
        if talktl.width(cand.replace(NBSP, ' ')) <= maxw:
            cur = cand
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return [ln.replace(NBSP, ' ') for ln in lines]


PAGE = '<FFFB><FFF7>'
PAGE_MARK = '\x06'


def cut_end(ja):
    cut = [ja.index(c) + 6 for c in ('<FFF5>', '<FFEF>') if c in ja]
    return ja[:min(cut)] if cut else ja


def psp_talk_text(units_b, jfd):
    """PSP unit -> (text with PS1 codes, PAGE_MARK between pages, nameplates as 'Name: '), end code"""
    toks = talk_tokens(units_b)
    s, fd, i = [], iter(jfd), 0
    while i < len(toks):
        t = toks[i]
        if t[0] == 't':
            s.append(t[1])
        elif t[1] in ('<FF03>', '<FFF6>'):
            if not (len(s) > 1 and s[-1] == '-' and s[-2].isalpha()):     # "part-<br>time" stays one word
                s.append(' ')
        elif t[1] in ('<FF02>', '<FF04>', '<FFFB>', '<FFF7>'):
            if not s or s[-1] != PAGE_MARK:
                s.append(PAGE_MARK)
        elif t[1] == '<FF1B>':                            # nameplate (ETC scenes): FF1B name FF03
            j, nm = i + 1, []
            while j < len(toks) and toks[j][1] != '<FF03>':
                nm.append(toks[j][1] if toks[j][0] == 't' else '')
                j += 1
            s.append(''.join(nm).strip() + ': ')
            i = j
        elif t[1] == '<FFFC>':
            pass
        elif t[1] == '<FFFD>':
            try:
                s.append('<FFFD>' + next(fd))
            except StopIteration:
                raise Fail('FFFD count')
        else:
            s.append(t[1])
        i += 1
    text = re.sub(PAGE_MARK + r'\] |^\] ', lambda m: m.group(0)[:-2], ''.join(s))   # narration bullet
    if not re.search(r'<FF(F5|EF)>$', text):
        raise Fail('no end code')
    return text[:-6].strip(PAGE_MARK + ' '), text[-6:]


def page_split(body, npages, need, maxw, maxlines):
    """split body (one string, inline codes as tokens) into npages pages of <= maxlines lines, where the code count
    before break b must be need[b]. Breaks at word gaps, preferring sentence ends. -> [page text] or None"""
    import talktl
    gaps = [m.start() for m in re.finditer(' ', glue(body))]
    codes_before = lambda pos: len(talktl.codes(body[:pos]))   # noqa: E731
    sent = set(m.end() for m in re.finditer(r'[.!?~]+"?(?:<FFFC>)?(?= )', body))     # a pause may follow
    clause = set(m.end() for m in re.finditer(r'(?:[,;:]|--)(?:<FFFC>)?(?= )', body))

    def fits(a, b):
        return len(wrap_talk(body[a:b].strip(' '), maxw)) <= maxlines
    from functools import lru_cache

    @lru_cache(None)
    def best(start, k):
        """(cost, breaks) splitting body[start:] into k pages"""
        if k == 1:
            if not fits(start, len(body)):
                return None
            return (maxlines - len(wrap_talk(body[start:].strip(' '), maxw)), ())   # an orphan last page costs too
        res = None
        for g in gaps:
            if g <= start or (need is not None and codes_before(g) != need[npages - k]):
                continue
            if not fits(start, g):
                break
            sub = best(g + 1, k - 1)
            if sub is None:
                continue
            # a break after a sentence is free, after a comma cheap, mid-sentence expensive; a short page before
            # the break costs per empty line (no "Oh, is that" / "so!" splits)
            empty = maxlines - len(wrap_talk(body[start:g].strip(' '), maxw))
            cost = sub[0] + (0 if g in sent else 3 if g in clause else 6) + empty
            if res is None or cost < res[0]:
                res = (cost, (g,) + sub[1])
        return res
    r = best(0, npages)
    if r is None:
        return None
    pos, pages = 0, []
    for g in r[1]:
        pages.append(body[pos:g].strip(' '))
        pos = g + 1
    pages.append(body[pos:].strip(' '))
    return pages


def convert_unit(ja, units_b, maxw=vwf_wrap.BOX_WIDTH, maxlines=3):
    import talktl
    ja = cut_end(ja)
    jcodes = talktl.codes(ja)
    jfd = [p for c, p in jcodes if c == '<FFFD>']
    body, endc = psp_talk_text(units_b, jfd)
    if not ja.endswith(endc):
        raise Fail('end code')
    jbody = ja[:-6]
    jinline = [c for c, p in talktl.codes(jbody.replace(PAGE, '')) if c not in ('<FFFB>', '<FFF7>')]
    pinline = [c for c, p in talktl.codes(body)]
    if jinline != pinline:
        raise Fail(f'codes psp {pinline} ja {jinline}')
    nfc = jbody.count('<FFFC>')
    if nfc:                               # PSP has no short pauses: put the Japanese ones at sentence ends
        plain_j = re.sub(r'<[0-9A-F]{4}>', lambda m: '\x05' if m.group(0) == '<FFFC>' else '', re.sub(r'<FFFD>.', '', jbody))
        fr, pos = [], 0
        for ch in plain_j:
            if ch == '\x05':
                fr.append(pos / max(1, len(plain_j) - nfc))
            else:
                pos += 1
        body = place_by_fraction(body, fr, lambda k: '<FFFC>')
    jpages = jbody.split(PAGE)
    ppages = [p.strip(' ') for p in body.split(PAGE_MARK)]

    def render(pages):
        return PAGE.join('<FFF6>'.join(wrap_talk(re.sub(' +', ' ', p), maxw)) for p in pages) + endc
    if len(ppages) == len(jpages):        # the PSP split may already match
        en = render(ppages)
        if not talktl.check(ja, en, False, maxw, maxlines):
            return en
    need, acc = [], 0
    for jp in jpages[:-1]:
        acc += len(talktl.codes(jp))
        need.append(acc)
    if b'\xff\x1b' in units_b:
        # several speakers in one unit (TALK/ETC card scenes): their pages cannot be redistributed
        raise Fail('speaker pages')
    flat = re.sub(' +', ' ', body.replace(PAGE_MARK, ' ')).strip(' ')
    pages = page_split(flat, len(jpages), need, maxw, maxlines)
    if pages is not None:
        en = render(pages)
        errs = talktl.check(ja, en, False, maxw, maxlines)
        if errs:
            raise Fail('qa ' + '; '.join(errs))
        return en
    if not EXTRA_PAGES:
        raise Fail(f'too long for {len(jpages)} page(s)')
    # the PSP line needs more pages than the Japanese: add page breaks (FFFB FFF7 = wait + clear, as in the
    # Japanese multi-page units); every other code keeps its order
    for extra in (1, 2):
        pages = page_split(flat, len(jpages) + extra, None, maxw, maxlines)
        if pages is None:
            continue
        en = render(pages)
        nopage = lambda s: [c for c in talktl.codes(s) if c[0] not in ('<FFFB>', '<FFF7>')]   # noqa: E731
        errs = [e for e in talktl.check(ja, en, False, maxw, maxlines) if not e.startswith('codes differ')]
        if not errs and nopage(en) == nopage(ja):
            raise ExtraPage(en)
    raise Fail(f'too long for {len(jpages)}+2 page(s)')


def psp_answer_slots(name):
    """{table slot: bytes} of the player's answer lines (section 1, same layout as the PS1 files)"""
    d = open(os.path.join(SRC, 'talk', name + '.BIN'), 'rb').read()
    h = struct.unpack_from('<6I', d, 0)
    if h[2] - h[1] < 2048 or h[1] + 2048 > len(d):
        return {}
    tab = struct.unpack_from('<512I', d, h[1])          # absolute file offsets on the PSP (PS1: from the section)
    return {k: d[v:h[2]] for k, v in enumerate(tab) if v != 0xFFFFFFFF}


def ps1_answer_slots(name):
    """{table slot: decoded Japanese answer} of a PS1 TALK file"""
    import talk
    t = talk.load(name)
    if not t.ok or not t.s1:
        return {}
    by_off = {v: sp for v, sp in t.s1}
    return {k: etext.decode(by_off[v][:t.s1_text_len(by_off[v])]) for k, v in enumerate(t.s1_tab) if v in by_off}


def convert_answer(ja, b):
    import talktl
    jfd = [p for c, p in talktl.codes(ja) if c == '<FFFD>']
    body, endc = psp_talk_text(b, jfd)
    en = re.sub(' +', ' ', body.replace(PAGE_MARK, ' ')).strip(' ') + endc
    errs = talktl.check(ja, en, False, talktl.ANS_W, 1)
    if errs:
        raise Fail('qa ' + '; '.join(errs))
    return en


# ---------------------------------------------------------------- convert
def read_tsv(p):
    lines = open(p, encoding='utf-8').read().split(NL)
    return lines[0], [ln.split(TAB) for ln in lines[1:] if ln]


def write_tsv(p, head, rows):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8', newline=NL).write(NL.join([head] + [TAB.join(r) for r in rows]) + NL)


KEEP = os.path.join(ROOT, 'translation', 'psp_keep_ours.tsv')


def keep_ours():
    """{'E0/12/3', 'SLIME/40', 'ANSWERS/7', ...}: boxes that keep the project's English in the PSP variant
    (translation/psp_keep_ours.tsv, first column; ids only, no PSP text)."""
    if not os.path.exists(KEEP):
        return set()
    return {ln.split(TAB)[0].strip() for ln in open(KEEP, encoding='utf-8').read().split(NL)[1:] if ln.strip()}


def cmd_convert():
    import tstatus
    tstatus.load_glossary()
    etext.PSP = True                  # QA as in the PSP build (PSP speaker names, PSP choice of player name)
    keep = keep_ours()
    report = []
    stats = collections.Counter()
    # events
    for n in etext.FILES:
        head, rows = read_tsv(os.path.join(ROOT, 'translation', 'events', n + '.tsv'))
        by_entry = collections.defaultdict(list)
        for k, r in enumerate(rows):
            by_entry[int(r[0])].append(k)
        ents = e_entries(n)
        for e, idxs in by_entry.items():
            pbox = [w for off, w in e_boxes(ents[e])] if e < len(ents) else []
            ours = [(rows[k][2], rows[k][3]) for k in idxs]
            amap = align(ours, pbox)
            for j, k in enumerate(idxs):
                r = rows[k]
                if j not in amap:
                    report.append([n, r[0], r[1], 'unaligned', '', plain(r[3])[:200], ''])
                    stats['ev_unaligned'] += 1
                    continue
                w = pbox[amap[j]]
                if f'{n}/{r[0]}/{r[1]}' in keep:
                    report.append([n, r[0], r[1], 'kept', 'psp_keep_ours.tsv', plain(r[3])[:300], e_show(w)[:300]])
                    stats['ev_kept'] += 1
                    continue
                try:
                    en = convert_box(r[2], r[3], w)
                    r[3] = en
                    stats['ev_psp'] += 1
                    report.append([n, r[0], r[1], 'psp', '', plain(ours[j][1])[:300], plain(en)[:300]])
                except Fail as ex:
                    stats['ev_fallback'] += 1
                    stats['ev_reason ' + str(ex).split(' ')[0]] += 1
                    report.append([n, r[0], r[1], 'fallback', str(ex)[:120], plain(ours[j][1])[:300], e_show(w)[:300]])
        write_tsv(os.path.join(OUT, 'events', n + '.tsv'), head, rows)
    # talk
    for p in sorted(glob.glob(os.path.join(ROOT, 'translation', 'talk', '*.tsv'))):
        name = os.path.basename(p)[:-4]
        head, rows = read_tsv(p)
        src = os.path.join(SRC, 'talk', name + '.BIN')
        if name == 'ANSWERS':
            cands, fails = collections.defaultdict(collections.Counter), {}
            for f in sorted(glob.glob(os.path.join(SRC, 'talk', '*.BIN'))):
                tn = os.path.basename(f)[:-4]
                if tn == 'ETC':
                    continue
                pa = psp_answer_slots(tn)
                for slot, ja in ps1_answer_slots(tn).items():
                    if slot not in pa:
                        continue
                    try:
                        en = convert_answer(ja, pa[slot])
                        cands[ja][en] += 1
                    except Fail as ex:
                        fails[ja] = str(ex)
            for r in rows:
                if len(r) < 3 or not r[2].strip():
                    continue
                if f'ANSWERS/{r[0]}' in keep:
                    stats['answer_kept'] += 1
                    report.append(['ANSWERS', r[0], '', 'kept', 'psp_keep_ours.tsv', plain(r[2]), ''])
                elif r[1] in cands:
                    # one Japanese answer is used in several places and the PSP words it differently there:
                    # take the PSP wording closest in meaning to the project's line, then the most frequent
                    want = stems(readable(r[2]))
                    en = max(cands[r[1]].items(), key=lambda kv: (len(want & stems(readable(kv[0]))), kv[1]))[0]
                    stats['answer_psp'] += 1
                    report.append(['ANSWERS', r[0], '', 'psp', '', plain(r[2]), plain(en)])
                    r[2] = en
                else:
                    stats['answer_fallback'] += 1
                    report.append(['ANSWERS', r[0], '', 'fallback', fails.get(r[1], 'no PSP line')[:120], plain(r[2]), ''])
            write_tsv(os.path.join(OUT, 'talk', name + '.tsv'), head, rows)
            continue
        if not os.path.exists(src):
            write_tsv(os.path.join(OUT, 'talk', name + '.tsv'), head, rows)
            continue
        units = talk_units(name)
        for r in rows:
            u = int(r[0])
            if not r[2].strip() or u >= len(units) or r[2].startswith('Dummy'):
                continue        # the last unit of a file is a 'Dummy' placeholder (the PSP repeats a line there)
            if f'{name}/{u}' in keep:
                stats['talk_kept'] += 1
                report.append([name, r[0], '', 'kept', 'psp_keep_ours.tsv', plain(r[2])[:300], ''])
                continue
            try:
                try:
                    en, st = convert_unit(r[1], units[u]), 'psp'
                except ExtraPage as ep:
                    en, st = ep.args[0], 'psp+page'
                stats['talk_' + st] += 1
                report.append([name, r[0], '', st, '', plain(r[2])[:300], plain(en)[:300]])
                r[2] = en
            except Fail as ex:
                stats['talk_fallback'] += 1
                stats['talk_reason ' + str(ex).split(' ')[0]] += 1
                try:
                    shown = ''.join(t[1] for t in talk_tokens(units[u]))
                except Fail:
                    shown = units[u][:80].hex()
                report.append([name, r[0], '', 'fallback', str(ex)[:120], plain(r[2])[:300], shown[:300]])
        write_tsv(os.path.join(OUT, 'talk', name + '.tsv'), head, rows)
    write_tsv(os.path.join(OUT, 'report.tsv'), TAB.join(['file', 'entry', 'box', 'status', 'reason', 'ours', 'psp']), report)
    for k, v in sorted(stats.items()):
        print(f'{k:30s} {v}')


def readable(s):
    s = re.sub(r'<FF0[78F]>.', '[Hero]', s)
    s = re.sub(r'<FFF3>', '[demon]', s)
    s = re.sub(r'<FFF0>', '[race]', s)
    s = re.sub(r'<FFF9>', '[member]', s)
    s = re.sub(r'<FFF4>', '[item]', s)
    s = re.sub(r'<FFF8>', '[number]', s)
    s = re.sub(r'<FFFD>.', '', s)
    s = re.sub(r'<FF0[34]>|<FFF6>|<FFF7>', ' ', s)
    s = re.sub(r'<[^>]+>', '', s)
    return re.sub(r'\s+', ' ', s).strip()


def cmd_review_prep(per_chunk=400):
    """psp_text/review/chunk_NN.tsv: the converted lines next to the project's literal ones (unique pairs, scene
    order) for a semantic check by a reviewer agent; psp_text/review/ids.tsv maps a pair to all its boxes."""
    rows = [ln.split(TAB) for ln in open(os.path.join(OUT, 'report.tsv'), encoding='utf-8').read().split(NL)[1:] if ln]
    ours_full, psp_full = {}, {}
    for n in etext.FILES:                                   # full texts (the report truncates)
        _, a = read_tsv(os.path.join(ROOT, 'translation', 'events', n + '.tsv'))
        _, b = read_tsv(os.path.join(OUT, 'events', n + '.tsv'))
        for x, y in zip(a, b):
            ours_full[(n, x[0], x[1])], psp_full[(n, x[0], x[1])] = x[3], y[3]
    for p in glob.glob(os.path.join(ROOT, 'translation', 'talk', '*.tsv')):
        name = os.path.basename(p)[:-4]
        _, a = read_tsv(p)
        _, b = read_tsv(os.path.join(OUT, 'talk', name + '.tsv'))
        for x, y in zip(a, b):
            ours_full[(name, x[0], '')], psp_full[(name, x[0], '')] = x[2], y[2]
    pairs, ids = {}, collections.defaultdict(list)
    for r in rows:
        if not r[3].startswith('psp'):
            continue
        k = (r[0], r[1], r[2])
        o, p = readable(ours_full[k]), readable(psp_full[k])
        key = (o, p)
        if key not in pairs:
            pairs[key] = '/'.join(x for x in k if x)
        ids[pairs[key]].append('/'.join(x for x in k if x))
    d = os.path.join(OUT, 'review')
    os.makedirs(d, exist_ok=True)
    for f in glob.glob(os.path.join(d, 'chunk_*.tsv')):
        os.remove(f)
    items = list(pairs.items())
    n = 0
    for i in range(0, len(items), per_chunk):
        part = items[i:i + per_chunk]
        write_tsv(os.path.join(d, f'chunk_{n:02d}.tsv'), TAB.join(['id', 'literal', 'psp']),
                  [[pid, o, p] for (o, p), pid in part])
        n += 1
    write_tsv(os.path.join(d, 'ids.tsv'), TAB.join(['id', 'boxes']), [[k, ' '.join(v)] for k, v in ids.items()])
    print(f'{len(items)} unique pairs in {n} chunks -> {d}')


def cmd_review_collect():
    """merge psp_text/review/out_NN.tsv -> psp_text/review/flags.tsv (every affected box, with both lines);
    MISMATCH boxes (PSP line belongs elsewhere) are added to translation/psp_keep_ours.tsv (ids only)."""
    d = os.path.join(OUT, 'review')
    ids = {r[0]: r[1].split() for r in read_tsv(os.path.join(d, 'ids.tsv'))[1]}
    pairs = {}
    for f in glob.glob(os.path.join(d, 'chunk_[0-9]*.tsv')):
        for r in read_tsv(f)[1]:
            pairs[r[0]] = r[1:3]
    flags = []
    for f in sorted(glob.glob(os.path.join(d, 'out_[0-9]*.tsv'))):
        for r in read_tsv(f)[1]:
            if len(r) >= 2 and r[0] in pairs:
                lit, psp = pairs[r[0]]
                for box in ids.get(r[0], [r[0]]):
                    flags.append([box, r[1].strip().upper(), r[2] if len(r) > 2 else '', lit, psp])
    write_tsv(os.path.join(d, 'flags.tsv'), TAB.join(['id', 'verdict', 'reason', 'literal', 'psp']), flags)
    keep = keep_ours()
    new = [f for f in flags if f[1] == 'MISMATCH' and f[0] not in keep]
    if new:
        if not os.path.exists(KEEP):
            open(KEEP, 'w', encoding='utf-8', newline=NL).write('id' + TAB + 'note' + NL)
        with open(KEEP, 'a', encoding='utf-8', newline=NL) as o:
            for f in new:
                o.write(f'{f[0]}{TAB}review: MISMATCH{NL}')
                keep.add(f[0])
    c = collections.Counter(f[1] for f in flags)
    print(f'{len(flags)} flagged boxes ({dict(c)}); {len(new)} MISMATCH ids added to {KEEP}')


def cmd_show(n, e):
    for off, w in e_boxes(e_entries(n)[e]):
        print(hex(off), e_show(w))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    a = sys.argv[1:]
    if a[:1] == ['extract']:
        cmd_extract(a[1])
    elif a[:1] == ['convert']:
        cmd_convert()
    elif a[:1] == ['review-prep']:
        cmd_review_prep()
    elif a[:1] == ['review-collect']:
        cmd_review_collect()
    elif a[:1] == ['show']:
        cmd_show(a[1], int(a[2]))
    else:
        raise SystemExit(__doc__)
