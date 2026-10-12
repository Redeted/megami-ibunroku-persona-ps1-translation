"""Dialogue boxes of the overworld (S2D.BIN): the party's comments while walking, locked-door texts ...

  python tools/s2dscript.py dump     write/refresh translation/strings/S2DSCRIPT.tsv (keeps the `en` column)
  python tools/s2dscript.py build    QA + generate build/s2dscript.asm (included in the S2D section of main.asm)

61 boxes at RAM 0x800AB054-0x800AC2F6 (file offset = RAM - 0x800643C4), same encoding as the event boxes (FF01 end, FF02
wait, FF03 newline, FF04 page, FF05 + 2 pause bytes, FF07 / FF0F + 1 byte = names). They are said by `FF 55 00 00 <ptr>`
commands (and a few other pointer words). The dialogue VWF hooks cover this interpreter, so English is ASCII VWF text.
The commands between the boxes stay where they are; only the boxes move: an English box that fits its Japanese slot
stays in it, the others are re-packed into the free slots (identical boxes share one copy) and, if needed, into the
SPILL regions (unreferenced SLPS functions, see tools/deadfuncs.py). Every pointer word that points at a box start is patched
(a pointer into the middle of a box is an error).

`en` syntax = the event TSVs (`<FF03>` newline ...; no trailing <FF01>; `<FF05>` on its own copies the two pause bytes of
the Japanese box in order). Checked with tools/tstatus.check.
"""
import os
import re
import struct
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import etext      # noqa: E402
import tstatus    # noqa: E402
import psp_terms  # noqa: E402

ROOT = etext.ROOT
B = 0x800643C4
BLOCK = (0x800AB040, 0x800AC400)
TSV = os.path.join(ROOT, 'translation', 'strings', 'S2DSCRIPT.tsv')
OUT = os.path.join(ROOT, 'build', 's2dscript.asm')
NL = chr(10)
# Overflow: S2D.BIN is loaded in whole sectors (352256 bytes = up to RAM 0x800BA3C4); the file is extended by the sectors that hold
# the English boxes that do not fit their Japanese slots. Nothing in the overlay or the main EXE refers to that RAM (static scan),
# it only held the tail of the ADV overlay that was resident before.
SPILL = [(0x800BA3C4, 0x800BB200)]       # up to S2D_GLUE_ADDR (common/addresses.inc), where the VWF glue code starts


def s2d():
    return open(os.path.join(ROOT, 'original', 'S2D.BIN'), 'rb').read()


def boxes(d):
    starts = set()
    for i in range(len(d) - 8):
        if d[i:i + 4] == b'\xff\x55\x00\x00':
            v = struct.unpack_from('<I', d, i + 4)[0]
            if BLOCK[0] <= v < BLOCK[1]:
                starts.add(v)
    out = []
    for s in sorted(starts):
        e = d.index(b'\xff\x01', s - B) + 2 + B
        out.append((s, e))
    return out


def refs(d, bx):
    """pointer words (4-aligned) at a box start; error for pointers into the middle of a box."""
    found = {i: [] for i in range(len(bx))}
    for k in range(0, len(d) - 3, 4):
        v = struct.unpack_from('<I', d, k)[0]
        for i, (a, e) in enumerate(bx):
            if a <= v < e:
                if v != a:
                    raise SystemExit(f's2dscript: pointer {B + k:#x} into the middle of box {i} ({v:#x})')
                found[i].append(B + k)
    return found


def dec(d, a, e):
    return etext.decode(d[a - B:e - B - 2])


def read_tsv():
    rows = {}
    if os.path.exists(TSV):
        for line in open(TSV, encoding='utf-8').read().split(NL)[1:]:
            c = line.rstrip('\r').split('\t')
            if len(c) >= 6 and c[0].isdigit():
                rows[int(c[0])] = c[5]
    return rows


def dump():
    d = s2d()
    bx = boxes(d)
    rf = refs(d, bx)
    old = read_tsv()
    with open(TSV, 'w', encoding='utf-8', newline=NL) as o:
        o.write('idx\tram\tsize\trefs\tja\ten' + NL)
        for i, (a, e) in enumerate(bx):
            o.write(f'{i}\t{a:08X}\t{e - a}\t{len(rf[i])}\t{dec(d, a, e)}\t{old.get(i, "")}' + NL)
    print('wrote', TSV, f'({len(bx)} boxes)')


def fill_pauses(ja, en):
    """`<FF05>` without parameter bytes in `en` -> the two parameter glyph bytes of the same FF05 in `ja`."""
    jb = etext.encode(ja)
    par = [jb[i + 2:i + 4] for i in range(len(jb) - 3) if jb[i] == 0xFF and jb[i + 1] == 5]
    k = iter(par)
    return re.sub(r'<FF05>(?!<[0-9A-F]{2}>)', lambda m: '<FF05>' + ''.join(f'<{x:02X}>' for x in next(k)), en)


def build():
    d = s2d()
    bx = boxes(d)
    rf = refs(d, bx)
    en = {k: psp_terms.fix(v) for k, v in read_tsv().items()}
    tstatus.load_glossary()
    todo, errors = {}, []
    for i, (a, e) in enumerate(bx):
        t = en.get(i, '').strip(' \t')
        if not t:
            continue
        ja = dec(d, a, e)
        t = fill_pauses(ja, t)
        bad = tstatus.check(ja, t)
        if bad:
            errors.append(f's2dscript: {i}: ' + '; '.join(f'[{k}] {m}' for k, m in bad))
            continue
        todo[i] = etext.encode(t)
    if errors:
        raise SystemExit(NL.join(errors))
    free = [bx[i] for i in todo]
    pools = [free, list(SPILL)]
    placed, addr_of = {}, {}
    for i in sorted(todo, key=lambda i: -len(todo[i])):
        b = todo[i]
        if b in placed:
            addr_of[i] = placed[b]
            continue
        a, e = bx[i]
        if len(b) <= e - a and (a, e) in free:                # its own slot first
            placed[b] = a
            addr_of[i] = a
            free[free.index((a, e))] = (a + len(b), e)
            continue
        for pool in pools:
            for k, (pa, pe) in enumerate(pool):
                if pe - pa >= len(b):
                    placed[b] = pa
                    addr_of[i] = pa
                    pool[k] = (pa + len(b), pe)
                    break
            else:
                continue
            break
        else:
            raise SystemExit(f's2dscript: out of space for box {i} ({len(b)} bytes); free '
                             f'{sum(e - a for p in pools for a, e in p)} bytes')
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', newline=NL) as o:
        o.write(';; generated by tools/s2dscript.py build - do not edit' + NL)
        for i in todo:
            a, e = bx[i]
            o.write(f'.org {a:#x}{NL}.fill {e - a}, 0{NL}')
        for b, a in placed.items():
            o.write(f'.org {a:#x}{NL}    .byte ' + ', '.join(f'0x{x:02X}' for x in b) + NL)
        for i in todo:
            for where in rf[i]:
                o.write(f'.org {where:#x}{NL}    .word {addr_of[i]:#x}{NL}')
    spilled = sum(len(b) for b, a in placed.items() if not (BLOCK[0] <= a < BLOCK[1]))
    print(f's2dscript: {len(todo)}/{len(bx)} translated, {sum(len(b) for b in placed)} bytes ({spilled} spilled) -> {OUT}')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    {'dump': dump, 'build': build}[sys.argv[1] if len(sys.argv) > 1 else 'build']()
