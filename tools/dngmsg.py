"""Dungeon in-room messages (locked doors, closed shops ...) inside the dungeon data files D0x/D??.BIN.

  python tools/dngmsg.py     patch build/<D0x>/D??.BIN (run after smallfont_pages.py; reads the original if there is no build copy)

The boxes are dialogue strings (FF02 wait + FF01 end) of the dungeon script data, shown by the DNG overlay dialogue engine
(VWF ASCII, 1 byte per letter; FF03 = new line, FF04 = new page). The slots are the Japanese lengths (mostly 1-byte kana), so the
English is abbreviated to fit and the rest of the slot is zero-filled. 15 distinct texts, 21 places in the 16 dungeon files
(D00 Mikage / D01 / D05 / D0A ...); every occurrence of a Japanese text is replaced.
"""
import glob
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import etext   # noqa: E402

ROOT = etext.ROOT
END = bytes((0xFF, 0x01))
MSGS = [
    ('鍵がかかっているようだ<FF02>', "It's locked.<FF02>"),
    ('鍵がかかっていて<FF03>入れそうにない<FF02>', "Locked. No entry.<FF02>"),
    ('扉には鍵がかけられている<FF02><FF04>…あの少女は<FF03>幻だったのだろうか…？<FF02>',
     "Door's locked.<FF02><FF04>...Was she an<FF03>illusion?<FF02>"),
    ('扉には鍵がかかっている<FF02>', "It's locked.<FF02>"),
    ('いつのまにかまた<FF03>鍵がかけられている………<FF02>', "It's locked again...<FF02>"),
    ('この部屋はもう<FF03>長い間使われていない・・・<FF02>', "This room is long<FF03>unused...<FF02>"),
    ('この部屋は<FF03>長い間使われていない・・・<FF02>', "This room is long<FF03>unused...<FF02>"),
    ('店は閉まっている<FF02>', "Closed.<FF02>"),
    ('いないようだ…<FF02>', "No one.<FF02>"),
    ('人の気配はない…<FF02>', "No one here.<FF02>"),
    ('鍵がかかっている…<FF02>', "Locked...<FF02>"),
    ('待っててくれ<FF02>', "Hold on<FF02>"),
    ('扉は凍り付いている<FF02>', "Frozen shut.<FF02>"),
    ('扉は固く閉ざされている<FF02>', "Sealed shut.<FF02>"),
    ('この教室は今は<FF03>使用されていない<FF02>', "Classroom unused.<FF02>"),
    ('体育館は閉鎖されている<FF02>', "Gym is closed.<FF02>"),
]


def main():
    total = files = 0
    for fp in sorted(glob.glob(os.path.join(ROOT, 'original', 'D0*', 'D*.BIN'))):
        name = os.path.basename(fp)
        if len(name) != 7:
            continue
        bp = fp.replace(os.sep + 'original' + os.sep, os.sep + 'build' + os.sep)
        d = bytearray(open(bp if os.path.exists(bp) else fp, 'rb').read())
        n = 0
        for ja, en in MSGS:
            jb = etext.encode(ja, end=None) + END
            eb = etext.encode(en, end=None) + END
            if len(eb) > len(jb):
                raise SystemExit(f'dngmsg: {en!r} needs {len(eb)} bytes, slot {len(jb)}')
            i = d.find(jb)
            while i >= 0:
                d[i:i + len(jb)] = eb + bytes(len(jb) - len(eb))
                n += 1
                i = d.find(jb, i + len(jb))
        if n:
            os.makedirs(os.path.dirname(bp), exist_ok=True)
            open(bp, 'wb').write(bytes(d))
            files += 1
            total += n
    print(f'dngmsg: {total} messages in {files} files')


if __name__ == '__main__':
    main()
