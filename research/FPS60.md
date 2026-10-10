# 60 fps feasibility (QoL build, not part of the translation release)

Design doc and build status: `qol/README.md`. CORRECTION: `VSync(1)` returns immediately (no wait), so the
live tests below were uncapped; the QoL build uses `VSync(0)` (next vblank).

Investigated 2026-10-09 on the dungeon (DNG overlay, base 0x800643C4 = DNG.BIN offset 0).

## Where the cap comes from
- PsyQ `VSync()` is SLPS 0x80025C98. `VSync(n)` (n>1) waits until n vblanks since the previous call.
- DNG per-frame function 0x800659B4 ends with `DrawSync(0)` (0x8006756C), `VSync(3)` (0x80067574, arg at
  0x80067578 = `ori a0,zero,3`) and the play-time clock `0x800678AC(3)` (arg at 0x80067580; the clock
  adds 3 ticks per frame and rolls over at 60). Measured: 59.8 vsync/s, 19.8 game frames/s.
- Overworld S2D: its frame routine 0x8008A438 takes the VSync count as a0 (VSync(s4) at 0x8008AF68);
  callers pass 4 (0x8008FAC0, 0x80091988) or 2 (0x80091D2C, 0x800922B0, 0x80094A34). Not measured live yet.

## Logic is frame-locked, built as blocking loops
Actions loop "update; call 0x800659B4" a fixed number of times, then snap to the exact end value.
72 call sites of 0x800659B4 in DNG.
- Step: 0x80068F64.. : 5 x advance (0x80068AA0, pos += dir*30 on 0x800A0CD0 and 0x800A0CDC),
  event check 0x8007108C, 4 more advances, snap 0x80068B64. Total 300 units.
- Turn: 0x80069028: 9 x (angle 0x15AC += dir*96), then angle = start + dir*1024.
- Unlocked without rescaling: a step takes 8 vsyncs instead of 24 (3x speed).

## Live proof of concept (RAM only, scratchpad poc60.py)
| addr | original | 60 fps |
|---|---|---|
| 0x80067578 | 34040003 | 34040001 VSync(1) |
| 0x80067580 | 34040003 | 34040001 clock +1 |
| 0x80068AE8 / 0x80068B38 | 00041100 | 00041080 (a*30 -> a*10) |
| 0x80068AEC / 0x80068B3C | 00441023 | 00441021 |
| 0x80068F7C | 2A020005 | 2A02000F (5 -> 15) |
| 0x80068FA4 | 2A020004 | 2A02000C (4 -> 12) |
| 0x80069050 | 00501021 | 02001021 (turn 96 -> 32) |
| 0x8006908C | 2A220009 | 2A22001C (9 -> 28 iterations) |
Result: step 28 vsyncs, turn 28 vsyncs (original 24-27), ~56 fps while moving.

## Performance
Unlocked VSync(1) at stock CPU: 51-57 fps in the Joy Street school corridor (not a locked 60).
`VSync(2)` (30 fps) holds 29.9 fps. PC samples while unlocked sit in GTE render code (SLPS 0x8003A9xx),
i.e. CPU-bound; DuckStation CPU overclock should give a locked 60 (the MCP set_setting for overclock
did not stick, so this was not verified).

## Approaches
A. Rescale every loop (count x3, delta /3) + other timers in the frame function. Simple per site,
   but 72 sites + fades/menus/text speed; missed sites run 3x fast; frame drops slow the game.
B. Interpolation: keep logic at 20 Hz, render 3 subframes per tick with the camera (pos 0x1580..,
   angle 0x15AC) lerped between the previous and current tick, VSync(1) between subframes, skip
   subframes when behind. Game speed identical to original; needs the side effects of 0x800659B4
   (clock, counters, input) split from rendering. Preferred.

## Overworld (S2D, base 0x800643C4) - investigated 2026-10-09
- Measured 14.9 fps (idle and walking). Main loop 0x8008B774: update 0x8008F91C (state machine,
  jump table by 0x800A5438), then tick 0x8008FA08 -> render 0x8008A438 with a0 = 4 (0x8008FAC0).
  The same count goes to VSync (0x8008AF68) and to the play clock 0x800978E0 (0x8008B0D0).
- Tick-based (not blocking loops), everything is a counter or a lerp:
  - Step: 0x8008B2F4(speed) (single caller 0x8008D73C, speed 0x400 = 4 ticks or 0x800 = 2 ticks at
    0x8008D734/38). Remaining 0x800B144C -= speed per tick (0x8008B39C), vector 0x800B143C (640 units).
    End of step: counter 0x800B1618, every 16 steps 0x801F2B30 += 1 (mod 16), then 0x8009686C and
    0x80096B5C (use rand(); look like encounter/event checks) -> all per STEP, not per frame.
  - Turn: 0x8008C01C loads tick count from table 0x80064F08 (8, 8, 16 = left, right, about-face) and
    dir from 0x80064F10; per tick 0x8008BFA4: heading 0x800B152E += dir<<7 (0x8008BFE4).
  - Camera lerps 0x8008F244/0x8008F28C speeds 0x100 (a2 at 0x8008FE34, 0x8008FF3C, 0x80091170;
    a3 at 0x8008FE48, 0x8008FF6C, 0x80091184). 0x8008EC28 passes 0x1000 (instant).
- Live PoC research/poc60_ow.py (VSync 1, speeds /4, turn counts x4, shift 7->5): turn 32 ticks of 32,
  step 16 ticks; correct motion. Stock speed only 42 fps (turn 50 vsyncs vs 34 original), so a locked
  60 needs more CPU overclock than the dungeon; `poc60_ow.py on 2` gives a 30 fps variant.
- Not yet checked: map banner/name animation, NPC/marker animation, transitions, menus opened from
  the overworld, fades.

## RNG / encounters
- rand() = BIOS A(0x2F) stub at SLPS 0x800413F8. The DNG frame routine calls rand() every frame
  (0x80067584), so a plain unlock (approach A) draws 3x more random numbers between steps: same odds,
  different sequence. Encounter/step logic itself is per step. Interpolation (approach B) keeps one
  rand() per logic tick = identical behaviour to the original.
- S2D frame/tick routines do not call rand() directly.
