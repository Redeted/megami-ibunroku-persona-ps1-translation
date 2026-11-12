"""Full-length item / equipment names drawn with a proportional small font (slps_005.00/fullnames.asm).

  python tools/fullnames.py      QA + generate build/fullnames_data.asm (included by slps_005.00/fullnames.asm)

How it works (see the .asm for the code):
  * A GsBG map cell holding 0x8000 | bank << 13 | id (id = 1-based item id, bank = palette set 0-3) is drawn by the
    hooked libgs cell sorter as the item's FULL name, glyph by glyph with the advances below, inside the run of blank
    cells to its right (budget). If the name is wider than the budget the spacing is tightened by 1 px per glyph.
  * Demons (marker id 0x800 | id, record 0x800417A0 + id * 0x38) work like items; Personas (0x1000 | id) use
    persona_name_copy and need no pool.
  * Name source: an entry of the pool below when the name needs one, else the 10-glyph record name title-cased
    (MEDICINE -> Medicine): only names that are longer than the record or do not title-case cleanly take pool bytes.
  * The data lives in kernel RAM (KERNEL_BLOB in the .asm), copied there by the boot stub.

Width table byte per small-font glyph code: bits 0-3 advance in px (0 = 8, cell width), bits 4-5 = first used
column of the cell (sprite u offset), bit 6 = word character (title case lowers an uppercase letter after it).
Advances = glyph width INCLUDING its 1 px drop shadow (measured from the field small-font page, VRAM 896,256).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import items          # noqa: E402
import demons         # noqa: E402
import skills         # noqa: E402
import smallfont_lc   # noqa: E402

ROOT = items.ROOT
OUT = os.path.join(ROOT, 'build', 'fullnames_data.asm')
NL = chr(10)
POOL_MAX = 0x1100          # bytes reserved for the pool in the kernel blob (see FN_POOL_SIZE in the .asm)

# (left column, width incl. shadow) measured 2026-11-09 from the field small-font page
UPPER = {c: (0, 7) for c in 'ABCDEFGHJKLNOPQRSUXYZ'}
UPPER.update({c: (0, 8) for c in 'MTVW'})
UPPER['I'] = (2, 3)                       # 1-column stem: one extra px so it does not touch the next letter
LOWER = {c: (0, 6) for c in 'abdeghmnopqrstuvwxyz'}
LOWER.update({c: (0, 5) for c in 'cfjk'})
LOWER.update({'i': (1, 4), 'l': (1, 4)})
DIGIT = {c: (0, 7) for c in '0234567890'}
DIGIT['1'] = (2, 4)
PUNCT = {"'": (2, 3), '-': (0, 7), '.': (1, 3), '/': (1, 6), ':': (2, 3)}
SPACE_ADV = 3
DEMON_FLAG = 0x800         # marker id = DEMON_FLAG | demon id (items: id 1-382; Personas: 0x1000 | id, no pool)
# Names that are far too wide for a 10-cell field even tightened (user, 2026-11-10: "Silver P. Wheel" style, only the
# way-too-long ones; names a few px over, like Gouma Daisetsudan, keep the 1 px squeeze). Item index -> shown name.
MENU_SHORT = {
    11: 'Silver P. Wheel',          # Silver Prayer Wheel
    77: 'Qtr. Moon Tablet',         # Quarter Moon Tablet
    124: "Masamune's Patch",        # Masamune's Eyepatch
    133: 'Judge. Contract',         # Judgement Contract
    141: "Emp. Wu's Peach",         # Emperor Wu's Peach
    230: 'Wu Huo S.Y. Shan',        # Wu Huo Shen Yan Shan
    257: 'S. Bakunetsu Sho',        # Shinsa Bakunetsu Sho
}
WORD = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' + "'")


def table():
    """256 width bytes + {char: code}."""
    t = [0] * 256
    codes = {}
    for group in (UPPER, LOWER, DIGIT, PUNCT):
        for ch, (left, w) in group.items():
            g = items.glyph(ch)
            assert 0 < w < 16 and left < 4 and t[g] == 0, (ch, g)
            t[g] = w | left << 4 | (0x40 if ch in WORD else 0)
            codes[ch] = g
    t[0] = SPACE_ADV
    codes[' '] = 0
    return t, codes


def title_case(codes, t, lc):
    """The renderer's derivation for a record name (list of glyph codes)."""
    out, prev_word = [], False
    for g in codes:
        if prev_word and g in lc:
            g = lc[g]
        out.append(g)
        prev_word = bool(t[g] & 0x40)
    return out


def build():
    t, codes = table()
    lc = {codes[c]: codes[c.lower()] for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    # (marker id, full name, record glyphs as the game holds them)
    names = []
    en = items.read_tsv(3)
    for k, name in sorted(items.full_names().items()):
        name = MENU_SHORT.get(k, name)
        rec = en.get(k, '').strip().upper()[:10].rstrip(' ')       # what items.py writes into the record
        names.append((k + 1, name, [codes[c] for c in rec]))
    for k, (name, _) in sorted(demons.read_tsv(demons.TSV).items()):
        name = name.strip()
        if name:                                                    # what demons.py writes: the first 10 glyphs
            names.append((DEMON_FLAG | k, name, list(skills.encode(k, name)[:demons.FIELD])))
    pool, n_title, n_tail = bytearray(), 0, 0
    for mid, name, rec in names:
        bad = [c for c in name if c not in codes]
        if bad:
            raise SystemExit(f'fullnames: {mid:#x} {name!r}: no small-font glyph for {bad}')
        want = [codes[c] for c in name]
        assert len(want) < 32 and mid < 0x1000, name
        tc = title_case(rec, t, lc) if rec else None
        if tc == want:
            n_title += 1
        elif tc and want[:len(tc)] == tc:
            pool += (mid | 0x8000).to_bytes(2, 'little') + bytes(want[len(tc):]) + b'\xff'
            n_tail += 1
        else:
            pool += mid.to_bytes(2, 'little') + bytes(want) + b'\xff'
    pool += b'\xff\xff'
    if len(pool) > POOL_MAX:
        raise SystemExit(f'fullnames: pool {len(pool)} bytes > {POOL_MAX}')
    lc_map = [lc[codes[c]] for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    # the renderer lowers A..Z as the range FN_UPPER_FIRST..FN_UPPER_LAST (slps_005.00/fullnames.asm)
    assert [codes[c] for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'] == list(range(0xA6, 0xC0))
    with open(OUT, 'w', newline=NL) as o:
        o.write(';; generated by tools/fullnames.py - do not edit' + NL)
        o.write('fn_width:' + NL)
        for i in range(0, 256, 16):
            o.write('    .byte ' + ', '.join(f'0x{x:02X}' for x in t[i:i + 16]) + NL)
        o.write('fn_lower:' + NL + '    .byte ' + ', '.join(f'0x{x:02X}' for x in lc_map) + NL)
        o.write('    .align 4' + NL + 'fn_pool:' + NL)
        for i in range(0, len(pool), 16):
            o.write('    .byte ' + ', '.join(f'0x{x:02X}' for x in pool[i:i + 16]) + NL)
        o.write('fn_pool_end:' + NL)
    print(f'fullnames: {len(names)} names, {n_title} = record title-cased, {n_tail} = record + tail, '
          f'{len(names) - n_title - n_tail} whole in the pool ({len(pool)} bytes) -> {OUT}')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    build()
