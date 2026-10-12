"""English text for the two ending-epilogue movies whose Japanese poem is drawn over the 3D picture:

  MV1E (STR1)  hospital epilogue: "時は流れ、人々は意識して…"   (9 lines)
  MV25 (STR2)  graduation epilogue: "時は流れ、事件が人々の記憶の底に…" (7 lines)

  python tools/fmv_poems.py [disc.bin]

The poem is static (same pixels in every frame) and only fades in/out, so: the glyph mask is taken once from a fully visible
frame; for every frame the strength of the Japanese text (contrast of the masked pixels against their surroundings) gives the
fade alpha; the glyph pixels are inpainted away and the English lines are drawn with that alpha (white + dark outline).
Frames are re-encoded in place by jPSXdec (see fmv_opening.py). Frame numbers are jPSXdec "header frame" numbers.
"""
import os
import re
import sys

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fmv_opening as fo   # noqa: E402

PITCH = 14
FONT_PX = 12
MAXW = 304
POEMS = {
    # movie: (item, first, last, reference frame, rect x0,y0,x1,y1, first line top y, English lines)
    'MV1E': ('STR1/MV1E.STR[0]', 36, 240, 120, (20, 50, 300, 188), 57, [
        'Time flows on,',
        'and people seem to consciously try to bury',
        'everything at the bottom of memory.',
        'In a world where nothing stands still,',
        'as if driven by something,',
        'as if trying to escape',
        'the contradictions within themselves,',
        'the waves of people flow somewhere...',
        'Again, today as well.']),
    'MV25': ('STR2/MV25.STR[0]', 20, 200, 100, (40, 30, 290, 175), 57, [
        'Time flows on,',
        'and as the incident began to sink',
        "into the depths of people's memories...",
        'having found their true selves,',
        'boys and girls with their bare faces',
        'begin to walk toward',
        'a future not yet seen...']),
}


def gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.int16)


def mask_of(g, rect, top):
    med = cv2.medianBlur(g.astype(np.uint8), 9).astype(np.int16)
    m = ((g - med) > 40) & (g >= 200)
    r = np.zeros(m.shape, bool)
    x0, y0, x1, y1 = rect
    r[y0:y1, x0:x1] = True
    return clean(m & r, rect, top)


def clean(m, rect, top):
    """keep only the glyph rows (text bands) and, per band, the biggest horizontal cluster (drops specular dots)"""
    out = np.zeros_like(m)
    k = 0
    while top + k * PITCH < rect[3]:
        y0, y1 = top + k * PITCH - 2, top + k * PITCH + 12
        band = m[y0:y1]
        ys, xs = np.nonzero(band)
        if len(xs):
            order = np.sort(np.unique(xs))
            groups, cur = [], [order[0]]
            for x in order[1:]:
                if x - cur[-1] > 45:
                    groups.append(cur)
                    cur = []
                cur.append(x)
            groups.append(cur)
            best = max(groups, key=lambda g: int(band[:, g[0]:g[-1] + 1].sum()))
            out[y0:y1, best[0]:best[-1] + 1] = band[:, best[0]:best[-1] + 1]
        k += 1
    return out


