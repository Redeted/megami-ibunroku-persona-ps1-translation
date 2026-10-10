"""Bring an OLD DuckStation save state in line with the current build (needs the DuckStation MCP server, port 2346).

  python tools/patch_state.py <slot>            load the slot, write the changed bytes of the resident main EXE
                                                (item names, choices, VWF code ...) and, if the ADV overlay is resident,
                                                of ADV.BIN (system messages ...), plus the menu graphics in VRAM
  python tools/patch_state.py <slot> --run      same, then resume the emulator
  --lean                                        skip the SLPS spans (item names, VWF engine ...), patch overlays + the dungeon file only
  --no-remap                                    skip the stale overworld-name pointer scan (slow; useless in battles)

Why: a save state keeps the resident SLPS tables, the loaded overlay and VRAM of the build it was made on. A fresh boot of
the rebuilt disc needs none of this. The spans are the differences original -> build, merged when closer than 48 bytes
(about 20 writes). The MCP server answers HTTP 400 after ~100 requests per session, so the session is re-initialised
every 20 writes.  Run `python tools/build.py` first (the disc can stay as it is; this reads build/).
"""
import json
import os
import struct
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = 'http://localhost:2346/mcp'
SLPS_BASE = 0x80010000 - 0x800
ADV_BASE = 0x800643C4
_sid = None


def rpc(method, params=None):
    global _sid
    h = {'Content-Type': 'application/json', 'Accept': 'application/json, text/event-stream'}
    if _sid:
        h['MCP-Session-Id'] = _sid
    body = {'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': params or {}}
    with urllib.request.urlopen(urllib.request.Request(URL, json.dumps(body).encode(), h), timeout=120) as r:
        _sid = r.headers.get('MCP-Session-Id') or _sid
        return json.loads(r.read().decode())


def init():
    rpc('initialize', {'protocolVersion': '2025-03-26', 'capabilities': {}, 'clientInfo': {'name': 'patch_state', 'version': '1'}})


_n = 0


def call(name, **args):
    global _n
    _n += 1
    if _n % 12 == 0:
        init()                    # the server answers HTTP 400 after ~100 requests per session
    r = rpc('tools/call', {'name': name, 'arguments': args})
    return json.loads(r['result']['content'][0]['text']) if r['result']['content'][0]['text'].startswith('{') else r


def spans(a, b, gap=48):
    out, i = [], 0
    while i < len(a):
        if a[i] != b[i]:
            j = i
            while True:
                k = j
                while k < len(a) and a[k] == b[k] and k - j < gap:
                    k += 1
                if k < len(a) and a[k] != b[k] and k - j < gap:
                    j = k + 1
                else:
                    break
            out.append((i, j))
            i = j + 1
        else:
            i += 1
    return out


def read(path):
    return open(os.path.join(ROOT, path), 'rb').read()


