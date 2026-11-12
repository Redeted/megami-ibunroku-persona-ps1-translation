"""Title-case the small-font tables the original game holds in English UPPERCASE (run from build.py after armips).

Persona status page (menus of ADV / DNG / S2D, the same data in each overlay):
  * arcana names, 22 x 10 bytes, FF-terminated when shorter ("MAGICIAN" ... "FOOL"); also inserted in the fusion
    result message (<FF13>)
  * attack-type names of the "Type" column, 18 x 10 bytes, 00-padded ("HOLYLIGHT" ... "WONDER")
Battle ANALYZE window (BTLP.BIN): the same names as FF-terminated strings in 00-padded slots, RAM 0x800D2938-0x800D2A26
("NORMAL" "ELEMENTAL" "PHYSICAL" "EVILDARK" "HOLYLIGHT" + the 18 types); every letter after the first of a word is lowered.
The words are kept (original English of the Japanese game); only the case changes, in place, same length:
PRIESTESS -> Priestess, HANGED MAN -> Hanged Man, HOLYLIGHT -> Holylight.  The lowercase glyphs are the redrawn kana
cells of tools/smallfont_lc.py (same derivation as the full item names: tools/fullnames.py title_case).

    python tools/titlecase_tables.py          patch build/ADV.BIN, DNG.BIN, S2D.BIN
    python tools/titlecase_tables.py list     print the tables
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fullnames

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 0x800643C4
REF = ('DNG.BIN', 0x8009AF94, 22 * 10, 0x8009B098, 18 * 10)     # where the tables sit in the reference overlay
FILES = ('ADV.BIN', 'DNG.BIN', 'S2D.BIN')


def main():
    t, codes = fullnames.table()
    lc = {codes[c]: codes[c.lower()] for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    back = {v: k for k, v in codes.items()}
    ref = open(os.path.join(ROOT, 'original', REF[0]), 'rb').read()
    tabs = [ref[REF[1] - BASE:REF[1] - BASE + REF[2]], ref[REF[3] - BASE:REF[3] - BASE + REF[4]]]
    # per 10-byte entry: a full-length entry has no terminator, the next one must still start with a capital
    new = [b''.join(bytes(fullnames.title_case(list(x[i:i + 10]), t, lc)) for i in range(0, len(x), 10)) for x in tabs]
    battle(lc)
    if 'list' in sys.argv:
        for x in new:
            print(' | '.join(''.join(back.get(c, '') for c in x[i:i + 10] if c != 0xFF).strip()
                             for i in range(0, len(x), 10)))
        return
    for name in FILES:
        orig = open(os.path.join(ROOT, 'original', name), 'rb').read()
        path = os.path.join(ROOT, 'build', name)
        d = bytearray(open(path, 'rb').read())
        size = len(d)
        for old, x in zip(tabs, new):
            assert orig.count(old) == 1, (name, 'table not found once')
            o = orig.find(old)
            assert d[o:o + len(old)] in (old, x), (name, hex(o), 'table changed by another tool')
            d[o:o + len(x)] = x
        assert len(d) == size
        open(path, 'wb').write(d)
        print(f'{name}: arcana + attack-type tables title-cased')


def battle(lc):
    """BTLP.BIN attack-type strings: lower every letter that follows a letter."""
    name, a0, a1 = 'BTLP.BIN', 0x800D2938, 0x800D2A27
    orig = open(os.path.join(ROOT, 'original', name), 'rb').read()[a0 - BASE:a1 - BASE]
    up = set(lc)
    assert all(c in up or c in (0, 0xFF) for c in orig) and orig.endswith(b'\xff'), 'BTLP type table moved'
    new = bytearray(orig)
    for i in range(1, len(new)):
        if orig[i] in up and orig[i - 1] in up:
            new[i] = lc[orig[i]]
    if 'list' in sys.argv:
        back = {v: k for k, v in fullnames.table()[1].items()}
        print(' | '.join(''.join(back[c] for c in w) for w in bytes(new).replace(b'\0', b'').split(b'\xff') if w))
        return
    path = os.path.join(ROOT, 'build', name)
    d = bytearray(open(path, 'rb').read())
    assert d[a0 - BASE:a1 - BASE] in (orig, bytes(new)), 'BTLP type table changed by another tool'
    d[a0 - BASE:a1 - BASE] = new
    open(path, 'wb').write(d)
    print(f'{name}: attack-type strings title-cased')


if __name__ == '__main__':
    main()
