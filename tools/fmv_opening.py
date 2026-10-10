"""English subtitles for the opening movie (STR1/MV1C.STR): the Zhuangzi butterfly quote is burned into the video.

  python tools/fmv_opening.py [disc.bin]      re-encode the text frames and write them into the (already built) disc image

Needs Java and jPSXdec (https://github.com/m35/jpsxdec, release v2.1): unpack it to tools/ext/jpsxdec/ (jpsxdec.jar), and
`pip install opencv-python-headless numpy pillow`. The frames are replaced IN PLACE (jPSXdec re-encodes them to MDEC and
rewrites the sector EDC/ECC), so the movie and its audio keep their timing. Frame numbers below are 0-based decoder indexes;
jPSXdec's "header frame" number is index + 1.

The Japanese text fades in/out line by line (and, in the last card, over the fading-in moon). For every frame the strokes of each
Japanese line are located, the brightness of that line is measured, the strokes are inpainted away and the English line is drawn
with the same brightness - so every fade is kept.
"""
import os
import subprocess
import sys

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JAR = os.path.join(ROOT, 'tools', 'ext', 'jpsxdec', 'jpsxdec.jar')
WORK = os.path.join(ROOT, 'build', 'fmv')
ORIG = os.environ.get('PERSONA_IMAGE') or os.path.join(os.path.dirname(ROOT), 'Megami Ibunroku Persona - Be Your True Mind (Japan).bin')
ITEM = 'STR1/MV1C.STR[0]'
FONTS = ['C:/Windows/Fonts/segoeui.ttf', 'C:/Windows/Fonts/arial.ttf', 'C:/Windows/Fonts/verdana.ttf']
FONT_PX = 14
MAXW = 292
# (first index, last index, [(band y0, y1) of each Japanese line], [English line each], attribution (band, text) or None)
CARDS = [
    (20, 98, [(107, 120)], ['Once, I dreamed I became a butterfly.']),
    (99, 230, [(79, 92), (99, 112), (119, 132), (139, 152)],
     ['I seemed to have become a butterfly entirely,', 'and could not tell it was my own dream,',
      'but when I suddenly woke up,', 'I was unmistakably myself, not a butterfly.']),
    (231, 338, [(85, 98), (125, 138)],
     ['Was it I who dreamed of being a butterfly,', 'or a butterfly who dreams of being me?']),
    (339, 492, [(83, 95), (102, 115), (122, 135), (165, 178)],
     ['Surely, between me and the butterfly,', 'there may be a distinction, but not an',
      'absolute difference; no causal link holds.', '~ Zhuangzi ~']),
]
ATTR_RIGHT = 286


def font():
    for f in FONTS:
        if os.path.exists(f):
            return f
    raise SystemExit('fmv_opening: no usable TrueType font')


def jpsx(*args, cwd):
    subprocess.run(['java', '-jar', JAR, *args], cwd=cwd, check=True, stdout=subprocess.DEVNULL)


def index(src):
    idx = os.path.join(WORK, 'idx.txt')
    if not os.path.exists(idx):
        jpsx('-f', src, '-x', idx, cwd=WORK)
    return idx


def extract(src):
    d = os.path.join(WORK, 'orig')
    if not os.path.isdir(d) or len(os.listdir(d)) < 480:
        os.makedirs(d, exist_ok=True)
        tmp = os.path.join(WORK, 'x')
        os.makedirs(tmp, exist_ok=True)
        jpsx('-x', index(src), '-f', src, '-i', ITEM, '-vf', 'png', '-start', '20', '-end', '495', '-num', 'Header', '-noaud', cwd=tmp)
        for r, _, fs in os.walk(tmp):
            for f in fs:
                if f.endswith('.png'):
                    os.replace(os.path.join(r, f), os.path.join(d, f[f.rindex('#'):f.rindex('#') + 5] + '.png'))
    return d


