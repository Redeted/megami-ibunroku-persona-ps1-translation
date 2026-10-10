;; =============================================================
;; QoL (separate enhancement build, `python tools/build.py --qol`): S2D.BIN 3D overworld at 60 fps,
;; "approach B" (qol/README.md): the game logic is untouched and still runs at 15 Hz (main loop: update
;; 0x8008F91C, then the draw tick 0x8008FA08 which ends in the render routine 0x8008A438 with VSync(4)).
;; Before the real draw tick, up to three extra draw ticks are made with the camera view, the map
;; transform and the two root transforms interpolated at 1/4, 2/4, 3/4 between the previous tick and this
;; one (s2dq_sub set). Per-frame side effects (pad read, play clock, frame counter, idle animation and its
;; rand(), banner angle, upload queue) run on real ticks only. Late subframes are skipped.
;; =============================================================
.definelabel S2D_VSYNC_FN, 0x80025C98
.definelabel S2D_PLAY_CLOCK, 0x800978E0          ; play time += a0 ticks
.definelabel S2D_DRAW_TICK, 0x8008FA08          ; draw tick (sort 3D, HUD, render + VSync(4))
.definelabel S2DQ_BUILD, 0x8008DEA0          ; build a transform: (VECTOR *pos, SVECTOR *rot, VECTOR *scale, out)
.definelabel S2DQ_PADREAD, 0x8008E6F4          ; pad read + edges + key repeat
.definelabel S2DQ_UPLOADQ, 0x80093BBC          ; one-shot image upload queue
.definelabel S2D_QOL_ADDR, 0x800BB5D0          ; behind the S2D VWF glue data (ends 0x800BB5C1), inside the last
                                                ; loaded sector (ends 0x800BBBC4); nothing else uses this RAM

;; main loop: update; draw tick -> subframes, then the real draw tick (delay slot nop kept)
.org 0x8008B77C
    jal     s2dq_tick

;; root transform build in the step / position tick: remember its position input (delay slot kept)
.org 0x8008B4F4
    jal     s2dq_rec_root

;; render routine: VSync(s4) / play clock(s4) / frame counter / pad / upload queue
.org 0x8008AF68
    jal     s2dq_vsync                          ; delay slot keeps move a0, s4
.org 0x8008AF80
    jal     s2dq_gate_upload                    ; delay slot keeps move s1, zero
.org 0x8008AF88
    jal     s2dq_gate_pad
.org 0x8008B0C4
    jal     s2dq_gate_ctr                       ; was addiu v1, v1, 1 (delay slot keeps lui at, 0x800C)
.org 0x8008B0D0
    jal     s2dq_clock                          ; delay slot keeps move a0, s4

;; player idle animation counter + rand(): real ticks only
.org 0x8008EE40
    j       s2dq_gate_idle
    nop                                         ; was lw v0, 0x5710(v0) (done in the gate)

;; banner angle += 0xF0 per draw: real ticks only
.org 0x80093E20
    jal     s2dq_gate_banner                    ; was addiu v0, v0, 0xF0 (delay slot keeps lui at, 0x800C)

.org S2D_QOL_ADDR
.area 0x5F4                                     ; up to the end of the last loaded sector

;; ---- draw-tick driver
s2dq_tick:
    addiu   sp, sp, -0x30
    sw      ra, 0x28(sp)
    sw      s1, 0x14(sp)
    sw      s2, 0x18(sp)
    sw      s3, 0x1C(sp)
    la      s1, s2dq_vars
    ; snapshot this tick: words -> cur_w, halfwords -> cur_h
    la      t0, s2dq_wtab
    move    t1, zero
@@snapw:
    addu    t2, t0, t1
    lw      t2, 0(t2)
    addu    t3, s1, t1
    lw      t2, 0(t2)
    nop
    sw      t2, 0x64(t3)                        ; cur_w
    addiu   t1, t1, 4
    slti    t2, t1, 60
    bnez    t2, @@snapw
    nop
    la      t0, s2dq_htab
    move    t1, zero