def line_mask(text):
    f = ImageFont.truetype(fo.font(), FONT_PX * 3)
    w = int(f.getlength(text)) + 24
    fg = Image.new('L', (w, FONT_PX * 3 + 30), 0)
    ImageDraw.Draw(fg).text((12, 8), text, 255, font=f)
    bg = Image.new('L', fg.size, 0)
    ImageDraw.Draw(bg).text((12, 8), text, 255, font=f, stroke_width=4, stroke_fill=255)
    sc = lambda i: i.resize((i.width // 3, i.height // 3), Image.LANCZOS)
    return sc(fg), sc(bg)


def extract(mv, item, a, b, src):
    d = os.path.join(fo.WORK, 'orig_' + mv)
    if not os.path.isdir(d) or len(os.listdir(d)) < (b - a):
        os.makedirs(d, exist_ok=True)
        tmp = os.path.join(fo.WORK, 'x_' + mv)
        os.makedirs(tmp, exist_ok=True)
        fo.jpsx('-x', fo.index(src), '-f', src, '-i', item, '-vf', 'png', '-start', str(a - 1), '-end', str(b - 1), '-num', 'Header',
                '-noaud', cwd=tmp)
        for r, _, fs in os.walk(tmp):
            for f in fs:
                if f.endswith('.png'):
                    os.replace(os.path.join(r, f), os.path.join(d, '#%04d.png' % int(re.search(r'#(\d+)\]', f).group(1))))
    return d


def do_movie(mv, target, src):
    item, a, b, ref, rect, top, lines = POEMS[mv]
    d = extract(mv, item, a, b, src)
    load = lambda h: cv2.imread(os.path.join(d, '#%04d.png' % h))
    m0 = mask_of(gray(load(ref)), rect, top)
    dil = cv2.dilate(m0.astype(np.uint8), np.ones((5, 5), np.uint8)) > 0
    holes = ~dil                                           # fill the small islands enclosed by the mask (glyph centres)
    nc, lab, st, _ = cv2.connectedComponentsWithStats(holes.astype(np.uint8), connectivity=4)
    for i in range(1, nc):
        if st[i, cv2.CC_STAT_AREA] < 80:
            dil |= lab == i
    core = cv2.dilate(m0.astype(np.uint8), np.ones((3, 3), np.uint8)) > 0
    ring = (cv2.dilate(core.astype(np.uint8), np.ones((9, 9), np.uint8)) > 0) & ~core

    def contrast(g):
        return float(g[m0].mean() - g[ring].mean())
    ref_c = contrast(gray(load(ref)))
    out = os.path.join(fo.WORK, 'new_' + mv)
    os.makedirs(out, exist_ok=True)
    xml = ['<?xml version="1.0"?>', '<str-replace version="0.3">']
    n = 0
    for h in range(a, b + 1):
        img = load(h)
        if img is None:
            continue
        alpha = max(0.0, min(1.0, contrast(gray(img)) / ref_c))
        if alpha < 0.012:                          # below ~1 % of the full contrast the Japanese strokes are invisible
            continue
        new = cv2.inpaint(img, dil.astype(np.uint8) * 255, 3, cv2.INPAINT_TELEA)
        # in the fades keep part of the original (less inpainting smear), but never more than ~1 % contrast of the
        # Japanese strokes (a faint trace of the poem was visible in the first fade-in frames)
        w = max(min(1.0, 2.0 * alpha), 1.0 - 0.01 / alpha)
        new = cv2.addWeighted(new, w, img, 1.0 - w, 0)
        pil = Image.fromarray(cv2.cvtColor(new, cv2.COLOR_BGR2RGB))
        for k, text in enumerate(lines):
            fg, bg = line_mask(text)
            if fg.width - 8 > MAXW:
                raise SystemExit(f'fmv_poems: {text!r} is {fg.width - 8}px wide (max {MAXW})')
            x = 160 - fg.width // 2
            y = top + k * PITCH + 6 - fg.height // 2
            pil.paste(Image.new('RGB', bg.size, (0, 0, 0)), (x, y), bg.point(lambda v: int(v * alpha * 0.75)))
            pil.paste(Image.new('RGB', fg.size, (255, 255, 255)), (x, y), fg.point(lambda v: int(v * alpha)))
        fp = os.path.join(out, 'f%04d.png' % h)
        pil.save(fp)
        xml.append(f'    <replace frame="#{h}">{fp}</replace>')
        n += 1
    xml.append('</str-replace>')
    xp = os.path.join(fo.WORK, 'replace_' + mv + '.xml')
    open(xp, 'w').write('\n'.join(xml))
    fo.jpsx('-x', fo.index(src), '-f', target, '-i', item, '-replaceframes', xp, cwd=fo.WORK)
    print(f'fmv_poems: {mv}: {n} frames replaced')


def main():
    args = sys.argv[1:]
    target = os.path.abspath(args.pop(0)) if args and args[0].lower().endswith('.bin') else \
        os.path.join(os.path.dirname(fo.ROOT), 'patched', 'Persona-TL.bin')
    if not os.path.exists(fo.JAR):
        raise SystemExit('fmv_poems: jPSXdec not found at ' + fo.JAR)
    os.makedirs(fo.WORK, exist_ok=True)
    for mv in args or sorted(POEMS):
        do_movie(mv, target, fo.ORIG)


if __name__ == '__main__':
    main()
