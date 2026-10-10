"""Casino "MAKE THE CODE" prize bar (CASINO.BIN): Shift-JIS prize strings -> English, in place.

  python tools/casinoprize.py          patch build/CASINO.BIN (run AFTER armips, which creates it)
  python tools/casinoprize.py list     print every prize string with its English and glyph count

Found 2026-10-09 (user: R1 on the START screen of the code machine, slot 2): the prize list is a table of ~95 records
(0x42 bytes: 4 header bytes, Shift-JIS text, 0x0A, zero fill; first at file 0x42A4C) inside CASINO.BIN. The text object
converter (RAM 0x8008CC48) turns every character into a glyph index (array of 20 halfwords per object) by lead byte:
0x82 digits (0x824F-0x8258) -> index second+0x53, 0x82 UPPERCASE letters (0x8260-0x8279) -> second+0x60, 0x81 space -> blank,
0x81 5B / 7C (the long-vowel mark / minus) -> 0xAC, katakana / hiragana via their own ranges. Lowercase letters have NO tile
(they map to blank), so the English is ALL CAPS. The bar shows 19 cells (the 20th is clipped by the bar edge) and the array holds
20: never write more than 19 glyphs (no bound check in the converter).
Record layout of one prize line: <name> [ 0x8258 ("9", drawn as "+") <tail> ] where the tail is `C 1000000` (coins; glyph C is the
coin), `C 5000` or the katakana metal card -> "MTL CARD". The English keeps the tail bytes except the metal card.
Names come from the item table (ITEMS.tsv, same names as the inventory) where one exists; the longest variant that fits the
19-cell budget is used.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'translation', 'src'))
from casinoprize_en import NAMES   # noqa: E402

MAX_CELLS = 19
PLUS = b'\x82\x58'                       # "9": drawn as "+"
METAL = 'メタルカード'
PAT = re.compile(rb'((?:[\x81-\x9f\xe0-\xef][\x40-\xfc]){2,})\x0a')
FIRST, LAST = 0x42A4C, 0x45200           # table range in the file (the first four matches are code, not text)


def fw(s):
    out = b''
    for c in s:
        if c == ' ':
            out += b'\x81\x40'
        elif c == '-':
            out += b'\x81\x7c'
        elif 'A' <= c <= 'Z':
            out += (0x8260 + ord(c) - 65).to_bytes(2, 'big')
        elif '0' <= c <= '9':
            out += (0x824F + ord(c) - 48).to_bytes(2, 'big')
        else:
            raise SystemExit(f'casinoprize: unsupported character {c!r} in {s!r}')
    return out


def records(d):
    for m in PAT.finditer(d):
        if not FIRST <= m.start() <= LAST:
            continue
        try:
            ja = m.group(1).decode('shift_jis')
        except UnicodeDecodeError:
            continue
        yield m.start(), m.group(1), ja


def translate(ja):
    """-> (english text, tail description, byte string)"""
    name, sep, tail = ja.partition('９')
    if name not in NAMES:
        raise SystemExit(f'casinoprize: no English for {name!r} ({ja})')
    if sep:
        if tail == METAL:
            tb, ts = PLUS + fw('MTL CARD'), '+MTL CARD'
        else:
            tb, ts = PLUS + tail.encode('shift_jis'), '+' + tail
    else:
        tb, ts = b'', ''
    cells = len(tb) // 2
    for opt in NAMES[name]:                          # longest first
        if len(opt) + cells <= MAX_CELLS:
            return opt + ts, fw(opt) + tb
    raise SystemExit(f'casinoprize: {name}: no variant fits {MAX_CELLS - cells} cells: {NAMES[name]}')


def main():
    src = open(os.path.join(ROOT, 'original', 'CASINO.BIN'), 'rb').read()
    out = bytearray(open(os.path.join(ROOT, 'build', 'CASINO.BIN'), 'rb').read()) if 'list' not in sys.argv else None
    n = 0
    for off, raw, ja in records(src):
        en, b = translate(ja)
        assert len(b) // 2 <= MAX_CELLS and len(b) + 1 <= 0x3E
        if out is not None:
            new = (b + bytes([0x0A])).ljust(len(raw) + 1, bytes([0]))   # never change the file size (a longer slice would shift the rest)
            assert not any(src[off + len(raw) + 1:off + len(new)]), f'{off:06X}: English overruns non-zero data'
            out[off:off + len(new)] = new
        else:
            sys.stdout.reconfigure(encoding='utf-8')
            print(f'{off:06X} {len(b) // 2:2d}  {ja}  ->  {en}')
        n += 1
    if out is not None:
        assert len(out) == len(src), 'casinoprize: size changed'
        open(os.path.join(ROOT, 'build', 'CASINO.BIN'), 'wb').write(out)
    print(f'casinoprize: {n} prize strings')


if __name__ == '__main__':
    main()
