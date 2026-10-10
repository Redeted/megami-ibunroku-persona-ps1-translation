"""Dungeon script boxes (story lines, locked doors, billboards ...) inside the dungeon data files D0x/D??.BIN.

  python tools/dngtext.py          patch build/<D0x>/D??.BIN (run after smallfont_pages.py; finds the boxes in the original, writes into the build copy if there is one)
  python tools/dngtext.py list     print every box found with its slot size and whether it is translated

Where the text comes from: the dungeon files are event records (fixed layout, sizes inside the records, no pointer table
for the text), the boxes are inline dialogue strings: ... FF21 00 00 <text> FF01 ... (also chained boxes without FF21,
speech between FF01 end codes). Boxes are found by scanning for FF01 and cutting the segment after the last FF21 0000 (or
after the previous FF01); a segment counts when it holds an FF02 wait code and >= 3 kana/kanji. Because the records cannot
grow, every English text is written IN PLACE into the Japanese slot (codes kept, rest zero-filled); the English must be
<= the slot including the FF01 end. English source: translation/src/dngtext_en.py (key = full Japanese string).
Dungeon speech engine: VWF ASCII, FF03 new line, FF04 new page, FF02 wait, FF0E choice, FF0F/FF07/FF08/FF10 name inserts + 1 param byte.
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'translation', 'src'))
import etext   # noqa: E402
import vwf_wrap   # noqa: E402
from dngtext_en import ROWS   # noqa: E402

ROOT = etext.ROOT
EN = dict(ROWS)
END = bytes((0xFF, 0x01))
# fragments inside records that have no FF02 (prompt of a menu, poster text): (Japanese, English), English <= Japanese bytes
SUBS = [
    ('どれにする？', 'Which?'),
    ('毎朝　　　鉄人　　　やすし<FF03>　文庫　　　タイトル　終わり', 'AM Tetsujin Yasushi<FF03>Bunko Title End'),
]
TOK = re.compile(r'<FF0[2-4]>')


def boxes(d):
    """[(offset, length, japanese text)] of every dialogue box in a dungeon file"""
    out, prev = [], 0
    for m in re.finditer(b'\xff\x01', d):
        seg = d[prev:m.start() + 2]
        start = prev
        prev = m.start() + 2
        k = seg.rfind(b'\xff\x21\x00\x00')
        if k >= 0:
            seg, start = seg[k + 4:], start + k + 4
        if b'\xff\x02' not in seg or len(seg) > 400:
            continue
        try:
            t = etext.decode(seg)
        except Exception:
            continue
        if sum(1 for c in t if ord(c) > 0x2000) < 3:
            continue
        out.append((start, len(seg), t))
    return out


def width_ok(en):
    t = en.replace('<FF0F>　', '<FF0F>あ').replace('<FF07>　', '<FF07>あ').replace('<FF08>　', '<FF08>あ')
    return all(vwf_wrap.text_width(l) <= 235 for l in TOK.sub('<FF03>', t).split('<FF03>'))


def files():
    for fp in sorted(glob.glob(os.path.join(ROOT, 'original', 'D0*', 'D*.BIN'))):
        if len(os.path.basename(fp)) == 7:
            bp = fp.replace(os.sep + 'original' + os.sep, os.sep + 'build' + os.sep)
            yield os.path.basename(fp), fp, bp


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    lst = len(sys.argv) > 1 and sys.argv[1] == 'list'
    total = nfiles = 0
    missing = set()
    for name, fp, bp in files():
        orig = open(fp, 'rb').read()
        d = bytearray(open(bp, 'rb').read() if os.path.exists(bp) else orig)
        n = 0
        for off, ln, ja in boxes(orig):          # offsets from the ORIGINAL (the build copy may hold older patches)
            en = EN.get(ja)
            if lst:
                print(f'{name} {off:#x} {ln:3d} B {"OK " if en else "-- "}{ja}')
            if en is None:
                missing.add(ja)
                continue
            lead = len(ja) - len(ja.lstrip('　'))      # the game drops as many leading glyphs as the Japanese has indent cells
            eb = etext.encode(en, end=None) + END
            if lead and not en.startswith('　') and '<FF06>' not in en:
                eb2 = etext.encode('　' * lead + en, end=None) + END
                if len(eb2) <= ln:
                    en, eb = '　' * lead + en, eb2
            if len(eb) > ln:
                raise SystemExit(f'dngtext: {en!r} needs {len(eb)} bytes, slot {ln}')
            if '<FF06>' not in en and not width_ok(en.lstrip('　')):   # FF06 boxes are name-token puzzles
                raise SystemExit(f'dngtext: line wider than 235 px in {en!r}')
            d[off:off + ln] = eb + bytes(ln - len(eb))
            n += 1
        for ja, en in SUBS:
            jb, eb = etext.encode(ja, end=None), etext.encode(en, end=None)
            if len(eb) > len(jb):
                raise SystemExit(f'dngtext: {en!r} needs {len(eb)} bytes, slot {len(jb)}')
            i = orig.find(jb)
            while i >= 0:
                d[i:i + len(jb)] = eb + bytes(len(jb) - len(eb))
                n += 1
                i = orig.find(jb, i + len(jb))
        if n and not lst:
            os.makedirs(os.path.dirname(bp), exist_ok=True)
            open(bp, 'wb').write(bytes(d))
            nfiles += 1
            total += n
    print(f'dngtext: {total} boxes in {nfiles} files, {len(missing)} Japanese boxes without English')
    for ja in sorted(missing):
        print('  missing:', ja)


if __name__ == '__main__':
    main()
