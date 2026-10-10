"""Print contiguous changed chunks between an original and a built binary as
RAM writes (for live-testing patches in the emulator before a disc rebuild).

Usage: python tools/ramdiff.py <original> <built> <file_base_addr>
"""
import sys

orig, built, base = open(sys.argv[1], "rb").read(), open(sys.argv[2], "rb").read(), int(sys.argv[3], 16)
i, n = 0, min(len(orig), len(built))
while i < n:
    if orig[i] == built[i]:
        i += 1
        continue
    j = i
    while j < n and (orig[j] != built[j] or (j + 4 < n and orig[j:j + 4] != built[j:j + 4])):
        j += 1
    j = (j + 3) & ~3
    s = i & ~3
    print(f"{base + s:#010x} {built[s:j].hex()}")
    i = j
if len(built) > len(orig):
    print(f"# built is {len(built) - len(orig)} bytes longer (from {base + len(orig):#010x})")
