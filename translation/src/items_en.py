"""English item names (translation/strings/ITEMS.tsv, tools/items.py).

The name field holds 10 glyphs of the 8x12 small font: UPPERCASE A-Z, 0-9, space, - . & / : ! ?  Names are
therefore abbreviated; spell stones use the spell name alone; tablets (せきばん) end in TAB.
Run: python translation/src/items_en.py  (fills the `en` column), then python tools/items.py build.
Draft 2026-10-04: official 2009 PSP names were not available offline; uncertain ones are romanised and flagged.
"""
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import items  # noqa: E402

EN = {
    0: 'MEDICINE', 1: 'GARA DRINK', 2: 'JEWEL', 3: 'CHIGAESHI', 4: 'HANGONKOU', 5: 'DI-STONE', 6: 'DI-PARALYZ',
    7: 'DI-POISON', 8: 'DI-SICK', 9: 'TSURU DROP', 10: 'KAME CANDY', 11: 'S. MANISHA', 12: 'MAGIC GRD',
    13: 'PHYS GUARD', 14: 'SKULL PEND', 15: 'MAGICSTONE', 16: 'FUMA BELL', 17: 'CORESHIELD',
    18: 'STR INCENS', 19: 'VIT INCENS', 20: 'TEC INCENS', 21: 'AGL INCENS', 22: 'LUK INCENS',
    23: 'HP INCENSE', 24: 'SP INCENSE', 25: 'MUSCLE DRK', 26: 'HIRANYA', 27: 'SOMA', 28: 'MUCH MONEY',
    29: 'GOD VOICE', 30: 'MIL. BOMB', 31: 'DEMON HOME', 32: 'DEMON LAIR', 33: 'CHEW SOUL', 34: 'METAL CARD',
    35: 'AGIDYNE', 36: 'MARAGI', 37: 'MARAGION', 38: 'ENMA TAB', 39: 'BUFUDYNE', 40: 'MABUFU', 41: 'MABUFULA',
    42: 'TOUMA TAB', 43: 'GARUDYNE', 44: 'MAGARU', 45: 'MAGARULA', 46: 'FUMA TAB', 47: 'MAGDYNE',
    48: 'MAMAGNA', 49: 'MAMAGNAS', 50: 'SHINMA TAB', 51: 'FREIDYNE', 52: 'MEGIDO', 53: 'MEGIDORA',
    54: 'SCORCH TAB', 55: 'ZANDYNE', 56: 'MAZAN', 57: 'MAZANMA', 58: 'FIERCE TAB', 59: 'GURADYNE',
    60: 'MAGURAI', 61: 'MAGURAIBA', 62: 'AZURE TAB', 63: 'ZIODYNE', 64: 'MAZIO', 65: 'MAZIONGA',
    66: 'FLASH TAB', 67: 'EIHA TAB', 68: 'GUSHI TAB', 69: 'KOKUJO TAB', 70: 'PETRAMA', 71: 'PARARAMA',
    72: 'POIZMA', 73: 'SHISHIRIKA', 74: 'KYOGI TAB', 75: 'KOHA TAB', 76: 'SEIMON TAB', 77: 'CRESCENT',
    78: 'HALF MOON', 79: 'POSUMUDI', 80: 'PARARADI', 81: 'PETRADI', 82: 'SHISHIRIDI', 83: 'FULL MOON',
    84: 'TRUTH TAB', 85: 'ALEXANDRIT', 86: 'DIAMOND', 87: 'SAPPHIRE', 88: 'EMERALD', 89: 'RUBY', 90: 'PEARL',
    91: 'TANZANITE', 92: 'OPAL', 93: 'AMETHYST', 94: 'GARNET', 95: 'AQUAMARINE', 96: 'TOPAZ',
    97: 'MOONSTONE', 98: 'MALACHITE', 99: 'ONYX', 100: 'TURQUOISE', 101: 'APPLE PIE', 102: 'ABBLE PIE',
    103: 'MABBLE PIE', 104: 'SNOW MASK', 105: 'MIRR SHARD', 106: 'WAX KEYS', 107: 'AMBROSIA',
    108: 'MIRROR FRM', 109: 'LAST APPLE', 110: 'LAST ABBLE', 111: 'LAST MABBL', 112: 'SEC CARD',
    113: 'BROKEN CMP', 114: 'CELL KEY', 115: 'N. HANIWA', 116: 'HAMA MIRR', 117: 'HALF CMPCT',
    118: 'GREEN CMPT', 119: 'MIRR CHIP', 120: 'RED CMPCT', 121: 'BLUE CMPCT', 122: 'AVATARA',
    123: 'ROSETTA ST', 124: 'MASA PATCH', 125: 'DRGN SCALE', 126: 'BLUE TBLT', 127: 'AVENIR', 128: 'PASSE',
    129: 'PRESENT', 130: 'WHITE TBLT', 131: 'GOOD DEED', 132: 'ACC. DIARY', 133: 'JUDG. PACT',
    134: 'FLAMESHAWL', 135: 'DORDONA SH', 136: 'DEER MOUNT', 137: 'SUITENGU', 138: 'BLK GARTER',
    139: 'SOUVENIR', 140: 'BUFFALO B.', 141: 'BUTEI SNTO', 142: 'RAVEN FTHR', 143: 'OLIVE NECK',
    144: 'WARLORD PC', 145: 'VICT. RUNE', 146: 'MAXI TEMP.', 147: 'HOLY WATER', 148: 'JUST DO IT',
    149: 'GARUDA IMG', 150: 'CRIM. TBLT', 151: 'TIGER WRAP', 152: 'OKOSHI', 153: 'ENMA BOOK',
    154: 'BLACK TBLT', 155: 'GLASSES', 156: 'MORNG STAR', 157: 'PAGAN IDOL', 158: 'COFFIN', 159: 'RASH MASK',
    160: 'NIBLE CRYS', 161: 'FIWOLRAINI', 162: 'SCALPEL',
}

REVIEW = ("item names (ITEMS.tsv) are a first draft: 10-glyph uppercase small font, abbreviated; official 2009 PSP names not "
          "checked (spell stones use the spell name only, readings of many names romanised)")

if __name__ == '__main__':
    rows = open(items.TSV, encoding='utf-8').read().split(items.NL)
    out = [rows[0]]
    for line in rows[1:]:
        c = line.split('\t')
        if len(c) >= 4 and c[0].isdigit():
            c[3] = EN.get(int(c[0]), c[3])      # rows 163+ (equipment) are filled elsewhere: keep
            line = '\t'.join(c)
        out.append(line)
    open(items.TSV, 'w', encoding='utf-8', newline=items.NL).write(items.NL.join(out))
    rv = os.path.join(ROOT, 'translation', 'review.tsv')
    if 'ITEMS\t0\t0' not in open(rv, encoding='utf-8').read():
        with open(rv, 'a', encoding='utf-8', newline=items.NL) as f:
            f.write('ITEMS\t0\t0\t' + REVIEW + items.NL)
    print('filled', len(EN), 'item names')
