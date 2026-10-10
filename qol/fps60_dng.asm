;; =============================================================
;; QoL (separate enhancement build, `python tools/build.py --qol`): DNG.BIN 3D dungeon at 60 fps,
;; "approach B" (qol/README.md section 5): the game logic is untouched and still runs at 20 Hz
;; (one frame-routine call = one tick, 3 vblanks). When the camera moved by a small amount since the
;; previous tick, the frame routine first draws up to two extra frames with the camera at 1/3 and 2/3
;; of the way (recursive call with dngq_sub set), then the real frame. Per-frame side effects inside
;; the routine (pad read, play clock, rand(), HUD / light / texture / door animation counters) run on
;; real frames only. A subframe that would be late is skipped: slow areas lose smoothness, not speed.
;; =============================================================
.definelabel DNGQ_VSYNC, 0x80025C98          ; PsyQ VSync(n): 0 = next vblank, -1 = vblank counter
.definelabel DNGQ_RAND, 0x800413F8          ; BIOS A(0x2F) rand()
.definelabel DNG_PLAY_CLOCK, 0x800678AC          ; play time += a0 ticks (60 per second)
.definelabel DNGQ_FRAME, 0x800659B4          ; frame routine (sort, draw, pad, swap); one call per game tick
.definelabel DNGQ_SETVIEW, 0x80032B90          ; GsSetRefView2(GsRVIEW2 *)
.definelabel DNGQ_ACTIVEBUFF, 0x80040464          ; GsGetActiveBuff()
.definelabel DNGQ_PADREAD, 0x80025140          ; pad read (a0 = 1) -> held buttons
.definelabel DNGQ_DOORANIM, 0x80067AE4          ; door opening animation step
.definelabel DNG_QOL_ADDR, 0x800A1600          ; extension behind dng/vwf_script.asm glue (ends ~0x800A14C8),
                                                ; still inside the last loaded sector (ends 0x800A1BC4)

;; frame routine start: GsSetRefView2(player struct + 0x1580) -> subframes first (delay slot kept)
.org 0x800659F4
    jal     dngq_view_hook

;; HUD animation counter 0x800A0E30 (gated on the play clock): real frames only (delay slot kept)
.org 0x80065FE8
    j       dngq_gate_hud

;; door animation step: real frames only (delay slot kept)
.org 0x80066AC4
    jal     dngq_gate_door

;; pulsing ambient light (0x80099C54/56) and flash countdown (0x80099C5A): real frames only
.org 0x80066AF8
    j       dngq_gate_light

;; texture scroll toggle 0x80099E6C + 4 x 0x8006774C: real frames only
.org 0x80066BD4
    j       dngq_gate_anim
    nop                                         ; was lhu v0, -0x6194(v0) (done in the gate)

;; frame routine tail: DrawSync(0); VSync(3); clock(3); rand()
.org 0x80067574
    jal     dngq_frame_sync
    nop
    nop                                         ; was jal DNG_PLAY_CLOCK
    nop                                         ; was li a0, 3
    nop                                         ; was jal DNGQ_RAND (result unused, it only stirs the RNG)

;; pad read: subframes return the previous held buttons (no edges lost or doubled; delay slot kept)
.org 0x80067640
    jal     dngq_gate_pad

.org DNG_QOL_ADDR
.area 0x5C0

;; ---- vblank pacing: real frame = original VSync(3) + clock(3) + rand(); subframe k waits for T + k
dngq_frame_sync:
    addiu   sp, sp, -0x20
    sw      ra, 0x18(sp)
    sw      s0, 0x14(sp)
    jal     DNGQ_VSYNC                          ; cost = vblanks since this frame started + 1
    li      a0, -1
    la      t0, dngq_vars
    lw      t1, 0xC(t0)
    nop
    subu    t1, v0, t1
    addiu   t1, t1, 1
    sw      t1, 0x50(t0)
    lbu     t1, 0(t0)                           ; dngq_sub
    lw      s0, 4(t0)                           ; T = vblank count of the last real frame
    beqz    t1, @@real
    nop
    lw      t2, 8(t0)                           ; k
    b       @@wait
    addu    s0, s0, t2
@@real:
    addiu   s0, s0, 3
@@wait:
    jal     DNGQ_VSYNC
    li      a0, -1
    subu    t0, v0, s0
    bgez    t0, @@done
    nop
    jal     DNGQ_VSYNC
    li      a0, 0
    b       @@wait
    nop
