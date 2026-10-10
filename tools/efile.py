"""Parser / rebuilder for ADV/E0..E3.BIN (event scripts).

Container: sector 0 = u16 cumulative sector offsets (entry i = sectors t[i]..t[i+1]).
Entry:     u32 0x80100008, u32 end address, then the image. The image is loaded at
           BASE=0x80100000 (body index = pointer - BASE) and is `end - BASE` bytes.
Image:     map header + command stream (`FF op a b`, ops 55/22/26/54/... carry a
           following u32 absolute pointer) + text pool + small tail.
Boxes:     a box is text tokens (glyph byte < 0x80, 80-87 + 1 byte = kanji,
           FF xx with xx < 0x20 = control code, no parameters) ending in FF 01, then
           zero padding to a 4-byte boundary. `FF 55 00 00 <ptr>` says the box at ptr;
           boxes right after it that parse as text are reached sequentially. Command
           blocks (FF op >= 0x20) and other data between boxes are "gaps".

Relocation: rebuild() re-lays the image out (boxes any length, re-padded to 4, gaps
moved as blocks) and remaps every u32 pointer whose target is a box start or lies in
a gap. A pointer into the middle of a box raises (entry is then not translatable).

CLI:
  python tools/efile.py <E?.BIN>                 summary + round-trip check
  python tools/efile.py <E?.BIN> <entry>         dump the boxes of an entry
"""
import struct
import sys

BASE = 0x80100000
SECTOR = 2048


def scan_box(b, i, limit=20000):
    """Index just past the FF 01 that ends the text box starting at i, else None."""
    n = len(b)
    s = i
    while i < n and i - s < limit:
        c = b[i]
        if c == 0xFF:
            if i + 1 >= n:
                return None
            op = b[i + 1]
            if op >= 0x20:
                return None          # command, not text
            i += 2
            if op == 1:
                return i
        elif 0x80 <= c <= 0x87:
            i += 2
        else:
            i += 1
    return None


class Entry:
    def __init__(self, index, raw):
        self.index = index
        self.load, self.end = struct.unpack_from('<II', raw, 0)
        self.size = self.end - BASE
        self.body = bytes(raw[8:8 + self.size])
        self.short = self.size - len(self.body)       # end field may overshoot the sectors
        self.trailer = bytes(raw[8 + self.size:])     # sector padding (normally zeros)
        self._parse()

    # --- structure -------------------------------------------------------
    def pointers(self):
        """(offset, target_offset) for every even-aligned u32 pointing into the image."""
        b = self.body
        out = []
        for off in range(0, len(b) - 3, 2):
            v = struct.unpack_from('<I', b, off)[0]
            if (v >> 16) == 0x8010 and BASE <= v < self.end:
                out.append((off, v - BASE))
        return out

    def _parse(self):
        b = self.body
        ptrs = self.pointers()
        say = sorted({tg for off, tg in ptrs
                      if off >= 4 and b[off - 4] == 0xFF and b[off - 3] == 0x55})
        pointed = set(say)
        # targets of pointers that are not "say" pointers (variable tables, jumps):
        # an unpointed sequential box that one of them lands in is data, not text
        other = sorted({tg for off, tg in ptrs
                        if not (off >= 4 and b[off - 4] == 0xFF and b[off - 3] == 0x55)})
        boxes = []               # (start, end_of_text), end excludes zero padding
        covered = 0              # end of the last accepted box (boxes never overlap)
        for s0 in say:
            if s0 < covered:
                continue         # pointer into the middle of a box
            i = s0
            first = True
            while i < len(b):
                if not first and (i in pointed or i < covered):
                    break
                e = scan_box(b, i)
                if e is None or (e - i) < 2:
                    break
                if not first:
                    pad = (-i) % 4
                    if not any(b[i:e - 2]):
                        break
                    if any(i <= t < e for t in other):
                        break
                boxes.append((i, e))
                covered = e
                pad = (-e) % 4
                if b[e:e + pad] != bytes(pad):
                    break        # something other than padding follows: chain ends
                i = e + pad
                first = False
        self.boxes = sorted(boxes)
        self.pool_start = self.boxes[0][0] if self.boxes else None
        self.pool_end = self.boxes[-1][1] if self.boxes else None

    def box_bytes(self, k):
        s, e = self.boxes[k]
        return self.body[s:e]

    def segments(self):
        """Ordered ('gap'|'box', start, end, box_index) covering the image except for
        zero padding (< 4 bytes) that sits between a box and the next box."""
        segs, pos = [], 0
        b = self.body
        for k, (s, e) in enumerate(self.boxes):
            if s > pos:
                if not (s - pos < 4 and not any(b[pos:s]) and segs and segs[-1][0] == 'box'):
                    segs.append(('gap', pos, s, None))
            segs.append(('box', s, e, k))
            pos = e
        if pos < len(b):
            segs.append(('gap', pos, len(b), None))
        return segs

    # --- rebuilding ------------------------------------------------------
    def rebuild(self, new_boxes=None):
        """New raw entry bytes (no sector padding) with boxes replaced.

        new_boxes: {box_index: bytes ending in FF 01}. Every segment keeps its start
        offset modulo 4 (the interpreter reads u32 operands with lw), padded with zeros.
        Returns raw."""
        new_boxes = new_boxes or {}
        b = self.body
        out = bytearray()
        gaps = []        # (old_start, old_end, new_start)
        starts = {}      # old box start -> new offset
        boxspan = []     # (old_start, old_end, new_start, new_end)
        for kind, s, e, k in self.segments():
            while len(out) % 4 != s % 4:
                out.append(0)
            if kind == 'gap':
                gaps.append((s, e, len(out)))
                out += b[s:e]
            else:
                t = new_boxes.get(k, b[s:e])
                if scan_box(t, 0, limit=1 << 16) != len(t):
                    raise ValueError(f'box {k}: text must have exactly one FF 01, at the end, '
                                     'and only text control codes (FF 00-1F)')
                starts[s] = len(out)
                ns = len(out)
                out += t
                boxspan.append((s, e, ns, len(out)))
        while len(out) % 4 != len(b) % 4:
            out.append(0)

        def newpos(o):
            for gs, ge, ns in gaps:
                if gs <= o < ge:
                    return ns + o - gs
            if o in starts:
                return starts[o]
            if o == len(b):
                return len(out)
            # pointer into the middle of a box (or into dropped padding): only valid
            # if that box did not move or change size
            for s, e, ns, ne in boxspan:
                if s <= o < e + (-e) % 4 and ne == e and ns == s:
                    return o
            raise ValueError(f'offset {o:#x} is inside a resized or moved box')

        for off, tg in self.pointers():
            if any(s <= off < e for s, e, _, _ in boxspan):
                continue          # u32-looking bytes inside a box: text, leave alone
            try:
                noff = newpos(off)
            except ValueError:
                continue          # inside dropped zero padding: not a real pointer
            try:
                new = BASE + newpos(tg)
            except ValueError:
                # Target inside a resized/moved box. Seen only in a handful of entries, always
                # at an offset that is not a text boundary (often mid-glyph), so these are
                # almost certainly data words that merely look like pointers: keep the value.
                print(f'E?/{self.index}: word at {off:#x} -> mid-box {tg:#x} kept unchanged')
                continue
            struct.pack_into('<I', out, noff, new)
        return self._raw(bytes(out), BASE + len(out) + self.short)

    def _raw(self, body, end=None):
        return struct.pack('<II', self.load, end if end is not None else self.end) + body


