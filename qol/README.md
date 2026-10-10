# Persona (SLPS-00500) enhancement patch ("QoL"): 60 fps 3D dungeons and overworld

Separate from the translation release: the translation build must not change the game's behaviour.
Everything here is only assembled when armips gets `-definelabel QOL60 1`.

| | translation release | enhancement build |
|---|---|---|
| command | `python tools/build.py` | `python tools/build.py --qol` |
| disc | `../patched/Persona-TL.bin/.cue` | `../patched_qol/Persona-TL-QoL.bin/.cue` |
| sources | everything | everything + `qol/fps60_dng.asm`, `qol/fps60_s2d.asm` |

`build/` is shared and holds whichever variant was built last (armips rewrites every overlay from
`original/` on each run, so the next normal build is clean again). Close DuckStation before building.
Save states made on one disc are not valid on the other (resident code differs).

Raw research log with measurements: `research/FPS60.md`. Live RAM test scripts: `research/poc60.py`
(dungeon) and `research/poc60_ow.py` (overworld); they talk to the DuckStation MCP server and contain
the old, uncapped VSync(1) values (see "VSync semantics").

## 1. Status (2026-10-09, evening): approach B implemented in both engines

Game logic is untouched (original step / turn / pan constants, 20 Hz dungeon ticks, 15 Hz overworld ticks).
Extra frames are drawn between logic ticks with the camera interpolated; per-frame side effects run on real
ticks only. A measured draw cost decides how many extra frames fit, so the game speed is always the original
(verified live: dungeon ticks 3 vblanks apart, overworld 4 vblanks apart, also while turning / walking).

- Dungeon (`qol/fps60_dng.asm`): hook on F's GsSetRefView2 (0x800659F4) draws up to 2 subframes at 1/3, 2/3
  by calling F recursively (`dngq_sub`), view = GsRVIEW2 at `*(0x800A0D70)+0x1580` (eye moves <= 40/tick,
  look-at radius 5000; eye jump > 200 = warp, no interpolation). Gated in subframes: pad read 0x80067640
  (returns the previous held buttons), HUD counter 0x80065FE8, door animation 0x80066AC4, light pulse /
  flash 0x80066AF8, texture scroll 0x80066BD4; play clock(3) + rand() only on real ticks. Subframes only
  when the last frame cost 1 vblank. Measured in the mall (stock CPU): turn 60 fps, step ~47 fps, idle 20.
- Overworld (`qol/fps60_s2d.asm`): driver on the main loop's draw-tick call 0x8008B77C. State lerped
  (k/4): view GsRVIEW2 0x800B1574 (6 words), map transform inputs 0x800B1040 (rot) / 0x800B1048 (pos), root
  transform (rot 0x800B152C, position recorded at 0x8008B4F4) and second root (0x800B14B4 / 0x800B14BC);
  both roots are rebuilt with S2DQ_BUILD 0x8008DEA0 per subframe and restored exactly afterwards. Gated:
  VSync / clock / frame counter 0x800B8D60 / pad 0x8008E6F4 / upload queue / idle animation + rand()
  0x8008EE40 / banner angle 0x80093E20. Policy from the measured draw cost: 1 vblank -> 3 subframes (60),
  2 -> 1 subframe (30), 3+ -> none (15, original).
- Fixed 2026-10-09 (user report: the world snapped back before each step, also with Up held): at the first
  tick of a step the overworld re-centres the map on the new cell: the root position jumps by the step
  vector 0x800B143C (0 -> 640 from standing, 160 -> 640 when walking on), and the map shift that cancels it
  is not interpolated. Detection: the step's remaining counter 0x800B144C went up since the previous tick.
  Then the previous root position is moved by the step vector too, so the in-between frame continues the
  motion. Word jump threshold also lowered 0x1000 -> 480. Verified with Up held: drawn root positions
  560 480 400 320 240 160 | 720 640 560 ... (80 per frame, no backward frame). S2D QoL code now fills its
  area exactly (0x800BB5D0..0x800BBBC4 = end of the last loaded sector): any further S2D code needs space
  elsewhere.
- Measured overworld at BMarket (stock CPU): a draw tick costs ~2.1 vblanks, 1.5 of them in the world
  object sort 0x8008B968 (52 GsSortObject4 objects), so the overworld stays at 15 fps there. Setting the
  CPU overclock through the MCP API did not change that time (2x, 4x); with the overclock set in the
  DuckStation UI (181%) the user gets a smooth 30 fps there (see the recommended setting below).
