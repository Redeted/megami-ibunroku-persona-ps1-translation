"""Find and dump FF01-terminated game strings in program/overlay files (menus, items, skills,
battle messages, system text ...).

  python tools/strscan.py                      scan all binaries, write translation/strings/<FILE>.tsv
  python tools/strscan.py SLPS_005.00 [min]    scan one file, print candidates

A candidate is a run of >= `min` (default 2) text tokens (one-byte glyph < 0x80 or lead 0x80-0x87
+ byte) ending in FF 01, at a 1- or 4-byte aligned address, where every glyph has a known
character in tools/font_map.tsv, preceded by a non-text byte (so we start at the real beginning).
Output rows: offset(hex) | file address | byte length | text. `en` is the translation column.
Strings are replaced in place (must fit; `strpad`) or relocated by hand; see TRANSLATION_GUIDE.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import etext  # noqa: E402

ROOT = etext.ROOT
FILES = {                       # name -> RAM base of file offset 0
    'SLPS_005.00': 0x8000F800, 'BTLP.BIN': 0x800643C4, 'ADV.BIN': 0x800643C4, 'DNG.BIN': 0x800643C4,
    'S2D.BIN': 0x800643C4, 'CASINO.BIN': 0x800643C4, 'NAME.BIN': 0x800643C4,
    'EXE/ATLUS.EXE': None, 'EXE/OPEN.EXE': None, 'EXE/MOVIE.EXE': None, 'EXE/END.EXE': None,
}
KNOWN = set(etext.glyph)


def candidates(d, minlen=2):
    out = []
    n = len(d)
    i = 0
    while i < n - 1:
        # find the next FF 01
        j = d.find(b'\xff\x01', i)
        if j < 0:
            break
        # walk backwards over text tokens
        k = j
        toks = 0
        while k >= 2:
            if 0x80 <= d[k - 2] <= 0x87 and (((d[k - 2] & 7) << 8) | d[k - 1]) in KNOWN:
                k -= 2
            elif d[k - 1] < 0x80 and d[k - 1] in KNOWN:
                k -= 1
            else:
                break
            toks += 1
        if toks >= minlen:
            out.append((k, j + 2))
        i = j + 2
    return out


def scan(name, minlen=2):
    p = os.path.join(ROOT, 'original', *name.split('/'))
    d = open(p, 'rb').read()
    return d, candidates(d, minlen)


def main():
    a = sys.argv[1:]
    sys.stdout.reconfigure(encoding='utf-8')
    if a:
        d, c = scan(a[0], int(a[1]) if len(a) > 1 else 2)
        base = FILES.get(a[0]) or 0
        for s, e in c[:400]:
            print(f'{s:06X} {e - s:4d}  {etext.decode(d[s:e])}')
        print(len(c), 'strings')
        return
    outdir = os.path.join(ROOT, 'translation', 'strings')
    os.makedirs(outdir, exist_ok=True)
    tab, nl = chr(9), chr(10)
    for name, base in FILES.items():
        try:
            d, c = scan(name, 2)
        except FileNotFoundError:
            continue
        fn = name.replace('/', '_') + '.tsv'
        with open(os.path.join(outdir, fn), 'w', encoding='utf-8', newline=nl) as o:
            o.write('offset\tlength\tja\ten' + nl)
            for s, e in c:
                o.write(f'{s:06X}{tab}{e - s}{tab}{etext.decode(d[s:e])}{tab}{nl}')
        print(f'{name:16s} {len(c):5d} strings, {sum(e - s for s, e in c):7d} bytes')


if __name__ == '__main__':
    main()
