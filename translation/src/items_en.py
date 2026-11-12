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

# Official 2009 PSP names (persona1.wikidot.com /item, /presonaspell, /personaitem, /gem) in 10 glyphs; checked
# 2026-10-11. Spell stones "<Spell> Stone": "<SPELL> ST" when it fits, else the spell alone (user decision
# 2026-10-11); tablets (せきばん) "<x> TAB". Key / quest items without an official list keep the draft names.
EN = {
    0: 'MEDICINE', 1: 'RATTLE DRK', 2: 'BEAD', 3: 'REV. BEAD', 4: 'LIFE BALM', 5: 'DIS-STONE', 6: 'DIS-PARA',
    7: 'DIS-POISON', 8: 'DIS-SICK', 9: 'SLICK DROP', 10: 'TURTLE CND', 11: 'PRAYER WHL', 12: 'MAGICAL GD',
    13: 'PHYS GUARD', 14: 'SKULL PEND', 15: 'LIFE STONE', 16: 'REPULSE BL', 17: 'CORE SHLD',
    18: 'ST INCENSE', 19: 'VI INCENSE', 20: 'DX INCENSE', 21: 'AG INCENSE', 22: 'LU INCENSE',
    23: 'HP INCENSE', 24: 'SP INCENSE', 25: 'MUSCLE DRK', 26: 'HIRANYA', 27: 'SOMA', 28: 'NUM. BELL',
    29: 'DIVINE VCE', 30: 'MILLN BOMB', 31: "DEVIL'S HS", 32: "DEVIL'S HM", 33: 'CHEW SOUL', 34: 'METAL CARD',
    # Bead / Revival Bead / Balm of Life / Dis-Para / Slick Drop / Turtle Candy / Silver Prayer Wheel / Magical Guard /
    # Physical Guard / Life Stone / Repulse Bell / Core Shield / St Vi Dx Ag Lu Incense / Muscle Drink / Numerous Bell /
    # Divine Voice / Millionaire Bomb / Devil's House / Devil's Home / Chewing Soul
    35: 'AGIDYNE ST', 36: 'MARAGI ST', 37: 'MARAGION', 38: 'E.FIRE TAB', 39: 'BUFUDYNE', 40: 'MABUFU ST',
    41: 'MABUFULA', 42: 'E.ICE TAB', 43: 'GARUDYNE', 44: 'MAGARU ST', 45: 'MAGARULA', 46: 'E.WIND TAB',
    47: 'MAGDYNE ST', 48: 'MAMAGNA ST', 49: 'MAMAGNARA', 50: 'E.QUAKE TB', 51: 'FREIDYNE', 52: 'MEGIDO ST',
    53: 'MEGIDOLA', 54: 'SCORCH TAB', 55: 'ZANDYNE ST', 56: 'MAZAN ST', 57: 'MAZANMA ST', 58: 'GALE TAB',
    59: 'GRYDYNE ST', 60: 'MAGRY ST', 61: 'MAGRYVA ST', 62: 'WALL TAB', 63: 'ZIODYNE ST', 64: 'MAZIO ST',
    65: 'MAZIONGA', 66: 'FLASH TAB', 67: 'D.WAVE TAB', 68: 'DOGGRL TAB', 69: 'E.ROPE TAB', 70: 'PETRA ST',
    71: 'PARA ST', 72: 'POISMA ST', 73: 'NERVE ST', 74: 'FALSHD TAB', 75: 'L.WAVE TAB', 76: 'H.WRIT TAB',
    77: 'Q.MOON TAB', 78: 'H.MOON TAB', 79: 'POSUMUDI', 80: 'PARALADI', 81: 'PETRADI ST', 82: 'NERVUNDI',
    83: 'F.MOON TAB', 84: 'VENITY TAB', 85: 'ALEXANDRIT',
    # Evil Fire / Ice / Wind / Quake Tablet, Scorching, Gale, Wall, Flash, Dark Wave, Doggerel, Ebon Rope, Falsehood,
    # Light Wave, Holy Writ, Quarter / Half / Full Moon, Venity Tablet; Petra / Para / Poisma / Nerve Stone
    86: 'DIAMOND', 87: 'SAPPHIRE', 88: 'EMERALD', 89: 'RUBY', 90: 'PEARL',
    91: 'TANZANITE', 92: 'OPAL', 93: 'AMETHYST', 94: 'GARNET', 95: 'AQUAMARINE', 96: 'TOPAZ',
    97: 'MOONSTONE', 98: 'MALACHITE', 99: 'ONYX', 100: 'TURQUOISE', 101: 'APPLE PIE', 102: 'ABBLE PIE',
    103: 'MABBLE PIE', 104: 'SNOW MASK', 105: 'MIRR SHARD', 106: 'WAX KEYS', 107: 'AMBROSIA',
    108: 'MIRROR FRM', 109: 'LAST APPLE', 110: 'CLEAN SALT', 111: 'EMERG EXIT', 112: 'SEC CARD',
    113: 'BROKEN CMP', 114: 'CELL KEY', 115: 'N. HANIWA', 116: 'HAMA MIRR', 117: 'HALF CMPCT',
    118: 'GREEN CMPT', 119: 'MIRR CHIP', 120: 'RED CMPCT', 121: 'BLUE CMPCT',
    # Persona artifacts (official /personaitem): Avatara, Rosetta Stone, Masamune's Eyepatch, Dragon Scale, Blue Tablet,
    # Avenir, (Passe: the wiki's "Pasque Flower" reads バッセ, the game has パッセ = passe), Present, White Tablet,
    # Daily Meal, Prosecutor's Diary, Judgement Contract, Flame Shawl, Dordona's Oar, Stuffed Deer, Suitengu Talisman,
    # Black Garter Belt, Kolkata Souvenir, Bisonskin Drums, Emperor Wu's Peach, Raven Feather, Olive Accessory,
    # General Piece, Victorian Rune, Maxi Tempest, Purified Water, Gottabe Shoes, Karura, Crimson Tablet,
    # Tora Stomachband, Kaminari-Okoshi, Enma Notebook, Black Tablet, Amber Glasses, Shining Star, Cultish Statue,
    # Babylonian Coffin, Faceless Mask, Nibel Crystal, Fomor Lineage
    122: 'AVATARA', 123: 'ROSETTA', 124: 'MASA.PATCH', 125: 'DRGN SCALE', 126: 'BLUE TBLT', 127: 'AVENIR',
    128: 'PASSE', 129: 'PRESENT', 130: 'WHITE TBLT', 131: 'DAILY MEAL', 132: 'PROS.DIARY', 133: 'JUDG.CONTR',
    134: 'FLAMESHAWL', 135: 'DORDNA OAR', 136: 'STUFF.DEER', 137: 'SUITENGU', 138: 'BLK GARTER',
    139: 'KOLKATA SV', 140: 'BISON DRUM', 141: "WU'S PEACH", 142: 'RAVEN FTHR', 143: 'OLIVE ACC.',
    144: 'GEN. PIECE', 145: 'VICT. RUNE', 146: 'MAXI TEMP.', 147: 'PURE WATER', 148: 'GOTTABE SH',
    149: 'KARURA', 150: 'CRIM. TBLT', 151: 'TORA BAND', 152: 'KAMINARI-O', 153: 'ENMA NOTE',
    154: 'BLACK TBLT', 155: 'AMBER GLSS', 156: 'SHINE STAR', 157: 'CULTSTATUE', 158: 'BAB.COFFIN', 159: 'FACELESS M',
    160: 'NIBEL CRYS', 161: 'FOMOR LIN.', 162: 'SCALPEL',
}

