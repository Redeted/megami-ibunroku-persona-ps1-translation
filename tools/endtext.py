"""Ending epilogue pages (EXE/END.BIN): the 1-bit 320x240 text pages shown after the movies.

  python tools/endtext.py      writes build/EXE/END.BIN (+ previews in translation/images/end_*.png)

END.BIN is a stream of TIMs: 16bpp backgrounds / portraits and 4bpp text pages (CLUT index 0 = white ink, 1 = black).
The credits roll pages (staff names in kanji, English job titles, "fin") need no translation. For each epilogue page the
Japanese ink is located, the page is cleared and the English text is drawn with the project's VWF font
(font/vwf_font.bin, 1-bit, proportional): centred pages stay centred on the old text, profile pages keep the left edge /
column width of the old paragraph (the portrait is on the other half of the screen).
The file keeps its size, so build_disc.py writes it in place.
"""
import os
import struct
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tim  # noqa: E402

ROOT = tim.ROOT
FONT = open(os.path.join(ROOT, 'font', 'vwf_font.bin'), 'rb').read()
WIDTH = open(os.path.join(ROOT, 'font', 'vwf_width.bin'), 'rb').read()
END_LBA, END_SIZE = 114505, 5058560
PITCH = 12

# TIM offset: ('c', [lines]) centred block | ('p', header, body text)
PAGES = {
    0x26804: ('c', ['For a while after the incident,', 'it drew the whole world\'s attention,', 'but Mikage-cho',
                    'is slowly regaining its peace.']),
    0x56004: ('c', ['The names of SEBEC and Kandori', 'were widely publicized, but the names', 'of the high school students deeply',
                    'involved in the incident', 'were never revealed.']),
    0x85804: ('p', 'Sonomura Maki',
              "Fully recovered from her illness, she has grown into a bright, positive woman. She won a prize at a "
              "major painting exhibition and seems to have good prospects, but her main interest is her new life with "
              "her mother. She was recently seen enjoying dinner with her mother and a man who seems to be her boyfriend."),
    0x9E004: ('p', 'Inaba Masao',
              "Overriding his parents' objections, he went alone to New York. His skill at painting art has won "
              "recognition, and rumors of it have reached Japan. Still, he apparently finds the phone call from his "
              "mother, which comes without fail once a week, annoying."),
    0xB7004: ('p', 'Nanjo Kei',
              "To train as a businessman, he hid his status and works in sales at a subcontracting company. "
              "Everywhere he goes he keenly feels both the warmth and the harshness of the world, and his personality "
              "is reportedly mellowing little by little. He has been seen dozing on the train wearing his best necktie."),
    0xCF804: ('p', 'Uesugi Hidehiko',
              "He debuted as a TV personality. On a TV talk show he cheerfully exposed his embarrassing past. His "
              "unpretentious attitude got him ranked near the top of a magazine popularity poll. Still, he is "
              "apparently as concerned as ever about rumors of Mark."),
    0xE8004: ('p', 'Kirishima Eriko',
              "As one of Japan's top models, she often graces the covers of women's magazines. Her unpretentious "
              "lifestyle is well liked, and she is active in many fields as an image leader for young women. "
              "Recently she was shown on a TV paranormal special, commenting with obvious delight."),
    0x101004: ('p', 'Ayase Yuka',
               "Awakened to the dream of having a happy family, she took an office job at a mid-sized trading "
               "company. She married a pleasant young coworker and reportedly has the family she longed for. "
               "However, she is apparently a little dissatisfied with her husband's annual income."),
    0x119804: ('p', 'Kido Reiji',
               "Freed from a life of only revenge, he began to walk through life positively, if clumsily. Soon after "
               "graduating he married, and he is now the father of one child. His bride was reportedly a gentle "
               "woman resembling his mother. The child takes after his father and is unfriendly, says Mark."),
    0x132804: ('c', ["Thanks to the boys' efforts, the school", 'that had turned into an ice castle', 'returned to normal.',
                     'The curse of the masks vanished,', "and one of the school's legends", 'came to an end.']),
    0x162004: ('c', ['As long as people have hearts', 'that turn hope into despair,', 'the eternal night will come',
                     'again and again']),
    0x191804: ('c', ['With the Queen\'s words behind them,', 'the boys and girls who shook off', 'the darkness in their hearts',
                     'begin to walk toward the future...']),
    0x1C1004: ('c', ['The boys\' struggle was in vain;', 'they could not protect', 'the school and Saeko...']),
    0x1CA804: ('c', ['The world is wrapped in eternal night,', 'and everything is dyed in the white', 'and black called despair.']),
    0x1FA004: ('c', ['What became of him...', '', 'That is for you to decide.']),
    0x229804: ('c', ['In the name of eternal beauty...']),
}


