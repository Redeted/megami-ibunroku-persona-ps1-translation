"""Decode Persona (SLPS-00500) text bytes using tools/font_map.tsv.

Usage: python tools/decode.py <file> <start_hex> <length_hex> [--raw]
  --raw  one line, no newlines inserted: output re-encodes byte-identically
         through common/persona.tbl with armips .stringn
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARAM_CODES = {0xFD}  # FF xx codes followed by one parameter byte (observed)

glyphs = {}
for line in open(os.path.join(ROOT, "tools", "font_map.tsv"), encoding="utf-8"):
    idx, ch = line.rstrip("\n").split("\t")[:2]
    glyphs[int(idx, 16)] = ch


def decode(data, raw=False):
    out, i = [], 0
    while i < len(data):
        b = data[i]
        if b < 0x80:
            out.append(glyphs.get(b, f"<{b:02X}>")); i += 1
        elif b <= 0x87 and i + 1 < len(data):
            g = ((b & 7) << 8) | data[i + 1]
            out.append(glyphs.get(g, f"<G{g:03X}>")); i += 2
        elif b == 0xFF and i + 1 < len(data):
            c = data[i + 1]
            out.append(f"<FF{c:02X}>"); i += 2
            if c in PARAM_CODES and i < len(data):
                out.append(f"<{data[i]:02X}>"); i += 1
            if c == 0xF6 and not raw:
                out.append("\n")
        else:
            out.append(f"<{b:02X}>"); i += 1
    return "".join(out)


if __name__ == "__main__":
    path, start, length = sys.argv[1], int(sys.argv[2], 16), int(sys.argv[3], 16)
    data = open(path, "rb").read()[start:start + length]
    sys.stdout.reconfigure(encoding="utf-8")
    print(decode(data, raw="--raw" in sys.argv))