# FULL names (mixed case) for the `full` column: drawn by the proportional name renderer (tools/fullnames.py) where a
# screen has been patched for it; the 10-glyph `en` above stays in the record for every other screen. Equipment
# (163-381) has its full name in `en` already. Checked 2026-11-09 against the PSP item table (decrypted EBOOT in
# PPSSPP RAM, 0x40-byte records at 0x08A6E37C): PSP names except project decisions (Hama Mirror, Abble / Mabble Pie,
# Passe, Prison Key, Compact Half: user 2026-11-09, dialogue updated).
_STONES = {35: 'Agidyne', 36: 'Maragi', 37: 'Maragion', 39: 'Bufudyne', 40: 'Mabufu', 41: 'Mabufula', 43: 'Garudyne',
           44: 'Magaru', 45: 'Magarula', 47: 'Magnadyne', 48: 'Mamagna', 49: 'Mamagnara', 51: 'Freidyne', 52: 'Megido',
           53: 'Megidola', 55: 'Zandyne', 56: 'Mazan', 57: 'Mazanma', 59: 'Grydyne', 60: 'Magry', 61: 'Magryva',
           63: 'Ziodyne', 64: 'Mazio', 65: 'Mazionga', 70: 'Petra', 71: 'Para', 72: 'Poisma', 73: 'Nerve',
           79: 'Posumudi', 80: 'Paraladi', 81: 'Petradi', 82: 'Nervundi'}
_TABLETS = {38: 'Evil Fire', 42: 'Evil Ice', 46: 'Evil Wind', 50: 'Evil Quake', 54: 'Scorching', 58: 'Gale',
            62: 'Wall', 66: 'Flash', 67: 'Dark Wave', 68: 'Doggerel', 69: 'Ebon Rope', 74: 'Falsehood',
            75: 'Light Wave', 76: 'Holy Writ', 77: 'Quarter Moon', 78: 'Half Moon', 83: 'Full Moon', 84: 'Verity'}
