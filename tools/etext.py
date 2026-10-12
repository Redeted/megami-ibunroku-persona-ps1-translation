"""Event script text: lossless box text codec, TSV dump and apply for ADV/E0..E3.BIN.

Text syntax (one line per box, no real newlines):
  any glyph character   one glyph of the game font (tools/font_map.tsv)
  ASCII 0x20-0x7E       VWF English byte (ord + 0x68) -- use for translations
  <FFxx>                control code (e.g. <FF03> newline, <FF02> wait, <FF01> end)
  <Gxxx>                glyph 0xxxx without a printable character
  <xx>                  raw byte
A box must end with <FF01>; the tool appends it when a translation omits it.

CLI (run from persona-tl/):
  python tools/etext.py check                 decode->encode identity over all boxes
  python tools/etext.py dump [outdir]         translation/events/E?.tsv  (entry box ja en)
  python tools/etext.py layout [--grow]       reserve fixed per-entry slots (translation/layout.json)
  python tools/etext.py build [outdir]        apply the `en` column -> build/ADV/E?.BIN + build/event_tables.asm
"""
import json
import os
import re
import struct
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import efile  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAYOUT = os.path.join(ROOT, 'translation', 'layout.json')
# build.py --psp: the event and TALK tables come from psp_text/ (tools/pspscript.py) instead of translation/
TEXT = os.environ.get('PERSONA_TEXT') or os.path.join(ROOT, 'translation')
PSP = bool(os.environ.get('PERSONA_TEXT'))
# the extracted original game files (tools/psp_patch.py points this at its own work folder)
ORIGINAL = os.environ.get('PERSONA_ORIGINAL') or os.path.join(ROOT, 'original')
VWF_BIAS = 0x68
NO_LITERAL = set('<>\t\r\n')

glyph = {}       # index -> char
char2g = {}
for _l in open(os.path.join(ROOT, 'tools', 'font_map.tsv'), encoding='utf-8'):
    _i, _c = _l.rstrip('\n').split('\t')[:2]
    glyph[int(_i, 16)] = _c
    char2g.setdefault(_c, int(_i, 16))


def _g(g):
    c = glyph.get(g)
    if c is None or c in NO_LITERAL or len(c) != 1 or (0x20 <= ord(c) <= 0x7E):
        return f'<G{g:03X}>'
    return c


def decode(b):
    out, i = [], 0
    while i < len(b):
        c = b[i]
        if c < 0x80:
            out.append(_g(c)); i += 1
        elif c <= 0x87 and i + 1 < len(b):
            out.append(_g(((c & 7) << 8) | b[i + 1])); i += 2
        elif c == 0xFF and i + 1 < len(b):
            out.append(f'<FF{b[i + 1]:02X}>'); i += 2
        elif 0x88 <= c <= 0xE6:
            ch = chr(c - VWF_BIAS)
            out.append(ch if ch not in NO_LITERAL else f'<{c:02X}>'); i += 1
        else:
            out.append(f'<{c:02X}>'); i += 1
    return ''.join(out)


_TOKEN = re.compile(r'<(FF[0-9A-F]{2}|G[0-9A-F]{3}|[0-9A-F]{2})>')


def encode(s, end=bytes([0xFF, 0x01])):
    out = bytearray()
    pos = 0
    while pos < len(s):
        m = _TOKEN.match(s, pos)
        if m:
            t = m.group(1)
            if t.startswith('FF'):
                out += bytes([0xFF, int(t[2:], 16)])
            elif t.startswith('G'):
                g = int(t[1:], 16)
                out += bytes([g]) if g < 0x80 else bytes([0x80 | (g >> 8), g & 0xFF])
            else:
                out.append(int(t, 16))
            pos = m.end()
            continue
        ch = s[pos]
        if 0x20 <= ord(ch) <= 0x7E:
            out.append(ord(ch) + VWF_BIAS)
        elif ch in char2g:
            g = char2g[ch]
            out += bytes([g]) if g < 0x80 else bytes([0x80 | (g >> 8), g & 0xFF])
        else:
            raise ValueError(f'no glyph for {ch!r} (U+{ord(ch):04X})')
        pos += 1
    if end and out[-2:] != end:
        out += end
    return bytes(out)


