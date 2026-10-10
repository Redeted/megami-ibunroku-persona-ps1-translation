"""Dialogue choice options of SLPS_005.00 (the text drawn after <FF0E><n> in event boxes).

  python tools/choices.py dump     write/refresh translation/strings/CHOICES.tsv (keeps the `en` column)
  python tools/choices.py build    QA + generate build/choices.asm (included by main.asm)

Layout (RAM, resident main EXE; file offset = addr - 0x80010000 + 0x800):
  0x8004D760: 32 entries x 8 bytes: u32 pointer to the option string, then 4 bytes
              [rows, cols, width_chars, 0]   (the <FF0E> handler is at 0x800672AC)
  strings:    0x8004D430-0x8004D75D, options separated by <FF03>, ended by <FF01>.
The strings are drawn by the dialogue text interpreter, so English goes through the dialogue VWF
(variable width, ASCII + 0x68). The option grid is fixed: column 2 of a 2-column menu starts at
(width_chars + 1) * 16 px, the cursor underline is width_chars * 16 px long.

CHOICES.tsv `en` syntax: rows joined by <FF03>; cells of a 2-column row joined by `|`
(e.g. `Start Game|Quit<FF03>Check Coins|Rules`). Column 1 is padded with VWF spaces (4 px) up to the
column 2 pixel start; if column 1 is too wide the build fails. Single-column menus: the underline
width byte is raised if an option is wider than width_chars * 16 px. Empty `en` = left Japanese.
The strings are repacked into the freed original slots and unreferenced SLPS functions (pointer table is
rewritten), so English may be longer than the Japanese.
"""
import os
import re
import struct
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import etext      # noqa: E402
import vwf_wrap   # noqa: E402

ROOT = etext.ROOT
TABLE = 0x8004D760
COUNT = 32
BASE = 0x80010000 - 0x800
# Unreferenced SLPS functions (tools/deadfuncs.py), not used by the VWF (0x80015510 is vwf_name_map). NOT the SLPS_FREE_START..END
# area of common/addresses.inc: that one holds runtime variables (e.g. the CD flag at 0x80055C34).
# (0x80011FBC, 0x800120A4) now holds skill_name_copy (common/addresses.inc SKILL_CODE_ADDR)
FREE = [(0x8002E698, 0x8002E744), (0x8002BC84, 0x8002BD60),
        (0x80011C40, 0x80011D0C), (0x80011AC0, 0x80011B88),
        (0x800316DC, 0x80031770), (0x8001FF24, 0x8001FFB4)]
TSV = os.path.join(ROOT, 'translation', 'strings', 'CHOICES.tsv')
OUT = os.path.join(ROOT, 'build', 'choices.asm')
NL = chr(10)


def original():
    d = open(os.path.join(ROOT, 'original', 'SLPS_005.00'), 'rb').read()
    rows = []
    for k in range(COUNT):
        at = TABLE + 8 * k - BASE
        ptr, = struct.unpack_from('<I', d, at)
        params = d[at + 4:at + 8]
        s = ptr - BASE
        e = d.index(b'\xff\x01', s) + 2
        rows.append(dict(idx=k, ptr=ptr, params=params, ja=etext.decode(d[s:e]), size=e - s))
    return rows


def read_tsv():
    rows = []
    for line in open(TSV, encoding='utf-8').read().split(NL)[1:]:
        if line.strip('\r'):
            c = line.rstrip('\r').split('\t')
            c += [''] * (5 - len(c))
            rows.append(c)
    return rows


def dump():
    old = {int(r[0]): r[4] for r in read_tsv()} if os.path.exists(TSV) else {}
    with open(TSV, 'w', encoding='utf-8', newline=NL) as o:
        o.write('idx\tptr\tparams\tja\ten' + NL)
        for r in original():
            o.write(f"{r['idx']}\t{r['ptr']:08X}\t{r['params'].hex()}\t{r['ja']}\t{old.get(r['idx'], '')}" + NL)
    print('wrote', TSV)


def layout(r, en):
    """-> (english string with padding and codes, new width byte)."""
    rows_p, cols_p, width_p, _ = r['params']
    lines = en.split('<FF03>')
    assert len(lines) == rows_p, f"{r['idx']}: {len(lines)} rows, expected {rows_p}"
    width_new = width_p
    out = []
    for ln in lines:
        cells = ln.split('|')
        assert len(cells) == cols_p, f"{r['idx']}: {len(cells)} columns in {ln!r}, expected {cols_p}"
        if cols_p == 1:
            w = vwf_wrap.text_width(cells[0])
            width_new = max(width_new, -(-w // 16))
            out.append(cells[0])
        else:
            target = (width_p + 1) * 16
            w1 = vwf_wrap.text_width(cells[0])
            assert w1 <= target - 4, f"{r['idx']}: {cells[0]!r} is {w1}px, column 1 has {target - 4}px"
            pad = round((target - w1) / 4)
            text = cells[0] + ' ' * pad + cells[1]
            assert vwf_wrap.text_width(text) <= 232, f"{r['idx']}: row {text!r} is wider than the box"
            out.append(text)
    assert width_new <= 14, f"{r['idx']}: needs {width_new} cells"
    return '<FF03>'.join(out), width_new


def build():
    orig = original()
    tsv = {int(r[0]): r[4] for r in read_tsv()}
    placed = {}                                   # idx -> (bytes, width)
    free = list(FREE)
    for r in orig:
        en = tsv.get(r['idx'], '').strip()
        if not en:
            continue
        text, w = layout(r, en)
        b = etext.encode(text)
        for ch in re.sub(r'<[^>]*>', '', text):
            assert 0x20 <= ord(ch) <= 0x7E, f"{r['idx']}: non-ASCII {ch!r}"
        placed[r['idx']] = (b, w)
        free.append((r['ptr'], r['ptr'] + r['size']))     # its Japanese slot becomes free
    # first-fit decreasing into the free list (merge touching slots first)
    free.sort()
    merged = []
    for a, b in free:
        if merged and merged[-1][1] == a:
            merged[-1] = (merged[-1][0], b)
        else:
            merged.append((a, b))
    addr = {}
    for idx in sorted(placed, key=lambda i: -len(placed[i][0])):
        n = len(placed[idx][0])
        for k, (a, b) in enumerate(merged):
            if b - a >= n:
                addr[idx] = a
                merged[k] = (a + n, b)
                break
        else:
            raise SystemExit(f'choices: out of space for entry {idx} ({n} bytes)')
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', newline=NL) as o:
        o.write(';; generated by tools/choices.py build - do not edit' + NL)
        o.write(';; English dialogue choices: strings repacked, pointer table + width bytes patched' + NL)
        for r in orig:
            if r['idx'] in placed:
                o.write(f".org {r['ptr']:#x}{NL}.fill {r['size']}, 0{NL}")
        for idx in sorted(placed):
            b, w = placed[idx]
            o.write(f'; choice {idx}{NL}.org {addr[idx]:#x}{NL}')
            for i in range(0, len(b), 16):
                o.write('.byte ' + ', '.join(f'0x{x:02X}' for x in b[i:i + 16]) + NL)
            o.write(f'.org {TABLE + 8 * idx:#x}{NL}.word {addr[idx]:#x}{NL}.org {TABLE + 8 * idx + 6:#x}{NL}.byte {w}{NL}')
    used = sum(len(placed[i][0]) for i in placed)
    print(f'choices: {len(placed)}/{COUNT} translated, {used} bytes placed -> {OUT}')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    {'dump': dump, 'build': build}[sys.argv[1] if len(sys.argv) > 1 else 'build']()
