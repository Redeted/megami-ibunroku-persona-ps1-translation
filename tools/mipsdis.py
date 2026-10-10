"""Disassemble a PSX binary range: python tools/mipsdis.py <file> <file_base_addr> <start_addr> <end_addr>
Example (ADV.BIN overlay): python tools/mipsdis.py original/ADV.BIN 0x800643D0 0x80067994 0x80067c00
For PS-X EXEs use base = t_addr - 0x800.
"""
import sys
import capstone

path, base, start, end = sys.argv[1], *(int(x, 16) for x in sys.argv[2:5])
data = open(path, "rb").read()
md = capstone.Cs(capstone.CS_ARCH_MIPS, capstone.CS_MODE_MIPS32 + capstone.CS_MODE_LITTLE_ENDIAN)
for addr in range(start, min(end, base + len(data)), 4):
    word = data[addr - base:addr - base + 4]
    ins = next(md.disasm(word, addr), None)
    if ins is None:
        print(f"{addr:08X}  .word    0x{int.from_bytes(word, 'little'):08X}")
    else:
        print(f"{addr:08X}  {ins.mnemonic:8} {ins.op_str}")
