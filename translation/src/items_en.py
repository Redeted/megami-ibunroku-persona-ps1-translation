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
    108: 'MIRROR FRM', 109: 'LAST APPLE', 110: 'LAST ABBLE', 111: 'LAST MABBL', 112: 'SEC CARD',
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

REVIEW = ("item names (ITEMS.tsv): consumables, spell stones, tablets, gems and Persona artifacts follow the official 2009 PSP "
          "names (checked 2026-10-11, abbreviated to 10 glyphs); key / quest items (101-121, SKULL PEND) are still draft names")

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
