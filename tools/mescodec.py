"""ADV/MES.BIN entry codec (decoder = ADV overlay function 0x800B15B4).

Entry = 8-byte header (u32 load addr 0x80100008, u32 end addr) + token stream.
Tokens (c = first byte):
  00-7F  back-reference: len = ((c>>2)&0x1F)+2, dist = 0x400 - (((c&3)<<8)|next)
         (7F FF = end of stream)
  80-9F  (c&0x1F)+1 literal bytes
  A0-BF  (c&0x1F)+1 pairs: 00, literal
  C0-DF  (c&0x1F)+2 copies of the next byte
  E0-FE  (c&0x1F)+1 zero bytes;  FF: next byte + 0x20 zero bytes
"""
import struct


def decode(data, limit=0x3F900):
    src, out = 0, bytearray()
    while len(out) < limit:
        c = data[src]; src += 1
        if c == 0x7F and data[src] == 0xFF:
            break
        if c < 0x80:
            n = ((c >> 2) & 0x1F) + 2
            dist = 0x400 - (((c & 3) << 8) | data[src]); src += 1
            for _ in range(n):
                out.append(out[-dist])
        else:
            k = c & 0xE0
            if k == 0x80:
                n = (c & 0x1F) + 1
                out += data[src:src + n]; src += n
            elif k == 0xA0:
                for _ in range((c & 0x1F) + 1):
                    out.append(0); out.append(data[src]); src += 1
            elif k == 0xC0:
                n = (c & 0x1F) + 2
                out += bytes([data[src]]) * n; src += 1
            else:
                if c == 0xFF:
                    n = data[src] + 0x20; src += 1
                else:
                    n = (c & 0x1F) + 1
                out += bytes(n)
    return bytes(out), src


def entries(mes):
    t = struct.unpack('<257H', mes[:514])
    return [(t[i], t[i + 1]) for i in range(256)]


def read_entry(mes, i):
    a, b = entries(mes)[i]
    raw = mes[a * 2048:b * 2048]
    load, end = struct.unpack('<II', raw[:8])
    return load, end, raw[8:]


def encode(data):
    """Greedy encoder for the same token stream (decode(encode(x)) == x); ends with 7F FF.
    Used to put edited graphics back into compressed battle data (tools/btlfont.py)."""
    out = bytearray()
    lit = bytearray()

    def flush():
        while lit:
            n = min(32, len(lit))
            out.append(0x80 | (n - 1))
            out.extend(lit[:n])
            del lit[:n]
    i, n = 0, len(data)
    while i < n:
        best = (0, None)                            # (gain, token bytes, length)
        # zero run
        z = 0
        while i + z < n and data[i + z] == 0 and z < 0xFF + 0x20:
            z += 1
        if z >= 1:
            if z >= 32:
                best = max(best, (z - 2, (bytes([0xFF, z - 0x20]), z)), key=lambda t: t[0])
            else:
                best = max(best, (z - 1, (bytes([0xE0 | (z - 1)]), z)), key=lambda t: t[0])
        # byte run
        r = 1
        while i + r < n and data[i + r] == data[i] and r < 33:
            r += 1
        if r >= 3:
            best = max(best, (r - 2, (bytes([0xC0 | (r - 2), data[i]]), r)), key=lambda t: t[0])
        # (00, x) pairs
        k = 0
        while i + 2 * k + 1 < n and data[i + 2 * k] == 0 and k < 32:
            k += 1
        if k >= 2:
            best = max(best, (2 * k - (1 + k), (bytes([0xA0 | (k - 1)]) + bytes(data[i + 2 * j + 1] for j in range(k)), 2 * k)),
                       key=lambda t: t[0])
        # back reference (dist 1..0x400, len 2..33; never the 7F FF end marker)
        bl, bd = 0, 0
        for d in range(1, min(0x400, i) + 1):
            L = 0
            while L < 33 and i + L < n and data[i + L - d] == data[i + L]:
                L += 1
            if L == 33 and d == 1:
                L = 32
            if L > bl:
                bl, bd = L, d
                if L == 33:
                    break
        if bl >= 3:
            f = 0x400 - bd
            best = max(best, (bl - 2, (bytes([((bl - 2) << 2) | (f >> 8), f & 0xFF]), bl)), key=lambda t: t[0])
        if best[0] > 0:
            flush()
            out.extend(best[1][0])
            i += best[1][1]
        else:
            lit.append(data[i])
            i += 1
            if len(lit) == 32:
                flush()
    flush()
    out.extend(b'\x7f\xff')
    assert decode(bytes(out), len(data))[0] == bytes(data)
    return bytes(out)


