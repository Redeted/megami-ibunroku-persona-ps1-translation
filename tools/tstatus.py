"""Translation progress, QA and duplicate propagation for the event scripts.

  python tools/tstatus.py status       write translation/PROGRESS.md (coverage + exactly where to continue)
  python tools/tstatus.py qa           check every translated box against its Japanese original
  python tools/tstatus.py propagate    copy a translation to every box with identical Japanese
  python tools/tstatus.py next [N]     print the next N untranslated boxes (default 25) in work order

QA errors (build.py fails on these):
  codes     control codes with parameters differ from the Japanese (order, count or value)
  width     a line is wider than 239 px (engine wraps at 240) or a page (between FF02/FF04) has more than 3 lines
  charset   anything but printable ASCII outside code parameters (Japanese left in the text)
  label     the speaker label does not match the glossary (e.g. ゆきの: must start "Yukino: ")
  encode    the text cannot be encoded
Warnings are listed but do not fail the build.
"""
import collections
import datetime
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import etext      # noqa: E402
import vwf_wrap   # noqa: E402

ROOT = etext.ROOT
EV = os.path.join(etext.TEXT, 'events')
TAB, NL = chr(9), chr(10)
# parameter bytes that follow each control code (observed in all 7344 boxes)
PARAM_LEN = {0x05: 2, 0x06: 1, 0x07: 1, 0x08: 1, 0x0E: 1, 0x0F: 1, 0x11: 0, 0x12: 0}
STRUCT = {0x01, 0x02, 0x03, 0x04}
TOKEN = re.compile(r'<(?:FF[0-9A-F]{2}|G[0-9A-F]{3}|[0-9A-F]{2})>')


def rows():
    """yield (file, entry, box, ja, en) for every box, file order."""
    for n in etext.FILES:
        p = os.path.join(EV, f'{n}.tsv')
        for line in open(p, encoding='utf-8').read().split(NL)[1:]:
            f = line.split(TAB)
            if len(f) >= 4 and f[0].isdigit():
                yield n, int(f[0]), int(f[1]), f[2], f[3]


def code_seq(b):
    """[(code, params)] for the parameter-carrying control codes of an encoded box."""
    out, i = [], 0
    while i < len(b):
        c = b[i]
        if c == 0xFF and i + 1 < len(b):
            op = b[i + 1]
            i += 2
            if op in PARAM_LEN:
                out.append((op, bytes(b[i:i + PARAM_LEN[op]])))
            i += PARAM_LEN.get(op, 0)
        elif 0x80 <= c <= 0x87:
            i += 2
        else:
            i += 1
    return out


def text_only(b):
    """encoded box -> bytes of displayed characters (codes and their parameters removed)."""
    out, i = bytearray(), 0
    while i < len(b):
        c = b[i]
        if c == 0xFF and i + 1 < len(b):
            op = b[i + 1]
            i += 2 + PARAM_LEN.get(op, 0)
        elif 0x80 <= c <= 0x87:
            out += b[i:i + 2]
            i += 2
        else:
            out.append(c)
            i += 1
    return bytes(out)


def segments(en):
    """pages for the width check: split on FF02/FF03-aware boundaries -> list of [lines]."""
    pages = []
    for page in re.split(r'<FF04>|<FF02>', en):
        pages.append(page.split('<FF03>'))
    return pages


GLOSS = {}


def load_glossary():
    p = os.path.join(ROOT, 'glossary.tsv')
    for line in open(p, encoding='utf-8').read().split(NL)[1:]:
        f = line.split(TAB)
        if len(f) >= 3 and f[0]:
            GLOSS[f[0]] = (f[1], f[2])


def speaker(ja):
    m = re.match(r'(?:<FF0[0-9A-F]>(?:<[0-9A-F]{2}>)?)*([^：<]{1,12})：', ja)
    return m.group(1) if m else None


