"""One-off: convert the companions' nicknames in a loaded game to the current small-font lowercase codes.

  python tools/fix_save_nicks.py          (DuckStation running a game loaded from the memory card; then SAVE in game)

Why: nicknames are copied into the party data when a member joins. Games started on the 2026-10-05 17:26 disc copied
them with the first lowercase set (ぢぺぁぉゎぬ...); the lowercase cells were then moved to the codes the name entry
screen stores (tools/smallfont_lc.py), so those copies would show kana. This rewrites the 8 companion records (the
hero's typed name already uses the new codes and is skipped) in the RAM party data and its save mirror.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import etext          # noqa: E402
import smallfont_lc   # noqa: E402
import patch_state as ps  # noqa: E402

OLD = 'ぢぺぁぉゎぬざぜぼぴぽぃぅぇそへだづどひぱぷねもぐゃ'      # first lowercase set, a..z
OLD_CODES = {etext.char2g[k]: i for i, k in enumerate(OLD)}
COPIES = [(0x8005D6B7, 0xEC), (0x801F1C0B, 0x60)]                 # (hero's field, stride per member)
FIELD = 10


def main():
    ps.init()
    n = 0
    for base, stride in COPIES:
        for m in range(1, 9):
            a = base + m * stride
            b = bytearray.fromhex(ps.call('read_memory', address=a, size=FIELD)['data'])
            if b[0] == 0 or b[0] == 0xFF:
                continue
            new = bytearray(b)
            for i, c in enumerate(b):
                if c == 0xFF:
                    break
                if c in OLD_CODES:
                    new[i] = smallfont_lc.LC_CODES[OLD_CODES[c]]
            if new != b:
                ps.call('write_memory', address=a, data=bytes(new).hex())
                n += 1
                print(f'{a:08X}: {b.hex()} -> {new.hex()}')
    print(f'{n} nickname copies converted; save the game on the memory card now')


if __name__ == '__main__':
    main()
