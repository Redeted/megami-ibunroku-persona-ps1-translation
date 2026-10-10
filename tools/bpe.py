"""Byte-pair packing of VWF message strings (same format as tools/btlevt.py; unpacker btlp/btlevt_unpack.asm).

pack(strings) -> (packed {key: bytes}, pairs [(left, right)])
  strings: {key: bytes} each = English VWF text (88..E6) and control codes (FF xx), ending FF F5 / FF EF.
  Format: FF xx = code copied as is (the FF F5 / FF EF end stops the unpacker), 88..E6 = a character, 01..87 / E7..FE = pair
  code k (index into `pairs`, in CODES order); a pair's two bytes may be pair codes again.
unpack(packed, pairs) mirrors the unpacker (used by the build to verify every string).
"""
import collections

CODES = list(range(0x01, 0x88)) + list(range(0xE7, 0xFF))


def _runs(b):
    out, i = [], 0
    while i < len(b):
        if b[i] == 0xFF:
            out.append((False, [b[i], b[i + 1]]))
            i += 2
        else:
            assert 0x88 <= b[i] <= 0xE6, (b[i], b)
            if out and out[-1][0]:
                out[-1][1].append(b[i])
            else:
                out.append((True, [b[i]]))
            i += 1
    return out


def pack(strings, max_pairs=len(CODES), min_count=3):
    seqs = {k: _runs(b) for k, b in strings.items()}
    pairs = []
    while len(pairs) < max_pairs:
        cnt = collections.Counter()
        for rs in seqs.values():
            for txt, sy in rs:
                if txt:
                    for k in range(len(sy) - 1):
                        cnt[(sy[k], sy[k + 1])] += 1
        if not cnt:
            break
        (x, y), n = cnt.most_common(1)[0]
        if n < min_count:
            break
        code = 0x100 + len(pairs)
        pairs.append((x, y))
        for rs in seqs.values():
            for txt, sy in rs:
                if txt:
                    k = 0
                    while k < len(sy) - 1:
                        if sy[k] == x and sy[k + 1] == y:
                            sy[k:k + 2] = [code]
                        k += 1

    def byte(sym):
        return CODES[sym - 0x100] if sym >= 0x100 else sym
    packed = {k: bytes(byte(v) for txt, sy in rs for v in sy) for k, rs in seqs.items()}
    real = [(byte(x), byte(y)) for x, y in pairs]
    for k in packed:
        assert unpack(packed[k], real) == strings[k], f'bpe: round trip failed for {k}'
    return packed, real


def unpack(b, pairs):
    ix = {c: k for k, c in enumerate(CODES)}
    out, i = [], 0
    while True:
        c = b[i]
        i += 1
        if c == 0xFF:
            out += [c, b[i]]
            i += 1
            if b[i - 1] in (0xF5, 0xEF):
                return bytes(out)
            continue
        st = [c]
        while st:
            x = st.pop()
            if x in ix:
                l, r = pairs[ix[x]]
                st += [r, l]
            else:
                out.append(x)
