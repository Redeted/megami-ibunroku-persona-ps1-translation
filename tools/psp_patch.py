"""PSP-script patcher for players: turns a disc patched with this project's xdelta (Persona-TL.bin or
Persona-TL-QoL.bin) into the PSP-script variant, whose story and demon negotiations use the English of the official
PSP release (Shin Megami Tensei: Persona, ULUS10432), read from the player's own PSP ISO. Nothing from the PSP is
distributed with the project.

  python tools/psp_patch.py --original JP.bin --patched Persona-TL.bin --psp Persona_PSP.iso [--out OUT.bin]

  --original  the untouched Japanese disc image (SLPS-00500, first release; .bin or its .cue)
  --patched   the same disc after applying Persona-TL.xdelta or Persona-TL-QoL.xdelta (.bin or .cue)
  --psp       the US PSP release as an ISO (ULUS10432)
  --out       result (default: next to --patched, "<name>-PSP.bin" + .cue)
  --work      work folder (default: psp_patch_work/ in the project; deleted unless --keep)

Needs Python 3.10+ and Java (no armips): the menus and every other change come from the
patched disc unchanged; ADV/E0..E3.BIN, the TALK files, the event sector tables in SLPS_005.00 and the shrine
name "Araya" -> "Alaya" (same length, patched in place in S2D.BIN / SLPS_005.00) are replaced. The inputs are
never modified.

Last step: the opening quote and the movie subtitles are re-encoded with the wording of the PSP release
(tools/fmv_opening.py, fmv_subs.py, fmv_poems.py with PERSONA_TEXT set; tools/psp_terms.py). This needs Java
(must be installed), jPSXdec 2.1 and opencv-python-headless / numpy / pillow; the last two are fetched
automatically on the first run (jPSXdec: pinned release zip into tools/ext/jpsxdec/, SHA-256 checked).

Steps: check the inputs -> extract ADV/E0..E3 + TALK from the original and pack/E0..E3 + pack/talk from the PSP
ISO -> tools/pspscript.py convert (PSP English in the PS1 control-code skeleton, QA, fallbacks: see
DEVELOPMENT.md "PSP-script variant") -> rebuild the event / TALK files -> tools/build_disc.py on a copy of the
patched disc.
"""
import argparse
import os
import re
import shutil
import struct
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import image_check  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLPS_BASE = 0x80010000 - 0x800              # PS-X EXE: t_addr 0x80010000, data from file offset 0x800
PATCH_MARK = (0x8002E7BC, bytes.fromhex('d0ffbd27'))    # first word of a hooked function: original e0ffbd27
PSP_ID = b'ULUS-10432'


def bin_of(path):
    """a .cue -> the .bin it names (single-track images)"""
    if path.lower().endswith('.cue'):
        for line in open(path, encoding='utf-8', errors='replace'):
            m = re.match(r'\s*FILE\s+"(.+)"', line)
            if m:
                return os.path.join(os.path.dirname(os.path.abspath(path)), m.group(1))
        sys.exit(f'{path}: no FILE line in the cue sheet')
    return path


def run(*cmd, env=None):
    print('+', ' '.join(os.path.basename(c) if os.path.isabs(c) else c for c in cmd), flush=True)
    r = subprocess.run([sys.executable, *cmd], cwd=ROOT, env=env)
    if r.returncode:
        sys.exit(f'step failed: {" ".join(cmd)}')


def read_disc_file(image, name):
    """one file of a MODE2/2352 PS1 image (path as on the disc, e.g. SLPS_005.00)"""
    import extract
    with open(image, 'rb') as f:
        pvd = extract.read_sectors(f, 16, 2048)
        root_lba, root_size = struct.unpack_from('<I', pvd, 158)[0], struct.unpack_from('<I', pvd, 166)[0]
        for path, lba, size in extract.walk(f, root_lba, root_size):
            if path.upper() == name.upper():
                return extract.read_sectors(f, lba, size)
    return None


