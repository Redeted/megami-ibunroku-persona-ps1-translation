"""RAM patches that bring an OLD save state in line with the current build.

A save state carries resident code and tables in RAM, so after a rebuild an old state
still has the previous SLPS code, FONT.BIN glyphs, file-location table (FSECT/FSIZE) and
the ADV/E?.BIN sector tables. Run this after build.py; it writes one .bin per chunk to
build/livepatch/ plus manifest.txt (address, file). Apply each with the emulator's
write_memory (or the DuckStation MCP write_memory path=...) right after load_state.

  python tools/live_patch.py <patched disc .bin>
Chunks: resident SLPS code changes (tools/ramdiff), FONT.BIN, E0..E3 FSECT/FSIZE entries
and sector tables. States made on a build with the same fixed layout need only the
code/font chunks (or nothing, if SLPS and FONT did not change).
"""
import os
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import extract as ex  # noqa: E402
import etext  # noqa: E402

FSECT_RAM, FSIZE_RAM = 0x80062BC8, 0x800633D8


def disc_tables(img):
    with open(img, 'rb') as f:
        pvd = ex.read_sectors(f, 16, 2048)
        rl, = struct.unpack_from('<I', pvd, 158)
        rs, = struct.unpack_from('<I', pvd, 166)
        files = {p: (l, s) for p, l, s in ex.walk(f, rl, rs)}
        data = {n: ex.read_sectors(f, *files[n]) for n in ('FNAME.DAT', 'FSECT.DAT', 'FSIZE.DAT')}
    return data


def main():
    img = sys.argv[1]
    out = os.path.join(ROOT, 'build', 'livepatch')
    os.makedirs(out, exist_ok=True)
    for f in os.listdir(out):
        os.remove(os.path.join(out, f))
    manifest = []

    def emit(name, addr, data):
        p = os.path.join(out, name)
        open(p, 'wb').write(data)
        manifest.append(f'0x{addr:08X} {p}')

    # resident SLPS code/data that differs from the original
    orig = open(os.path.join(ROOT, 'original', 'SLPS_005.00'), 'rb').read()
    built = open(os.path.join(ROOT, 'build', 'SLPS_005.00'), 'rb').read()
    base, i, n, k = 0x8000F800, 0, min(len(orig), len(built)), 0
    while i < n:
        if orig[i] == built[i]:
            i += 1
            continue
        j = i
        while j < n and (orig[j] != built[j] or (j + 4 < n and orig[j:j + 4] != built[j:j + 4])):
            j += 1
        j = (j + 3) & ~3
        s = i & ~3
        emit(f'slps_{k:02d}.bin', base + s, built[s:j])
        k += 1
        i = j
    emit('font.bin', 0x801E0000, open(os.path.join(ROOT, 'build', 'FONT.BIN'), 'rb').read())

    # file-location entries + sector tables of the E files
    tab = disc_tables(img)
    names = tab['FNAME.DAT'].split(b'\0')
    for fn in etext.FILES:
        idx = names.index(b'\\ADV\\' + fn.encode() + b'.BIN;1')
        lba, = struct.unpack_from('<I', tab['FSECT.DAT'], 4 * idx)
        size, = struct.unpack_from('<I', tab['FSIZE.DAT'], 4 * idx)
        emit(f'{fn}_fsect.bin', FSECT_RAM + 4 * idx, struct.pack('<I', lba))
        emit(f'{fn}_fsize.bin', FSIZE_RAM + 4 * idx, struct.pack('<I', size))
        bp = os.path.join(ROOT, 'build', 'ADV', f'{fn}.BIN')
        src = open(bp if os.path.exists(bp) else os.path.join(ROOT, 'original', 'ADV', f'{fn}.BIN'), 'rb').read()
        t = struct.unpack_from('<1024H', src, 0)
        cnt = 0
        while t[cnt + 1] > t[cnt]:
            cnt += 1
        cnt += 1
        emit(f'{fn}_table.bin', etext.SLPS_TABLES[fn], struct.pack(f'<{cnt}H', *t[:cnt]))
        print(f'{fn}: idx {idx}, LBA {lba}, size {size}, {cnt} table values')
    open(os.path.join(out, 'manifest.txt'), 'w').write('\n'.join(manifest) + '\n')
    print(len(manifest), 'chunks ->', out)


if __name__ == '__main__':
    main()
