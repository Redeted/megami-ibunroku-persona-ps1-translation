"""Build a patched disc image from build/ (armips output).

For every file in build/ that differs from the original disc file:
  - if it fits in the sectors the original occupied, it is written in place;
  - otherwise it is appended after the end of the volume and its ISO9660
    directory record is pointed at the new extent.
Directory records get the new size, the PVD gets the new volume size, every
written sector gets fresh EDC/ECC, and a matching .cue is written.

The game resolves file names through its own table: FNAME.DAT (NUL-separated
names) indexes FSECT.DAT (u32 LBA) and FSIZE.DAT (u32 size, whole sectors).
Those tables are themselves found through the ISO directory. Both the ISO
records and the game tables are updated for every relocated/resized file.

Usage: python tools/build_disc.py <original.bin> <out.bin> [build_dir]
"""
import os
import shutil
import struct
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cdsector import SECTOR, make_form1, msf, SYNC  # noqa: E402

SUB_DATA = b"\x00\x00\x08\x00"
SUB_LAST = b"\x00\x00\x89\x00"   # data | EOR | EOF
POSTGAP = 150


class Disc:
    def __init__(self, path):
        self.f = open(path, "r+b")
        self.f.seek(0, 2)
        self.sectors = self.f.tell() // SECTOR

    def raw(self, lba):
        self.f.seek(lba * SECTOR)
        return self.f.read(SECTOR)

    def user(self, lba):
        return self.raw(lba)[24:24 + 2048]

    def write_user(self, lba, data, sub=None):
        sub = sub if sub is not None else self.raw(lba)[16:20] if lba < self.sectors else SUB_DATA
        self.f.seek(lba * SECTOR)
        self.f.write(make_form1(lba, sub, data.ljust(2048, b"\x00")))
        self.sectors = max(self.sectors, lba + 1)

    def write_empty(self, lba):
        s = bytearray(SECTOR)
        s[0:12] = SYNC
        s[12:15] = msf(lba)
        s[15] = 2
        self.f.seek(lba * SECTOR)
        self.f.write(s)
        self.sectors = max(self.sectors, lba + 1)

    def walk(self, lba, size, prefix=""):
        """Yield (path, extent_lba, size, record_lba, record_offset) for files."""
        for n in range((size + 2047) // 2048):
            sec = self.user(lba + n)
            pos = 0
            while pos < 2048:
                rec_len = sec[pos]
                if rec_len == 0:
                    break
                ext, = struct.unpack_from("<I", sec, pos + 2)
                ext_size, = struct.unpack_from("<I", sec, pos + 10)
                flags = sec[pos + 25]
                name = sec[pos + 33:pos + 33 + sec[pos + 32]]
                if name not in (b"\x00", b"\x01"):
                    name = name.decode("ascii").split(";")[0]
                    if flags & 2:
                        yield from self.walk(ext, ext_size, prefix + name + "/")
                    else:
                        yield prefix + name, ext, ext_size, lba + n, pos
                pos += rec_len

    def set_record(self, rec_lba, rec_off, ext, size):
        sec = bytearray(self.user(rec_lba))
        struct.pack_into("<I", sec, rec_off + 2, ext)
        struct.pack_into(">I", sec, rec_off + 6, ext)
        struct.pack_into("<I", sec, rec_off + 10, size)
        struct.pack_into(">I", sec, rec_off + 14, size)
        self.write_user(rec_lba, bytes(sec))

    def write_file(self, lba, data):
        count = max(1, (len(data) + 2047) // 2048)
        for n in range(count):
            self.write_user(lba + n, data[n * 2048:(n + 1) * 2048],
                            SUB_LAST if n == count - 1 else SUB_DATA)
        return count


def main():
    src, out = sys.argv[1], sys.argv[2]
    build = sys.argv[3] if len(sys.argv) > 3 else "build"
    shutil.copyfile(src, out)
    disc = Disc(out)
    pvd = bytearray(disc.user(16))
    volume = struct.unpack_from("<I", pvd, 80)[0]
    root_lba, = struct.unpack_from("<I", pvd, 156 + 2)
    root_size, = struct.unpack_from("<I", pvd, 156 + 10)
    entries = {p.upper(): e for p, *e in disc.walk(root_lba, root_size)}

    def read_file(path):
        ext, size, _, _ = entries[path]
        return b"".join(disc.user(ext + n) for n in range((size + 2047) // 2048))[:size]

    fnames = [n.decode("ascii") for n in read_file("FNAME.DAT").split(b"\x00") if n]
    fsect = bytearray(read_file("FSECT.DAT"))
    fsize = bytearray(read_file("FSIZE.DAT"))
    game_index = {n.lstrip("\\").split(";")[0].replace("\\", "/").upper(): i for i, n in enumerate(fnames)}
    tables_dirty = False

    orig_end = disc.sectors
    append_at = orig_end          # after the original volume + its padding
    changed = 0
    for r, _, files in os.walk(build):
        for f in sorted(files):
            local = os.path.join(r, f)
            disc_path = os.path.relpath(local, build).replace(os.sep, "/").upper()
            if disc_path not in entries:
                continue          # not a disc file (symbols, temp output, ...)
            ext, size, rec_lba, rec_off = entries[disc_path]
            data = open(local, "rb").read()
            orig = b"".join(disc.user(ext + n) for n in range((size + 2047) // 2048))[:size]
            if data == orig:
                continue
            changed += 1
            if (len(data) + 2047) // 2048 <= (size + 2047) // 2048:
                disc.write_file(ext, data)
                where = f"in place @ {ext}"
            else:
                ext = append_at
                append_at += disc.write_file(ext, data)
                where = f"relocated -> {ext}"
            disc.set_record(rec_lba, rec_off, ext, len(data))
            if disc_path in game_index:
                i = game_index[disc_path]
                struct.pack_into("<I", fsect, i * 4, ext)
                struct.pack_into("<I", fsize, i * 4, (len(data) + 2047) // 2048 * 2048)
                tables_dirty = True
            print(f"{disc_path:20} {size:>9} -> {len(data):>9} bytes  {where}")

    if tables_dirty:
        for name, table in (("FSECT.DAT", fsect), ("FSIZE.DAT", fsize)):
            ext, size, _, _ = entries[name]
            disc.write_file(ext, bytes(table))
        print("updated game file tables FSECT.DAT / FSIZE.DAT")

    if append_at > orig_end:
        for lba in range(append_at, append_at + POSTGAP):
            disc.write_empty(lba)
        volume = append_at + POSTGAP
        struct.pack_into("<I", pvd, 80, volume)
        struct.pack_into(">I", pvd, 84, volume)
        disc.write_user(16, bytes(pvd))
    disc.f.close()

    cue = os.path.splitext(out)[0] + ".cue"
    with open(cue, "w", newline="\r\n") as c:
        c.write(f'FILE "{os.path.basename(out)}" BINARY\n  TRACK 01 MODE2/2352\n    INDEX 01 00:00:00\n')
    print(f"{changed} file(s) changed; volume {volume} sectors; wrote {out} + {os.path.basename(cue)}")


if __name__ == "__main__":
    main()