def check_inputs(a):
    p = image_check.problem(a.original)
    if p:
        sys.exit(f'--original: {p}')
    slps = read_disc_file(a.patched, 'SLPS_005.00')
    if slps is None:
        sys.exit(f'--patched: {a.patched} is not a Persona (SLPS-00500) disc image')
    addr, mark = PATCH_MARK
    if slps[addr - SLPS_BASE:addr - SLPS_BASE + 4] != mark:
        sys.exit(f'--patched: {a.patched} is not patched with Persona-TL(-QoL).xdelta (apply the xdelta first)')
    with open(a.psp, 'rb') as f:
        head = f.read(32 * 2048)
    if len(head) < 17 * 2048 or head[16 * 2048 + 1:16 * 2048 + 6] != b'CD001':
        sys.exit(f'--psp: {a.psp} is not an ISO image (a .cso / .pbp must be converted to .iso first)')
    import pspscript
    files, f = pspscript.iso_files(a.psp)
    if '/UMD_DATA.BIN' not in files:
        sys.exit(f'--psp: {a.psp} is not a PSP game ISO')
    lba, size = files['/UMD_DATA.BIN']
    f.seek(lba * 2048)
    if not f.read(size).startswith(PSP_ID):
        sys.exit(f'--psp: {a.psp} is not the US release of Shin Megami Tensei: Persona (ULUS10432)')
    return slps


def patch_tables(slps, asm):
    """apply the `.org addr` / `.halfword ...` lines of etext.py's event_tables.asm to SLPS_005.00 bytes"""
    out, addr = bytearray(slps), None
    for line in open(asm, encoding='utf-8'):
        line = line.split(';')[0].strip()
        if line.startswith('.org'):
            addr = int(line.split()[1], 16)
        elif line.startswith('.halfword') and addr is not None:
            for v in line[len('.halfword'):].split(','):
                struct.pack_into('<H', out, addr - SLPS_BASE, int(v))
                addr += 2
    return bytes(out)


def same_length_patch(data, old, new, expect, what):
    """replace every `old` by `new` (same length) in data; `expect` occurrences are required"""
    assert len(old) == len(new)
    n = data.count(old)
    if n != expect:
        sys.exit(f'{what}: found {n} occurrences of the shrine name, expected {expect} (is the patched disc the '
                 'unmodified result of Persona-TL(-QoL).xdelta?)')
    return data.replace(old, new)


def patch_shrine_name(slps, patched, disc):
    """PSP wording of the overworld: Araya Shrine -> Alaya Shrine (tools/psp_terms.py GAME). Two dialogue boxes in
    S2D.BIN and the area label in SLPS_005.00 (full-width glyph codes); same lengths, so nothing moves."""
    import etext
    import s2dnames
    s2d = read_disc_file(patched, 'S2D.BIN')
    if s2d is None:
        sys.exit('--patched: S2D.BIN not found on the disc')
    a, b = etext.encode('Araya')[:-2], etext.encode('Alaya')[:-2]
    open(os.path.join(disc, 'S2D.BIN'), 'wb').write(same_length_patch(s2d, a, b, 2, 'S2D.BIN'))
    a, b = s2dnames.wide('Araya')[:-2], s2dnames.wide('Alaya')[:-2]
    return same_length_patch(slps, a, b, 1, 'SLPS_005.00')


JPSXDEC_URL = 'https://github.com/m35/jpsxdec/releases/download/v2.1/jpsxdec_v2.1-beta.zip'
JPSXDEC_SHA256 = 'e11787a2e05b6a4b6ee07972439e50da9e6798f0ca505e748f4969b3d91cd45b'
PIP_PACKAGES = {'cv2': 'opencv-python-headless', 'numpy': 'numpy', 'PIL': 'pillow'}


def ensure_movie_tools():
    """the opening quote and the movie subtitles are part of the variant: Java + jPSXdec + opencv/numpy/pillow.
    Missing jPSXdec and Python packages are installed here (jPSXdec: pinned release zip into tools/ext/jpsxdec)."""
    import importlib.util
    if shutil.which('java') is None:
        sys.exit('Java is required (it runs jPSXdec, which re-encodes the movies). Install a JRE, e.g. '
                 'https://adoptium.net/ , then run this command again.')
    missing = [pkg for mod, pkg in PIP_PACKAGES.items() if importlib.util.find_spec(mod) is None]
    if missing:
        print('installing Python packages:', ' '.join(missing), flush=True)
        if subprocess.run([sys.executable, '-m', 'pip', 'install', *missing]).returncode:
            sys.exit('pip install failed; install manually: pip install ' + ' '.join(missing))
    jar = os.path.join(ROOT, 'tools', 'ext', 'jpsxdec', 'jpsxdec.jar')
    if not os.path.exists(jar):
        import hashlib
        import io
        import urllib.request
        import zipfile
        print('downloading jPSXdec 2.1 (3.7 MB) from github.com/m35/jpsxdec ...', flush=True)
        try:
            data = urllib.request.urlopen(JPSXDEC_URL, timeout=120).read()
        except OSError as e:
            sys.exit(f'download failed ({e}). Download {JPSXDEC_URL} yourself and unpack its files into tools/ext/jpsxdec/')
        if hashlib.sha256(data).hexdigest() != JPSXDEC_SHA256:
            sys.exit('the jPSXdec download does not match the expected checksum; not using it')
        dest = os.path.join(ROOT, 'tools', 'ext', 'jpsxdec')
        os.makedirs(dest, exist_ok=True)
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            for info in z.infolist():
                name = info.filename.split('/', 1)[1] if '/' in info.filename else ''
                if name and not info.is_dir():
                    target = os.path.normpath(os.path.join(dest, name))
                    if os.path.commonpath([dest, target]) != dest:
                        sys.exit('unexpected path in the jPSXdec archive')
                    os.makedirs(os.path.dirname(target), exist_ok=True)
                    with open(target, 'wb') as o:
                        o.write(z.read(info))
    return jar