def check(ja, en):
    errs = []
    try:
        be = etext.encode(en)
    except ValueError as ex:
        return [('encode', str(ex))]
    bj = etext.encode(ja)
    if etext.PSP:                     # PSP variant: the player-name codes follow the PSP (given / family / nickname)
        norm = lambda seq: [(0x0F if o in (0x07, 0x08, 0x0F) else o, p) for o, p in seq]   # noqa: E731
    else:
        norm = lambda seq: seq       # noqa: E731
    if norm(code_seq(be)) != norm(code_seq(bj)):
        errs.append(('codes', f'ja {[(hex(o), p.hex()) for o, p in code_seq(bj)][:6]} en {[(hex(o), p.hex()) for o, p in code_seq(be)][:6]}'))
    for pg in segments(en):
        if len(pg) > 3:
            errs.append(('width', f'{len(pg)} lines on a page'))
            break
        bad = [ln for ln in pg if vwf_wrap.text_width(ln) > vwf_wrap.BOX_WIDTH]
        if bad:
            errs.append(('width', f'too wide: {bad[0][:40]}'))
            break
    if '<FF0E>' in en and not re.search(r'(?:^|<FF03>|<FF04>)<FF0E>', en):
        # a full 15-glyph Japanese question ends its line; English must break before the options itself
        errs.append(('choice', 'put <FF03> before <FF0E> (options would start mid-line)'))
    bad = [c for c in text_only(be) if not (0x88 <= c <= 0xE6)]
    if bad:
        errs.append(('charset', f'non-ASCII bytes in text: {bytes(bad[:6]).hex()}'))
    sp = speaker(ja)
    if sp and not etext.PSP and sp in GLOSS and GLOSS[sp][1] in ('character', 'speaker label'):
        want = GLOSS[sp][0]
        if not en.lstrip().replace('<FF06><02>', '').startswith(want + ':') and not re.match(r'(?:<FF0[0-9A-F]>(?:<[0-9A-F]{2}>)?)*' + re.escape(want) + ':', en):
            errs.append(('label', f'{sp} should be "{want}:"'))
    return errs


def cmd_qa(limit=40):
    load_glossary()
    counts, shown, total = collections.Counter(), 0, 0
    for n, e, k, ja, en in rows():
        if not en:
            continue
        total += 1
        for kind, msg in check(ja, en):
            counts[kind] += 1
            if shown < limit:
                print(f'{n}/{e}/{k} [{kind}] {msg}')
                shown += 1
    print(f'QA: {total} translated boxes, errors: {dict(counts) or "none"}')
    return sum(counts.values())


def cmd_propagate():
    by_ja = collections.defaultdict(collections.Counter)
    for n, e, k, ja, en in rows():
        if en:
            by_ja[ja][en] += 1
    conflicts = {ja: c for ja, c in by_ja.items() if len(c) > 1}
    filled = 0
    for n in etext.FILES:
        p = os.path.join(EV, f'{n}.tsv')
        lines = open(p, encoding='utf-8').read().split(NL)
        for i, line in enumerate(lines[1:], 1):
            f = line.split(TAB)
            if len(f) >= 4 and f[0].isdigit() and not f[3] and f[2] in by_ja:
                f[3] = by_ja[f[2]].most_common(1)[0][0]
                lines[i] = TAB.join(f)
                filled += 1
        open(p, 'w', encoding='utf-8', newline=NL).write(NL.join(lines))
    print(f'propagated {filled} boxes; {len(conflicts)} Japanese texts have conflicting translations')
    for ja, c in list(conflicts.items())[:5]:
        print('  conflict:', ja[:50])
    return filled


def stats():
    per = collections.OrderedDict()
    uniq, uniq_done = {}, set()
    for n, e, k, ja, en in rows():
        d = per.setdefault(n, collections.OrderedDict()).setdefault(e, [0, 0])
        d[0] += 1
        d[1] += 1 if en else 0
        uniq.setdefault(ja, False)
        if en:
            uniq[ja] = True
    return per, uniq


