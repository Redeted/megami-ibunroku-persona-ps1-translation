"""Lowercase a-z for the 8x12 "small font" (menus, item / skill / Persona names, battle panels).

The font page is a 4bpp 256x256 TIM with glyph g at row g // 31, column g % 31 (8x12 cells, see tools/items.py).
Its renderers read ONE byte per character (two-byte codes are not supported) and every byte value is already a glyph
(0xD9.. are the coloured digits / icons of the HP-SP numbers), so lowercase has no free code: instead 26 hiragana that
the small-font tables (practically) never use are redrawn as a..z, and English text writes a..z as those codes.
A Japanese small-font string still containing one of them shows a Latin letter there (acceptable once the tables are
translated).  Page copies on the disc: ADV/ADVCMD.BIN, ADV/ADVCMD0.BIN, OPEN.BIN (tools/menu_gfx.py patches all three).
Style of the capitals: colour 1, shadow colour 2 at (+1,+1), capitals span cell rows 2..8. Verified 2026-10-05.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import etext  # noqa: E402

# a..z = the LOW BYTES of the full-width glyphs ａ..ｚ (0x723..): the name entry screen stores only the low byte of a
# typed character, so typed lowercase names land on exactly these cells (もやゆらを + voiced kana, cell rows 1-2).
LC_CODES = [etext.char2g[chr(0xFF41 + i)] & 0xFF for i in range(26)]
KANA = ''.join(etext.glyph[c] for c in LC_CODES)   # the hiragana whose small-font cells are redrawn
assert len(set(LC_CODES)) == 26 and max(LC_CODES) < 0xD9
# punctuation the page lacks as a single-byte glyph, drawn over more rare hiragana (cell rows 0-2 like a..z)
PUNCT = {"'": 'ゎ', '.': 'ぽ'}
PUNCT_CODES = {c: etext.char2g[k] for c, k in PUNCT.items()}
assert not set(PUNCT_CODES.values()) & set(LC_CODES)


# 5-column bitmaps; (top row in the cell, rows)
G = {
    'a': (4, ['.111.', '....1', '.1111', '1...1', '.1111']),
    'b': (2, ['1....', '1....', '1111.', '1...1', '1...1', '1...1', '1111.']),
    'c': (4, ['.111.', '1....', '1....', '1....', '.111.']),
    'd': (2, ['....1', '....1', '.1111', '1...1', '1...1', '1...1', '.1111']),
    'e': (4, ['.111.', '1...1', '11111', '1....', '.111.']),
    'f': (2, ['..11.', '.1...', '1111.', '.1...', '.1...', '.1...', '.1...']),
    'g': (4, ['.1111', '1...1', '1...1', '1...1', '.1111', '....1', '.111.']),
    'h': (2, ['1....', '1....', '1111.', '1...1', '1...1', '1...1', '1...1']),
    'i': (2, ['..1..', '.....', '.11..', '..1..', '..1..', '..1..', '.111.']),
    'j': (2, ['...1.', '.....', '..11.', '...1.', '...1.', '...1.', '...1.', '1..1.', '.11..']),
    'k': (2, ['1....', '1....', '1..1.', '1.1..', '11...', '1.1..', '1..1.']),
    'l': (2, ['.11..', '..1..', '..1..', '..1..', '..1..', '..1..', '.111.']),
    'm': (4, ['11.1.', '1.1.1', '1.1.1', '1.1.1', '1.1.1']),
    'n': (4, ['1111.', '1...1', '1...1', '1...1', '1...1']),
    'o': (4, ['.111.', '1...1', '1...1', '1...1', '.111.']),
    'p': (4, ['1111.', '1...1', '1...1', '1...1', '1111.', '1....', '1....']),
    'q': (4, ['.1111', '1...1', '1...1', '1...1', '.1111', '....1', '....1']),
    'r': (4, ['1.11.', '11..1', '1....', '1....', '1....']),
    's': (4, ['.1111', '1....', '.111.', '....1', '1111.']),
    't': (3, ['.1...', '1111.', '.1...', '.1...', '.1..1', '..11.']),
    'u': (4, ['1...1', '1...1', '1...1', '1..11', '.11.1']),
    'v': (4, ['1...1', '1...1', '1...1', '.1.1.', '..1..']),
    'w': (4, ['1...1', '1.1.1', '1.1.1', '1.1.1', '.1.1.']),
    'x': (4, ['1...1', '.1.1.', '..1..', '.1.1.', '1...1']),
    'y': (4, ['1...1', '1...1', '1...1', '1...1', '.1111', '....1', '.111.']),
    'z': (4, ['11111', '...1.', '..1..', '.1...', '11111']),
    "'": (2, ['..11.', '...1.', '..1..']),
    '.': (7, ['.11..', '.11..']),
}


def code(c):
    if c in PUNCT_CODES:
        return PUNCT_CODES[c]
    return LC_CODES[ord(c) - ord('a')]


def draw(pix, w):
    """pix: list/bytearray of 4bpp indices of the 256-px-wide page."""
    for c in 'abcdefghijklmnopqrstuvwxyz' + ''.join(PUNCT):
        g = code(c)
        x0, y0 = (g % 31) * 8, (g // 31) * 12
        for y in range(12):
            for x in range(8):
                pix[(y0 + y) * w + x0 + x] = 0
        top, rows = G[c]
        main = {(x, top + r) for r, row in enumerate(rows) for x, b in enumerate(row) if b == '1'}
        for x, y in main:
            pix[(y0 + y) * w + x0 + x] = 1
        for x, y in main:
            sx, sy = x + 1, y + 1
            if (sx, sy) not in main and sx < 8 and sy < 12:
                pix[(y0 + sy) * w + x0 + sx] = 2