@@snaph:
    sll     t2, t1, 1
    addu    t2, t0, t2
    lw      t2, 0(t2)
    addu    t3, s1, t1
    lhu     t2, 0(t2)
    nop
    sh      t2, 0xA0(t3)                        ; cur_h
    addiu   t1, t1, 2
    slti    t2, t1, 18
    bnez    t2, @@snaph
    nop
    lui     t4, 0x800B                          ; a new step started (remaining 0x800B144C went up): the map
    lh      t4, 0x144C(t4)                      ; was re-centred on the new cell, which moved the root by the
    lh      t5, 2(s1)                           ; step vector 0x800B143C -> move the previous root position
    sh      t4, 2(s1)                           ; by it too, so the in-between frames continue smoothly
    slt     t6, t5, t4
    beqz    t6, @@noshift
    lui     t4, 0x800B
    addiu   t4, t4, 0x143C
    addiu   t3, s1, 0x14 + 36                   ; prev root position (words 9..11)
    addiu   t1, t3, 8
@@shift:
    lw      t5, 0(t4)
    lw      t6, 0(t3)
    addiu   t4, t4, 4
    addu    t6, t6, t5
    sw      t6, 0(t3)
    bne     t3, t1, @@shift
    addiu   t3, t3, 4
@@noshift:
    lbu     t0, 1(s1)                           ; prev valid?
    nop
    beqz    t0, @@store
    move    t9, zero                            ; t9 = OR of all differences
    move    t1, zero                            ; words: jump above 480 -> no interpolation (a step moves the
                                                ; root 160 / 320 per tick; a new step re-centres the map: 640)
@@chkw:
    addu    t3, s1, t1
    lw      t4, 0x64(t3)
    lw      t5, 0x14(t3)                        ; prev_w
    nop
    subu    t4, t4, t5
    or      t9, t9, t4
    bgez    t4, @@posw
    nop
    negu    t4, t4
@@posw:
    slti    t4, t4, 481
    beqz    t4, @@store
    addiu   t1, t1, 4
    slti    t2, t1, 60
    bnez    t2, @@chkw
    nop
    move    t1, zero                            ; halfword angles: wrap, jump above 0x300 -> no interpolation
@@chkh:
    addu    t3, s1, t1
    lhu     t4, 0xA0(t3)
    lhu     t5, 0x50(t3)                        ; prev_h
    nop
    subu    t4, t4, t5
    addiu   t4, t4, 0x800
    andi    t4, t4, 0xFFF
    addiu   t4, t4, -0x800
    or      t9, t9, t4
    bgez    t4, @@posh
    nop
    negu    t4, t4
@@posh:
    slti    t4, t4, 0x301
    beqz    t4, @@store
    addiu   t1, t1, 2
    slti    t2, t1, 18
    bnez    t2, @@chkh
    nop
    beqz    t9, @@store                         ; nothing moved
    nop
    lw      s3, 0x10(s1)                        ; draw cost in vblanks (measured by s2dq_vsync)
    li      s2, 1                               ; subframes k = 1..3
@@sub:
    slti    t0, s3, 2
    bnez    t0, @@try                           ; cost 1: k = 1, 2, 3 (60 fps)
    li      t0, 2
    bne     s3, t0, @@next                      ; cost 3+: none (15 fps)
    nop
    bne     s2, t0, @@next                      ; cost 2: k = 2 only (30 fps)
    nop
@@try:
    jal     S2D_VSYNC_FN
    li      a0, -1
    lw      t0, 4(s1)
    nop
    addu    t0, t0, s2
    subu    t0, v0, t0
    bgez    t0, @@next                          ; already late for this subframe
    nop
    jal     s2dq_apply                          ; write the lerped state (a0 = k)
    move    a0, s2
    sw      s2, 8(s1)
    jal     S2D_VSYNC_FN
    li      a0, -1
    sw      v0, 0xC(s1)                         ; draw start
    li      t0, 1
    jal     S2D_DRAW_TICK
    sb      t0, 0(s1)                           ; s2dq_sub = 1
    sb      zero, 0(s1)
@@next:
    addiu   s2, s2, 1
    slti    t0, s2, 4
    bnez    t0, @@sub
    nop
    jal     s2dq_apply                          ; k = 4: back to the real state
    li      a0, 4
@@store:
    move    t1, zero                            ; prev = cur (words + halfwords, one block)
@@cp:
    addu    t3, s1, t1
    lw      t4, 0x64(t3)
    addiu   t1, t1, 4
    sw      t4, 0x14(t3)
    slti    t2, t1, 80
    bnez    t2, @@cp
    nop
    li      t0, 1
    sb      t0, 1(s1)
    jal     S2D_VSYNC_FN
    li      a0, -1
    sw      v0, 0xC(s1)                         ; draw start of the real tick
    lw      ra, 0x28(sp)
    lw      s1, 0x14(sp)
    lw      s2, 0x18(sp)
    lw      s3, 0x1C(sp)
    j       S2D_DRAW_TICK                           ; the real draw tick
    addiu   sp, sp, 0x30

