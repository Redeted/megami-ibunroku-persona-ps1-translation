"""English labels of the name-entry screen (NAME.BIN overlay + NAMEDT.BIN graphics).

  python tools/name_gfx.py     build build/gfx/namedt_111C.bin, namedt_clut4.bin, build/name_gfx.asm and previews

How the screen is built (found 2026-10-04 with a GPU dump + write watchpoints):
  * NAMEDT.BIN entry 11 (file offset 0x111C) is a 4bpp TIM, 256x64 px, VRAM (320,0), CLUT at (256,480):
    the button-label atlas. Every label is a 48x16 cell: row v=0 kana/katakana/alnum/kanji/clear-all,
    v=16 confirm ("OK?", YES, NO, left arrow stay), v=48 family/given/nickname/delete/back.
  * NAME.BIN has a 50-entry GsSPRITE layout table (RAM 0x800682EC, 20 bytes each: x, y, w, h, tpage, u, v,
    ..., clut y) that the overlay turns into sprites at 0x8007A80C. Sprites 7-22 draw the buttons.
    Sprites 23-25 draw the window labels family/given/nickname from a runtime font page (16x16 / 32x16 px);
    here they are redirected to the atlas cells of the bottom-left toggle button, with a new all-white
    palette row (CLUT row 4, y=484), and widened to 48 px.
Text is drawn with the dialogue VWF font (font/vwf_*.bin), vertical gradient (palette index 1..13) and a
black outline (index 15) like the original labels.
"""
import os
import struct
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tim  # noqa: E402

ROOT = tim.ROOT
OUT = os.path.join(ROOT, 'build', 'gfx')
PREVIEW = os.path.join(ROOT, 'translation', 'images')
TIM_OFF = 0x111C
FONT = open(os.path.join(ROOT, 'font', 'vwf_font.bin'), 'rb').read()
WIDTH = open(os.path.join(ROOT, 'font', 'vwf_width.bin'), 'rb').read()

# (u, v) of a 48x16 cell -> English
CELLS = {
    (0, 0): 'Hira', (48, 0): 'Kata', (96, 0): 'ABC', (144, 0): 'Kanji', (192, 0): 'Clear',
    (0, 16): 'Enter',
    (0, 48): 'Family', (48, 48): 'Given', (96, 48): 'Nick', (144, 48): 'Delete', (192, 48): 'Back',
}
# window labels (sprite index -> atlas cell); x centred on 136 like the originals, 48 px wide
WINDOW_LABELS = {23: (0, 48), 24: (48, 48), 25: (96, 48)}
LABEL_X = 112
LABEL_CLUT_ROW = 4             # y = 480 + 4
SPRITE_TABLE = 0x800682EC      # NAME.BIN, 20 bytes per sprite


def text_rows(s):
    """-> list of (x, rowbits) glyph bitmaps as a set of (x, y) ink pixels and the text width"""
    ink = set()
    x = 0
    for c in s:
        g = ord(c) - 0x20
        for r in range(16):
            bits = FONT[g * 16 + r]
            for b in range(8):
                if bits & (0x80 >> b):
                    ink.add((x + b, r))
        x += WIDTH[g]
    return ink, x - 1


def draw_cell(pix, w, u, v, text):
    for y in range(16):
        for x in range(48):
            pix[(v + y) * w + u + x] = 0
    ink, tw = text_rows(text)
    ys = [y for _, y in ink]
    y0, y1 = min(ys), max(ys)
    h = y1 - y0 + 1
    ox = u + (48 - tw) // 2
    oy = v + (16 - h) // 2
    body = {}
    for x, y in ink:
        body[(x, y - y0)] = 1 + (y - y0) * 12 // max(h - 1, 1)     # gradient 1..13
    for (x, y), idx in body.items():
        pix[(oy + y) * w + ox + x] = idx
    for (x, y) in body:                                           # outline
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                px, py = ox + x + dx, oy + y + dy
                if (x + dx, y + dy) not in body and u <= px < u + 48 and v <= py < v + 16:
                    if pix[py * w + px] == 0:
                        pix[py * w + px] = 15
    return tw


def main():
    from PIL import Image
    os.makedirs(OUT, exist_ok=True)
    d = open(tim.locate('NAMEDT.BIN'), 'rb').read()
    t = tim.parse(d, TIM_OFF)
    w, h = t['px_w'], t['h']
    raw = d[t['at']:t['at'] + t['w'] * 2 * h]
    pix = bytearray()
    for b in raw:
        pix += bytes((b & 15, b >> 4))
    for (u, v), s in CELLS.items():
        tw = draw_cell(pix, w, u, v, s)
        assert tw + 2 <= 48, f'{s!r} is {tw}px'
    packed = bytes(pix[i] | (pix[i + 1] << 4) for i in range(0, len(pix), 2))
    open(os.path.join(OUT, 'namedt_111C.bin'), 'wb').write(packed)
    # white palette row (STP set so the black outline stays opaque)
    row = [0]
    for i in range(1, 15):
        c = 31 - i // 4
        row.append(0x8000 | (c << 10) | (c << 5) | c)
    row.append(0x8000)
    open(os.path.join(OUT, 'namedt_clut4.bin'), 'wb').write(struct.pack('<16H', *row))
    clut_at = t['clut']['at'] + 32 * LABEL_CLUT_ROW
    # preview with the three palettes
    pal_orange = tim.palette(d, t)[16:32]
    pal_white = [((v & 31) << 3, ((v >> 5) & 31) << 3, ((v >> 10) & 31) << 3) for v in row]
    for name, pal in (('orange', pal_orange), ('white', pal_white)):
        im = Image.frombytes('P', (w, h), bytes(pix))
        flat = [c for rgb in pal for c in rgb]
        im.putpalette(flat + [0] * (768 - len(flat)))
        im.convert('RGB').resize((w * 3, h * 3), Image.NEAREST).save(os.path.join(PREVIEW, f'namedt_111C_{name}.png'))
    # assembler patch
    with open(os.path.join(ROOT, 'build', 'name_gfx.asm'), 'w', newline=chr(10)) as o:
        o.write(';; generated by tools/name_gfx.py - do not edit' + chr(10))
        o.write(f'.org NAMEDT_ADDR + {t["at"]:#x}{chr(10)}    .incbin "build/gfx/namedt_111C.bin"{chr(10)}')
        o.write(f'.org NAMEDT_ADDR + {clut_at:#x}{chr(10)}    .incbin "build/gfx/namedt_clut4.bin"{chr(10)}')
    with open(os.path.join(ROOT, 'build', 'name_sprites.asm'), 'w', newline=chr(10)) as o:
        o.write(';; generated by tools/name_gfx.py - window labels -> atlas cells (NAME.BIN sprite table)' + chr(10))
        for k, (u, v) in WINDOW_LABELS.items():
            e = SPRITE_TABLE + 20 * k
            o.write(f'.org {e:#x}{chr(10)}    .halfword {LABEL_X}   ; x{chr(10)}')
            o.write(f'.org {e + 8:#x}{chr(10)}    .byte 0x30, 0x10, 5, {u}, {v}   ; w, h, tpage, u, v{chr(10)}')
            o.write(f'.org {e + 16:#x}{chr(10)}    .halfword {480 + LABEL_CLUT_ROW}   ; clut y{chr(10)}')
    print('name gfx:', ', '.join(f'{s}={text_rows(s)[1]}px' for s in CELLS.values()))


if __name__ == '__main__':
    main()