FULL = {
    0: 'Medicine', 1: 'Rattle Drink', 2: 'Bead', 3: 'Revival Bead', 4: 'Balm of Life', 5: 'Dis-Stone',
    6: 'Dis-Para', 7: 'Dis-Poison', 8: 'Dis-Sick', 9: 'Slick Drop', 10: 'Turtle Candy', 11: 'Silver Prayer Wheel',
    12: 'Magical Guard', 13: 'Physical Guard', 14: 'Skull Pendulum', 15: 'Life Stone', 16: 'Repulse Bell',
    17: 'Core Shield', 18: 'St Incense', 19: 'Vi Incense', 20: 'Dx Incense', 21: 'Ag Incense', 22: 'Lu Incense',
    23: 'HP Incense', 24: 'SP Incense', 25: 'Muscle Drink', 26: 'Hiranya', 27: 'Soma', 28: 'Numerous Bell',
    29: 'Divine Voice', 30: 'Millionaire Bomb', 31: 'Demon House', 32: 'Demon Den', 33: 'Chewing Soul',
    34: 'Metal Card', 85: 'Alexandrite',
    86: 'Diamond', 87: 'Sapphire', 88: 'Emerald', 89: 'Ruby', 90: 'Pearl', 91: 'Tanzanite', 92: 'Opal',
    93: 'Amethyst', 94: 'Garnet', 95: 'Aquamarine', 96: 'Topaz', 97: 'Moonstone', 98: 'Malachite', 99: 'Onyx',
    100: 'Turquoise', 101: 'Apple Pie', 102: 'Abble Pie', 103: 'Mabble Pie', 104: 'Snow Queen Mask',
    105: 'Mirror Shard', 106: 'Cell Key Ring', 107: 'Ambrosia', 108: 'Mirror Frame', 109: 'Last Apple Pie',
    110: 'Clean Salt', 111: 'Emergency Exit', 112: 'Security Card', 113: 'Broken Compact', 114: 'Prison Key',
    115: 'Northern Haniwa', 116: 'Hama Mirror', 117: 'Compact Half', 118: 'Green Compact', 119: 'Mirror Piece',
    120: 'Red Compact', 121: 'Blue Compact',
    122: 'Avatar', 123: 'Rosetta Stone', 124: "Masamune's Eyepatch", 125: 'Dragon Scale', 126: 'Blue Tablet',
    127: 'Avenir', 128: 'Passe', 129: 'Present', 130: 'White Tablet', 131: 'Daily Meal', 132: "Prosecutor's Diary",
    133: 'Judgement Contract', 134: 'Flame Shawl', 135: "Dordona's Oar", 136: 'Stuffed Deer',
    137: 'Suitengu Talisman', 138: 'Black Garter Belt', 139: 'Kolkata Souvenir', 140: 'Bisonskin Drums',
    141: "Emperor Wu's Peach", 142: 'Raven Feather', 143: 'Olive Necklace', 144: 'General Piece',
    145: 'Victorian Rune', 146: 'Maxi Tempest', 147: 'Purified Water', 148: 'Gottabe Shoes', 149: 'Karura',
    150: 'Crimson Tablet', 151: 'Tora Stomachband', 152: 'Kaminari-Okoshi', 153: 'Enma Notebook',
    154: 'Black Tablet', 155: 'Amber Glasses', 156: 'Morning Star', 157: 'Pagan Idol', 158: 'Babylonian Coffin',
    159: 'Faceless Mask', 160: 'Nibel Crystal', 161: 'Fomor Lineage', 162: 'Scalpel',
}
FULL.update({k: v + ' Stone' for k, v in _STONES.items()})
FULL.update({k: v + ' Tablet' for k, v in _TABLETS.items()})
assert sorted(FULL) == list(range(163)), sorted(set(range(163)) - set(FULL))

REVIEW = ("item names (ITEMS.tsv): consumables, spell stones, tablets, gems and Persona artifacts follow the official 2009 PSP "
          "names (checked 2026-10-11, abbreviated to 10 glyphs); key / quest items (101-121, SKULL PEND) are still draft names")

if __name__ == '__main__':
    rows = open(items.TSV, encoding='utf-8').read().split(items.NL)
    out = ['idx	addr	ja	en	full']
    for line in rows[1:]:
        c = line.split('\t')
        if len(c) >= 4 and c[0].isdigit():
            c[3] = EN.get(int(c[0]), c[3])      # rows 163+ (equipment) are filled elsewhere: keep
            c = (c + [''])[:5]
            c[4] = FULL.get(int(c[0]), c[4])    # `full`: rows 163+ fall back to `en` in tools/items.py
            line = '\t'.join(c)
        out.append(line)
    open(items.TSV, 'w', encoding='utf-8', newline=items.NL).write(items.NL.join(out))
    rv = os.path.join(ROOT, 'translation', 'review.tsv')
    if 'ITEMS\t0\t0' not in open(rv, encoding='utf-8').read():
        with open(rv, 'a', encoding='utf-8', newline=items.NL) as f:
            f.write('ITEMS\t0\t0\t' + REVIEW + items.NL)
    print('filled', len(EN), 'item names')