def render(text, size_px, alpha, right=None):
    """grey mask (H=240 x W=320 canvas drawn by caller) of one line"""
    f = ImageFont.truetype(font(), size_px * 3)
    w = int(f.getlength(text))
    im = Image.new('L', (w + 12, size_px * 3 + 24), 0)
    ImageDraw.Draw(im).text((6, 6), text, 255, font=f)
    im = im.resize((im.width // 3, im.height // 3), Image.LANCZOS)
    return im


def main():
    src = ORIG
    target = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(os.path.dirname(ROOT), 'patched', 'Persona-TL.bin')
    if not os.path.exists(JAR):
        raise SystemExit('fmv_opening: jPSXdec not found at ' + JAR)
    os.makedirs(WORK, exist_ok=True)
    d = extract(src)
    out = os.path.join(WORK, 'new')
    os.makedirs(out, exist_ok=True)
    xml = ['<?xml version="1.0"?>', '<str-replace version="0.3">']
    nrep = 0
    for first, last, bands, lines in CARDS:
        # reference brightness per band (full brightness of the Japanese line in this card)
        stats = {}
        for i in range(first, last + 1):
            g = cv2.cvtColor(cv2.imread(os.path.join(d, '#%04d.png' % (i + 1))), cv2.COLOR_BGR2GRAY).astype(np.int16)
            stats[i] = [strokes(g, b) for b in bands]
        ref = [max([s[k][1] for s in stats.values() if s[k][0]] or [255]) for k in range(len(bands))]
        for i in range(first, last + 1):
            img = cv2.imread(os.path.join(d, '#%04d.png' % (i + 1)))
            g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.int16)
            black = (np.delete(g, np.r_[80:180], axis=0).max() < 6)
            present = [k for k in range(len(bands)) if stats[i][k][0]]
            if not present:
                continue
            if black:
                new = np.zeros_like(img)
            else:
                mask = np.zeros(g.shape, np.uint8)
                for k in present:
                    m = stroke_mask(g, bands[k])
                    mask |= cv2.dilate(m, np.ones((5, 5), np.uint8))
                new = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
            pil = Image.fromarray(cv2.cvtColor(new, cv2.COLOR_BGR2RGB))
            for k in present:
                alpha = min(1.0, stats[i][k][1] / ref[k])
                tl = render(lines[k], FONT_PX, alpha)
                if tl.width > MAXW + 12:
                    raise SystemExit(f'fmv_opening: {lines[k]!r} is {tl.width - 12}px wide (max {MAXW})')
                y0, y1 = bands[k]
                x = (ATTR_RIGHT - (tl.width - 12) - 6) if lines[k].startswith('~') else (160 - tl.width // 2)
                y = (y0 + y1) // 2 - tl.height // 2 - 1
                col = Image.new('RGB', tl.size, (int(255 * alpha),) * 3)
                pil.paste(col, (x, y), tl)
            fp = os.path.join(out, 'f%04d.png' % (i + 1))
            pil.save(fp)
            xml.append(f'    <replace frame="#{i + 1}">{fp}</replace>')
            nrep += 1
    xml.append('</str-replace>')
    xp = os.path.join(WORK, 'replace.xml')
    open(xp, 'w').write('\n'.join(xml))
    jpsx('-x', index(src), '-f', target, '-i', ITEM, '-replaceframes', xp, cwd=WORK)
    print(f'fmv_opening: {nrep} frames of MV1C replaced in {os.path.basename(target)}')


def stroke_mask(g, band, pad=3):
    y0, y1 = band
    ys = slice(max(0, y0 - pad), y1 + pad + 1)
    gu = np.clip(g, 0, 255).astype(np.uint8)
    med = cv2.medianBlur(gu, 9).astype(np.int16)
    th = max(6, int(0.15 * (g[ys].max() - med[ys].min() + 1)))
    m = np.zeros(g.shape, np.uint8)
    m[ys] = ((g[ys] - med[ys]) > th)
    return m


def strokes(g, band):
    """(present, brightness) of the Japanese line in this band"""
    m = stroke_mask(g, band)
    if m.sum() < 25:
        return (False, 0)
    return (True, float(np.percentile(g[m > 0], 95)))


if __name__ == '__main__':
    main()
