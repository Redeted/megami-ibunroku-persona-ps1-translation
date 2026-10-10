"""CD-ROM MODE2/2352 sector helpers: Form 1 EDC/ECC generation.

Layout of a Form 1 sector:
  0    sync (12)        00 FF*10 00
  12   header (4)       minute, second, frame (BCD), mode = 2
  16   subheader (8)    file, channel, submode, coding (twice)
  24   user data (2048)
  2072 EDC (4)          over bytes 16..2071
  2076 ECC P (172) + Q (104), computed with the header treated as zero
"""

SECTOR = 2352
SYNC = b"\x00" + b"\xff" * 10 + b"\x00"

_edc = []
for i in range(256):
    e = i
    for _ in range(8):
        e = (e >> 1) ^ (0xD8018001 if e & 1 else 0)
    _edc.append(e)

_ecc_f = [0] * 256
_ecc_b = [0] * 256
for i in range(256):
    j = (i << 1) ^ (0x11D if i & 0x80 else 0)
    _ecc_f[i] = j
    _ecc_b[i ^ j] = i


def edc(data):
    e = 0
    for b in data:
        e = (e >> 8) ^ _edc[(e ^ b) & 0xFF]
    return e


def _ecc_pq(buf, major_count, minor_count, major_mult, minor_inc, out_off):
    """Compute one ECC block (P or Q) over buf[12:] and store at buf[out_off]."""
    size = major_count * minor_count
    for major in range(major_count):
        index = (major >> 1) * major_mult + (major & 1)
        a = b = 0
        for _ in range(minor_count):
            t = buf[12 + index]
            index += minor_inc
            if index >= size:
                index -= size
            a ^= t
            b ^= t
            a = _ecc_f[a]
        a = _ecc_b[_ecc_f[a] ^ b]
        buf[out_off + major] = a
        buf[out_off + major + major_count] = a ^ b


def bcd(n):
    return ((n // 10) << 4) | (n % 10)


def msf(lba):
    lba += 150
    return bytes((bcd(lba // 4500), bcd(lba // 75 % 60), bcd(lba % 75)))


def make_form1(lba, subheader, user_data):
    """Build a full 2352-byte Form 1 sector. subheader: 4 bytes (written twice)."""
    assert len(user_data) <= 2048
    buf = bytearray(SECTOR)
    buf[0:12] = SYNC
    buf[12:15] = msf(lba)
    buf[15] = 2
    buf[16:20] = subheader
    buf[20:24] = subheader
    buf[24:24 + len(user_data)] = user_data
    buf[2072:2076] = edc(buf[16:2072]).to_bytes(4, "little")
    header = bytes(buf[12:16])
    buf[12:16] = b"\x00\x00\x00\x00"           # Mode 2: ECC ignores the header
    _ecc_pq(buf, 86, 24, 2, 86, 2076)          # P
    _ecc_pq(buf, 52, 43, 86, 88, 2076 + 172)   # Q
    buf[12:16] = header
    return bytes(buf)