@@done:
    la      t0, dngq_vars
    lbu     t1, 0(t0)
    nop
    bnez    t1, @@ret
    nop
    sw      v0, 4(t0)                           ; T = now
    jal     DNG_PLAY_CLOCK
    li      a0, 3
    jal     DNGQ_RAND
    nop
@@ret:
    lw      ra, 0x18(sp)
    lw      s0, 0x14(sp)
    jr      ra
    addiu   sp, sp, 0x20

;; ---- a0 = GsRVIEW2 (vpx vpy vpz vrx vry vrz rz super) of this tick
dngq_view_hook:
    la      t0, dngq_vars
    lbu     t1, 0(t0)
    nop
    bnez    t1, @@direct                        ; inside a subframe: just set the view
    nop
    addiu   sp, sp, -0x30
    sw      ra, 0x28(sp)
    sw      s0, 0x10(sp)
    sw      s1, 0x14(sp)
    sw      s2, 0x18(sp)
    sw      s3, 0x1C(sp)
    move    s0, a0
    move    s1, t0
    lbu     t1, 1(s1)                           ; previous view valid?
    nop
    beqz    t1, @@store
    move    t3, zero                            ; t3 = OR of all differences
    ; eye (words 0..2): any jump above 200 = warp / floor change -> no interpolation
    move    t4, zero
@@eye:
    addu    t5, s0, t4
    lw      t6, 0(t5)
    addu    t7, s1, t4
    lw      t7, 0x10(t7)                        ; prev
    nop
    subu    t6, t6, t7
    or      t3, t3, t6
    bgez    t6, @@pos
    nop
    negu    t6, t6
@@pos:
    slti    t6, t6, 201                         ; eye moves 30 (step) / <= 40 (turn) per tick; a cell is 300
    beqz    t6, @@store
    addiu   t4, t4, 4
    slti    t6, t4, 12
    bnez    t6, @@eye
    nop
    ; look-at (words 3..5) only counts as change; rz / super (words 6, 7) must be equal
@@ref:
    addu    t5, s0, t4
    lw      t6, 0(t5)
    addu    t7, s1, t4
    lw      t7, 0x10(t7)
    nop
    subu    t6, t6, t7
    addiu   t4, t4, 4
    slti    t5, t4, 24
    bnez    t5, @@ref
    or      t3, t3, t6
    lw      t6, 0x18(s0)
    lw      t7, 0x28(s1)
    lw      t8, 0x1C(s0)
    lw      t9, 0x2C(s1)
    bne     t6, t7, @@store
    nop
    bne     t8, t9, @@store
    nop
    beqz    t3, @@store                         ; camera did not move: nothing to interpolate
    nop
    lw      t0, 0x50(s1)                        ; a frame must fit in one vblank (tick = 3 vblanks)
    nop
    slti    t0, t0, 2
    beqz    t0, @@store
    nop
    ; keep the real view, draw subframes k = 1, 2
    move    t4, zero
@@save:
    addu    t5, s0, t4
    lw      t6, 0(t5)
    addu    t7, s1, t4
    sw      t6, 0x30(t7)                        ; cur
    addiu   t4, t4, 4
    slti    t5, t4, 32
    bnez    t5, @@save
    nop
    li      s2, 1
@@sub:
    jal     DNGQ_VSYNC
    li      a0, -1
    lw      t0, 4(s1)
    nop
    addu    t0, t0, s2
    subu    t0, v0, t0
    bgez    t0, @@next                          ; already late for this subframe: skip it
    nop
    move    t4, zero
@@lerp:
    addu    t7, s1, t4
    lw      t5, 0x10(t7)                        ; prev
    lw      t6, 0x30(t7)                        ; cur
    nop
    subu    t6, t6, t5
    mult    t6, s2
    mflo    t6
    li      t8, 3
    nop
    div     t6, t8
    mflo    t6
    addu    t6, t5, t6
    addu    t7, s0, t4
    sw      t6, 0(t7)
    addiu   t4, t4, 4
    slti    t5, t4, 24
    bnez    t5, @@lerp
    nop
    sw      s2, 8(s1)                           ; k
    jal     DNGQ_VSYNC
    li      a0, -1
    sw      v0, 0xC(s1)                         ; frame start
    li      t1, 1
    jal     DNGQ_FRAME
    sb      t1, 0(s1)                           ; dngq_sub = 1
    sb      zero, 0(s1)