def cmd_next(count=25, quiet=False):
    seen, out = set(), []
    done_ja = {ja for n, e, k, ja, en in rows() if en}
    for n, e, k, ja, en in rows():
        if en or ja in done_ja or ja in seen:
            continue
        seen.add(ja)
        out.append((n, e, k, ja))
        if len(out) >= count:
            break
    if not quiet:
        for n, e, k, ja in out:
            print(f'{n}/{e}/{k}: {ja}')
    return out


def talk_stats():
    d = os.path.join(ROOT, 'translation', 'talk')
    tot = done = 0
    uniq = set()
    if os.path.isdir(d):
        for fn in os.listdir(d):
            if fn.endswith('.tsv'):
                for line in open(os.path.join(d, fn), encoding='utf-8').read().split(NL)[1:]:
                    f = line.split(TAB)
                    if len(f) >= 3 and f[0].isdigit():
                        tot += 1
                        uniq.add(f[1])
                        done += 1 if f[2] else 0
    return tot, done, len(uniq)


def cmd_status():
    load_glossary()
    per, uniq = stats()
    tot_boxes = sum(v[0] for f in per.values() for v in f.values())
    done_boxes = sum(v[1] for f in per.values() for v in f.values())
    tu, du = len(uniq), sum(1 for v in uniq.values() if v)
    review = 0
    rp = os.path.join(ROOT, 'translation', 'review.tsv')
    if os.path.exists(rp):
        review = sum(1 for l in open(rp, encoding='utf-8').read().split(NL)[1:] if l.strip())
    nxt = cmd_next(1, quiet=True)
    talk = talk_stats()
    lines = [
        '# Translation progress (generated by `python tools/tstatus.py status` - do not edit)', '',
        f'Updated: {datetime.date.today()}', '',
        f'- Event script boxes: **{done_boxes} / {tot_boxes}** translated ({100 * done_boxes // max(tot_boxes, 1)}%)',
        f'- Unique Japanese texts: **{du} / {tu}** ({100 * du // max(tu, 1)}%) - identical boxes share one translation (`propagate`)',
        f'- Negotiation (TALK/*.BIN) units: **{talk[1]} / {talk[0]}** translated ({talk[2]} unique Japanese texts) - extraction only, no English can be shown until the BTLP renderer has a VWF hook',
        f'- Open review items: **{review}** (translation/review.tsv)', '',
        '## Continue here', '',
    ]
    if nxt:
        n, e, k, ja = nxt[0]
        lines += [f'Next untranslated text in work order: `{n}` entry **{e}** box **{k}**.',
                  '', 'Print the next batch: `python tools/tstatus.py next 40`', '']
    else:
        lines += ['All event boxes are translated.', '']
    lines += ['## Coverage by file', '', '| file | entries | boxes | translated | untouched entries |', '|---|---|---|---|---|']
    for n, ents in per.items():
        b = sum(v[0] for v in ents.values())
        d = sum(v[1] for v in ents.values())
        untouched = sum(1 for v in ents.values() if v[1] == 0)
        lines.append(f'| {n} | {len(ents)} | {b} | {d} | {untouched} |')
    lines += ['', '## Entries with partial translation (finish these first)', '']
    part = [(n, e, v) for n, ents in per.items() for e, v in ents.items() if 0 < v[1] < v[0]]
    lines += [f'- {n} entry {e}: {v[1]}/{v[0]}' for n, e, v in part] or ['- none']
    lines += ['', 'See translation/LOG.md for the batch history.', '']
    open(os.path.join(ROOT, 'translation', 'PROGRESS.md'), 'w', encoding='utf-8', newline=NL).write(NL.join(lines))
    print(f'boxes {done_boxes}/{tot_boxes}, unique {du}/{tu}, review {review}; wrote translation/PROGRESS.md')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    a = sys.argv[1:] or ['status']
    if a[0] == 'status':
        cmd_status()
    elif a[0] == 'qa':
        sys.exit(1 if cmd_qa() else 0)
    elif a[0] == 'propagate':
        cmd_propagate()
    elif a[0] == 'next':
        cmd_next(int(a[1]) if len(a) > 1 else 25)
    else:
        raise SystemExit(__doc__)
