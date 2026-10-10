"""Generate common/persona.tbl from tools/font_map.tsv.

Encoding (SLPS-00500):
  00-7F       glyph 0x000-0x07F (single byte)
  80-87 xx    glyph ((b & 7) << 8) | xx  (0x000-0x7FF)
  FF xx       control code
Two tables are written:
  common/persona.tbl      original encoding; ASCII aliases the full-width glyphs
                          (for renderers without VWF: menus, battle, ...)
  common/persona_vwf.tbl  same, but ASCII maps to single bytes 88-E6
                          (ASCII + 0x68) drawn by the VWF engine (vwf/)
Run from the project root: python tools/make_tbl.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def code(g):
    return f"{g:02X}" if g < 0x80 else f"{0x80 | (g >> 8):02X}{g & 0xFF:02X}"


glyphs = {}
for line in open(os.path.join(ROOT, "tools", "font_map.tsv"), encoding="utf-8"):
    idx, ch = line.rstrip("\n").split("\t")[:2]
    glyphs[int(idx, 16)] = ch

# ASCII aliases onto the existing full-width glyphs, for writing English
ascii_alias = {" ": 0x000, "/": 0x0CA, ":": 0x0CB, ".": 0x0CD, "?": 0x0D0, "!": 0x0D1,
               "*": 0x0D2, ",": 0x0D5, "~": 0x0D6, "(": 0x0D8, ")": 0x0D9, "+": 0x0E0,
               "-": 0x0E1, "%": 0x0E5, "#": 0x0E6, "&": 0x0E7, "=": 0x0F1, "'": 0x783}
for i in range(26):
    ascii_alias[chr(0x41 + i)] = 0x0A6 + i
for i in range(10):
    ascii_alias[chr(0x30 + i)] = 0x0C0 + i
for c, g in zip("abcdefghijklmnopqrstuvwxyz",
                [0x723, 0x724, 0x725, 0x727, 0x72D] + list(range(0x731, 0x746))):
    ascii_alias[c] = g

VWF_CHAR_BIAS = 0x68  # keep in sync with vwf/vwf_adv.asm


def write_table(name, ascii_lines):
    lines = [f"{code(g)}={glyphs[g]}" for g in sorted(glyphs)]
    lines += ascii_lines
    # control codes and raw bytes: write "<FFF6>" or "<24>" inside strings
    lines += [f"FF{b:02X}=<FF{b:02X}>" for b in range(256)]
    lines += [f"{b:02X}=<{b:02X}>" for b in range(256)]
    # glyphs with no character (filler / unnamed symbols) stay reachable as <Gxxx>
    lines += [f"{code(g)}=<G{g:03X}>" for g in range(0x800) if g not in glyphs]
    lines.append("/FF01")
    with open(os.path.join(ROOT, "common", name), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")


write_table("persona.tbl", [f"{code(g)}={c}" for c, g in ascii_alias.items()])
write_table("persona_vwf.tbl", [f"{ord(c) + VWF_CHAR_BIAS:02X}={c}" for c in map(chr, range(0x20, 0x7F))])
print(f"{len(glyphs)} glyphs -> common/persona.tbl, common/persona_vwf.tbl")
