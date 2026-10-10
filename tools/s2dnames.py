"""Location names of the overworld (S2D.BIN): the banner shown on arrival, the map, ...

  python tools/s2dnames.py dump     write/refresh translation/strings/S2DNAMES.tsv (keeps the `en` column)
  python tools/s2dnames.py build    QA + generate build/s2dnames.asm (included in the S2D section of main.asm)

47 names (御影町１丁目, 学園入口, 御影町２丁目 ...) at RAM 0x800AAE0E-0x800AB033 (file offset = RAM - 0x800643C4), FF01-terminated, in the
dialogue encoding. They are reached through pointer words (a table at 0x800A54E0, a 20-byte-stride record table at 0x800AC324,
...) and a few `lui 0x800B ; addiu` pairs; every pointer word anywhere in the file that points into a name is patched, as
are the addiu immediates (the lui stays 0x800B). The English strings are re-packed inside the zone.
`en` = plain ASCII text (no codes); the build adds FF01. IMPORTANT: the banner is drawn by a second text interpreter
(S2D 0x8009B2F4, a 15x1 cell box, 16 px per glyph, NOT the VWF-hooked dialogue engine): every character is a full-width
glyph code of the game font (A=0xA6, 0=0xC0, lowercase 0x723.., space = glyph 0; glyphs >= 0x80 are two bytes) so a name has
at most 7 characters: the overworld pre-renders every area label of the current area (loop at 0x80090E88, arrays of
{u16, u32 name ptr} records) into a box of 8 cells x 1 row (cols constant at 0x80090F1C); text filling the box (8 glyphs) or
overflowing it makes the interpreter wait forever = freeze (music keeps playing). The banner (15 cells) shares the pointers.
Widening is not possible (the box textures sit in a dense VRAM area at x=640..704). A narrow-font hook for this engine would
lift the limit (not done).
"""
import os
import struct
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import etext      # noqa: E402
import vwf_wrap   # noqa: E402

ROOT = etext.ROOT
B = 0x800643C4
ZONE = (0x800AAE0E, 0x800AB034)
TSV = os.path.join(ROOT, 'translation', 'strings', 'S2DNAMES.tsv')
OUT = os.path.join(ROOT, 'build', 's2dnames.asm')
OUT_SLPS = os.path.join(ROOT, 'build', 's2dnames_slps.asm')   # strings spilled into the resident main EXE
BANNER_CELLS = 7         # area labels are pre-rendered into 8-cell boxes (S2D 0x80090F1C); 8 glyphs fill the box and hang the loop: max 7
EXTRA = {'-': '－', '.': '．', '&': '＆', '/': '／', ':': '：', '!': '！', '?': '？', "'": '’', ',': '，'}
# Spill space: unreferenced SLPS functions (tools/deadfuncs.py) that no other tool uses (choices.py, vwf_name_map ...).
# Only names reached through pointer words may live here; names with `lui 0x800B` references stay in the zone.
# (0x8002C248, 0x8002C2B4) is now the battle skill menu buffer (common/addresses.inc SKILL_MENU_BUF)
SPILL = [(0x800182B4, 0x8001831C), (0x8002C374, 0x8002C3E0), (0x80024744, 0x8002479C)]
# (0x8002E048, 0x8002E0C0), (0x80030A6C, 0x80030AD4) now hold battle messages (tools/btlmsg.py SPILL)
# (0x80031878, 0x800318E8) is now persona_name_copy (common/addresses.inc PERSONA_CODE_ADDR)
NL = chr(10)


def wide(t):
    """ASCII -> the game's own (full-width) glyph codes; glyphs >= 0x80 are two bytes (0x80|hi, lo); + FF01."""
    out = bytearray()
    for c in t:
        if c == ' ':
            g = 0
        elif 'A' <= c <= 'Z':
            g = etext.char2g[chr(0xFF21 + ord(c) - 0x41)]
        elif 'a' <= c <= 'z':
            g = etext.char2g[chr(0xFF41 + ord(c) - 0x61)]
        elif '0' <= c <= '9':
            g = etext.char2g[chr(0xFF10 + ord(c) - 0x30)]
        else:
            g = etext.char2g[EXTRA[c]]
        out += bytes([g]) if g < 0x80 else bytes([0x80 | (g >> 8), g & 0xFF])
    return bytes(out) + bytes([0xFF, 0x01])


def s2d():
    return open(os.path.join(ROOT, 'original', 'S2D.BIN'), 'rb').read()


def names(d):
    out, p = [], ZONE[0]
    while p < ZONE[1]:
        e = d.index(b'\xff\x01', p - B) + 2 + B
        out.append((p, e))
        p = e
    return out