def movies(out, original):
    """PSP wording in the opening quote + subtitles of the voiced and epilogue movies (tools/psp_terms.py)"""
    env = dict(os.environ, PERSONA_TEXT='psp', PERSONA_IMAGE=original, PYTHONUTF8='1')
    for tool in ('fmv_opening.py', 'fmv_subs.py', 'fmv_poems.py'):
        run(os.path.join('tools', tool), out, env=env)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('--original', required=True)
    ap.add_argument('--patched', required=True)
    ap.add_argument('--psp', required=True)
    ap.add_argument('--out')
    ap.add_argument('--work', default=os.path.join(ROOT, 'psp_patch_work'))
    ap.add_argument('--keep', action='store_true', help='keep the work folder')
    a = ap.parse_args()
    a.original, a.patched, a.psp = (os.path.abspath(bin_of(x)) for x in (a.original, a.patched, a.psp))
    for x in (a.original, a.patched, a.psp):
        if not os.path.exists(x):
            sys.exit(f'not found: {x}')
    a.out = os.path.abspath(a.out or os.path.splitext(a.patched)[0] + '-PSP.bin')
    if os.path.abspath(a.out) in (a.original, a.patched, a.psp):
        sys.exit('--out must be a new file')
    work = os.path.abspath(a.work)

    print('checking the inputs ...', flush=True)
    slps = check_inputs(a)
    ensure_movie_tools()

    if os.path.isdir(work):
        shutil.rmtree(work)
    orig, disc = os.path.join(work, 'original'), os.path.join(work, 'disc')
    os.makedirs(disc)
    env = dict(os.environ, PYTHONHASHSEED='0', PYTHONUTF8='1',
               PERSONA_ORIGINAL=orig,
               PERSONA_PSP_FILES=os.path.join(work, 'psp'),
               PERSONA_PSP_TEXT=os.path.join(work, 'psp_text'))
    run(os.path.join('tools', 'extract.py'), a.original, orig, 'ADV/E0.BIN', 'ADV/E1.BIN', 'ADV/E2.BIN',
        'ADV/E3.BIN', 'TALK/*', env=env)
    run(os.path.join('tools', 'pspscript.py'), 'extract', a.psp, env=env)
    run(os.path.join('tools', 'pspscript.py'), 'convert', env=env)

    env['PERSONA_TEXT'] = env['PERSONA_PSP_TEXT']          # the event / TALK tools read the PSP tables from here on
    run(os.path.join('tools', 'tstatus.py'), 'qa', env=env)
    run(os.path.join('tools', 'talktl.py'), 'qa', env=env)
    run(os.path.join('tools', 'etext.py'), 'build', os.path.join(disc, 'ADV'), env=env)
    run(os.path.join('tools', 'talk.py'), 'build', os.path.join(disc, 'TALK'), env=env)
    run(os.path.join('tools', 'etctalk.py'), 'build', os.path.join(disc, 'TALK'), env=env)

    new_slps = patch_tables(slps, os.path.join(disc, 'event_tables.asm'))     # written by etext.py next to ADV/
    new_slps = patch_shrine_name(new_slps, a.patched, disc)
    open(os.path.join(disc, 'SLPS_005.00'), 'wb').write(new_slps)
    print('SLPS_005.00: event sector tables + area label updated, S2D.BIN: shrine name', flush=True)

    run(os.path.join('tools', 'build_disc.py'), a.patched, a.out, disc, env=env)
    movies(a.out, a.original)
    if not a.keep:
        shutil.rmtree(work, ignore_errors=True)
    print(f'\ndone: {a.out}\n(+ {os.path.splitext(os.path.basename(a.out))[0]}.cue). Load the .cue in the emulator.')


if __name__ == '__main__':
    main()
