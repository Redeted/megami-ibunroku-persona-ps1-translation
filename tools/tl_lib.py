"""Authoring helpers for event translations (ADV/E0..E3.BIN -> translation/events/E?.tsv).

A scene script (translation/src/*.py) maps box numbers to English and calls apply():

    from tl_lib import apply, P, F6
    apply('E0', 0, {
        0: ["Mark: First page.", "Mark: Second page."],        # pages -> wrapped, joined
        11: "=So, which will it be?<FF03><FF0E>の",              # '=' prefix: used verbatim
    })

Page boxes are wrapped with tools/vwf_wrap.py (240 px, at most 3 lines per page),
pages are joined with <FF02><FF04> and the box ends with <FF02> (the build adds <FF01>).
Control codes with parameters must be kept as in the Japanese; helpers build them:
    P('キ')   -> <FF05><xx><00>   pause (u16 parameter; xx = the glyph byte of that char)
    F6('い')  -> <FF06><xx>       style switch; F6(0) -> <FF06><00> (reset)
Write the player-name token as <FF0F>あ exactly as in the Japanese text.
"""
import datetime
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import etext      # noqa: E402
import vwf_wrap   # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAB, NL = chr(9), chr(10)


def _glyph_byte(ch):
    g = etext.char2g[ch]
    assert g < 0x80, ch
    return g


def P(ch='み'):
    return f'<FF05><{_glyph_byte(ch):02X}><00>'


def F6(ch):
    return '<FF06><00>' if ch == 0 else f'<FF06><{_glyph_byte(ch):02X}>'


_LABEL = re.compile(r"^([A-Z][A-Za-z.' -]{0,30}: )")


def _paginate(page):
    """Split a page that wraps to more than 3 lines into pages of 3 lines.
    Later pages repeat the speaker label (guide: label on every page)."""
    m = _LABEL.match(page)
    label = m.group(1) if m else ''
    pages, rest = [], page
    while True:
        lines = vwf_wrap.wrap(rest).split(vwf_wrap.NEWLINE)
        if len(lines) <= 3:
            pages.append(rest)
            return pages
        first = lines[:3]
        pages.append(vwf_wrap.NEWLINE.join(first))
        rest = label + ' '.join(lines[3:])


def build(pages):
    out = []
    for p in (q for page in pages for q in _paginate(page)):
        w = vwf_wrap.wrap(p)
        lines = w.split(vwf_wrap.NEWLINE)
        if len(lines) > 3:
            raise ValueError(f'more than 3 lines ({len(lines)}): {w}')
        for ln in lines:
            if vwf_wrap.text_width(ln) > vwf_wrap.BOX_WIDTH:
                raise ValueError(f'line too wide: {ln}')
        out.append(w)
    return '<FF02><FF04>'.join(out) + '<FF02>'


def _log(fname, entry, n, review):
    path = os.path.join(ROOT, 'translation', 'LOG.md')
    new = not os.path.exists(path)
    with open(path, 'a', encoding='utf-8', newline=NL) as f:
        if new:
            f.write('# Translation log (append-only; one line per batch)' + NL + NL)
        f.write(f'- {datetime.date.today()} {fname}/{entry}: {n} boxes' + (f', {len(review)} flagged for review' if review else '') + NL)


def _flag(fname, entry, review):
    """review = {box: reason}; appended to translation/review.tsv (one row per box, latest reason wins)."""
    path = os.path.join(ROOT, 'translation', 'review.tsv')
    rows = {}
    if os.path.exists(path):
        for line in open(path, encoding='utf-8').read().split(NL)[1:]:
            f = line.split(TAB)
            if len(f) >= 4:
                rows[(f[0], f[1], f[2])] = f[3]
    for box, why in review.items():
        rows[(fname, str(entry), str(box))] = why
    with open(path, 'w', encoding='utf-8', newline=NL) as f:
        f.write(TAB.join(['file', 'entry', 'box', 'reason']) + NL)
        for (a, b, c), why in sorted(rows.items(), key=lambda x: (x[0][0], int(x[0][1]), int(x[0][2]))):
            f.write(TAB.join([a, b, c, why]) + NL)


def apply(fname, entry, boxes, review=None):
    """Write English for the given boxes of one entry into translation/events/<fname>.tsv.

    boxes:  {box: [pages...] | "=verbatim text"}
    review: {box: "why unsure"} -> translation/review.tsv (the line is still written)
    Every box is checked (tools/tstatus.py check): codes, width, charset, speaker label.
    Nothing is written unless all boxes pass."""
    import tstatus
    tstatus.load_glossary()
    review = review or {}
    path = os.path.join(ROOT, 'translation', 'events', f'{fname}.tsv')
    rows = open(path, encoding='utf-8').read().split(NL)
    done, errors = set(), []
    for i, line in enumerate(rows):
        f = line.split(TAB)
        if len(f) >= 4 and f[0] == str(entry) and f[1].isdigit() and int(f[1]) in boxes:
            v = boxes[int(f[1])]
            if isinstance(v, list) and len(v) == 1 and v[0].startswith('='):
                v = v[0]            # ['=verbatim'] means the same as '=verbatim'
            try:
                text = v[1:] if isinstance(v, str) and v.startswith('=') else build(v)
                etext.encode(text)          # must be encodable
            except ValueError as ex:
                errors.append(f'  box {f[1]}: {ex}')
                continue
            bad = tstatus.check(f[2], text)
            if bad:
                errors.append(f'  box {f[1]}: ' + '; '.join(f'[{k}] {m}' for k, m in bad))
                continue
            f[3] = text
            rows[i] = TAB.join(f)
            done.add(int(f[1]))
    failed = {int(e.split()[1][:-1]) for e in errors}
    missing = set(boxes) - done - failed
    if missing:
        raise SystemExit(f'{fname}/{entry}: no such boxes {sorted(missing)}')
    if errors:
        raise SystemExit(f'{fname}/{entry}: {len(errors)} boxes need rework, nothing written:' + NL + NL.join(errors))
    open(path, 'w', encoding='utf-8', newline=NL).write(NL.join(rows))
    if review:
        _flag(fname, entry, review)
    _log(fname, entry, len(done), review)
    print(f'{fname}/{entry}: {len(done)} boxes written')