- Space: DNG code 0x800A1600..0x800A1A30 (sector ends 0x800A1BC4); S2D code 0x800BB5D0..0x800BBBA8 (sector
  ends 0x800BBBC4; only the ADV overlay references this range).
- Test helpers (scratchpad, not in the repo): fps.py (presented frames vs vblanks), ticks.py (vblank
  stamps of real ticks, `dngq_vars+4` / `s2dq_vars+4`), qpatch.py / qpatch_s2d.py (live patch from build/).

### Gameplay tweaks in the QoL build (2026-10-09, user request)
Only in the QoL disc (`.ifdef QOL60` in main.asm); the translation release keeps the original balance.
- Half the random encounter rate: `qol/encounters_s2d.asm` (overworld: grace period 16 -> 32 steps, roll
  rand() % 32 -> % 64 against the zone threshold 2 / 4 / 8; mean steps between battles 32 / 24 / 20 ->
  64 / 48 / 40) and `qol/encounters_dng.asm` (3D dungeons: cooldown 7 -> 14 steps, per-step chance 1 / 8,
  1 / 4, 1 / 2 -> 1 / 16, 1 / 8, 1 / 4; mean 15 / 11 / 9 -> 30 / 22 / 18). Constants only.
- EXP, Persona points (P.P.) and money after a battle x2 (x << 1; was x1.5 until 2026-10-10): `qol/rewards_btlp.asm`, three
  hooks at 0x800F8900 (behind the BTLP image, inside its last loaded sector). The totals
  0x800F746C (EXP), 0x800F70F0 (P.P.) and 0x800F83A4 (money) are multiplied when the end-of-battle code
  first reads them (0x80097A38, 0x80097A88, 0x800AAD70), so the split between members, the results screen
  and the wallet all see the new values. Bosses get x2 as well.
- Verified live with the old x1.5 (same battle twice): money 5460 -> 8190, EXP total 1783 -> 2674, P.P. per member
  224 / 326 / 282 / 236 / 118 -> 336 / 489 / 424 / 354 / 178. The encounter changes are verified by
  disassembly only; the user tests them in a new game.
- 2026-10-10: rewards raised to x2 (`sll a0, a0, 1`); QoL disc rebuilt 13:09 and checked on user slot 5 (dungeon
  battle, AUTO Replay): hooks present at 0x800F8900, results screen paid out. AUTO Normal can stall on a last
  enemy (everyone DEF); Replay finishes the battle.

### Recommended emulator setting (user-tested 2026-10-09)
DuckStation: Settings > Console > CPU emulation > enable **Overclock** and set it to **181%** (61.30 MHz).
Result reported by the user: the 3D dungeons run at 60 fps with no lag spikes (also the heavy mall area)
and the overworld at a smooth 30 fps. Verified live: with 181% the dungeon turn is a full 60 fps and the
logic ticks stay exactly 3 vblanks apart, so the game speed is the original. Without overclock the patch
still never slows the game down; it only draws fewer extra frames (dungeon ~45-60, overworld 15 at heavy
spots like BMarket). The overclock must be set in the DuckStation UI: changing it through the MCP API did
not affect timing in our tests. Real hardware cannot overclock, so expect the stock-speed results there.

## 2. Engine facts

Common
- Overlays load at 0x800643C4 (`OVERLAY_SLOT_ADDR`); DNG.BIN = dungeon, S2D.BIN = overworld.
- PsyQ `VSync` = SLPS 0x80025C98, `DrawSync` = 0x8002B5E8, `rand()` = 0x800413F8 (BIOS A(0x2F)).
- The vblank counter variable used by VSync is 0x8004FD3C (`VSync(-1)` returns it).

VSync semantics (read from the code, important):
- `VSync(-1)`: returns the vblank counter, no wait.
- `VSync(0)`: waits for the next vblank. **Use this for 60 fps.**
- `VSync(1)`: returns immediately (horizontal count since the last call), no wait. The live tests used
  this, i.e. they were uncapped: below 60 at stock speed, but with enough CPU overclock the game logic
  runs faster than real time.
- `VSync(n>1)`: waits until n vblanks have passed since the previous call (3 = 20 fps, 4 = 15 fps).

### Dungeon (DNG)
- Frame routine 0x800659B4 (draws the 3D view, 11x11 cell loop, HUD) ends with
  `DrawSync(0)` 0x8006756C, `VSync(3)` 0x80067574, play clock `0x800678AC(3)` 0x8006757C,
  `rand()` 0x80067584 (result unused: it only stirs the RNG every frame).
