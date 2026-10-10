"""List absolute addresses formed by lui+addiu/ori (and lui+load/store) in a code range.

Usage: python tools/mipsconst.py <file> <file_base_addr> <start_addr> <end_addr>
Useful for finding which RAM tables a routine touches.
"""
import sys
import capstone

path, base, start, end = sys.argv[1], *(int(x, 16) for x in sys.argv[2:5])
data = open(path, "rb").read()
md = capstone.Cs(capstone.CS_ARCH_MIPS, capstone.CS_MODE_MIPS32 + capstone.CS_MODE_LITTLE_ENDIAN)
md.detail = True
hi = {}
for addr in range(start, end, 4):
    ins = next(md.disasm(data[addr - base:addr - base + 4], addr), None)
    if ins is None:
        continue
    ops = ins.operands
    if ins.mnemonic == "lui":
        hi[ins.reg_name(ops[0].reg)] = (ops[1].imm & 0xFFFF) << 16
        continue
    if ins.mnemonic in ("addiu", "ori") and len(ops) == 3:
        src = ins.reg_name(ops[1].reg)
        if src in hi:
            imm = ops[2].imm
            val = hi[src] + (imm if ins.mnemonic == "addiu" else imm & 0xFFFF)
            print(f"{addr:08X}  {ins.mnemonic} {ins.op_str:32} = {val & 0xFFFFFFFF:08X}")
    elif len(ops) == 2 and ops[1].type == capstone.mips.MIPS_OP_MEM:
        b = ins.reg_name(ops[1].mem.base)
        if b in hi:
            val = hi[b] + ops[1].mem.disp
            print(f"{addr:08X}  {ins.mnemonic} {ins.op_str:32} @ {val & 0xFFFFFFFF:08X}")
