"""Dungeon / floor names of the map files (D0x/D??M.BIN): the title of the MAP screen, probably the arrival banner.

  python tools/dngnames.py     write build/<D0x>/D??M.BIN (same size) with the English names

Every dungeon map file starts with a table {u32 x4}; word 2 is the offset of the NAME FIELD (one per floor, stride 0xC4): 10 slots of u16 glyph
indices (game font), padded with blank glyph 0, e.g. "　　ジョイ通り　　　" or "聖エルミン学園　１Ｆ" (floor suffix in the last
slots). At map load the field is copied to a buffer (RAM 0x801DD7FC for the current floor) and drawn by the overlay: Latin
full-width glyph codes (A = 0xA6, 0 = 0xC0, lowercase 0x723..) are drawn at HALF width, so 10 slots hold 10 characters.
English = plain text of at most 10 characters, centred with blanks. Verified in game 2026-10-06 (Joy-dori).
"""
import glob
import os
import re
import struct
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import etext   # noqa: E402

ROOT = etext.ROOT
SLOTS = 10
# base JA name (blanks removed) -> English base; the floor suffix (１Ｆ / Ｂ７ / １０Ｆ) is converted automatically
BASES = {
    '聖エルミン学園': 'Academy', '御影総合病院': 'Hosp.', '御影署': 'Police', 'セベクビル': 'Sebec',
    '御影遺跡': 'Ruins', 'カーマ宮殿': 'Kama', 'マナの城': 'Castle', '幽霊屋敷': 'Haunted',
    'デヴァ・ユガ': 'DevaYuga', 'アラヤの岩戸': 'Araya', '氷の城': 'Ice Cs.', '悪魔の山': 'DemonMt',
    'ヒュプノスの塔': 'Hypnos', 'ネメシスの塔': 'Nemesis', 'タナトスの塔': 'Thanatos',
}
# whole names without a floor number (blanks removed) -> English, max 10 characters
FIXED = {
    'ジョイ通り': 'Joy-dori', '聖エルミン学園？？？': 'Academy???', '聖エルミン学園体育館': 'Acad. Gym',
    '御影サンモール': 'Sun Mall', '地下鉄御影駅構内': 'Subway Stn', '地下鉄御影駅入口': 'SubwayGate',
    '地下鉄御影駅構内西': 'Subway W', '地下鉄御影駅入口西': 'SubGate W',
    '地下鉄御影駅構内東': 'Subway E', '地下鉄御影駅入口東': 'SubGate E',
    '廃工場地下通路': 'Fac.Tunnel', 'セベク地下研究所': 'Sebec Lab', 'ブラックマーケット': 'Black Mkt',
    '迷いの森': 'Forest', '迷いの森奧': 'Forest In', 'アヴィデア界': 'Avidya', '反夢界': 'Anti-Dream',
    'タルタロス': 'Tartarus',
}
FW = {chr(0xFF10 + i): str(i) for i in range(10)}


def translate(ja):
    """JA name field text (blanks U+3000) -> English, or None when it is not a name."""
    t = ja.replace('　', '')
    if t in FIXED:
        return FIXED[t]
    for b, en in BASES.items():
        if t.startswith(b):
            if re.fullmatch(r'(Ｂ[０-９]+|[０-９]+Ｆ)', t[len(b):]):
                fl = ''.join(FW.get(c, c) for c in t[len(b):]).replace('Ｂ', 'B').replace('Ｆ', 'F')
                sep = ' ' if len(en) + 1 + len(fl) <= SLOTS else ''      # DevaYuga1F, Thanatos1F, Ice Cs.10F
                return f'{en}{sep}{fl}'
    return None


EXTRA = {'-': '－', '.': '．', '?': '？', '&': '＆', '/': '／', ':': '：', '!': '！'}


def glyph(c):
    if c == ' ':
        return 0
    if 'A' <= c <= 'Z':
        return etext.char2g[chr(0xFF21 + ord(c) - 65)]
    if 'a' <= c <= 'z':
        return etext.char2g[chr(0xFF41 + ord(c) - 97)]
    if '0' <= c <= '9':
        return etext.char2g[chr(0xFF10 + ord(c) - 48)]
    return etext.char2g[EXTRA[c]]


def field(t):
    if len(t) > SLOTS:
        raise SystemExit(f'dngnames: {t!r} is {len(t)} characters, max {SLOTS}')
    lead = (SLOTS - len(t)) // 2
    s = ' ' * lead + t
    s += ' ' * (SLOTS - len(s))
    return b''.join(struct.pack('<H', glyph(c)) for c in s)


def main():
    n = 0
    for fp in sorted(glob.glob(os.path.join(ROOT, 'original', 'D0*', 'D*M.BIN'))):
        d = bytearray(open(fp, 'rb').read())
        if len(d) < 16:
            continue
        o = struct.unpack_from('<4I', d, 0)[2]
        # one 10-slot name field per floor, stride 0xC4 (the list ends at the first record that is not a known name)
        p, k = o, 0
        while p + 2 * SLOTS <= len(d):
            ja = ''.join(etext.glyph.get(w, '<%X>' % w) for w in struct.unpack_from('<10H', d, p))
            en = translate(ja)
            if en is None:
                break
            d[p:p + 2 * SLOTS] = field(en)
            p, k = p + 0xC4, k + 1
        if k == 0:
            raise SystemExit(f'dngnames: {os.path.basename(fp)}: no English for {ja!r}')
        out = os.path.join(ROOT, 'build', os.path.basename(os.path.dirname(fp)), os.path.basename(fp))
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, 'wb').write(bytes(d))
        print(f'  {os.path.basename(fp)}: {k} floor name(s)')
        n += 1
    print(f'dngnames: {n} map files patched')


if __name__ == '__main__':
    main()
