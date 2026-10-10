"""Render game glyph bitmaps next to their assigned characters for visual auditing.

  python tools/glyph_sheet.py <out_dir> [max_score] [per_sheet]

Tiles: the game's 16x16 bitmap (zoomed) | the assigned character in a reference font | hex
index, usage count, score and the matcher's runner-up candidates. Only glyphs used in the
event scripts whose match score is below max_score (default 0.90) and that are not
hand-verified; a negative max_score selects the manual overrides ('fix') instead. Review them to find misread kanji; corrections go into tools/font_map.tsv.
"""
import collections
import os
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import etext      # noqa: E402
import tstatus    # noqa: E402

Z = 4
TILE_W, TILE_H = 190, 92


def load_map():
    rows = {}
    for line in open(os.path.join(ROOT, 'tools', 'font_map.tsv'), encoding='utf-8'):
        p = line.rstrip('\n').split('\t')
        if len(p) >= 4:
            rows[int(p[0], 16)] = (p[1], p[2], float(p[3]), p[4] if len(p) > 4 else '')
    return rows


def used_glyphs():
    use, seen = collections.Counter(), set()
    for n, e, k, ja, en in tstatus.rows():
        if ja in seen:
            continue
        seen.add(ja)
        b = etext.encode(ja)
        i = 0
        while i < len(b):
            c = b[i]
            if c == 0xFF:
                i += 2 + tstatus.PARAM_LEN.get(b[i + 1], 0)
            elif 0x80 <= c <= 0x87:
                use[((c & 7) << 8) | b[i + 1]] += 1
                i += 2
            else:
                use[c] += 1
                i += 1
    return use


def bitmap(font, g):
    im = Image.new('L', (16, 16), 255)
    px = im.load()
    for y in range(16):
        row = (font[g * 32 + y * 2] << 8) | font[g * 32 + y * 2 + 1]
        for x in range(16):
            if row & (0x8000 >> x):
                px[x, y] = 0
    return im.resize((16 * Z, 16 * Z), Image.NEAREST)


def main():
    out = sys.argv[1]
    maxs = float(sys.argv[2]) if len(sys.argv) > 2 else 0.90
    overridden = maxs == -1
    rare = maxs == -2
    per = int(sys.argv[3]) if len(sys.argv) > 3 else 40
    os.makedirs(out, exist_ok=True)
    font = open(os.path.join(ROOT, 'original', 'FONT.BIN'), 'rb').read()
    rows, use = load_map(), used_glyphs()
    if overridden:    # max_score < 0: manual overrides ('fix') - the entries most likely to be wrong
        sel = [g for g in use if g >= 0x10F and g in rows and rows[g][1] == 'fix']
    elif rare:        # max_score == -2: auto matches with score >= 0.90 used at most 3 times
        sel = [g for g in use if g >= 0x10F and g in rows and rows[g][1] == 'auto'
               and rows[g][2] >= 0.90 and use[g] <= 3]
    else:
        sel = [g for g in use if g >= 0x10F and g in rows and rows[g][1] != 'hand' and rows[g][2] < maxs]
    sel.sort(key=lambda g: rows[g][2])
    ref = ImageFont.truetype(os.path.join(ROOT, 'research', 'fonts', 'NotoSansJP-Regular.otf'), 46)
    small = ImageFont.truetype(os.path.join(ROOT, 'research', 'fonts', 'NotoSansJP-Regular.otf'), 14)
    cols = 5
    n_sheets = 0
    for s in range(0, len(sel), per):
        chunk = sel[s:s + per]
        rws = -(-len(chunk) // cols)
        sheet = Image.new('RGB', (cols * TILE_W, rws * TILE_H), 'white')
        d = ImageDraw.Draw(sheet)
        for i, g in enumerate(chunk):
            x0, y0 = (i % cols) * TILE_W, (i // cols) * TILE_H
            d.rectangle([x0, y0, x0 + TILE_W - 1, y0 + TILE_H - 1], outline=(200, 200, 200))
            sheet.paste(bitmap(font, g).convert('RGB'), (x0 + 4, y0 + 4))
            d.text((x0 + 76, y0 + 2), rows[g][0], font=ref, fill=(0, 0, 160))
            d.text((x0 + 4, y0 + 70), f'{g:03X} x{use[g]} {rows[g][2]:.2f}', font=small, fill=(90, 90, 90))
            d.text((x0 + 126, y0 + 6), rows[g][3][:5], font=small, fill=(150, 0, 0))
        name = os.path.join(out, f'sheet_{n_sheets:02d}.png')
        sheet.save(name)
        n_sheets += 1
    print(len(sel), 'glyphs ->', n_sheets, 'sheets in', out)
    open(os.path.join(out, 'index.txt'), 'w', encoding='utf-8').write(
        '\n'.join(f'{i // per:02d} {g:03X} {rows[g][0]} {rows[g][3]}' for i, g in enumerate(sel)))


if __name__ == '__main__':
    main()
