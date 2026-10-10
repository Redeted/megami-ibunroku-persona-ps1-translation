"""English bitmap labels of the ADV menus (ADV/ADVCMD.BIN): save/load slot screen and command labels.

  python tools/menu_gfx.py      write build/ADV/ADVCMD.BIN (same size, pixel data edited) and previews

Findings (2026-10-04, GPU dump of the save screen):
  * ADVCMD.BIN TIM 0x281D8 (4bpp 256x64, loaded to VRAM (768,416)) is the label atlas of 48x16 cells, drawn as 48x16
    sprites: u=96,v=48 "slot 1" (header of the slot screen), u=144,v=48 "slot 2", u=48,v=32 "execute",
    u=96,v=32 "settings". Its palette: indices 1..14 = light-to-dark orange ramp, 15 = black outline.
  * ADVCMD.BIN TIM 0x38 (4bpp 256x256) is the 8x12 small-font page (loaded to VRAM (512,256) and (896,256));
    the tag after every slot row is three 8x12 sprites at u=224,232,240, v=168 ("data"). It is replaced by "DATA" drawn
    with a 5x7 pixel font on a 6 px pitch (24 px = the three cells), palette index 3 like the neighbouring labels.
Text in the 48x16 cells uses the dialogue VWF font (font/vwf_*.bin) like tools/name_gfx.py.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tim  # noqa: E402
import smallfont_lc  # noqa: E402

ROOT = tim.ROOT
PREVIEW = os.path.join(ROOT, 'translation', 'images')
FONT = open(os.path.join(ROOT, 'font', 'vwf_font.bin'), 'rb').read()
WIDTH = open(os.path.join(ROOT, 'font', 'vwf_width.bin'), 'rb').read()

ATLAS = 0x281D8
PAGE = 0x38
CELLS = {(96, 48): 'SLOT 1', (144, 48): 'SLOT 2', (48, 32): 'EXEC', (96, 32): 'SET'}
RAMP = [13, 11, 12, 14, 8, 7, 9, 4, 10, 5, 6, 3, 2, 1]          # light -> dark (palette luminance)
OUTLINE = 15

# 5x7 glyphs for the "DATA" tag (small font cells are 8x12, orange index 3)
G57 = {
    'D': ['11110', '10001', '10001', '10001', '10001', '10001', '11110'],
    'A': ['01110', '10001', '10001', '11111', '10001', '10001', '10001'],
    'T': ['11111', '00100', '00100', '00100', '00100', '00100', '00100'],
}
TAG = ('DATA', 224, 168)           # text, u, v of the first of the three 8x12 cells
# Persona status page: the kanji labels 魔攻 / 魔防 are 3 bitmap cells each in the page (BG tiles 0x3CB.. / 0x3D1..,
# ADV 0x8006FA7C; same page, CLUT 0x683C). Redrawn as 4 letters of 5x7 at a 6 px pitch, colour 1 + shadow 2 like
# the kanji. Patched in every page copy whose cells still hold the kanji (label_rows / smallfont_pages.py).
G57.update({
    'M': ['10001', '11011', '10101', '10101', '10001', '10001', '10001'],
    'K': ['10001', '10010', '10100', '11000', '10100', '10010', '10001'],
    'E': ['11111', '10000', '10000', '11110', '10000', '10000', '11111'],
    'F': ['11111', '10000', '10000', '11110', '10000', '10000', '10000'],
    'H': ['10001', '10001', '10001', '11111', '10001', '10001', '10001'],
    'I': ['01110', '00100', '00100', '00100', '00100', '00100', '01110'],
    'V': ['10001', '10001', '10001', '10001', '10001', '01010', '00100'],
})
# equipment screen stat labels 攻撃 / 命中 / 防御 / 回避 are the 12 px kanji at row 156, u = 112, 136, 160, 184
LABELS = [('MATK', 208, 156), ('MDEF', 0, 168), ('ATK', 112, 156), ('HIT', 136, 156), ('DEF', 160, 156),
          ('EVA', 184, 156)]
LABEL_Y0, LABEL_Y1 = 156, 180      # pixel rows holding the two labels


def text_pixels(s):
    ink, x = set(), 0
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
    ink, tw = text_pixels(text)
    ys = [y for _, y in ink]
    y0, y1 = min(ys), max(ys)
    h = y1 - y0 + 1
    ox, oy = u + (48 - tw) // 2, v + (16 - h) // 2
    body = {(x, y - y0): RAMP[(y - y0) * (len(RAMP) - 1) // max(h - 1, 1)] for x, y in ink}
    for (x, y), idx in body.items():
        pix[(oy + y) * w + ox + x] = idx
    for (x, y) in body:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                px, py = ox + x + dx, oy + y + dy
                if (x + dx, y + dy) not in body and u <= px < u + 48 and v <= py < v + 16 and pix[py * w + px] == 0:
                    pix[py * w + px] = OUTLINE
    return tw


def pack(pix):
    return bytes(pix[i] | (pix[i + 1] << 4) for i in range(0, len(pix), 2))


def unpack(d, t):
    raw = d[t['at']:t['at'] + t['w'] * 2 * t['h']]
    pix = bytearray()
    for b in raw:
        pix += bytes((b & 15, b >> 4))
    return pix


PAGE_COPIES = {'ADV/ADVCMD0.BIN': (0x240, 248), 'OPEN.BIN': (0x35AA0, 256)}   # other small-font pages: pixel offset, width
GLYPH_ROWS = 3 * 12                  # cell rows 0-2 (the kana cells reused for a-z; identical in every copy)


def lc_page(raw, w):
    """4bpp page bytes (w px wide) -> same with lowercase a-z drawn (tools/smallfont_lc.py)."""
    pix = bytearray()
    for b in raw:
        pix += bytes((b & 15, b >> 4))
    smallfont_lc.draw(pix, w)
    return pack(pix)


def draw_labels(pix, w, y0=0):
    """Draw LABELS into 4bpp pixels of a page (w px wide) whose first row is page row y0."""
    for text, u, v in LABELS:
        for y in range(12):
            for x in range(24):
                pix[(v - y0 + y) * w + u + x] = 0
        x0 = (24 - 6 * len(text) + 1) // 2
        main = {(x0 + 6 * i + b, 2 + r) for i, c in enumerate(text) for r, row in enumerate(G57[c])
                for b, bit in enumerate(row) if bit == '1'}
        for x, y in main:
            pix[(v - y0 + y) * w + u + x] = 1
        for x, y in main:
            if (x + 1, y + 1) not in main and x + 1 < 24:
                pix[(v - y0 + y + 1) * w + u + x + 1] = 2


def label_rows(b, at, bpr, ref):
    """Patch the label cells of a page copy (bytearray b, page row 0 at offset at, bpr bytes per row) in place,
    if those cells hold the same kanji as the reference page bytes `ref` (128 bytes per row). -> True if patched."""
    for text, u, v in LABELS:
        for y in range(12):
            r = (v + y)
            if b[at + r * bpr + u // 2:at + r * bpr + (u + 24) // 2] != ref[r * 128 + u // 2:r * 128 + (u + 24) // 2]:
                return False
    w = bpr * 2
    raw = bytes(b[at + LABEL_Y0 * bpr:at + LABEL_Y1 * bpr])
    pix = bytearray()
    for x in raw:
        pix += bytes((x & 15, x >> 4))
    draw_labels(pix, w, LABEL_Y0)
    b[at + LABEL_Y0 * bpr:at + LABEL_Y1 * bpr] = pack(pix)
    return True


def other_pages():
    ref = open(tim.locate('ADV/ADVCMD.BIN'), 'rb').read()
    t = tim.parse(ref, PAGE)
    page = ref[t['at']:t['at'] + 128 * 256]
    for name, (at, w) in PAGE_COPIES.items():
        bpr = w // 2
        d = bytearray(open(os.path.join(ROOT, 'original', name), 'rb').read())
        for y in range(GLYPH_ROWS):
            assert d[at + y * bpr:at + y * bpr + bpr] == page[y * 128:y * 128 + bpr], f'{name}: glyph row {y} differs'
        old = bytes(d[at:at + bpr * GLYPH_ROWS])
        new = lc_page(old, w)
        if name == 'OPEN.BIN':                       # armips owns build/OPEN.BIN: emit a patch for main.asm
            with open(os.path.join(ROOT, 'build', 'open_smallfont.asm'), 'w', newline=chr(10)) as o:
                o.write(';; generated by tools/menu_gfx.py - lowercase a-z in the small-font page of OPEN.BIN' + chr(10))
                i = 0
                while i < len(old):
                    if new[i] != old[i]:
                        j = i
                        while j < len(old) and new[j] != old[j]:
                            j += 1
                        o.write(f'.org OPEN_ADDR + {at + i:#x}' + chr(10) + '    .byte ' +
                                ', '.join(f'0x{x:02X}' for x in new[i:j]) + chr(10))
                        i = j
                    else:
                        i += 1
        else:
            d[at:at + bpr * GLYPH_ROWS] = new
            label_rows(d, at, bpr, page)
            open(os.path.join(ROOT, 'build', name), 'wb').write(bytes(d))


def main():
    from PIL import Image
    src = open(tim.locate('ADV/ADVCMD.BIN'), 'rb').read()
    out = bytearray(src)
    # label atlas
    t = tim.parse(src, ATLAS)
    w = t['px_w']
    pix = unpack(src, t)
    for (u, v), s in CELLS.items():
        tw = draw_cell(pix, w, u, v, s)
        assert tw + 2 <= 48, f'{s!r} is {tw}px'
    out[t['at']:t['at'] + t['w'] * 2 * t['h']] = pack(pix)
    pal = tim.palette(src, t)
    im = Image.frombytes('P', (w, t['h']), bytes(pix))
    im.putpalette([c for rgb in pal for c in rgb] + [0] * (768 - 3 * len(pal)))
    im.convert('RGB').resize((w * 3, t['h'] * 3), Image.NEAREST).save(os.path.join(PREVIEW, 'advcmd_atlas_preview.png'))
    # small-font page: "DATA" tag
    t2 = tim.parse(src, PAGE)
    w2 = t2['px_w']
    pg = unpack(src, t2)
    text, u, v = TAG
    for y in range(12):
        for x in range(24):
            pg[(v + y) * w2 + u + x] = 0
    for i, c in enumerate(text):
        for r, row in enumerate(G57[c]):
            for b, bit in enumerate(row):
                if bit == '1':
                    pg[(v + 2 + r) * w2 + u + 6 * i + b] = 3
    smallfont_lc.draw(pg, w2)                       # lowercase a-z in reused kana cells, tools/smallfont_lc.py
    draw_labels(pg, w2)                             # MATK / MDEF status labels
    out[t2['at']:t2['at'] + t2['w'] * 2 * t2['h']] = pack(pg)
    os.makedirs(os.path.join(ROOT, 'build', 'ADV'), exist_ok=True)
    open(os.path.join(ROOT, 'build', 'ADV', 'ADVCMD.BIN'), 'wb').write(bytes(out))
    other_pages()
    print('menu gfx:', ', '.join(f'{s}={text_pixels(s)[1]}px' for s in CELLS.values()), '+ DATA tag; ADVCMD.BIN',
          len(out), 'bytes')


if __name__ == '__main__':
    main()
