"""Post-mortem / live diagnosis of glitched BTLP text (negotiation box, answer windows, command windows).

  python tools/btlp_diag.py                      read the running DuckStation (MCP server, port 2346); pauses it, dumps RAM, resumes
  python tools/btlp_diag.py ram.bin              analyse a RAM dump (2 MB, e.g. from the MCP dump_ram tool)
  python tools/btlp_diag.py watch [seconds]      live monitor: break at the end of every frame's LoadImage flush while text is
                                                 being queued and report the peak queue/ring use (catches a glitch in the act)

What it checks (all of it went wrong in the 2026-10-08 "glitched answer window after a demon spoke first" bug):
  * the three text structs of an answer window (0x800F7470 / 0x800F76E4 / 0x800F7958) and the dialogue struct (0x800EB890):
    cell counters, sprite counts, read pointers, the TALK file in use (matched against build/TALK/*.BIN) and the string they point at;
  * the circular LoadImage queue (0x800EAC50, 72 x 12 B, count at 0x800C8744): the glyph-ring slots of its entries (ring 0x800EBE48,
    128 B per slot, only 90 slots before the GPU packet area at 0x800EEB48), duplicate targets, entries lost by the wrap;
  * verdict: "queue overflow" = more uploads than the queue holds (the flush then loads only the last count-72 entries), or
    "ring overflow" = slot >= 90.
Healthy windows (after the fix in vwf/vwf_btlp_queue.asm) queue every VRAM cell once.
"""
import glob
import json
import os
import struct
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = 'http://localhost:2346/mcp'
QUEUE, QCOUNT, QCAP = 0x800EAC50, 0x800C8744, 72
RING, RING_SLOTS, RING_CNT = 0x800EBE48, 90, 0x800EBE44
FLUSH = 0x800667BC            # BTLP: end-of-frame DrawSync + clears + LoadImage loop
STRUCTS = {'dialogue': 0x800EB890, 'answer1': 0x800F7470, 'answer2': 0x800F76E4, 'answer3': 0x800F7958}
_sid = None
_n = 0


def rpc(method, params=None):
    global _sid
    h = {'Content-Type': 'application/json', 'Accept': 'application/json, text/event-stream'}
    if _sid:
        h['MCP-Session-Id'] = _sid
    body = {'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': params or {}}
    with urllib.request.urlopen(urllib.request.Request(URL, json.dumps(body).encode(), h), timeout=120) as r:
        _sid = r.headers.get('MCP-Session-Id') or _sid
        return json.loads(r.read().decode())


def call(name, **args):
    global _n
    if _sid is None or _n % 30 == 0:
        rpc('initialize', {'protocolVersion': '2025-03-26', 'capabilities': {}, 'clientInfo': {'name': 'btlp_diag', 'version': '1'}})
    _n += 1
    t = rpc('tools/call', {'name': name, 'arguments': args})['result']['content'][0]['text']
    try:
        return json.loads(t)
    except ValueError:
        return t


class Ram:
    def __init__(self, data):
        self.d = data

    def w(self, a):
        return struct.unpack_from('<I', self.d, a & 0x1FFFFF)[0]

    def h(self, a):
        return struct.unpack_from('<h', self.d, a & 0x1FFFFF)[0]

    def u16(self, a):
        return struct.unpack_from('<H', self.d, a & 0x1FFFFF)[0]

    def b(self, a, n):
        return self.d[a & 0x1FFFFF:(a & 0x1FFFFF) + n]


def text_of(ram, p):
    out = ''
    for c in ram.b(p, 80):
        if c == 0xFF:
            break
        out += chr(c - 0x68) if c >= 0x88 else '<%02X>' % c
    return out


def talk_file(ram):
    buf = ram.b(0x801C0000, 0x4000)
    best = ('?', 0.0)
    for f in glob.glob(os.path.join(ROOT, 'build', 'TALK', '*.BIN')):
        d = open(f, 'rb').read(0x4000)
        n = min(len(d), len(buf))
        same = sum(1 for i in range(0, n, 4) if d[i:i + 4] == buf[i:i + 4]) / (n / 4)
        if same > best[1]:
            best = (os.path.basename(f), same)
    return best


