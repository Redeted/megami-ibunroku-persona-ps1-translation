"""Find functions in SLPS_005.00 that nothing references.

A function start is any jal target in the main EXE plus every word after a
'jr ra' + delay slot that begins with 'addiu sp,sp,-N'. A function is
reported as unreferenced when no binary on the disc (main EXE, overlays,
EXEs) contains:
  - a jal/j to its start, or
  - its address as a 32-bit word anywhere (function pointer tables), or
  - a lui/addiu|ori pair forming its address.
Usage: python tools/deadfuncs.py [min_size]
"""
import glob
import os
import struct
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLPS_BASE = 0x80010000 - 0x800
MIN = int(sys.argv[1]) if len(sys.argv) > 1 else 256


def words(data):
    return struct.unpack_from(f"<{len(data) // 4}I", data, 0)


def lui_pairs(w, base):
    """Addresses formed by lui rX followed (within 8 instr) by addiu/ori rY, rX, imm."""
    out = set()
    for i, x in enumerate(w):
        if x >> 26 != 0x0F:          # lui
            continue
        rt, hi = (x >> 16) & 31, (x & 0xFFFF) << 16
        for y in w[i + 1:i + 9]:
            op = y >> 26
            if op in (0x09, 0x0D) and (y >> 21) & 31 == rt:   # addiu / ori
                imm = y & 0xFFFF
                if op == 0x09 and imm & 0x8000:
                    imm -= 0x10000
                out.add((hi + imm) & 0xFFFFFFFF)
    return out


slps = open(os.path.join(ROOT, "original", "SLPS_005.00"), "rb").read()
text = slps[0x800:]
w = words(text)

binaries = [os.path.join(ROOT, "original", "SLPS_005.00")] + \
    sorted(glob.glob(os.path.join(ROOT, "original", "*.BIN"))) + \
    sorted(glob.glob(os.path.join(ROOT, "original", "EXE", "*.EXE")))
jal_targets, word_refs, pair_refs = set(), set(), set()
for path in binaries:
    data = open(path, "rb").read()
    if len(data) > 3_000_000:
        continue
    ww = words(data[:len(data) & ~3])
    for x in ww:
        if x >> 26 in (2, 3):
            jal_targets.add(0x80000000 | ((x & 0x3FFFFFF) << 2))
        if 0x80010000 <= x < 0x80056000:
            word_refs.add(x)
    pair_refs |= lui_pairs(ww, 0)

starts = {t for t in jal_targets if 0x80010000 <= t < 0x80056000}
for i in range(len(w) - 2):
    if w[i] == 0x03E00008 and (w[i + 2] >> 16) == 0x27BD and (w[i + 2] & 0x8000):
        starts.add(0x80010000 + (i + 2) * 4)
starts = sorted(starts)

dead = []
for k, s in enumerate(starts):
    end = starts[k + 1] if k + 1 < len(starts) else 0x80056000
    # trim to the last 'jr ra' + delay slot inside the span
    i0, i1 = (s - 0x80010000) // 4, (end - 0x80010000) // 4
    last = max((i for i in range(i0, i1) if w[i] == 0x03E00008), default=None)
    if last is None:
        continue
    fend = 0x80010000 + (last + 2) * 4
    size = fend - s
    referenced = s in jal_targets or s in word_refs or s in pair_refs
    if not referenced and size >= MIN:
        dead.append((s, fend, size))

total = 0
for s, e, n in dead:
    total += n
    print(f"{s:08X}-{e:08X} {n:6} bytes")
print(f"{len(dead)} unreferenced functions >= {MIN} bytes, {total} bytes total")
