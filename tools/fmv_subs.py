"""Burn English subtitles into the spoken movies (Philemon / Kandori speeches) of the disc image.

  python tools/fmv_subs.py [disc.bin] [MV11 MV12 ...]      (default: every movie in translation/src/fmv_subs_en.py)

Same method as fmv_opening.py: the frames that carry a subtitle are decoded (jPSXdec), the text is composited on (white with a
black outline, 2 lines max, short fades) and the frames are re-encoded in place into the (already built) disc image; the audio
and the timing do not change. translation/src/fmv_subs_en.py holds SUBS = {'MV11': [(start_s, end_s, 'line 1\\nline 2'), ...]}
with seconds from the start of the movie (frame = seconds * 15).
"""
import os
import re
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'translation', 'src'))
import fmv_opening as fo   # noqa: E402
from fmv_subs_en import SUBS   # noqa: E402
import psp_terms   # noqa: E402

SUBS = {mv: [(a, b, psp_terms.fix_fmv(t)) for a, b, t in v] for mv, v in SUBS.items()}   # PSP variant: official terms

FPS = 15
FADE = 3                 # frames of fade in / out
LINE_Y = (196, 216)      # baseline-ish centre of line 1 / line 2 (320x240 frame)
MAXW = 304


def line_img(text, px=14):
    f = ImageFont.truetype(fo.font(), px * 3)
    w = int(f.getlength(text)) + 24
    im = Image.new('L', (w, px * 3 + 30), 0)
    ImageDraw.Draw(im).text((12, 8), text, 255, font=f)
    dark = Image.new('L', im.size, 0)
    ImageDraw.Draw(dark).text((12, 8), text, 255, font=f, stroke_width=4, stroke_fill=255)
    sc = lambda i: i.resize((i.width // 3, i.height // 3), Image.LANCZOS)
    return sc(im), sc(dark)


def overlay(frame, lines, alpha):
    """frame: PIL RGB 320x240"""
    n = len(lines)
    for k, text in enumerate(lines):
        fg, bg = line_img(text)
        if fg.width - 8 > MAXW:
            raise SystemExit(f'fmv_subs: {text!r} is {fg.width - 8}px wide (max {MAXW})')
        cy = LINE_Y[0] + (k + (2 - n)) * 20 if n < 2 else LINE_Y[k]
        x, y = 160 - fg.width // 2, cy - fg.height // 2
        frame.paste(Image.new('RGB', bg.size, (0, 0, 0)), (x, y), bg.point(lambda v: int(v * alpha)))
        frame.paste(Image.new('RGB', fg.size, (255, 255, 255)), (x, y), fg.point(lambda v: int(v * alpha)))
    return frame


def item_of(idx_path, mv):
    for ln in open(idx_path, encoding='utf-8', errors='replace'):
        m = re.search(r'\|ID:(STR\d/%s\.STR\[0\])\|' % mv, ln)
        if m:
            return m.group(1)
    raise SystemExit('fmv_subs: ' + mv + ' not in the jPSXdec index')


def do_movie(mv, target, src):
    subs = SUBS[mv]
    item = item_of(fo.index(src), mv)
    f0 = int(subs[0][0] * FPS) - FADE
    f1 = int(subs[-1][1] * FPS) + FADE + 1
    d = os.path.join(fo.WORK, 'orig_' + mv)
    if not os.path.isdir(d) or len(os.listdir(d)) < (f1 - f0):
        os.makedirs(d, exist_ok=True)
        tmp = os.path.join(fo.WORK, 'x_' + mv)
        os.makedirs(tmp, exist_ok=True)
        fo.jpsx('-x', fo.index(src), '-f', src, '-i', item, '-vf', 'png', '-start', str(f0 + 1), '-end', str(f1 + 1),
                '-num', 'Header', '-noaud', cwd=tmp)
        for r, _, fs in os.walk(tmp):
            for f in fs:
                if f.endswith('.png'):
                    os.replace(os.path.join(r, f), os.path.join(d, '#%04d.png' % int(re.search(r'#(\d+)\]', f).group(1))))
    out = os.path.join(fo.WORK, 'new_' + mv)
    os.makedirs(out, exist_ok=True)
    xml = ['<?xml version="1.0"?>', '<str-replace version="0.3">']
    n = 0
    seen = done.setdefault(mv, set())
    for s, e, text in subs:
        a, b = int(round(s * FPS)), int(round(e * FPS))
        for i in range(a - FADE, b + FADE + 1):
            al = min(1.0, (i - (a - FADE) + 1) / (FADE + 1), (b + FADE - i + 1) / (FADE + 1))
            fn = os.path.join(d, '#%04d.png' % (i + 1))
            if not os.path.exists(fn):
                continue
            fr = Image.open(fn).convert('RGB')
            fp = os.path.join(out, 'f%04d.png' % (i + 1))
            prev = Image.open(fp).convert('RGB') if os.path.exists(fp) and i in seen else fr
            overlay(prev, text.split('\n'), max(0.0, al))
            prev.save(fp)
            seen.add(i)
    for i in sorted(done.get(mv, ())):
        xml.append(f'    <replace frame="#{i + 1}">{os.path.join(out, "f%04d.png" % (i + 1))}</replace>')
        n += 1
    xml.append('</str-replace>')
    xp = os.path.join(fo.WORK, 'replace_' + mv + '.xml')
    open(xp, 'w').write('\n'.join(xml))
    fo.jpsx('-x', fo.index(src), '-f', target, '-i', item, '-replaceframes', xp, cwd=fo.WORK)
    print(f'fmv_subs: {mv}: {len(subs)} subtitles, {n} frames replaced')


done = {}


def main():
    args = [a for a in sys.argv[1:]]
    target = os.path.abspath(args.pop(0)) if args and args[0].lower().endswith('.bin') else \
        os.path.join(os.path.dirname(fo.ROOT), 'patched', 'Persona-TL.bin')
    movies = args or sorted(SUBS)
    if not os.path.exists(fo.JAR):
        raise SystemExit('fmv_subs: jPSXdec not found at ' + fo.JAR)
    os.makedirs(fo.WORK, exist_ok=True)
    for mv in movies:
        done.pop(mv, None)
        d = os.path.join(fo.WORK, 'new_' + mv)
        if os.path.isdir(d):
            for f in os.listdir(d):
                os.remove(os.path.join(d, f))
        do_movie(mv, target, fo.ORIG)


if __name__ == '__main__':
    main()