def text_width(s):
    return sum(WIDTH[ord(c) - 0x20] for c in s) - 1 if s else 0


def wrap(text, width):
    lines, cur = [], ''
    for w in text.split():
        t = (cur + ' ' + w).strip()
        if text_width(t) <= width:
            cur = t
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines


def put(pix, w, x, y, s, ink=0):
    for c in s:
        g = ord(c) - 0x20
        for r in range(16):
            bits = FONT[g * 16 + r]
            for b in range(8):
                if bits & (0x80 >> b) and 0 <= y + r < 240 and 0 <= x + b < w:
                    pix[(y + r) * w + x + b] = ink
        x += WIDTH[g]


def bbox(pix, w, h):
    rows = [y for y in range(h) if 0 in pix[y * w:(y + 1) * w]]
    cols = [x for x in range(w) if any(pix[y * w + x] == 0 for y in rows)]
    return rows, cols


def layout(pix, w, h, spec):
    rows, cols = bbox(pix, w, h)
    top, left, right = rows[0], cols[0], cols[-1]
    out = []                               # (x, y, text)
    if spec[0] == 'c':
        cx = (left + right) // 2
        lines = spec[1]
        for i, s in enumerate(lines):
            out.append((cx - text_width(s) // 2, top + i * 14, s))
        return out
    _, head, body = spec
    gap = next(y for y in rows[1:] if y > rows[0] + 1 and (y - 1) not in rows)   # first empty row after the name
    body_top = next(y for y in rows if y > gap)
    col_w = right - left + 1
    out.append((left, top, head))
    lines = wrap(body, col_w)
    pitch = PITCH if body_top + len(lines) * PITCH <= 236 else 11
    for i, s in enumerate(lines):
        out.append((left, body_top + i * pitch, s))
    return out


def main():
    from PIL import Image
    from build_disc import Disc
    img = os.environ.get('PERSONA_IMAGE') or os.path.join(os.path.dirname(ROOT), 'Megami Ibunroku Persona - Be Your True Mind (Japan).bin')
    disc = Disc(img)
    d = bytearray(b''.join(disc.user(END_LBA + i) for i in range((END_SIZE + 2047) // 2048))[:END_SIZE])
    prev = os.path.join(ROOT, 'translation', 'images')
    os.makedirs(prev, exist_ok=True)
    for off, spec in PAGES.items():
        t = tim.parse(d, off)
        assert t['bpp'] == 4 and t['px_w'] == 320 and t['h'] == 240, hex(off)
        w, h = 320, 240
        raw = d[t['at']:t['at'] + t['w'] * 2 * h]
        pix = bytearray()
        for b in raw:
            pix += bytes((b & 15, b >> 4))
        items = layout(pix, w, h, spec)
        for i in range(len(pix)):
            pix[i] = 1
        for x, y, s in items:
            assert text_width(s) + x <= w and x >= 0, (hex(off), s)
            put(pix, w, x, y, s)
        last = max(y for _, y, _ in items) + 12
        assert last <= 240, (hex(off), last)
        packed = bytes(pix[i] | (pix[i + 1] << 4) for i in range(0, len(pix), 2))
        d[t['at']:t['at'] + len(packed)] = packed
        im = Image.frombytes('P', (w, h), bytes(pix))
        im.putpalette([255, 255, 255, 0, 0, 0] + [0] * 762)
        im.save(os.path.join(prev, f'end_{off:X}.png'))
        print(f'{off:#x}: {len(items)} lines, bottom y {last}')
    os.makedirs(os.path.join(ROOT, 'build', 'EXE'), exist_ok=True)
    open(os.path.join(ROOT, 'build', 'EXE', 'END.BIN'), 'wb').write(bytes(d))


if __name__ == '__main__':
    main()
