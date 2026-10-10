"""System messages of ADV.BIN (shop / Persona exchange / memory card and save messages), dialogue-box format.

  python tools/sysmsg.py dump     write/refresh translation/strings/SYSMSG.tsv (keeps the `en` column)
  python tools/sysmsg.py build    QA + generate build/sysmsg.asm (included in the ADV section of main.asm)

The messages live in ADV.BIN at RAM 0x800BB0E8-0x800BB517 (file offset = RAM - 0x800643C4), in the same encoding as the
event boxes (FF01 end, FF02 wait, FF03 newline, FF04 new page, FF0E choice ...) and are shown by the dialogue engine,
so English goes through the dialogue VWF. Every message is reached either through a pointer table (RAM 0x800BB518,
11 words) or through `lui a0,0x800C ; addiu a0,a0,imm` pairs in the ADV code (found by scanning). Because both kinds of
reference are patched (only the addiu immediate changes, the lui stays 0x800C), the English strings are re-packed freely
inside the two zones below. Messages with no reference found are left where they are.
The small-font label block 0x800BB115-0x800BB153 (TOTAL COIN ...) is not touched; 0x800BB154 is the Velvet Room
fusion prompt (message 24, own zone so the older message indices stay put).

`en` syntax = the event TSVs (`<FF03>` newline, `<FF02>` wait, ...; no trailing <FF01>, the build adds it); checked with
tools/tstatus.check (control codes identical to the Japanese, 239 px lines, <= 3 lines per page, ASCII).
"""
import os
import re
import struct
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import etext      # noqa: E402
import tstatus    # noqa: E402

ROOT = etext.ROOT
B = 0x800643C4                       # RAM address of ADV.BIN file offset 0
ZONES = [(0x800BB0E8, 0x800BB115), (0x800BB166, 0x800BB518),
         (0x800BB154, 0x800BB166)]     # Velvet Room 'add an item?' prompt; listed last to keep the older indices
TABLE = 0x800BB518
PROTECT = [(0x800BB1CC, 0x800BB1D2)]   # tile label "BUTTON" (6 small-font cells) inside message 8's slot: drawn by ADV 0x800A5290 (Velvet Room hint line)
DEAD = {3}                           # unreferenced duplicate of message 7: its slot is reused as free space
TSV = os.path.join(ROOT, 'translation', 'strings', 'SYSMSG.tsv')
OUT = os.path.join(ROOT, 'build', 'sysmsg.asm')
NL = chr(10)


def adv():
    return open(os.path.join(ROOT, 'original', 'ADV.BIN'), 'rb').read()


def messages(d):
    out = []
    for a, b in ZONES:
        p = a
        while p < b:
            e = d.index(b'\xff\x01', p - B) + 2 + B
            out.append((p, e))
            p = e
            while p < b and d[p - B] == 0 and False:
                p += 1
    return out


def refs(d, msgs):
    """-> (table_slots, code_refs) as {msg_index: [(kind, ram_address_of_patch, old_value)]}"""
    found = {i: [] for i in range(len(msgs))}

    def which(v):
        for i, (a, e) in enumerate(msgs):
            if a <= v < e:
                return i

    t = TABLE
    while True:
        v = struct.unpack_from('<I', d, t - B)[0]
        i = which(v) if B <= v < 0x80100000 else None
        if i is None:
            break
        found[i].append(('ptr', t, v))
        t += 4
    nwords = (0x800BB000 - B) // 4
    end = (len(d)) // 4
    for k in range(end - 9):
        w = struct.unpack_from('<I', d, 4 * k)[0]
        if (w >> 26) == 0xF and (w & 0xFFFF) in (0x800B, 0x800C):
            rt = (w >> 16) & 31
            for j in range(1, 9):
                x = struct.unpack_from('<I', d, 4 * (k + j))[0]
                op, imm = x >> 26, x & 0xFFFF
                if op in (9, 0xD) and ((x >> 21) & 31) == rt:
                    v = ((w & 0xFFFF) << 16) + (imm - 0x10000 if (imm & 0x8000 and op == 9) else imm)
                    i = which(v)
                    if any(pa <= v < pe for pa, pe in PROTECT):
                        i = None                    # label inside a message slot that must stay where it is
                    if i is not None and (w & 0xFFFF) == 0x800C and op == 9:
                        found[i].append(('code', B + 4 * (k + j), v))
    return found


def dec(d, a, e):
    return etext.decode(d[a - B:e - B])