;; a0 = k (1..4): state = prev + (cur - prev) * k / 4, then rebuild the two root transforms
s2dq_apply:
    addiu   sp, sp, -0x20
    sw      ra, 0x18(sp)
    la      t6, s2dq_vars
    la      t7, s2dq_wtab
    li      t8, 4
    move    t1, zero
@@lw:
    addu    t3, t6, t1
    lw      t4, 0x64(t3)                        ; cur
    lw      t5, 0x14(t3)                        ; prev
    addu    t2, t7, t1
    lw      t2, 0(t2)                           ; target address
    beq     a0, t8, @@wst                       ; k = 4: the exact real value
    subu    t0, t4, t5
    mult    t0, a0
    mflo    t0
    sra     t0, t0, 2
    addu    t4, t5, t0
@@wst:
    sw      t4, 0(t2)
    addiu   t1, t1, 4
    slti    t2, t1, 60
    bnez    t2, @@lw
    nop
    la      t7, s2dq_htab
    move    t1, zero
@@lh:
    addu    t3, t6, t1
    lhu     t4, 0xA0(t3)                        ; cur
    lhu     t5, 0x50(t3)                        ; prev
    sll     t2, t1, 1
    addu    t2, t7, t2
    lw      t2, 0(t2)                           ; target address
    beq     a0, t8, @@hst                       ; k = 4: the exact real value
    subu    t0, t4, t5
    addiu   t0, t0, 0x800                       ; shortest way round (angles are 4096 per turn)
    andi    t0, t0, 0xFFF
    addiu   t0, t0, -0x800
    mult    t0, a0
    mflo    t0
    sra     t0, t0, 2
    addu    t4, t5, t0
@@hst:
    sh      t4, 0(t2)
    addiu   t1, t1, 2
    slti    t2, t1, 18
    bnez    t2, @@lh
    nop
    la      a0, s2dq_rootpos                    ; root: (pos, 0x800B152C, 0x800B1544) -> 0x800B14DC
    lui     a1, 0x800B
    addiu   a1, a1, 0x152C
    lui     a2, 0x800B
    addiu   a2, a2, 0x1544
    lui     a3, 0x800B
    jal     S2DQ_BUILD
    addiu   a3, a3, 0x14DC
    lui     a0, 0x800B                          ; second root: (0x800B14BC, 0x800B14B4, 0x800B14CC) -> 0x800B1464
    addiu   a0, a0, 0x14BC
    lui     a1, 0x800B
    addiu   a1, a1, 0x14B4
    lui     a2, 0x800B
    addiu   a2, a2, 0x14CC
    lui     a3, 0x800B
    jal     S2DQ_BUILD
    addiu   a3, a3, 0x1464
    lw      ra, 0x18(sp)
    nop
    jr      ra
    addiu   sp, sp, 0x20

;; root build in the position tick: keep a copy of the position vector, then build as before
s2dq_rec_root:
    la      t0, s2dq_rootpos
    lw      t1, 0(a0)
    lw      t2, 4(a0)
    lw      t3, 8(a0)
    sw      t1, 0(t0)
    sw      t2, 4(t0)
    j       S2DQ_BUILD
    sw      t3, 8(t0)

;; VSync(s4): mode 4 = 15 Hz main mode -> real tick waits for T + 4, subframe k for T + k
s2dq_vsync:
    li      t0, 4
    bne     a0, t0, @@orig
    nop
    addiu   sp, sp, -0x20
    sw      ra, 0x18(sp)
    sw      s0, 0x14(sp)
    jal     S2D_VSYNC_FN                        ; cost = vblanks since the draw started + 1
    li      a0, -1
    la      t0, s2dq_vars
    lw      t1, 0xC(t0)
    nop
    subu    t1, v0, t1
    addiu   t1, t1, 1                           ; always >= 1
    sw      t1, 0x10(t0)
    lbu     t1, 0(t0)
    lw      s0, 4(t0)
    beqz    t1, @@real
    nop
    lw      t2, 8(t0)
    b       @@wait
    addu    s0, s0, t2