- Play clock 0x800678AC: byte 0x800A0380 += a0 (wraps at 60); in-game time bytes 0x801F29BC..C3.
- Game logic is written as blocking loops: "update; call 0x800659B4" N times. 72 call sites.
- Step (0x80068F64): 5 x advance 0x80068AA0 (pos 0x800A0CD0 / 0x800A0CDC += dir*30), event check
  0x8007108C, 4 x advance, snap 0x80068B64 (300 units per cell), then 0x80069754.
- Turn (0x80069028, a0 = dir): 9 x (angle `*(0x800A0D70)+0x15AC` += dir*96; 0x800690F4 rebuilds the
  camera), then angle = start + dir*1024 (90 degrees = 1024).
- Camera copy: 0x80067D40 copies `*(0x800A0D70)+0x1580..` (player pos/angle struct, base 0x801F0000)
  to 0x800A0CD0..
- Measured: 19.8 fps capped; uncapped 51-57 fps at stock CPU (Joy Street school corridor); 30 fps
  holds 29.9. CPU-bound in GTE render code (SLPS 0x8003A9xx); the user reports a small DuckStation CPU
  overclock gives a solid 60.
- Free space: DNG bss ends 0x800A1124; the VWF script glue uses 0x800A1200..~0x800A14C4 (grew on 2026-10-09: name
  insertion fix, `dng_skill_name`); the QoL stub is at 0x800A1800 (area 0x100), so they do not overlap. The last loaded sector ends at 0x800A1BC4.

### Overworld (S2D)
- Tick based. Main loop 0x8008B774: update 0x8008F91C (state machine, jump table indexed by
  0x800A5438), then tick 0x8008FA08 -> render 0x8008A438 with a0 = 4 (0x8008FAC0). Another caller
  passes 4 (0x80091988), others 2 (0x80091D2C, 0x800922B0, 0x80094A34) or 0.
- Render routine: `VSync(s4)` 0x8008AF68 and play clock `0x800978E0(s4)` 0x8008B0D0.
- Step: 0x8008B2F4(speed), single caller 0x8008D73C with 0x400 (4 ticks) or 0x800 (2 ticks) from
  0x8008D734/38. Remaining 0x800B144C starts at 0x1000, -= speed per tick in 0x8008B39C; vector
  0x800B143C (640 units per step, rotated by the heading). The world (not the camera) is translated;
  object matrices are rebuilt by SLPS 0x80040xxx.
- End of every step (0x8008B42C..): step counter 0x800B1618, every 16 steps 0x801F2B30 += 1 (mod 16,
  read by the HUD, probably the moon phase), then 0x8009686C and 0x80096B5C (use rand(), most likely
  encounter / event checks).
- Turn: 0x8008C01C loads the tick count from 0x80064F08 (8 left, 8 right, 16 about-face) and the
  direction from 0x80064F10; per tick 0x8008BFA4: heading 0x800B152E += dir<<7 (0x8008BFE4); the
  rendered heading 0x800B1042 = 0x800B14B4 + 0x800B152E.
- Camera lerps: 0x8008F244 / 0x8008F28C set targets and speeds (a2 -> 0x800B3464, a3 -> 0x800B3468);
  0x8008F2EC advances t (0x800A5718, 0x800A573C) by the speed per tick, clamped at 0x1000. Speeds
  0x100 at 0x8008FE34, 0x8008FF3C, 0x80091170 (a2) and 0x8008FE48, 0x8008FF6C, 0x80091184 (a3);
  0x8008EC28 passes 0x1000 (instant).
- Measured: 14.9 fps idle and walking; uncapped ~42 fps at stock CPU (needs more overclock than the
  dungeon for 60); 30 fps holds.
- Free space: S2D glue area 0x800BB200..0x800BB8E8 (used up to ~0x800BB550); the QoL stubs are at
  0x800BB800 (area 0xE8).

### Encounters / RNG
- Encounter-related work happens per step in both engines, so encounter odds per step do not depend on
  the frame rate.
- The dungeon frame routine calls rand() every frame. A plain unlock would draw 3x more numbers
  between steps (same odds, different sequence). The QoL stub calls rand() once every 3 frames, so the
  number of draws per step/turn matches the original.
- The overworld frame/tick routines do not call rand() directly.

## 3. What the current QoL build patches

`qol/fps60_dng.asm`
| addr | change |
|---|---|
| 0x80067574..84 | `jal dng_frame_sync` + nops (replaces VSync(3), clock(3), rand()) |
| 0x80068AE8/EC, 0x80068B38/3C | step delta dir*30 -> dir*10 |
| 0x80068F7C / 0x80068FA4 | step loops 5 -> 15, 4 -> 12 frames |
| 0x80069050 / 0x8006908C | turn delta dir*96 -> dir*32, loop 9 -> 28 frames (ends with the original snap) |
| 0x800A1800 | `dng_frame_sync`: VSync(0); clock(elapsed vblanks, 1..6); rand() every 3rd frame |

