"""Demon negotiation scripts: TALK/*.BIN (parse, dump, rebuild).

File layout (verified against BTLP.BIN 0x80074BAC, which returns base + table[i] + 0x14):
  0x00  u32[5]   header: [0]=0x14 (text offsets are relative to this), [1..4] = absolute file
                 offsets of four data sections that follow the text pool ([1] = pool end)
  0x14  u32[n]   text table, ascending; unit i starts at  table[i] + 0x14
  ...   FF       padding up to 0x2014, where the text pool starts
  0x2014         text pool: unit i = bytes [start_i, start_{i+1}); the last one runs to header[1].
                 Displayed text ends at the first FF F5 (page) / FF EF; a few units carry stray
                 bytes after it, which are kept as part of the span (lossless).
  [1]..          sections 1-4: u16 index/script tables (no file pointers seen)
Control codes: FFF5 end of page, FFEF end, FFF6 newline, FFFC/FFFD(+1 byte) pause/branch,
FFFB/FFF7, FFF1, FFEC ... Parameter bytes are kept as is. The renderer is BTLP's own
(16 px glyphs, 15 per line): English needs a VWF hook there before it can be shown.

CLI (run from persona-tl/):
  python tools/talk.py check            parse every file, rebuild unchanged, compare bytes
  python tools/talk.py dump             write translation/talk/<NAME>.tsv  (unit ja en)
  python tools/talk.py build [outdir]   apply `en` -> build/TALK/<NAME>.BIN (only edited files)
"""
import glob
import os
import struct
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import etext  # noqa: E402

ROOT = etext.ROOT
SRC = os.path.join(etext.ORIGINAL, 'TALK')
TSV = os.path.join(etext.TEXT, 'talk')
POOL = 0x2014
ENDS = {0xF5, 0xEF}


def end_codes(b):
    """positions just past every FF F5 / FF EF in an encoded unit (aligned parse)."""
    out, i = [], 0
    while i + 1 < len(b):
        c = b[i]
        if c == 0xFF:
            if b[i + 1] in ENDS:
                out.append(i + 2)
            i += 2
        elif 0x80 <= c <= 0x87:
            i += 2
        else:
            i += 1
    return out


class Talk:
    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.hdr = list(struct.unpack_from('<5I', data, 0))
        base = self.base = self.hdr[0]
        offs, i = [], base
        while i + 4 <= len(data):
            v = struct.unpack_from('<I', data, i)[0]
            if v == 0xFFFFFFFF:
                break
            offs.append(v)
            i += 4
        self.starts = [o + base for o in offs]
        self.ok = (bool(self.starts) and self.starts == sorted(self.starts)
                   and self.starts[0] == POOL and self.starts[-1] < self.hdr[1] <= len(data))
        self.units = []
        if self.ok:
            ends = self.starts[1:] + [self.hdr[1]]
            self.units = [bytes(data[s:e]) for s, e in zip(self.starts, ends)]
        # section 1 = the player's answer lines: u32[512] table (offset from the section start, 0xFFFFFFFF = none), then the
        # strings packed in table order (each ends with FF F5 / FF EF, a few carry stray bytes before the next one)
        self.s1_tab, self.s1 = [], []
        if self.ok and self.hdr[2] - self.hdr[1] >= 2048:
            a, b = self.hdr[1], self.hdr[2]
            self.s1_tab = list(struct.unpack_from('<512I', data, a))
            offs = sorted({v for v in self.s1_tab if v != 0xFFFFFFFF})
            if offs and offs[0] == 2048:
                ends = offs[1:] + [b - a]
                self.s1 = [(v, bytes(data[a + v:a + e])) for v, e in zip(offs, ends)]

    def s1_text_len(self, span):
        e = [x for x in (span.find(bytes((0xFF, 0xF5))), span.find(bytes((0xFF, 0xEF)))) if x >= 0]
        return min(e) + 2 if e else len(span)

    def rebuild(self, edits=None, s1_edits=None):
        """file bytes with units replaced ({index: bytes}) and answer strings replaced ({position in self.s1: text bytes},
        the stray bytes behind the original end code are kept)."""
        edits = edits or {}
        s1_edits = s1_edits or {}
        units = [edits.get(i, u) for i, u in enumerate(self.units)]
        starts, pos = [], POOL
        for u in units:
            starts.append(pos)
            pos += len(u)
        head = bytearray(self.data[:POOL])
        for k, s in enumerate(starts):
            struct.pack_into('<I', head, self.base + 4 * k, s - self.base)
        # section 1
        old1 = self.hdr[2] - self.hdr[1]
        if self.s1:
            spans, offs, p = [], {}, 2048
            for k, (v, sp) in enumerate(self.s1):
                if k in s1_edits:
                    sp = s1_edits[k] + sp[self.s1_text_len(sp):]
                offs[v] = p
                spans.append(sp)
                p += len(sp)
            tab = [offs.get(v, v) if v != 0xFFFFFFFF else v for v in self.s1_tab]
            sec1 = struct.pack('<512I', *tab) + b''.join(spans)
        else:
            sec1 = self.data[self.hdr[1]:self.hdr[2]]
        # sections keep their alignment modulo 4 (pad with FF)
        fill = (self.hdr[1] - pos) % 4
        delta = pos + fill - self.hdr[1]
        pad = (old1 - len(sec1)) % 4
        sec1 += bytes((0xFF,)) * pad
        delta1 = len(sec1) - old1
        for k in range(1, 5):
            v = self.hdr[k] + delta + (delta1 if k >= 2 else 0)
            struct.pack_into('<I', head, 4 * k, v)
        return bytes(head) + b''.join(units) + bytes((0xFF,)) * fill + sec1 + self.data[self.hdr[2]:]