def refs(d, msgs):
    found = {i: [] for i in range(len(msgs))}

    def which(v):
        for i, (a, e) in enumerate(msgs):
            if a <= v < e:
                return i

    for k in range(0, len(d) - 3, 4):
        v = struct.unpack_from('<I', d, k)[0]
        if ZONE[0] <= v < ZONE[1]:
            i = which(v)
            if i is not None:
                found[i].append(('ptr', B + k, v, 0))
    for k in range(0, len(d) - 36, 4):
        w = struct.unpack_from('<I', d, k)[0]
        hi = w & 0xFFFF
        if (w >> 26) == 0xF and hi in (0x800A, 0x800B):
            rt = (w >> 16) & 31
            for j in range(1, 8):
                x = struct.unpack_from('<I', d, k + 4 * j)[0]
                op, imm = x >> 26, x & 0xFFFF
                if ((x >> 21) & 31) != rt or op not in (9, 0xD):
                    continue
                v = (hi << 16) + (imm - 0x10000 if (imm & 0x8000 and op == 9) else imm)
                i = which(v)
                if i is not None:
                    found[i].append(('addiu' if op == 9 else 'ori', B + k + 4 * j, v, B + k))
    return found


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
    msgs = names(d)
    rf = refs(d, msgs)
    old = read_tsv()
    with open(TSV, 'w', encoding='utf-8', newline=NL) as o:
        o.write('idx\tram\tsize\trefs\tja\ten' + NL)
        for i, (a, e) in enumerate(msgs):
            ja = etext.decode(d[a - B:e - B - 2]).replace('<00>', '')
            o.write(f'{i}\t{a:08X}\t{e - a}\t{len(rf[i])}\t{ja}\t{old.get(i, "")}' + NL)
    print('wrote', TSV, f'({len(msgs)} names)')


def build():
    d = s2d()
    msgs = names(d)
    rf = refs(d, msgs)
    en = read_tsv()
    todo = {}
    for i, (a, e) in enumerate(msgs):
        t = en.get(i, '').strip()
        if not t:
            continue
        if not rf[i]:
            raise SystemExit(f's2dnames: {i} has no reference')
        if len(t) > BANNER_CELLS:
            raise SystemExit(f's2dnames: {i} {t!r} is {len(t)} characters (> {BANNER_CELLS} cells)')
        todo[i] = wide(t)
    free = sorted(msgs[i] for i in todo)
    merged = []
    for a, e in free:
        if merged and merged[-1][1] == a:
            merged[-1] = (merged[-1][0], e)
        else:
            merged.append((a, e))
    placed, addr_of = {}, {}
    spill = list(SPILL)

    def put(i, pools):
        b = todo[i]
        if b in placed:
            addr_of[i] = placed[b]
            return True
        for pool in pools:
            for k, (a, e) in enumerate(pool):
                if e - a >= len(b):
                    placed[b] = a
                    addr_of[i] = a
                    pool[k] = (a + len(b), e)
                    return True
        return False

    order = sorted(todo, key=lambda i: (not any(r[0] in ('addiu', 'ori') for r in rf[i]), -len(todo[i])))
    for i in order:
        has_code = any(r[0] in ('addiu', 'ori') for r in rf[i])
        if not put(i, [merged] if has_code else [merged, spill]):
            raise SystemExit(f's2dnames: out of space for {i} ({len(todo[i])} bytes, code refs: {has_code})')
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', newline=NL) as o:
        o.write(';; generated by tools/s2dnames.py build - do not edit' + NL)
        for i in todo:
            a, e = msgs[i]
            o.write(f'.org {a:#x}{NL}.fill {e - a}, 0{NL}')
        for b, a in placed.items():
            if ZONE[0] <= a < ZONE[1]:
                o.write(f'.org {a:#x}{NL}    .byte ' + ', '.join(f'0x{x:02X}' for x in b) + NL)
        for i in todo:
            for kind, where, old, lui in rf[i]:
                new = addr_of[i]
                if kind == 'ptr':
                    o.write(f'.org {where:#x}{NL}    .word {new:#x}{NL}')
                elif kind == 'addiu':
                    o.write(f'.org {where:#x}{NL}    .halfword {(new - 0x800B0000) & 0xFFFF:#x}{NL}')
                else:                                                  # ori with lui 0x800A
                    o.write(f'.org {where:#x}{NL}    .halfword {new & 0xFFFF:#x}{NL}')
    import json
    ptrmap = {}
    content = {}
    for i in todo:
        for kind, where, old, lui in rf[i]:
            ptrmap[f'{old:#010x}'] = f'{addr_of[i]:#010x}'
        content[todo[i].hex()] = f'{addr_of[i]:#010x}'          # encoded English (+FF01) -> new address
    with open(os.path.join(ROOT, 'build', 's2dnames_map.json'), 'w') as o:
        json.dump({'ptr': ptrmap, 'content': content}, o)
    with open(OUT_SLPS, 'w', newline=NL) as o:
        o.write(';; generated by tools/s2dnames.py build - overworld names spilled into unused SLPS functions' + NL)
        for b, a in placed.items():
            if not (ZONE[0] <= a < ZONE[1]):
                o.write(f'.org {a:#x}{NL}    .byte ' + ', '.join(f'0x{x:02X}' for x in b) + NL)
    print(f's2dnames: {len(todo)}/{len(msgs)} translated, {sum(len(b) for b in placed)} of {sum(e - a for a, e in (msgs[i] for i in todo))} bytes -> {OUT}')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    {'dump': dump, 'build': build}[sys.argv[1] if len(sys.argv) > 1 else 'build']()
