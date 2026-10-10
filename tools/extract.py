"""Extract files from the Persona (SLPS-00500) MODE2/2352 disc image.

Usage: python tools/extract.py <image.bin> <out_dir> [path ...]
With no paths, extracts every file the build reads (everything except the movie folders STR0..STR2).
"""
import os
import struct
import sys

SECTOR = 2352
DATA_OFS = 24  # MODE2 Form1: 12 sync + 4 header + 8 subheader

DEFAULT_TARGETS = [
    "SLPS_005.00",
    "ADV.BIN", "BTLP.BIN", "CASINO.BIN", "DNG.BIN", "OPEN.BIN", "S2D.BIN",
    "EXE/ATLUS.EXE", "EXE/OPEN.EXE", "EXE/MOVIE.EXE", "EXE/END.EXE",
    "ADV/MES.BIN", "NAME.BIN", "NAMEDT.BIN", "FONT.BIN",
    "TALK/*",
]


def read_sectors(f, lba, size):
    out = bytearray()
    while len(out) < size:
        f.seek(lba * SECTOR + DATA_OFS)
        out += f.read(2048)
        lba += 1
    return bytes(out[:size])


def walk(f, lba, size, prefix=""):
    data = read_sectors(f, lba, size)
    pos = 0
    while pos < len(data):
        rec_len = data[pos]
        if rec_len == 0:
            pos = (pos // 2048 + 1) * 2048  # records never span sectors
            continue
        ext_lba, = struct.unpack_from("<I", data, pos + 2)
        ext_size, = struct.unpack_from("<I", data, pos + 10)
        flags = data[pos + 25]
        name_len = data[pos + 32]
        name = data[pos + 33:pos + 33 + name_len]
        pos += rec_len
        if name in (b"\x00", b"\x01"):
            continue
        name = name.decode("ascii").split(";")[0]
        path = prefix + name
        if flags & 2:
            yield from walk(f, ext_lba, ext_size, path + "/")
        else:
            yield path, ext_lba, ext_size


def matches(path, targets):
    if targets is None:
        return not path.startswith("STR")
    for t in targets:
        if t.endswith("/*") and path.startswith(t[:-1]):
            return True
        if path == t:
            return True
    return False


def main():
    image, out_dir = sys.argv[1], sys.argv[2]
    targets = sys.argv[3:] or None
    if targets is None:
        import image_check
        image_check.require(image)
    with open(image, "rb") as f:
        pvd = read_sectors(f, 16, 2048)
        root_lba, = struct.unpack_from("<I", pvd, 156 + 2)
        root_size, = struct.unpack_from("<I", pvd, 156 + 10)
        for path, lba, size in walk(f, root_lba, root_size):
            if not matches(path, targets):
                continue
            dest = os.path.join(out_dir, path)
            os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
            with open(dest, "wb") as o:
                o.write(read_sectors(f, lba, size))
            print(f"{path:24} lba={lba:6} size={size}")


if __name__ == "__main__":
    main()