@@real:
    addiu   s0, s0, 4
@@wait:
    jal     S2D_VSYNC_FN
    li      a0, -1
    subu    t0, v0, s0
    bgez    t0, @@done
    nop
    jal     S2D_VSYNC_FN
    li      a0, 0
    b       @@wait
    nop
@@done:
    la      t0, s2dq_vars
    lbu     t1, 0(t0)
    nop
    bnez    t1, @@ret
    nop
    sw      v0, 4(t0)                           ; T = now
@@ret:
    lw      ra, 0x18(sp)
    lw      s0, 0x14(sp)
    jr      ra
    addiu   sp, sp, 0x20
@@orig:
    j       S2D_VSYNC_FN
    nop

;; calls skipped in subframes: play clock(s4), pad read, upload queue (t1 = the original function)
s2dq_clock:
    lui     t1, hi(S2D_PLAY_CLOCK)
    b       s2dq_gate_call
    addiu   t1, t1, lo(S2D_PLAY_CLOCK)
s2dq_gate_pad:
    lui     t1, hi(S2DQ_PADREAD)
    b       s2dq_gate_call
    addiu   t1, t1, lo(S2DQ_PADREAD)
s2dq_gate_upload:
    lui     t1, hi(S2DQ_UPLOADQ)
    addiu   t1, t1, lo(S2DQ_UPLOADQ)
s2dq_gate_call:
    lui     t0, hi(s2dq_vars)
    lbu     t0, lo(s2dq_vars)(t0)
    nop
    bnez    t0, @@ret
    nop
    jr      t1
    nop
@@ret:
    jr      ra
    nop

s2dq_gate_ctr:                                  ; frame counter 0x800B8D60 (v1) += 1 on real ticks; at is live
    lui     t9, hi(s2dq_vars)
    lbu     t9, lo(s2dq_vars)(t9)
    nop
    bnez    t9, @@ret
    nop
    addiu   v1, v1, 1
@@ret:
    jr      ra
    nop

s2dq_gate_banner:                               ; v0 += 0xF0 on real ticks; at is live
    lui     t9, hi(s2dq_vars)
    lbu     t9, lo(s2dq_vars)(t9)
    nop
    bnez    t9, @@ret
    nop
    addiu   v0, v0, 0xF0
@@ret:
    jr      ra
    nop

s2dq_gate_idle:                                 ; was lui v0, 0x800A; lw v0, 0x5710(v0)
    lui     at, hi(s2dq_vars)
    lbu     at, lo(s2dq_vars)(at)
    nop
    bnez    at, @@skip
    lui     v0, 0x800A
    j       0x8008EE48
    lw      v0, 0x5710(v0)
@@skip:
    j       0x8008EFEC
    nop

.align 4
;; interpolated state: 15 words (view eye / look-at, map position, root position, second root position)
s2dq_wtab:
    .word 0x800B1574, 0x800B1578, 0x800B157C, 0x800B1580, 0x800B1584, 0x800B1588
    .word 0x800B1048, 0x800B104C, 0x800B1050
    .word s2dq_rootpos, s2dq_rootpos + 4, s2dq_rootpos + 8
    .word 0x800B14BC, 0x800B14C0, 0x800B14C4
;; 9 halfword angles (map rotation incl. the rendered heading, root rotation, second root rotation)
s2dq_htab:
    .word 0x800B1040, 0x800B1042, 0x800B1044
    .word 0x800B152C, 0x800B152E, 0x800B1530
    .word 0x800B14B4, 0x800B14B6, 0x800B14B8
s2dq_rootpos:
    .word 0, 0, 0                               ; last position input of the root transform
s2dq_vars:
    .byte 0                                     ; +0 s2dq_sub
    .byte 0                                     ; +1 prev valid
    .halfword 0                                 ; +2 step remaining of the previous tick
    .word 0                                     ; +4 T: vblank count of the last real tick
    .word 0                                     ; +8 k
    .word 0                                     ; +0xC vblank count when the current draw started
    .word 4                                     ; +0x10 measured draw cost (vblanks), start pessimistic
    .fill 60, 0                                 ; +0x14 prev words
    .fill 20, 0                                 ; +0x50 prev halfwords (18 + pad)
    .fill 60, 0                                 ; +0x64 cur words
    .fill 20, 0                                 ; +0xA0 cur halfwords (18 + pad)
.endarea
