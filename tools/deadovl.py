"""Unreferenced functions inside an overlay (candidate homes for patch code that only that
overlay needs).

  python tools/deadovl.py BTLP.BIN [min_size]

A function start is any jal target inside the overlay plus every word after a `jr ra` + delay
slot that begins with addiu sp,sp,-N. A function is reported when nothing on the disc (this
overlay, the main EXE, all other overlays) contains a jal/j to it, its address as a 32-bit word
(function pointer tables), or a lui/addiu|ori pair forming its address.
"""
import glob
import os
import struct
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 0x800643C4


def words(d):
    return struct.unpack_from(f'<{len(d) // 4}I', d, 0)


def lui_pairs(w):
    out = set()
    for i, x in enumerate(w):
        if x >> 26 != 0x0F:
            continue
        rt, hi = (x >> 16) & 31, (x & 0xFFFF) << 16
        for y in w[i + 1:i + 9]:
            op = y >> 26
            if op in (0x09, 0x0D) and (y >> 21) & 31 == rt:
                imm = y & 0xFFFF
                if op == 0x09 and imm & 0x8000:
                    imm -= 0x10000
                out.add((hi + imm) & 0xFFFFFFFF)
    return out


def main():
    name = sys.argv[1]
    minsize = int(sys.argv[2]) if len(sys.argv) > 2 else 256
    path = os.path.join(ROOT, 'original', name)
    d = open(path, 'rb').read()
    n4 = len(d) & ~3
    w = words(d[:n4])
    lo, hi = BASE, BASE + n4
    refs_jal, refs_word, refs_pair = set(), set(), set()
    others = [os.path.join(ROOT, 'original', 'SLPS_005.00')] + sorted(glob.glob(os.path.join(ROOT, 'original', '*.BIN')))
    for p in others:
        dd = open(p, 'rb').read()
        if len(dd) > 3_000_000:
            continue
        ww = words(dd[:len(dd) & ~3])
        for x in ww:
            if x >> 26 in (2, 3):
                refs_jal.add(0x80000000 | ((x & 0x3FFFFFF) << 2))
            if lo <= x < hi:
                refs_word.add(x)
        refs_pair |= {a for a in lui_pairs(ww) if lo <= a < hi}
    starts = {t for t in refs_jal if lo <= t < hi}
    for i in range(len(w) - 2):
        if w[i] == 0x03E00008 and (w[i + 2] >> 16) == 0x27BD and (w[i + 2] & 0x8000):
            starts.add(lo + (i + 2) * 4)
    starts = sorted(starts)
    total, out = 0, []
    for k, s in enumerate(starts):
        end = starts[k + 1] if k + 1 < len(starts) else hi
        i0, i1 = (s - lo) // 4, (end - lo) // 4
        last = max((i for i in range(i0, i1) if w[i] == 0x03E00008), default=None)
        if last is None:
            continue
        fend = lo + (last + 2) * 4
        size = fend - s
        if s in refs_jal or s in refs_word or s in refs_pair or size < minsize:
            continue
        out.append((s, fend, size))
        total += size
    for s, e, sz in out:
        print(f'{s:08X}-{e:08X} {sz:5d} bytes')
    print(len(out), 'unreferenced functions', total, 'bytes')


if __name__ == '__main__':
    main()