@@next:
    addiu   s2, s2, 1
    slti    t0, s2, 3
    bnez    t0, @@sub
    nop
    move    t4, zero                            ; restore the real view
@@restore:
    addu    t7, s1, t4
    lw      t6, 0x30(t7)
    addu    t5, s0, t4
    sw      t6, 0(t5)
    addiu   t4, t4, 4
    slti    t5, t4, 32
    bnez    t5, @@restore
    nop
    jal     DNGQ_ACTIVEBUFF                     ; the subframes swapped buffers: refresh the index
    nop
    lui     at, 0x800A
    sw      v0, 0x388(at)
@@store:
    move    t4, zero                            ; prev = this tick's view
@@copy:
    addu    t5, s0, t4
    lw      t6, 0(t5)
    addu    t7, s1, t4
    sw      t6, 0x10(t7)
    addiu   t4, t4, 4
    slti    t5, t4, 32
    bnez    t5, @@copy
    nop
    li      t1, 1
    sb      t1, 1(s1)
    jal     DNGQ_VSYNC
    li      a0, -1
    sw      v0, 0xC(s1)                         ; start of the real frame
    jal     DNGQ_SETVIEW
    move    a0, s0
    lw      ra, 0x28(sp)
    lw      s0, 0x10(sp)
    lw      s1, 0x14(sp)
    lw      s2, 0x18(sp)
    lw      s3, 0x1C(sp)
    jr      ra
    addiu   sp, sp, 0x30
@@direct:
    j       DNGQ_SETVIEW
    nop

;; ---- side-effect gates (only at is used; the original registers are kept)
dngq_gate_hud:                                  ; was bnez a0, 0x80066088
    lui     at, hi(dngq_vars)
    lbu     at, lo(dngq_vars)(at)
    nop
    bnez    at, @@skip
    nop
    bnez    a0, @@skip
    nop
    j       0x80065FF0
    nop
@@skip:
    j       0x80066088
    nop

dngq_gate_door:                                 ; was jal DNGQ_DOORANIM
    lui     at, hi(dngq_vars)
    lbu     at, lo(dngq_vars)(at)
    nop
    bnez    at, @@ret
    nop
    j       DNGQ_DOORANIM
    nop
@@ret:
    jr      ra
    nop

dngq_gate_light:                                ; was beqz v1, 0x80066B60 (pulse), flash block follows at B60
    lui     at, hi(dngq_vars)
    lbu     at, lo(dngq_vars)(at)
    nop
    bnez    at, @@skip
    nop
    beqz    v1, @@flash
    nop
    j       0x80066B00
    nop
@@flash:
    j       0x80066B60
    nop
@@skip:
    j       0x80066BC0
    nop

dngq_gate_anim:                                 ; was lui v0, 0x800A; lhu v0, -0x6194(v0)
    lui     at, hi(dngq_vars)
    lbu     at, lo(dngq_vars)(at)
    nop
    bnez    at, @@skip
    lui     v0, 0x800A
    j       0x80066BDC
    lhu     v0, -0x6194(v0)
@@skip:
    j       0x80066C38
    nop

dngq_gate_pad:                                  ; was jal DNGQ_PADREAD
    lui     at, hi(dngq_vars)
    lbu     at, lo(dngq_vars)(at)
    nop
    bnez    at, @@old
    nop
    j       DNGQ_PADREAD
    nop
@@old:
    lui     v0, 0x800A
    lw      v0, 0x10D8(v0)
    lui     at, 7
    addu    at, v0, at
    lw      v0, -0x1AFC(at)                     ; held buttons of the last real read
    jr      ra
    nop

.align 4
dngq_vars:
    .byte 0                                     ; +0 dngq_sub: 1 while a subframe is drawn
    .byte 0                                     ; +1 previous view valid
    .byte 0, 0
    .word 0                                     ; +4 T: vblank count of the last real frame
    .word 0                                     ; +8 k of the subframe being drawn
    .word 0                                     ; +C vblank count when the current frame started
    .fill 32, 0                                 ; +0x10 previous tick's view (GsRVIEW2)
    .fill 32, 0                                 ; +0x30 this tick's view while subframes are drawn
    .word 3                                     ; +0x50 measured frame cost (vblanks), start pessimistic
.endarea