def read_tsv():
    rows = {}
    if os.path.exists(TSV):
        for line in open(TSV, encoding='utf-8').read().split(NL)[1:]:
            c = line.rstrip('\r').split('\t')
            if len(c) >= 6 and c[0].isdigit():
                rows[int(c[0])] = c[5]
    return rows


def dump():
    d = adv()
    msgs = messages(d)
    rf = refs(d, msgs)
    old = read_tsv()
    with open(TSV, 'w', encoding='utf-8', newline=NL) as o:
        o.write('idx\tram\tsize\trefs\tja\ten' + NL)
        for i, (a, e) in enumerate(msgs):
            r = ','.join(f'{k[0]}:{k[1]:08X}' for k in rf[i])
            o.write(f'{i}\t{a:08X}\t{e - a}\t{r}\t{dec(d, a, e)}\t{old.get(i, "")}' + NL)
    print('wrote', TSV, f'({len(msgs)} messages)')


def cut(a, e):
    """[a, e) minus the PROTECT ranges -> list of (a, e)"""
    out = [(a, e)]
    for pa, pe in PROTECT:
        nxt = []
        for x, y in out:
            if pe <= x or pa >= y:
                nxt.append((x, y))
                continue
            if x < pa:
                nxt.append((x, pa))
            if pe < y:
                nxt.append((pe, y))
        out = nxt
    return out


def build():
    d = adv()
    msgs = messages(d)
    rf = refs(d, msgs)
    en = read_tsv()
    tstatus.load_glossary()
    todo = {}
    inplace = set()
    for i, (a, e) in enumerate(msgs):
        t = en.get(i, '').strip(' 	')
        if not t:
            continue
        if not rf[i]:
            inplace.add(i)                  # nothing points at it that we can patch: must fit its own slot
        ja = dec(d, a, e)
        ja = re.sub(r'^(<00>|　)+', '', ja)
        bad = tstatus.check(ja, t)
        if bad:
            raise SystemExit(f'sysmsg: {i}: ' + '; '.join(f'[{k}] {m}' for k, m in bad))
        todo[i] = etext.encode(t)                      # + FF01
    # free space = the old slots of the translated messages (per zone)
    free = []
    for i in todo:
        a, e = msgs[i]
        if i in inplace:
            if len(todo[i]) > e - a:
                raise SystemExit(f'sysmsg: unreferenced message {i} needs {len(todo[i])} bytes, slot has {e - a}')
            continue
        free.extend(cut(a, e))
    for i in DEAD:
        free.extend(cut(*msgs[i]))
    free.sort()
    merged = []
    for a, e in free:
        if merged and merged[-1][1] == a:
            merged[-1] = (merged[-1][0], e)
        else:
            merged.append((a, e))
    # share identical English between messages with identical content
    placed = {}
    addr_of = {}
    fixed = {}
    for i in sorted(todo, key=lambda i: -len(todo[i])):
        b = todo[i]
        if i in inplace:
            fixed[msgs[i][0]] = b
            continue
        if b in placed:
            addr_of[i] = placed[b]
            continue
        for k, (a, e) in enumerate(merged):
            if e - a >= len(b):
                placed[b] = a
                addr_of[i] = a
                merged[k] = (a + len(b), e)
                break
        else:
            raise SystemExit(f'sysmsg: out of space for message {i} ({len(b)} bytes); free {[(hex(a), e - a) for a, e in merged]}')
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', newline=NL) as o:
        o.write(';; generated by tools/sysmsg.py build - do not edit' + NL)
        for i in list(todo) + sorted(DEAD - set(todo)):
            for a, e in cut(*msgs[i]):
                o.write(f'.org {a:#x}{NL}.fill {e - a}, 0{NL}')
        for b, a in list(placed.items()) + [(b, a) for a, b in fixed.items()]:
            o.write(f'; {a:#x}{NL}.org {a:#x}{NL}    .byte ' + ', '.join(f'0x{x:02X}' for x in b) + NL)
        for i in todo:
            for kind, where, old in rf[i]:
                new = addr_of[i]
                if kind == 'ptr':
                    o.write(f'.org {where:#x}{NL}    .word {new:#x}{NL}')
                else:
                    o.write(f'.org {where:#x}{NL}    .halfword {(new - 0x800C0000) & 0xFFFF:#x}{NL}')
    used = sum(len(b) for b in placed) + sum(len(b) for b in fixed.values())
    print(f'sysmsg: {len(todo)}/{len(msgs)} translated, {used} bytes -> {OUT}')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    {'dump': dump, 'build': build}[sys.argv[1] if len(sys.argv) > 1 else 'build']()
