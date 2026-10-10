"""Battle label atlas: English stat labels on the level-up / status screens (in /B/BF.BIN, after tools/btlfont.py).

  python tools/btlstat.py     patch build/B/BF.BIN in place (run after btlfont.py)

/B/BF.BIN holds 67 identical copies of a compressed 4bpp TIM (MES codec, 64x128 words) that BTLP uploads to VRAM
(960,384): the battle label atlas (menu labels FIGHT/CONTACT.., status names, icons; sprites are 24x12 cells, CLUT 0x79D0).
Its white kanji cells (colour 1, shadow 15) are the stat labels of the level-up allocation screen and the battle status page.
Cells (u, v = VRAM page coordinates, atlas row = v - 128), redrawn as letters of 5x7 at a 6 px pitch (like menu_gfx.LABELS):
  v=128: u=168 剣攻 -> SWD, u=192 命中 -> HIT, u=216 銃攻 -> GUN
  v=144: u=144 防御 -> DEF, u=168 回避 -> EVA, u=192 魔威 -> MATK, u=216 魔防 -> MDEF
  v=156: u=136 力 -> STR, u=160 体 -> VIT, u=184 技 -> DEX, u=208 速 -> AGI;  v=168: u=136 運 -> LUK
(Found 2026-10-07 with a GPU dump of the level-up screen: five 24x12 sprites at x=48, six at x=192/248.)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mescodec   # noqa: E402
import menu_gfx   # noqa: E402
import tim        # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BF = os.path.join(ROOT, 'build', 'B', 'BF.BIN')
PREFIX = bytes.fromhex('8010e28008e2')
ATLAS_V0 = 128
OLD = 16608                      # decoded size of the label atlas TIM (the font page / icon atlas differ)

LABELS = [('SWD', 168, 128), ('HIT', 192, 128), ('GUN', 216, 128),
          ('DEF', 144, 144), ('EVA', 168, 144), ('MATK', 192, 144), ('MDEF', 216, 144),
          ('STR', 136, 156), ('VIT', 160, 156), ('DEX', 184, 156), ('AGI', 208, 156), ('LUK', 136, 168)]
G = dict(menu_gfx.G57)
G.update({
    'S': ['01111', '10000', '10000', '01110', '00001', '00001', '11110'],
    'W': ['10001', '10001', '10001', '10101', '10101', '11011', '10001'],
    'G': ['01110', '10001', '10000', '10111', '10001', '10001', '01111'],
    'U': ['10001', '10001', '10001', '10001', '10001', '10001', '01110'],
    'N': ['10001', '11001', '10101', '10011', '10001', '10001', '10001'],
    'R': ['11110', '10001', '10001', '11110', '10100', '10010', '10001'],
    'X': ['10001', '10001', '01010', '00100', '01010', '10001', '10001'],
    'L': ['10000', '10000', '10000', '10000', '10000', '10000', '11111'],
})
WHITE, SHADOW = 1, 15


def draw(pix, w):
    for text, u, v in LABELS:
        y0 = v - ATLAS_V0
        for y in range(12):
            for x in range(24):
                pix[(y0 + y) * w + u + x] = 0
        x0 = (24 - 6 * len(text) + 1) // 2
        main = {(x0 + 6 * i + b, 2 + r) for i, c in enumerate(text) for r, row in enumerate(G[c])
                for b, bit in enumerate(row) if bit == '1'}
        for x, y in main:
            pix[(y0 + y) * w + u + x] = WHITE
        for x, y in main:
            if (x + 1, y + 1) not in main and x + 1 < 24:
                pix[(y0 + y + 1) * w + u + x + 1] = SHADOW


def main():
    d = bytearray(open(BF, 'rb').read())
    n, cache = 0, {}
    i = d.find(PREFIX)
    while i >= 0:
        raw, used = mescodec.decode(bytes(d[i:i + 0x6000]), 0x10000)
        if len(raw) == OLD:
            if raw not in cache:
                t = tim.parse(raw, 0)
                pix = menu_gfx.unpack(raw, t)
                draw(pix, 256)
                new = bytearray(raw)
                new[t['at']:t['at'] + len(pix) // 2] = menu_gfx.pack(pix)
                cache[raw] = mescodec.encode_opt(bytes(new))
            enc = cache[raw]
            if len(enc) > used:
                raise SystemExit(f'btlstat: atlas at {i:#x} re-encodes to {len(enc)} bytes > {used}')
            d[i:i + len(enc)] = enc
            n += 1
        i = d.find(PREFIX, i + 1)
    if not n:
        raise SystemExit('btlstat: label atlas not found in BF.BIN')
    open(BF, 'wb').write(bytes(d))
    print(f'btlstat: {n} label atlases patched -> {BF}')


if __name__ == '__main__':
    main()