FILES = ['E0', 'E1', 'E2', 'E3']
# sector tables of the E files embedded in SLPS_005.00 (RAM addresses; the loader at
# 0x800159EC indexes them by script id; each equals the file's own sector 0 table)
SLPS_TABLES = {'E0': 0x8004DA70, 'E1': 0x8004DC34, 'E2': 0x8004DDF8, 'E3': 0x8004DFDC}


def path(n):
    return os.path.join(ORIGINAL, 'ADV', f'{n}.BIN')


def cmd_check():
    bad = total = 0
    for n in FILES:
        for e in efile.load(path(n)).entries:
            for k, (s, en) in enumerate(e.boxes):
                total += 1
                raw = e.body[s:en]
                if encode(decode(raw)) != raw:
                    bad += 1
                    if bad <= 5:
                        print('MISMATCH', n, e.index, k, raw[:24].hex(' '), decode(raw)[:40])
    print(f'{total} boxes, {bad} not identical after decode->encode')


def read_rows(tp):
    """{(entry, box): (ja, en)} from an existing TSV (empty if missing)."""
    rows = {}
    if os.path.exists(tp):
        for line in open(tp, encoding='utf-8').read().split('\n')[1:]:
            p = line.split('\t')
            if len(p) >= 4 and p[0].isdigit():
                rows[(int(p[0]), int(p[1]))] = (p[2], p[3])
    return rows


def cmd_dump(outdir):
    """(Re)write translation/events/E?.tsv. Existing `en` values are kept when the same
    (entry, box) still has the same Japanese text; otherwise they are reported."""
    os.makedirs(outdir, exist_ok=True)
    for n in FILES:
        tp = os.path.join(outdir, f'{n}.tsv')
        old = read_rows(tp)
        c = efile.load(path(n))
        kept, seen = 0, set()
        with open(tp, 'w', encoding='utf-8', newline='\n') as f:
            f.write('entry\tbox\tja\ten\n')
            for e in c.entries:
                for k, (s, en) in enumerate(e.boxes):
                    ja = decode(e.body[s:en])
                    prev = old.get((e.index, k))
                    tr = ''
                    if prev and prev[1]:
                        if prev[0] == ja:
                            tr = prev[1]
                            kept += 1
                        else:
                            print(f'{n}/{e.index}/{k}: Japanese changed, translation dropped: {prev[1][:50]}')
                    f.write(f'{e.index}\t{k}\t{ja}\t{tr}\n')
                    seen.add((e.index, k))
        lost = [k for k, v in old.items() if v[1] and k not in seen]
        print(f'wrote {tp}: {kept} translations kept' + (f', {len(lost)} orphaned {lost[:5]}' if lost else ''))


def load_edits(n, tsvdir):
    """{entry: {box: encoded bytes}} for the rows of translation/events/<n>.tsv with an `en`."""
    edits = {}
    tp = os.path.join(tsvdir, f'{n}.tsv')
    if os.path.exists(tp):
        nl, tab = chr(10), chr(9)
        for ln, line in enumerate(open(tp, encoding='utf-8').read().split(nl)[1:], 2):
            p = line.split(tab)
            if len(p) >= 4 and p[3].strip():
                try:
                    edits.setdefault(int(p[0]), {})[int(p[1])] = encode(p[3])
                except ValueError as ex:
                    raise SystemExit(f'{tp}:{ln}: {ex}')
    return edits


