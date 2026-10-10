"""Check that a disc image is the release this project patches.

  python tools/image_check.py <image.bin>

The patches use fixed addresses in the game's code, so they only fit the first Japanese release of
Megami Ibunroku Persona: Be Your True Mind (SLPS-00500). "Rev 1" has different code in SLPS_005.00, ADV,
BTLP, DNG, S2D, NAME, CASINO and the EXE files and is not supported.
"""
import os
import sys
import zlib

SIZE = 699705888
CRC32 = 0x360EB310
REV1_SIZE = 699672960


def crc32(path):
    c = 0
    with open(path, 'rb') as f:
        while True:
            b = f.read(1 << 24)
            if not b:
                return c & 0xFFFFFFFF
            c = zlib.crc32(b, c)


def problem(path):
    """None if the image is the supported release, else a message."""
    if not os.path.exists(path):
        return f'disc image not found: {path}'
    size = os.path.getsize(path)
    if size == REV1_SIZE:
        return (f'{path} looks like the "Rev 1" release ({size} bytes). Only the first release is supported '
                f'({SIZE} bytes, CRC32 {CRC32:08X}).')
    if size != SIZE:
        return f'{path}: {size} bytes, expected {SIZE} (single-track BIN of the first release, CRC32 {CRC32:08X}).'
    c = crc32(path)
    if c != CRC32:
        return f'{path}: CRC32 {c:08X}, expected {CRC32:08X} (a modified or different dump).'
    return None


def require(path):
    msg = problem(path)
    if msg:
        sys.exit('Wrong disc image: ' + msg)


if __name__ == '__main__':
    msg = problem(sys.argv[1])
    print(msg or 'OK: first release of SLPS-00500 (CRC32 %08X)' % CRC32)
    sys.exit(1 if msg else 0)
