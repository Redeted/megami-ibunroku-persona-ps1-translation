"""Export / import 4bpp and 8bpp PlayStation TIM images inside a game file (e.g. OPEN.BIN).

  python tools/tim.py list   <file>                       list TIMs (offset, bpp, VRAM rect, CLUT)
  python tools/tim.py export <file> <offset> <out.png>    palette PNG (exact indices + CLUT)
  python tools/tim.py import <file> <offset> <in.png> <out_file>
                                                          write the PNG's pixels back (same size);
                                                          colours are mapped to the nearest CLUT entry

<file> is read from original/ (relative name such as OPEN.BIN) unless it is an existing path.
Image data stays uncompressed at the same size, so the file layout does not change.
"""
import os
import struct
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def locate(name):
    return name if os.path.exists(name) else os.path.join(ROOT, 'original', *name.split('/'))


def parse(d, off):
    flag = struct.unpack_from('<I', d, off + 4)[0]
    bpp = {0: 4, 1: 8, 2: 16}[flag & 3]
    p = off + 8
    clut = None
    if flag & 8:
        bl, x, y, w, h = struct.unpack_from('<IHHHH', d, p)
        clut = dict(x=x, y=y, w=w, h=h, at=p + 12, n=w * h)
        p += bl
    bl, x, y, w, h = struct.unpack_from('<IHHHH', d, p)
    return dict(bpp=bpp, clut=clut, x=x, y=y, w=w, h=h, at=p + 12, end=p + bl,
                px_w={4: w * 4, 8: w * 2, 16: w}[bpp])


def find_tims(d):
    i = 0
    while True:
        i = d.find(b'\x10\x00\x00\x00', i)
        if i < 0:
            return
        if i + 8 <= len(d) and struct.unpack_from('<I', d, i + 4)[0] in (0, 1, 2, 8, 9, 10):
            try:
                t = parse(d, i)
                if t['end'] <= len(d):
                    yield i, t
            except struct.error:
                pass
        i += 4


def palette(d, t):
    c = t['clut']
    pal = []
    for k in range(min(c['n'], 256)):
        v = struct.unpack_from('<H', d, c['at'] + 2 * k)[0]
        r, g, b = (v & 31) << 3, ((v >> 5) & 31) << 3, ((v >> 10) & 31) << 3
        pal.append((r | r >> 5, g | g >> 5, b | b >> 5))
    return pal


def export(d, off, out):
    t = parse(d, off)
    assert t['bpp'] in (4, 8), 'only 4/8 bpp'
    w, h = t['px_w'], t['h']
    raw = d[t['at']:t['at'] + t['w'] * 2 * h]
    if t['bpp'] == 8:
        pix = raw
    else:
        pix = bytearray()
        for b in raw:
            pix += bytes((b & 15, b >> 4))
    im = Image.frombytes('P', (w, h), bytes(pix))
    pal = palette(d, t)
    flat = [c for rgb in pal for c in rgb]
    im.putpalette(flat + [0] * (768 - len(flat)))
    im.save(out)
    return t


def import_(d, off, png):
    t = parse(d, off)
    pal = palette(d, t)
    im = Image.open(png)
    assert im.size == (t['px_w'], t['h']), (im.size, (t['px_w'], t['h']))
    if im.mode == 'P':
        ip = im.getpalette()
        rgb = im.convert('RGB')
        idx = list(im.getdata())
        cmap = {}
        pix = []
        for i, v in enumerate(idx):
            if v not in cmap:
                c = (ip[3 * v], ip[3 * v + 1], ip[3 * v + 2])
                cmap[v] = min(range(len(pal)), key=lambda k: sum((pal[k][j] - c[j]) ** 2 for j in range(3)))
            pix.append(cmap[v])
    else:
        rgb = im.convert('RGB')
        cache = {}
        pix = []
        for c in rgb.getdata():
            if c not in cache:
                cache[c] = min(range(len(pal)), key=lambda k: sum((pal[k][j] - c[j]) ** 2 for j in range(3)))
            pix.append(cache[c])
    if t['bpp'] == 8:
        raw = bytes(pix)
    else:
        raw = bytes(pix[i] | (pix[i + 1] << 4) for i in range(0, len(pix), 2))
    out = bytearray(d)
    out[t['at']:t['at'] + len(raw)] = raw
    return bytes(out)


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        return
    d = open(locate(a[1]), 'rb').read()
    if a[0] == 'list':
        for off, t in find_tims(d):
            c = t['clut']
            print(f"{off:07X} {t['bpp']:2d}bpp vram=({t['x']},{t['y']}) {t['px_w']}x{t['h']}px"
                  + (f" clut=({c['x']},{c['y']}) n={c['n']}" if c else ''))
    elif a[0] == 'export':
        export(d, int(a[2], 16), a[3])
    elif a[0] == 'import':
        open(a[4], 'wb').write(import_(d, int(a[2], 16), a[3]))


if __name__ == '__main__':
    main()
