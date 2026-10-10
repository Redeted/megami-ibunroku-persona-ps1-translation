"""Negotiation (CONTACT) messages of BTLP.BIN outside the btlmsg zone: demon-state banners, action announcements, reactions.

  python tools/btlneg.py dump     refresh translation/strings/BTLNEG.tsv (keeps `en` and `note`)
  python tools/btlneg.py build    QA + generate build/btlneg.asm (BTLP section of main.asm, before btlui / btlcmd)

Same machinery as tools/btlmsg.py with the zone BTLP RAM 0x800C87EC-0x800CEE30: strings in dialogue encoding ending FF F5
(FFF6 newline, FFFC pause, FFFA member, FFF9 name, FFF3 demon name, FFF4 item, FFF8 number), shown through the VWF-hooked
text interpreter. Only strings that have a reference (pointer word or lui/addiu pair) are handled: the 353 in BTLNEG.tsv; the
two blocks done by tools/btlui.py (personalities) and tools/btlcmd.py (commands) are excluded. A translated string leaves its
original slot to a free list; English is placed first-fit (longest first) in the freed slots (4-byte alignment not needed), all
references patched. Strings without `en` stay where they are. Everything stays below 0x800D0000 (the code references are
`lui 0x800D ; addiu` with a negative immediate).
`en`: control codes of the Japanese in any order, <= 239 px per line (tools/vwf_wrap.py).
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bpe       # noqa: E402
import btlmsg    # noqa: E402
import etext     # noqa: E402
import vwf_wrap  # noqa: E402

B = btlmsg.B
ROOT = btlmsg.ROOT
NL = chr(10)
ZONE = (0x800C87EC, 0x800CEE30)
SKIP = [(0x800C87EC, 0x800C882C), (0x800CB330, 0x800CB459)]       # btlui personalities, btlcmd commands
SPILL = [(0x800ABD50, 0x800ABDB0)]   # dead BTLP function (tools/deadovl.py), word references only; 0x800AAFEC, 0x800663F0 and 0x8007D6CC hold btlp_act_queue
TSV = os.path.join(ROOT, 'translation', 'strings', 'BTLNEG.tsv')
OUT = os.path.join(ROOT, 'build', 'btlneg.asm')
END = b'\xff\xf5'
BUF = 256                                        # unpack buffer (btlp/btlevt_unpack.asm BTLEVT_BUF_SIZE)
WIDTHS = {'<FFF3>': 80, '<FFF9>': 72, '<FFFA>': 72, '<FFF4>': 100, '<FFF2>': 80, '<FFF8>': 27, '<FFF0>': 54}


EXTRA = [0x800C92B0, 0x800C9488, 0x800C94D0, 0x800C9968, 0x800CD518, 0x800CB55C, 0x800C97B8]   # referenced strings the sequential scan swallows into junk before them (idx 353+)


def strings(d, rf):
    out, p = [], ZONE[0]
    while p < ZONE[1]:
        if d[p - B] == 0:
            p += 1
            continue
        q = d.index(END, p - B) + 2 + B
        if not any(a <= p < b for a, b in SKIP) and p in rf:
            out.append((p, q))
        p = q
    for a in EXTRA:
        out.append((a, d.index(END, a - B) + 2 + B))
    return out


def read_tsv():
    rows = {}
    if os.path.exists(TSV):
        for line in open(TSV, encoding='utf-8').read().split(NL)[1:]:
            c = line.rstrip('\r').split('\t')
            if len(c) >= 4 and c[0].isdigit():
                rows[int(c[0])] = (c[3], c[4] if len(c) > 4 else '')
    return rows


def dump():
    btlmsg.ZONE = ZONE
    d = btlmsg.data()
    rf = btlmsg.refs(d)
    old = read_tsv()
    with open(TSV, 'w', encoding='utf-8', newline=NL) as o:
        o.write('idx\tram\tja\ten\tnote' + NL)
        for i, (a, q) in enumerate(strings(d, rf)):
            en, note = old.get(i, ('', ''))
            kinds = ','.join(sorted({k for k, _ in rf[a]}))
            o.write(f'{i}\t{a:08X}\t{btlmsg.dec(d, a, q)}\t{en}\t{note or kinds + " " + str(q - a) + "B"}' + NL)
    print('wrote', TSV)


PACK_IDX = set(range(43, 79)) | set(range(168, 195)) | set(range(196, 300))   # message-box strings; 0-42 = top banner strings (another path, no unpacker), 34 = two messages


STUB = """
;; unpacker front for negotiation strings (jumped to from btl_unpack when the string is below the story-battle zone):
;; a string of the negotiation zone starting with the marker byte 0 is byte-pair packed with the table at PAIRS
.org 0x800ABD50
.area 0x800ABDB0 - 0x800ABD50
btl_neg:
    la      t0, 0x800C87EC
    sltu    t1, a0, t0
    beqz    t1, @@in
    nop
    j       btl_unpack_store
    nop