def main():
    slot = int(sys.argv[1])
    run = '--run' in sys.argv
    jobs = []                                               # (ram address, bytes)
    a, b = read('original/SLPS_005.00'), read('build/SLPS_005.00')
    for s, e in spans(a, b):
        if '--lean' not in sys.argv:                        # --lean: overlays + dungeon file only (fast, ~70 writes)
            jobs.append((s + SLPS_BASE, b[s:e]))
    ovl = {}
    for nm in ('ADV', 'S2D', 'BTLP', 'DNG'):
        oa, ob = read(f'original/{nm}.BIN'), read(f'build/{nm}.BIN')
        oa = oa + bytes(max(0, len(ob) - len(oa)))               # the build may be longer (s2dscript extension)
        ovl[nm] = (oa, ob, [(s + ADV_BASE, ob[s:e]) for s, e in spans(oa, ob)])
    adv_a, adv_b, adv_jobs = ovl['ADV'][0], ovl['ADV'][1], [(a, b, None) for a, b in ovl['ADV'][2]]
    init()
    call('pause')
    call('breakpoint', action='clear')
    for bt in ('circle', 'cross', 'triangle', 'square', 'up', 'down', 'left', 'right'):
        call('release_button', button=bt)
    print(call('load_state', slot=slot))
    # is the ADV overlay resident? compare a stable stretch of the code with the original or the build
    cur = bytes.fromhex(call('read_memory', address=ADV_BASE + 0x1000, size=32)['data'])
    which = None
    for nm, (oa, ob, js) in ovl.items():
        if cur in (oa[0x1000:0x1020], ob[0x1000:0x1020]):
            which = nm
            jobs += js
    print(f'{len(jobs)} writes (resident overlay: {which or "none of ADV/S2D/BTLP/DNG (skipped)"})')
    # the dungeon script file (D0x/D??.BIN, the boxes of tools/dngtext.py) is resident at 0x80130000 while a 3D dungeon is up
    import glob
    head = bytes.fromhex(call('read_memory', address=0x80130000, size=32)['data'])
    for fp in sorted(glob.glob(os.path.join(ROOT, 'original', 'D0*', 'D*.BIN'))):
        if len(os.path.basename(fp)) != 7:
            continue
        oa = open(fp, 'rb').read()
        bp = fp.replace(os.sep + 'original' + os.sep, os.sep + 'build' + os.sep)
        if oa[:32] == head and os.path.exists(bp):
            ob = open(bp, 'rb').read()
            sp = spans(oa, ob[:len(oa)]) if len(ob) >= len(oa) else []
            jobs += [(s_ + 0x80130000, ob[s_:e_]) for s_, e_ in sp]
            print(f'dungeon file {os.path.basename(fp)} resident: {len(sp)} spans')
    # stale pointers saved in the game state (e.g. the current overworld location name, RAM 0x801F....): a fresh game writes the
    # new addresses itself, an old state still holds old ones: from the original build (map `ptr`) or from an earlier layout of
    # the English names (found by the content of the string they point at, map `content`)
    mp = os.path.join(ROOT, 'build', 's2dnames_map.json')
    if os.path.exists(mp) and '--no-remap' not in sys.argv:
        mj = json.load(open(mp))
        remap = {int(k, 16): int(v, 16) for k, v in mj['ptr'].items()}
        content = {bytes.fromhex(k): int(v, 16) for k, v in mj['content'].items()}
        init()
        fixes = []
        n = 0
        areas = [(0x801F0000 + k, 0x1000) for k in range(0, 0x10000, 0x1000)] + [(0x800A5380, 0x150)]
        for base, size in areas:
          ram = bytes.fromhex(call('read_memory', address=base, size=size)['data'])
          for off in range(0, len(ram) - 3, 4):
            v = struct.unpack_from('<I', ram, off)[0]
            new = remap.get(v)
            if new is None and (0x800AA000 <= v < 0x800AB100 or 0x80010000 <= v < 0x80040000):
                s_ = bytes.fromhex(call('read_memory', address=v, size=40)['data'])
                e = s_.find(bytes([0xFF, 0x01]))
                new = content.get(s_[:e + 2]) if e >= 0 else None
            if new is not None and new != v:
                fixes.append((base + off, new))
                n += 1
        print(f'{n} stale name pointers found')
    for n, (addr, data) in enumerate(jobs):
        if n % 20 == 0:
            init()
        call('write_memory', address=addr, data=data.hex())
    for addr, new in (fixes if 'fixes' in dir() else []):
        call('write_memory', address=addr, data=struct.pack('<I', new).hex())
    # menu graphics (slot screen) in VRAM: only meaningful if the screen is up, harmless otherwise
    try:
        import tim
        d = read('build/ADV/ADVCMD.BIN')
        ta, tp = tim.parse(d, 0x281D8), tim.parse(d, 0x38)
        tmp = os.path.join(os.environ.get('TEMP', '.'), 'ps_atlas.bin')
        open(tmp, 'wb').write(d[ta['at']:ta['at'] + ta['w'] * 2 * ta['h']])
        init()
        call('write_vram_region', x=768, y=416, width=64, height=64, input_path=tmp)
        page = d[tp['at']:tp['at'] + tp['w'] * 2 * tp['h']]
        tmp2 = os.path.join(os.environ.get('TEMP', '.'), 'ps_tag.bin')
        open(tmp2, 'wb').write(b''.join(page[(168 + y) * 128 + 112:(168 + y) * 128 + 124] for y in range(12)))
        for px in (512, 896):
            call('write_vram_region', x=px + 56, y=256 + 168, width=6, height=12, input_path=tmp2)
        tmp3 = os.path.join(os.environ.get('TEMP', '.'), 'ps_lc.bin')    # small-font lowercase row 17 (tools/smallfont_lc.py)
        open(tmp3, 'wb').write(b''.join(page[(204 + y) * 128:(205 + y) * 128] for y in range(12)))
        for px in (512, 896):
            call('write_vram_region', x=px, y=256 + 204, width=64, height=12, input_path=tmp3)
    except Exception as ex:                                 # noqa: BLE001
        print('VRAM patch skipped:', ex)
    if run:
        call('continue')
    print('done')


if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    main()