`qol/fps60_s2d.asm`
| addr | change |
|---|---|
| 0x8008AF68 | `jal s2d_vsync`: mode 4 -> VSync(0), other modes unchanged |
| 0x8008B0D0 | `jal s2d_clock_sync`: mode 4 -> clock(elapsed vblanks), other modes unchanged |
| 0x8008D734/38 | step speed 0x400 -> 0x100, 0x800 -> 0x200 |
| 0x80064F08 | turn ticks 8/8/16 -> 32/32/64 |
| 0x8008BFE4 | heading step dir<<7 -> dir<<5 |
| six lerp speed sites | 0x100 -> 0x40 |

Consequence of approach A: when a frame takes longer than one vblank, the game logic slows down
(like any PS1 slowdown). Real-time speed matches the original only at a locked 60.

## 4. Test procedure

User save states (on the translation disc; for the QoL disc make new ones from a hard save):
- Dungeon: slot 1 = 2D room, press Down once -> 3D dungeon (Joy Street / school).
- Overworld: slot 2 = school hall, Up once -> overworld. Left/Right twice = about-face, Up into the
  school 2D room; from the overworld about 10 steps Down = school 3D dungeon (and back: about-face,
  10 steps Up).
Checks: fps (DuckStation OSD), step/turn duration vs the original disc, door/stairs/menu/fade speed,
in-game play time vs a stopwatch, encounters after the story allows them, entering/leaving rooms.

Measuring from a script: DuckStation MCP over HTTP at `http://127.0.0.1:2346/mcp` (not `localhost`:
that costs 2 s per call); `get_status` gives `frame_number` (vblanks) and `internal_frame_number`
(presented frames), so fps = d(internal)/dt. A breakpoint on 0x80025C98 + `ra`/`a0` shows who calls
VSync with what.

## 5. Next steps

### Dungeon: approach B (camera interpolation), chosen by the user
Keep all game logic at 20 Hz exactly as the original; draw up to 3 frames per logic tick.
1. Revert the step/turn/loop constants (logic unchanged), keep VSync(3) timing semantics per tick.
2. Split 0x800659B4 into side effects and drawing. Known side effects: play clock, rand(), counters
   inside the HUD/map code (to be audited: compass, moon icon, map blink, text box, effect timers).
3. Per logic tick: remember the previous camera (pos 0x1580.., angle 0x15AC, and the copy at
   0x800A0CD0); draw subframes k = 1..3 with camera = lerp(prev, cur, k/3) (angle with wrap-around),
   VSync(0) between subframes; run the side effects once on the real tick. Skip remaining subframes
   when the vblank counter shows the tick budget (3 vblanks) is used up, so game speed stays constant.
4. Disable interpolation when the camera jumps (floor change, warp, battle return): delta above one
   cell (300) or angle step above 1024.
5. Needs ordering-table / double-buffer care: each subframe must build and draw a full frame
   (check how 0x800659B4 swaps buffers: 0x80040464 at its start returns the buffer index 0x800A0388).

### Overworld
- Option 1: finish approach A (audit banner, marker animation, fades, menus, the other mode-4 caller
  0x80091988 and the 2-mode loops).
- Option 2 (preferred, consistent with the dungeon): keep ticks at 15 Hz and interpolate. The step
  is already a lerp (remaining 0x800B144C) and the turn a linear counter, so subframes can evaluate
  them at fractional ticks (remaining - speed*k/4, heading + (dir<<7)*k/4) without touching logic.

### Performance / options
- Stock hardware: dungeon 51-57 fps, overworld ~42 fps uncapped. Offer a 30 fps option (dungeon
  VSync(0) x2 subframes, overworld 2 subframes) for real hardware, 60 fps for emulators with CPU
  overclock. With approach B, dropped subframes cost smoothness, not speed.

### Open questions
- Exact routines behind 0x8009686C / 0x80096B5C (encounter?).
- Whether any dungeon timer (damage floors, effect durations) counts frames instead of steps.
- BTLP (battles) frame rate was not examined.

### Sync note (2026-10-09)
`patched_qol/Persona-TL-QoL.bin` was built BEFORE the dungeon "wore off" / name-insert fix; rebuild it with `python tools/build.py --qol` to get the fix plus the 60 fps patches (they touch different addresses).