def encode_opt(data):
    """Optimal-parse encoder (dynamic programming over all token choices); smaller than encode()."""
    n = len(data)
    INF = 1 << 30
    cost = [INF] * (n + 1)
    choice = [None] * (n + 1)
    cost[n] = 0
    # candidate match positions by 3-byte prefix
    heads = {}
    prev3 = [[] for _ in range(n)]
    for i in range(n - 2):
        k = data[i:i + 3]
        lst = heads.setdefault(k, [])
        prev3[i] = lst[-64:]                        # most recent candidates
        lst.append(i)
    zr = [0] * (n + 1)                              # zero run length from i
    br = [0] * (n + 1)                              # same-byte run length from i
    for i in range(n - 1, -1, -1):
        zr[i] = zr[i + 1] + 1 if data[i] == 0 else 0
        br[i] = br[i + 1] + 1 if i + 1 < n and data[i + 1] == data[i] else 1
    for i in range(n - 1, -1, -1):
        best, bc = INF, None
        for L in range(1, min(32, n - i) + 1):      # literal run
            c = 1 + L + cost[i + L]
            if c < best:
                best, bc = c, ('L', L)
        z = min(zr[i], 0xFF + 0x20)
        for L in range(1, z + 1):                   # zero run
            c = (1 if L < 32 else 2) + cost[i + L]
            if c < best:
                best, bc = c, ('Z', L)
        r = min(br[i], 33)
        for L in range(3, r + 1):                   # byte run
            c = 2 + cost[i + L]
            if c < best:
                best, bc = c, ('R', L)
        k = 0
        while i + 2 * k + 1 < n and data[i + 2 * k] == 0 and k < 32:
            k += 1
            c = 1 + k + cost[i + 2 * k]
            if k >= 2 and c < best:
                best, bc = c, ('P', k)
        if i >= 1:                                  # back references
            cands = [p for p in prev3[i] if i - p <= 0x400] if i + 2 < n else []
            if data[i - 1:i] and i + 1 < n:
                cands.append(i - 1)
            seen = set()
            for p in cands:
                d = i - p
                if d in seen or d < 1:
                    continue
                seen.add(d)
                L = 0
                while L < 33 and i + L < n and data[i + L - d] == data[i + L]:
                    L += 1
                if d == 1 and L == 33:
                    L = 32
                for l in range(3, L + 1):
                    c = 2 + cost[i + l]
                    if c < best:
                        best, bc = c, ('B', l, d)
        cost[i], choice[i] = best, bc
    out = bytearray()
    i = 0
    while i < n:
        t = choice[i]
        if t[0] == 'L':
            out.append(0x80 | (t[1] - 1))
            out += data[i:i + t[1]]
            i += t[1]
        elif t[0] == 'Z':
            out += bytes([0xE0 | (t[1] - 1)]) if t[1] < 32 else bytes([0xFF, t[1] - 0x20])
            i += t[1]
        elif t[0] == 'R':
            out += bytes([0xC0 | (t[1] - 2), data[i]])
            i += t[1]
        elif t[0] == 'P':
            out.append(0xA0 | (t[1] - 1))
            out += bytes(data[i + 2 * j + 1] for j in range(t[1]))
            i += 2 * t[1]
        else:
            l, d = t[1], t[2]
            f = 0x400 - d
            out += bytes([((l - 2) << 2) | (f >> 8), f & 0xFF])
            i += l
    out += b'\x7f\xff'
    assert decode(bytes(out), n)[0] == bytes(data)
    return bytes(out)