def analyse(ram):
    problems = []
    name, same = talk_file(ram)
    print(f'TALK file in RAM 0x801C0000: {name} ({same:.0%} of the first 16 KB equal to build/TALK)')
    for k, a in STRUCTS.items():
        cells, spr, ptr = ram.w(a + 0x1C), ram.w(a + 0x20), ram.w(a + 8)
        tex = (ram.h(a + 0x26C), ram.h(a + 0x26E))
        info = text_of(ram, ptr - 0x20) if 0x80000000 <= ptr < 0x80200000 else ''
        print(f'{k:9s} {a:#x}: cells {cells:2d} sprites {spr:2d} tex ({tex[0]:#x},{tex[1]:#x}) read ptr {ptr:#x}')
    n = ram.w(QCOUNT)
    print(f'LoadImage queue count {n} (capacity {QCAP}), glyph ring counter {ram.w(RING_CNT)}')
    ents = []
    for k in range(QCAP):
        a = QUEUE + 12 * k
        x, y, w, hgt = struct.unpack_from('<4H', ram.d, a & 0x1FFFFF)
        src = ram.w(a + 8)
        if src:
            ents.append((k, x, y, w, src))
    slots = [(e[4] - RING) // 128 for e in ents if RING <= e[4] < RING + 0x4000 and (e[4] - RING) % 128 == 0 and e[3] == 4]
    if slots:
        print(f'queue entries with a ring source: {len(slots)}, ring slot range {min(slots)}..{max(slots)}')
        if max(slots) >= RING_SLOTS:
            problems.append(f'ring overflow: slot {max(slots)} >= {RING_SLOTS} (writes into the GPU packet area at 0x800EEB48)')
        if max(slots) + 1 > QCAP:
            problems.append(f'POSSIBLE queue overflow (entries of older frames stay in the table: confirm with `watch`): {max(slots) + 1} uploads in one frame, the circular queue holds {QCAP}; '
                            f'the flush loads only entries 0..count-1 of the wrapped queue, so the first {max(slots) + 1 - QCAP} '
                            f'uploads were overwritten and everything before them is lost')
    seen = {}
    for k, x, y, w, src in ents:
        seen.setdefault((x, y), []).append(k)
    dups = {c: v for c, v in seen.items() if len(v) > 1}
    if dups:
        print(f'{len(dups)} VRAM cells are queued more than once, e.g. {list(dups.items())[:3]}'
              ' (fine only when the last one carries the final pixels; the fixed build queues every cell once)')
    if problems:
        print('\nVERDICT:')
        for p in problems:
            print('  *', p)
    else:
        print('\nVERDICT: no queue/ring overflow signature in this snapshot (the queue is empty after each flush, so a'
              ' snapshot taken after the glitch only shows leftovers: run `watch` to catch the frame itself)')
    return problems


def watch(seconds):
    """execute breakpoint on the flush: the queue holds this frame's uploads right before it is loaded"""
    call('breakpoint', action='clear')
    call('breakpoint', action='add', type='execute', address=FLUSH)
    peak = (0, 0)
    t0 = time.time()
    frames = 0
    call('continue')
    try:
        while time.time() - t0 < seconds:
            st = call('get_status').get('state')
            if st != 'paused':
                time.sleep(0.005)
                continue
            raw = call('read_memory', address=hex(QCOUNT), size=4, format='hex')['data']
            n = int.from_bytes(bytes.fromhex(raw), 'little')
            raw = call('read_memory', address=hex(RING_CNT), size=4, format='hex')['data']
            ring = int.from_bytes(bytes.fromhex(raw), 'little')
            frames += 1
            if n or ring:
                flag = ''
                if n >= QCAP - 8 or ring >= RING_SLOTS - 10:
                    flag = '   <-- NEAR OVERFLOW'
                print(f'frame {frames}: queue {n:2d}/{QCAP}  ring {ring:3d}/{RING_SLOTS}{flag}')
                if (n, ring) > peak:
                    peak = (n, ring)
                if flag:
                    call('take_screenshot', path=os.path.join(os.environ.get('TEMP', '.'), 'btlp_near_overflow.png'))
            call('continue')
    finally:
        call('breakpoint', action='clear')
        call('continue')
    print('peak queue/ring:', peak)


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    if len(sys.argv) > 1 and sys.argv[1] == 'watch':
        watch(float(sys.argv[2]) if len(sys.argv) > 2 else 60)
        return
    if len(sys.argv) > 1:
        analyse(Ram(open(sys.argv[1], 'rb').read()))
        return
    call('pause')
    path = os.path.join(os.environ.get('TEMP', '.'), 'btlp_diag_ram.bin')
    call('dump_ram', path=path)
    analyse(Ram(open(path, 'rb').read()))
    print('\n(emulation left paused; use the MCP continue tool or the emulator to resume)')


if __name__ == '__main__':
    main()
