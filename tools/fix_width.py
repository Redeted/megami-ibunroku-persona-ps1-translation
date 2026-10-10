"""Re-wrap translated event boxes whose lines are too wide for the engine (>= 240 px).

  python tools/fix_width.py            dry run: report what would change
  python tools/fix_width.py --apply    rewrite translation/events/E?.tsv (then run tstatus propagate/qa/status)

vwf_dialog.asm wraps when the pen reaches 240 px, so lines must be <= 239 px (vwf_wrap.BOX_WIDTH).
For each page (split at <FF02><FF04>) the last word of a too-wide line is moved down to the next line
(cascade). Boxes where a page would then exceed 3 lines are NOT written; they are
listed for a manual rephrase. Pages that are fine are not touched.
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vwf_wrap  # noqa: E402

ROOT = vwf_wrap.ROOT
NL = vwf_wrap.NEWLINE
PAGE = '<FF02><FF04>'
LABEL = re.compile(r'^((?:<FF06><[0-9A-F]{2}>)?[A-Z][A-Za-z\'/ ]*: )')


def fix_page(lines):
    """Cascade: move the last word of a too-wide line to the start of the next line. -> new lines"""
    lines = list(lines)
    i = 0
    while i < len(lines):
        while vwf_wrap.text_width(lines[i]) > vwf_wrap.BOX_WIDTH:
            if ' ' not in lines[i]:
                raise ValueError('single word too wide: ' + lines[i])
            head, word = lines[i].rsplit(' ', 1)
            lines[i] = head
            if i + 1 < len(lines):
                lines[i + 1] = word + ' ' + lines[i + 1]
            else:
                lines.append(word)
        i += 1
    return lines


def fix_box(en):
    """-> (new text, changed, pages that now have more than 3 lines)"""
    pages = en.split(PAGE)
    out, changed, long_pages = [], False, []
    for pg in pages:
        lines = pg.split(NL)
        if all(vwf_wrap.text_width(ln) <= vwf_wrap.BOX_WIDTH for ln in lines):
            out.append(pg)
            continue
        changed = True
        new = fix_page(lines)
        if len(new) > 3:
            long_pages.append(NL.join(new))
        out.append(NL.join(new))
    return PAGE.join(out), changed, long_pages


def main():
    apply = '--apply' in sys.argv
    n = 0
    manual = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'translation', 'events', 'E?.tsv'))):
        nl = chr(10)
        rows = open(f, encoding='utf-8').read().split(nl)
        for i, line in enumerate(rows):
            c = line.split('\t')
            if i == 0 or len(c) < 4 or not c[3]:
                continue
            new, changed, long_pages = fix_box(c[3])
            if long_pages:
                manual.append((os.path.basename(f)[:2], c[0], c[1], long_pages))
                continue
            if changed:
                n += 1
                c[3] = new
                rows[i] = '\t'.join(c)
        if apply:
            open(f, 'w', encoding='utf-8', newline=nl).write(nl.join(rows))
    print(f'{n} boxes {"rewritten" if apply else "to rewrite"}; {len(manual)} need a manual rephrase (page > 3 lines):')
    for fl, e, bx, pgs in manual:
        print(f'  {fl}/{e}/{bx}: ' + ' || '.join(p.replace(NL, ' / ') for p in pgs))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