@@in:
    lbu     t1, 0(a0)
    nop
    beqz    t1, @@pk
    nop
    j       btl_unpack_store
    nop
@@pk:
    la      t0, PAIRS
    sw      t0, 32(sp)
    j       btl_unpack_go
    addiu   a0, a0, 1
.endarea
"""


def pack_candidates():
    """{idx: unpacked bytes (text + FF F5)} of the translated message-box strings: tools/btlevt.py puts them in its shared
    byte-pair table and writes build/btlneg_packed.json"""
    btlmsg.ZONE = ZONE
    d = btlmsg.data()
    rf = btlmsg.refs(d)
    msgs = strings(d, rf)
    en = read_tsv()
    out = {}
    for i in range(len(msgs)):
        t = en.get(i, ('', ''))[0].strip()
        if t and i in PACK_IDX:
            out[i] = etext.encode(t, end=None) + END
    return out


def width(t):
    w = 0
    for c, tw in WIDTHS.items():
        w += t.count(c) * tw
        t = t.replace(c, '')
    return w + vwf_wrap.text_width(re.sub(r'<[^>]*>', '', t))


def build():
    btlmsg.ZONE = ZONE
    d = btlmsg.data()
    rf = btlmsg.refs(d)
    msgs = strings(d, rf)
    en = read_tsv()
    new = {}
    for i, (a, q) in enumerate(msgs):
        t = en.get(i, ('', ''))[0].strip()
        if not t:
            continue
        orig = bytes(d[a - B:q - B])
        try:
            b = etext.encode(t, end=None) + END
        except ValueError as ex:
            raise SystemExit(f'btlneg: {i} {t!r}: {ex}')
        if btlmsg.codes(b) != btlmsg.codes(orig):
            raise SystemExit(f'btlneg: {i} {t!r}: control codes differ from the Japanese')
        for ln in t.split('<FFF6>'):
            if width(ln) > vwf_wrap.BOX_WIDTH:
                raise SystemExit(f'btlneg: {i} {ln!r} is {width(ln)} px wide (max {vwf_wrap.BOX_WIDTH})')
        new[i] = b
    # message-box strings are byte-pair packed (tools/bpe.py, marker byte 0, own pair table; unpacker btlp/btlevt_unpack.asm)
    for i, b in new.items():
        if i in PACK_IDX and len(b) > BUF:
            raise SystemExit(f'btlneg: {i} is {len(b)} bytes unpacked (unpack buffer {BUF})')
    packed, pairs = bpe.pack({i: b for i, b in new.items() if i in PACK_IDX}) if any(i in PACK_IDX for i in new) else ({}, [])
    for i in packed:
        new[i] = bytes((0,)) + packed[i]
    pair_blob = bytes(x for pr in pairs for x in pr)
    free = sorted(msgs[i] for i in new)
    merged = []
    for a, q in free:
        if merged and not any(d[merged[-1][1] - B:a - B]):          # adjacent, or only zero padding between
            merged[-1][1] = q
        else:
            merged.append([a, q])
    place = {}
    shared = {}
    spill = [list(z) for z in SPILL]
    spilled = set()
    code = {i for i in new if any(k == 'addiu' for k, _ in rf.get(msgs[i][0], []))}

    def put(zones, b):
        for z in zones:
            if z[1] - z[0] >= len(b):
                p = z[0]
                z[0] += len(b)
                return p
        return None
    pairs_at = put(merged, pair_blob) if pair_blob else 0
    if pair_blob and pairs_at is None:
        raise SystemExit('btlneg: no room for the pair table')
    for i in sorted(new, key=lambda i: (i not in code, -len(new[i]))):      # code-referenced strings first (must stay below 0x800D8000)
        b = new[i]
        if b in shared:
            place[i] = shared[b]
            continue
        p = put(merged, b)
        if p is None and i not in code:
            p = put(spill, b)
            spilled.add(b)
        if p is None:
            raise SystemExit(f'btlneg: out of space at {i} ({len(b)} bytes); free {[(hex(a), e - a) for a, e in merged + spill]}')
        place[i] = shared[b] = p
    with open(OUT, 'w', newline=NL) as o:
        o.write(';; generated by tools/btlneg.py build - do not edit' + NL)
        for i in new:
            a, q = msgs[i]
            o.write(f'.org {a:#x}{NL}    .fill {q - a}, 0{NL}')
        for a, q in SPILL:
            o.write(f'.org {a:#x}{NL}    .fill {q - a}, 0{NL}')
        for b, p in shared.items():
            o.write(f'.org {p:#x}{NL}    .byte ' + ', '.join(f'0x{x:02X}' for x in b) + NL)
        if pair_blob:
            o.write(f'.org {pairs_at:#x}{NL}    .byte ' + ', '.join(f'0x{x:02X}' for x in pair_blob) + NL)
        o.write(STUB.replace('PAIRS', f'{pairs_at:#x}'))
        for i in new:
            for kind, w in rf.get(msgs[i][0], []):
                if kind == 'word':
                    o.write(f'.org {w:#x}{NL}    .word {place[i]:#x}{NL}')
                else:
                    assert shared.get(new[i]) is not None and new[i] not in spilled, i
                    o.write(f'.org {w:#x}{NL}    .halfword {place[i] & 0xFFFF:#x}{NL}')
    used = sum(len(b) for b in shared)
    print(f'btlneg: {len(new)}/{len(msgs)} translated, {used} bytes placed in {sum(q - a for a, q in (msgs[i] for i in new))} freed -> {OUT}')


def work(apply=False):
    """validate translation/work/btlneg_en.tsv (idx, en, note) against btlneg_ja.tsv (idx, class, ja): classes A / D / P =
    message-box text (<= 3 lines, 239 px), O = choice-window option (1 line, <= 215 px); same control codes as the Japanese"""
    wdir = os.path.join(ROOT, 'translation', 'work')
    ja = {}
    for line in open(os.path.join(wdir, 'btlneg_ja.tsv'), encoding='utf-8').read().split(NL)[1:]:
        c = line.split('	')
        if len(c) >= 3 and c[0].isdigit():
            ja[int(c[0])] = (c[1], c[2])
    en = {}
    if os.path.exists(os.path.join(wdir, 'btlneg_en.tsv')):
        for line in open(os.path.join(wdir, 'btlneg_en.tsv'), encoding='utf-8').read().split(NL)[1:]:
            c = line.split('	')
            if len(c) >= 2 and c[0].isdigit() and c[1].strip():
                en[int(c[0])] = c[1].strip()
    bad = 0
    for i, t in sorted(en.items()):
        if i not in ja:
            print(f'{i}: not in the _ja file')
            bad += 1
            continue
        cls, j = ja[i]
        errs = []
        try:
            b = etext.encode(t, end=None) + END
            if btlmsg.codes(b) != btlmsg.codes(etext.encode(j, end=None) + END):
                errs.append('control codes differ from the Japanese')
        except ValueError as ex:
            errs.append(str(ex))
        lines = t.split('<FFF6>')
        if cls == 'O':
            if len(lines) > 1 or width(t) > 215:
                errs.append(f'option must be ONE line of <= 215 px (is {width(t)} px, {len(lines)} lines)')
        else:
            if len(lines) > 3 * (1 + t.count('<FFFB><FFF7>') + t.count('<FFEF>')):
                errs.append('more than 3 lines per page')
            for ln in lines:
                if width(ln) > vwf_wrap.BOX_WIDTH:
                    errs.append(f'{width(ln)} px: {ln[:30]}')
                    break
        if errs:
            bad += 1
            print(f'{i}: ' + '; '.join(errs))
    print(f'BTLNEG work: {len(en)}/{len(ja)} translated, {len(ja) - len(en)} missing, {bad} with problems')
    if apply and not bad:
        r = {}
        rp = os.path.join(wdir, 'btlneg_race.tsv')
        if os.path.exists(rp):
            for line in open(rp, encoding='utf-8').read().split(NL):
                c = line.split('	')
                if len(c) == 2 and c[0].isdigit():
                    r[int(c[0])] = c[1]
        L = open(TSV, encoding='utf-8').read().split(NL)
        out = [L[0]]
        n = 0
        for line in L[1:]:
            c = line.split('	')
            if len(c) >= 4 and c[0].isdigit():
                k = int(c[0])
                if k in en:
                    c[3] = en[k]; n += 1
                elif k in r:
                    c[3] = r[k]; n += 1
                line = '	'.join(c)
            out.append(line)
        open(TSV, 'w', encoding='utf-8', newline=NL).write(NL.join(out))
        print(f'wrote {n} strings into {TSV}')
    return bad


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    a = sys.argv[1] if len(sys.argv) > 1 else 'build'
    if a in ('check', 'apply'):
        sys.exit(1 if work(a == 'apply') else 0)
    {'dump': dump, 'build': build}[a]()
