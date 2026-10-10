"""Translated bitmap text in OPEN.BIN (title screen graphics).

  python tools/title_gfx.py            build build/gfx/*.bin and preview PNGs (translation/images/)

Each EDIT redraws a text panel inside an 8bpp TIM with the project's VWF font (font/vwf_font.bin,
font/vwf_width.bin), centred, 1-bit, in a palette index taken from the image.  The result is the
whole pixel block of that TIM (same size, uncompressed), included by open/feature.asm at the
TIM's image data address. Only OPEN.BIN TIM 0x25840 (VRAM 832,0) is edited so far:
  * "Memory card checking" box shown for ~1 s before NEW GAME / LOAD GAME.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tim  # noqa: E402

ROOT = tim.ROOT
OUT = os.path.join(ROOT, 'build', 'gfx')
PREVIEW = os.path.join(ROOT, 'translation', 'images')

FONT = open(os.path.join(ROOT, 'font', 'vwf_font.bin'), 'rb').read()      # 95 glyphs x 16 rows
WIDTH = open(os.path.join(ROOT, 'font', 'vwf_width.bin'), 'rb').read()    # advance per glyph

# file, TIM offset, text panel (x0, y0, x1, y1 inclusive: area to clear), fill index, ink index, text
EDITS = [
    ('OPEN.BIN', 0x25840, (6, 73, 170, 95), 111, 2, 'Checking Memory Card'),
]


def text_width(s):
    return sum(WIDTH[ord(c) - 0x20] for c in s) - 1


def draw(pix, w, rect, fill, ink, s):
    x0, y0, x1, y1 = rect
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            pix[y * w + x] = fill
    tw = text_width(s)
    assert tw <= x1 - x0 + 1, f'{s!r} is {tw}px, panel {x1 - x0 + 1}px'
    x = x0 + (x1 - x0 + 1 - tw) // 2
    y = y0 + (y1 - y0 + 1 - 16) // 2
    for c in s:
        g = ord(c) - 0x20
        for r in range(16):
            bits = FONT[g * 16 + r]
            for b in range(8):
                if bits & (0x80 >> b):
                    pix[(y + r) * w + x + b] = ink
        x += WIDTH[g]
    return tw


def main():
    from PIL import Image
    os.makedirs(OUT, exist_ok=True)
    for name, off, rect, fill, ink, s in EDITS:
        d = open(tim.locate(name), 'rb').read()
        t = tim.parse(d, off)
        assert t['bpp'] == 8
        w, h = t['px_w'], t['h']
        pix = bytearray(d[t['at']:t['at'] + t['w'] * 2 * h])
        tw = draw(pix, w, rect, fill, ink, s)
        stem = f"{name.split('.')[0].lower()}_{off:X}"
        open(os.path.join(OUT, stem + '.bin'), 'wb').write(bytes(pix))
        print(f'{stem}: {s!r} {tw}px of {rect[2] - rect[0] + 1}px, data at {t["at"]:#x} ({len(pix)} bytes)')
        im = Image.frombytes('P', (w, h), bytes(pix))
        pal = tim.palette(d, t)
        flat = [c for rgb in pal for c in rgb]
        im.putpalette(flat + [0] * (768 - len(flat)))
        im.crop((0, 60, 180, 105)).resize((540, 135), Image.NEAREST).save(os.path.join(PREVIEW, stem + '_preview.png'))


if __name__ == '__main__':
    main()
