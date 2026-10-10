"""Lowercase a-z in every copy of the 8x12 small-font page on the disc (tools/smallfont_lc.py).

  python tools/smallfont_pages.py        write build/<dir>/<file> for each 2D/ and D0x/ file carrying the page

Every 2D-map (2D/2DLTS0x.BIN) and dungeon file (D0x/Dxx.BIN) loads its own copy of the page to VRAM (the battle panels
use the one at (960,256)), as do ADV/ADVCMD.BIN, ADV/ADVCMD0.BIN and OPEN.BIN (those three: tools/menu_gfx.py).
Copies are 256 or 248 px wide; they are found by their kana glyph rows (identical in all copies) and only the 26 kana
cells reused for a..z change, so the files keep their size. Needs the files in original/ (tools/extract.py <image>
original "2D/*" "D00/*" ... "D04/*").
"""
import glob
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import menu_gfx      # noqa: E402
import smallfont_lc  # noqa: E402
import tim           # noqa: E402

ROOT = tim.ROOT
DIRS = ['2D', 'D00', 'D01', 'D02', 'D03', 'D04']
ROWS = 3 * 12                       # the reused kana cells are in cell rows 0-2


def reference():
    d = open(os.path.join(ROOT, 'original', 'ADV', 'ADVCMD.BIN'), 'rb').read()
    t = tim.parse(d, menu_gfx.PAGE)
    return d[t['at']:t['at'] + 128 * 256]


def find_pages(b, page):
    """-> [(offset of pixel row 0, bytes per row)]"""
    out = []
    probe = page[13 * 128:13 * 128 + 120]
    i = b.find(probe)
    while i >= 0:
        for bpr in (128, 124):
            at = i - 13 * bpr
            if at >= 0 and all(b[at + y * bpr:at + y * bpr + bpr] == page[y * 128:y * 128 + bpr] for y in range(ROWS)):
                out.append((at, bpr))
                break
        i = b.find(probe, i + 1)
    return out


def main():
    page = reference()
    n = nl = 0
    for dname in DIRS:
        for path in sorted(glob.glob(os.path.join(ROOT, 'original', dname, '*.BIN'))):
            b = bytearray(open(path, 'rb').read())
            pages = find_pages(b, page)
            if not pages:
                continue
            for at, bpr in pages:
                b[at:at + bpr * ROWS] = menu_gfx.lc_page(bytes(b[at:at + bpr * ROWS]), bpr * 2)
                nl += menu_gfx.label_rows(b, at, bpr, page)     # MATK / MDEF where the kanji labels exist
            out = os.path.join(ROOT, 'build', dname, os.path.basename(path))
            os.makedirs(os.path.dirname(out), exist_ok=True)
            open(out, 'wb').write(bytes(b))
            n += 1
    print(f'small-font pages: {n} files patched (lowercase a-z), {nl} pages with MATK/MDEF labels')


if __name__ == '__main__':
    main()