class Container:
    def __init__(self, data):
        self.t = struct.unpack_from('<1024H', data, 0)
        self.entries = []
        for i in range(1023):
            if self.t[i] == 0 or self.t[i + 1] <= self.t[i]:
                break
            self.entries.append(Entry(i, data[self.t[i] * SECTOR:self.t[i + 1] * SECTOR]))
        self.total_sectors = self.t[len(self.entries)]
        self.data = data

    def build(self, raws, min_sectors=None):
        """raws: list of per-entry raw bytes (header+body). Returns (file, table).

        table = cumulative sector offsets, len(entries)+1 u16 values. The game does not
        read the file's own sector 0: it uses a copy embedded in SLPS_005.00
        (etext.SLPS_TABLES), which must be patched with this table.
        min_sectors: reserved slot size per entry (sectors). With a fixed layout the
        table and the file size never change when text grows, so save states made on an
        earlier build keep reading the right sectors."""
        sectors = [1]
        blobs = []
        for i, r in enumerate(raws):
            n = -(-len(r) // SECTOR)
            if min_sectors:
                n = max(n, min_sectors[i])
            blobs.append(r + bytes(n * SECTOR - len(r)))
            sectors.append(sectors[-1] + n)
        if sectors[-1] > 0xFFFF:
            raise ValueError('sector table overflow')
        head = struct.pack('<1024H', *(sectors + [0] * (1024 - len(sectors))))
        return head + b''.join(blobs), sectors


def load(path):
    return Container(open(path, 'rb').read())


def main():
    sys.path.insert(0, __file__.rsplit('tools', 1)[0] + 'tools')
    import decode as D
    sys.stdout.reconfigure(encoding='utf-8')
    c = load(sys.argv[1])
    if len(sys.argv) > 2:
        e = c.entries[int(sys.argv[2])]
        print(f'entry {e.index}: image {e.size} B, {len(e.boxes)} boxes')
        for k, (s, en) in enumerate(e.boxes):
            print(f'[{k}] {s:#06x} {D.decode(e.body[s:en])}')
        return
    nb = sum(len(e.boxes) for e in c.entries)
    nopool = [e.index for e in c.entries if not e.boxes]
    print(f'{len(c.entries)} entries, {nb} boxes, {len(nopool)} without text {nopool[:10]}')
    raws, unsafe, bad = [], [], 0
    for e in c.entries:
        orig = c.data[c.t[e.index] * SECTOR:c.t[e.index + 1] * SECTOR]
        try:
            raw = e.rebuild()
        except ValueError as ex:
            unsafe.append((e.index, str(ex)))
            raws.append(orig)
            continue
        if raw != orig[:len(raw)]:
            bad += 1
        raws.append(raw)
    print('round-trip mismatches:', bad, ' unsafe (mid-box pointers):', len(unsafe), unsafe[:4])
    print('sector table identical:', c.build(raws)[1] == list(c.t[:len(c.entries) + 1]))


if __name__ == '__main__':
    main()
