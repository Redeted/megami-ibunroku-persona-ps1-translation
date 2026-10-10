"""English location names of the overworld (translation/strings/S2DNAMES.tsv, tools/s2dnames.py).

ASCII, at most 7 characters (area labels are 8-cell boxes; the banner is a 15-cell box drawn with full-width game glyphs, see tools/s2dnames.py). Spellings follow glossary.tsv; unsure readings are in review.tsv.
Run: python translation/src/s2dnames_en.py (fills the `en` column), then python tools/s2dnames.py build.
"""
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import s2dnames  # noqa: E402

EN = {
    0: '2-chome', 1: '3-chome', 2: 'School', 3: 'Academy', 4: 'S.Gate',
    5: 'Hosp.', 6: 'H.Gate', 7: 'Shrine', 8: 'Araya', 9: 'Sh.Gate',
    10: 'Police', 11: 'P.Gate', 12: 'Factory', 13: 'F.Gate', 14: 'Sebec', 15: 'Sb.Gate',
    16: 'SW Gate', 17: 'Subway', 18: 'SunMall', 19: 'JoyDori', 20: 'Ruins', 21: 'R.Gate',
    22: 'Museum', 23: 'M.Gate', 24: 'Kaneda', 25: 'K.Gate', 26: 'Himeno', 27: 'Hm.Gate',
    28: 'Agastya', 29: 'Agastya', 30: 'Agastya', 31: 'Store', 32: 'YIN&YAN', 33: 'St.Gate',
    34: 'Clinic', 35: 'C.Gate', 36: 'Castle', 37: 'Cs.Gate', 38: 'Forest', 39: 'Fo.Gate',
    40: 'Haunted', 41: 'Hn.Gate', 42: 'BMarket', 43: 'Hosp.', 44: 'Museum', 45: 'SunMall',
}
REVIEW = ("overworld location names (S2DNAMES.tsv): 7-character abbreviations because of the 8-cell label boxes (full names need a narrow-font hook for the S2D text engine 0x8009B2F4); draft; 金田邸 read as Kaneda, 姫野 as Himeno, 迷いの森 as Lost Forest, "
          "御影署 as Mikage Police; check against the 2009 PSP names")

# the zone starts one name earlier (0x800AAE0E = Mikage-cho 1-chome): shift the indices
EN = {0: '1-chome', **{k + 1: v for k, v in EN.items()}}

if __name__ == '__main__':
    rows = open(s2dnames.TSV, encoding='utf-8').read().split(s2dnames.NL)
    out = [rows[0]]
    for line in rows[1:]:
        c = line.split('\t')
        if len(c) >= 5 and c[0].isdigit():
            c = c[:5] + [EN.get(int(c[0]), '')]
            line = '\t'.join(c)
        out.append(line)
    open(s2dnames.TSV, 'w', encoding='utf-8', newline=s2dnames.NL).write(s2dnames.NL.join(out))
    rv = os.path.join(ROOT, 'translation', 'review.tsv')
    if 'S2DNAMES\t0\t0' not in open(rv, encoding='utf-8').read():
        with open(rv, 'a', encoding='utf-8', newline=s2dnames.NL) as f:
            f.write('S2DNAMES\t0\t0\t' + REVIEW + s2dnames.NL)
    print('filled', len(EN), 'names')