def files():
    return sorted(glob.glob(os.path.join(SRC, '*.BIN')))


def load(name):
    return Talk(name, open(os.path.join(SRC, name + '.BIN'), 'rb').read())


def cmd_check():
    tot = good = nunits = 0
    for f in files():
        name = os.path.basename(f)[:-4]
        t = load(name)
        tot += 1
        if not t.ok:
            print(f'{name}: layout not recognised (header {[hex(x) for x in t.hdr]}) - needs its own handling')
            continue
        same = t.rebuild() == t.data
        good += same
        nunits += len(t.units)
        # text codec must be lossless on every unit
        bad = sum(1 for u in t.units if etext.encode(etext.decode(u), end=None) != u)
        multi = sum(1 for u in t.units if len(end_codes(u)) != 1)
        print(f'{name:10s} {len(t.units):4d} units  rebuild identical: {same}  codec mismatches: {bad}  units without exactly one end code: {multi}')
    print(f'{good}/{tot} files round-trip, {nunits} units')


def cmd_dump():
    os.makedirs(TSV, exist_ok=True)
    tab, nl = chr(9), chr(10)
    for f in files():
        name = os.path.basename(f)[:-4]
        t = load(name)
        if not t.ok:
            continue
        p = os.path.join(TSV, name + '.tsv')
        old = {}
        if os.path.exists(p):
            for line in open(p, encoding='utf-8').read().split(nl)[1:]:
                x = line.split(tab)
                if len(x) >= 3 and x[0].isdigit():
                    old[int(x[0])] = (x[1], x[2])
        with open(p, 'w', encoding='utf-8', newline=nl) as o:
            o.write('unit\tja\ten' + nl)
            for i, u in enumerate(t.units):
                ja = etext.decode(u)
                en = old[i][1] if i in old and old[i][0] == ja else ''
                o.write(f'{i}{tab}{ja}{tab}{en}{nl}')
    print('wrote', TSV)


def cmd_build(outdir):
    os.makedirs(outdir, exist_ok=True)
    tab, nl = chr(9), chr(10)
    ans = {}
    ap = os.path.join(TSV, 'ANSWERS.tsv')
    if os.path.exists(ap):
        for line in open(ap, encoding='utf-8').read().split(nl)[1:]:
            x = line.split(tab)
            if len(x) >= 3 and x[0].isdigit() and x[2].strip():
                ans[x[1]] = x[2]
    for f in files():
        name = os.path.basename(f)[:-4]
        t = load(name)
        out = os.path.join(outdir, name + '.BIN')
        p = os.path.join(TSV, name + '.tsv')
        edits = {}
        if t.ok and os.path.exists(p):
            for ln, line in enumerate(open(p, encoding='utf-8').read().split(nl)[1:], 2):
                x = line.split(tab)
                if len(x) >= 3 and x[0].isdigit() and x[2].strip():
                    try:
                        u = etext.encode(x[2], end=None)
                    except ValueError as ex:
                        raise SystemExit(f'{p}:{ln}: {ex}')
                    if len(end_codes(u)) != 1 or end_codes(u)[0] != len(u):
                        raise SystemExit(f'{p}:{ln}: a unit must end with exactly one <FFF5> (or <FFEF>)')
                    edits[int(x[0])] = u
        s1e = {}
        for k, (v, sp) in enumerate(t.s1 if t.ok else []):
            ja = etext.decode(sp[:t.s1_text_len(sp)])
            if ja in ans:
                u = etext.encode(ans[ja], end=None)
                if len(end_codes(u)) != 1 or end_codes(u)[0] != len(u):
                    raise SystemExit(f'{name} answer {ja!r}: must end with exactly one end code')
                s1e[k] = u
        if not edits and not s1e:
            if os.path.exists(out):
                os.remove(out)
            continue
        data = t.rebuild(edits, s1e)
        open(out, 'wb').write(data)
        print(f'{name}: {len(edits)} units + {len(s1e)} answers edited, {len(t.data)} -> {len(data)} bytes')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    a = sys.argv[1:] or ['check']
    if a[0] == 'check':
        cmd_check()
    elif a[0] == 'dump':
        cmd_dump()
    elif a[0] == 'build':
        cmd_build(a[1] if len(a) > 1 else os.path.join(ROOT, 'build', 'TALK'))
    else:
        raise SystemExit(__doc__)