def cmd_layout(grow=False):
    """Reserve a fixed slot (sectors) per entry, once: translation/layout.json.
    slot = max(original sectors, ceil(1.5 * image / 2048) + 1), at most 31 sectors (the game
    loads an entry into a 0xFFF8-byte buffer). With --grow, existing slots are kept and only
    raised where the current translation needs more."""
    S = efile.SECTOR
    cur = json.load(open(LAYOUT, encoding='utf-8')) if (grow and os.path.exists(LAYOUT)) else {}
    tsvdir = os.path.join(ROOT, 'translation', 'events')
    for n in FILES:
        c = efile.load(path(n))
        edits = load_edits(n, tsvdir) if grow else {}
        slots = list(cur.get(n, []))
        for e in c.entries:
            orig = c.t[e.index + 1] - c.t[e.index]
            if e.index < len(slots):
                want = slots[e.index]
            else:
                want = min(31, max(orig, -(-int((8 + e.size) * 1.5) // S) + 1))
            if grow and e.index in edits:
                need = -(-len(e.rebuild(edits[e.index])) // S)
                want = max(want, min(31, need))
            if e.index < len(slots):
                slots[e.index] = want
            else:
                slots.append(want)
        cur[n] = slots
    json.dump(cur, open(LAYOUT, 'w', encoding='utf-8', newline=chr(10)))
    print('layout written:', {n: f'{sum(v)} sectors' for n, v in cur.items()})


def cmd_build(tsvdir, outdir, asm=None):
    """Apply translated rows. Writes outdir/E?.BIN only for files that have edits (stale
    ones are removed) and `asm`: an armips include that patches the sector tables the
    game reads from SLPS_005.00 for those files."""
    os.makedirs(outdir, exist_ok=True)
    layout = {}
    if os.path.exists(LAYOUT):
        layout = json.load(open(LAYOUT, encoding='utf-8'))
    asm = asm or os.path.join(os.path.dirname(os.path.abspath(outdir)), 'event_tables.asm')
    lines = [';; generated by tools/etext.py build - do not edit',
             ';; sector tables of the edited ADV/E?.BIN files (the game reads these copies)']
    for n in FILES:
        c = efile.load(path(n))
        edits = load_edits(n, tsvdir)
        out = os.path.join(outdir, f'{n}.BIN')
        slots = layout.get(n)
        if not edits and not slots:
            if os.path.exists(out):
                os.remove(out)
            print(f'{n}: no edits')
            continue
        for idx in edits:
            if idx >= len(c.entries):
                raise SystemExit(f'{n}: no entry {idx}')
        raws = []
        for e in c.entries:
            try:
                raws.append(e.rebuild(edits.get(e.index)))
            except ValueError as ex:
                raise SystemExit(f'{n}/{e.index}: {ex}')
        for e, r in zip(c.entries, raws):
            if len(r) - 8 > 0xFFF8:
                raise SystemExit(f'{n}/{e.index}: image {len(r) - 8} bytes exceeds 0xFFF8')
            if slots and len(r) > slots[e.index] * efile.SECTOR:
                print(f'WARNING {n}/{e.index}: needs {-(-len(r) // efile.SECTOR)} sectors but its reserved slot is '
                      f'{slots[e.index]}: the sector table changes, save states made earlier go stale. '
                      f'Raise the slot in translation/layout.json (python tools/etext.py layout --grow).')
        data, table = c.build(raws, slots)
        with open(out, 'wb') as f:
            f.write(data)
        lines.append(f'.org 0x{SLPS_TABLES[n]:08X}   ; {n} ({len(table)} values)')
        for i in range(0, len(table), 16):
            lines.append('.halfword ' + ', '.join(str(v) for v in table[i:i + 16]))
        print(f'{n}: {sum(len(v) for v in edits.values())} boxes edited, '
              f'{len(c.data)} -> {len(data)} bytes')
    with open(asm, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    a = sys.argv[1:] or ['check']
    if a[0] == 'check':
        cmd_check()
    elif a[0] == 'dump':
        cmd_dump(a[1] if len(a) > 1 else os.path.join(ROOT, 'translation', 'events'))
    elif a[0] == 'layout':
        cmd_layout('--grow' in a)
    elif a[0] == 'build':
        cmd_build(os.path.join(TEXT, 'events'),
                  a[1] if len(a) > 1 else os.path.join(ROOT, 'build', 'ADV'))
    else:
        raise SystemExit(__doc__)
