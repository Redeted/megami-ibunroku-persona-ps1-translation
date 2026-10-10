"""Battle small-font page with the redrawn lowercase / punctuation cells (tools/smallfont_lc.py) in /B/BF.BIN.

  python tools/btlfont.py        write build/B/BF.BIN (original/B/BF.BIN = /B/BF.BIN of the original disc,
                                 `python tools/extract.py <original.bin> original B/BF.BIN`)

At battle start BTLP decompresses (MES codec, decoder BTLP 0x80081C08; tools/mescodec.py) a 4bpp TIM from the battle
field data (/B/BF.BIN, one copy per battle field, 67 identical copies) and uploads it to VRAM (960,256) 64x128: the
battle small-font page. Its cells 0xCD+ are battle icons, cell rows 0-2 match every other small-font page. Each copy
is decoded, rows 0-2 get the redrawn a-z . ' (menu_gfx.lc_page), and it is re-encoded with the optimal-parse encoder
(smaller than the original stream, so it is written in place; the bytes after the end code are left alone).
Replaces the earlier VRAM copy hook, which copied garbage in overworld battles.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mescodec   # noqa: E402
import menu_gfx   # noqa: E402
import tim        # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'original', 'B', 'BF.BIN')
OUT = os.path.join(ROOT, 'build', 'B', 'BF.BIN')
ROWS = 36                          # cell rows 0-2 (12 px each)
# first bytes of the compressed page (TIM header 10 00 00 00 08 00 00 00 ec 00 ... as literal / zero-run tokens)
PREFIX = bytes.fromhex('8010e28008e280ece482e0011' + '0e08007e281ff7f')


def main():
    d = bytearray(open(SRC, 'rb').read())
    hits = []
    i = d.find(PREFIX)
    while i >= 0:
        raw, used = mescodec.decode(bytes(d[i:i + 0x4000]), 0x8000)
        t = tim.parse(raw, 0)
        if (t['w'], t['h']) == (64, 128):           # the TIM says (768,0); BTLP uploads it to (960,256) itself
            hits.append((i, used, raw))
        i = d.find(PREFIX, i + 1)
    if not hits:
        raise SystemExit('btlfont: no battle font page found in BF.BIN')
    cache = {}
    for s, used, raw in hits:
        if raw not in cache:
            at = tim.parse(raw, 0)['at']
            new = bytearray(raw)
            new[at:at + 128 * ROWS] = menu_gfx.lc_page(bytes(raw[at:at + 128 * ROWS]), 256)
            cache[raw] = mescodec.encode_opt(bytes(new))
        enc = cache[raw]
        if len(enc) > used:
            raise SystemExit(f'btlfont: page at {s:#x} re-encodes to {len(enc)} bytes > {used}')
        d[s:s + len(enc)] = enc
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, 'wb').write(bytes(d))
    print(f'btlfont: {len(hits)} battle font pages patched ({len(cache)} distinct, '
          f'{len(next(iter(cache.values())))} of {hits[0][1]} bytes) -> {OUT}')


if __name__ == '__main__':
    main()
