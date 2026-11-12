;; =============================================================
;; BTLP.BIN - battle fast-forward ("skip"), toggled with START (2026-11-12)
;;
;; The PSP version lets START skip the battle animations. Here START (while the turn plays, phase != 0) toggles a
;; fast-forward: the battle runs SKIP_RATE logic ticks per displayed frame, so every animation (party, enemies,
;; Persona summons, skill effects, damage numbers) plays faster (about 2x, GPU bound) with the battle logic untouched.
;; It ends by itself when the command menu comes back for input (phase 0 with AUTO off: end of the turn, or AUTO stopped); START again
;; turns it off earlier. A small ">>" icon (two flat triangles, top right) shows while it is on.
;;
;; How: the main loop runs one tick and calls the frame function 0x80080F14 (also called from ~280 scripted
;; sequences). While the fast-forward is on, every tick still runs the whole frame (draw pass, DrawSync, PutDrawEnv,
;; DrawOTag); only every SKIP_RATE-th tick waits for VSync and flips the display (PutDispEnv). The hidden ticks draw
;; into the back buffer: the buffer index is swapped only before a shown tick, so the shown tick displays the last
;; finished frame. History (2026-11-12): skipping the draw pass froze the animations (they advance inside it,
;; 0x80082718 object handlers); running the draw pass but skipping the GPU submit lost the text sprites and the ">>"
;; of the last OT entry (skill-name banner empty, user report); drawing every tick fixes both.
;; Measured (QoL disc, emulator): user's slot 5 Persona turn, results after 2641 -> 1600 vblanks; slot 7 enemy
;; melee + spell rounds 0.55 -> 1.07 ticks per vblank (GPU bound). New button presses of hidden ticks are kept and
;; handed to the next shown tick. The results window (0x80098CF4) turns the fast-forward off.
;;
;; The frame function (-O0 code, 0x80080F14..0x8008136B) is rewritten compactly with the same calls in the same
;; order; the skip code and data use the room this frees. Nothing jumps into the old body (only jal 0x80080F14).
;; QoL build only (.ifdef QOL60 below); the normal build keeps the original frame function. The QoL double-speed
;; effects (qol/battle_speed_btlp.asm: no second VSync in the half-rate mode) are built in: the rewrite has only the
;; one VSync. START is read elsewhere in BTLP only by debug code (0x80055C10 set).
;; =============================================================

SKIP_RATE       equ 4                   ; ticks per displayed frame while the fast-forward is on
SKIP_BUTTON     equ 0x0800              ; START (pad word 0x800F88E8 held / 0x800F88F0 new)
BTL_PHASE       equ -0xF95              ; 0x800CF06B (from 0x800D0000): battle phase, 0 = command menu
BTL_AUTO        equ 0x2250              ; 0x800D2250: AUTO mode (0 off; Cross clears it; phase 0 also passes between AUTO rounds)
SKIP_ON         equ 0                   ; skip_vars: u8 fast-forward on
SKIP_CNT        equ 1                   ; u8 ticks since the last shown one
SKIP_HIDE       equ 2                   ; u8 this tick is not drawn
SKIP_LATCH      equ 4                   ; u16 new presses of hidden ticks

SKIP_X          equ 296
SKIP_Y          equ 10
SKIP_COLOR      equ 0x20F0F0F0          ; POLY_F3, light grey
.macro skip_tri, dx
    .word   0
    .word   SKIP_COLOR
    .word   ((SKIP_Y) << 16) | (SKIP_X + dx)
    .word   ((SKIP_Y + 12) << 16) | (SKIP_X + dx)
    .word   ((SKIP_Y + 6) << 16) | (SKIP_X + dx + 9)
.endmacro

.ifdef QOL60                            ; QoL build only (equ / macro above: armips allows none inside .ifdef)
.org 0x80080F14
.area 0x8008136C - 0x80080F14, 0
btl_frame:
    addiu   sp, sp, -0x20
    sw      ra, 0x1C(sp)
    sw      s1, 0x14(sp)
    jal     0x8008EA70
    sw      s0, 0x18(sp)
    jal     0x8008F05C
    lui     s0, 0x800D                  ; s0 = 0x800D0000 (battle globals)
    lbu     v0, -0xF6D(s0)
    nop
    beqz    v0, @@no_snd
    ori     a1, zero, 0x3E8
    jal     0x8001950C
    ori     a0, zero, 4
    ori     a0, zero, 0x7F
    jal     0x8001B6DC
    ori     a1, zero, 0x7F
    ori     a0, zero, 0x38
    jal     0x8001B06C
    ori     a1, zero, 0x38
    jal     0x80018E2C
    nop
    lui     v0, 0x8010
    lbu     v0, -0x7F7C(v0)
    lui     at, 0x800D
    addu    at, at, v0
    lbu     v1, 0x7A08(at)
    ori     v0, zero, 3
    move    a0, zero
    bne     v1, v0, @@snd_call
    move    a1, zero
    ori     a1, zero, 2
@@snd_call:
    jal     0x80082310
    nop
    sb      zero, -0xF6D(s0)
    ori     a1, zero, 0x3E8
@@no_snd:
    lw      v1, -0xFE0(s0)
    jal     btl_buf                     ; keeps a1
    sw      v1, -0xF4C(s0)
    move    s1, v0                      ; s1 = draw buffer (the index changes only in the tail)
    ori     v1, zero, 0xD6C0
    jal     0x8002B99C                  ; (buffer + 0xD6C0, 1000)
    addu    a0, s1, v1
    jal     skip_tick               ; sets SKIP_HIDE; the draw pass below also runs on hidden ticks (it advances
    nop                             ; the model animations), only the GPU submit and the waits are skipped
    jal     0x8008B620
    nop
    jal     0x8008AF14
    nop
    jal     0x8008B230
    nop
    jal     0x8008B13C
    nop
    jal     0x80082718
    nop
    jal     skip_icon
    nop
    lbu     v0, -0xF8C(s0)
    nop
    bnez    v0, @@no_obj
    nop
    ori     v1, zero, 0xE65C
    jal     0x8006B8EC
    addu    a0, s1, v1
    ori     v1, zero, 0xE65C
    jal     0x80065E98
    addu    a0, s1, v1
    jal     0x800667BC
    nop
@@no_obj:
    lw      v1, -0xF68(s0)
    lbu     v0, -0xF0C(s0)
    lui     at, 1
    sb      v0, 0x6C(v1)
    addu    at, at, v1
    sb      v0, -0x1934(at)
    lbu     v0, -0xF0B(s0)
    nop
    beqz    v0, @@n1
    nop
    jal     0x8002B54C
    move    a0, zero
@@n1:
    lbu     v0, -0xF8C(s0)
    nop
    bnez    v0, @@n2
    nop
    lw      a1, -0xFC0(s0)
    jal     0x8002B810
    addiu   a0, s0, -0xEC4
@@n2:
    jal     0x8002B5E8                  ; DrawSync(0)
    move    a0, zero
    lbu     v0, -0xF0B(s0)
    nop
    beqz    v0, @@n3
    nop
    jal     0x8002B54C
    ori     a0, zero, 1
@@n3:
    lui     t1, hi(skip_vars)
    lbu     t1, lo(skip_vars + SKIP_HIDE)(t1)
    nop
    bnez    t1, @@no_disp               ; hidden tick: drawn into the back buffer, no VSync, no display flip
    nop
    jal     0x80025C98                  ; VSync(0)
    move    a0, zero
    jal     0x8002BD98                  ; PutDispEnv
    addiu   a0, s1, 0x5C
@@no_disp:
    jal     0x8002BBC0                  ; PutDrawEnv
    move    a0, s1
    ori     v1, zero, 0xD6C0
    jal     0x8002BB4C                  ; DrawOTag
    addu    a0, s1, v1
    jal     0x8008E980                  ; pad
    nop
    lui     at, 0x8010
    lhu     v1, -0x7710(at)             ; new presses
    lui     v0, 0x800F
    lhu     v0, 0x7E04(v0)
    nop
    and     v0, v1, v0
    beqz    v0, @@n5
    nop
    lbu     v0, -0xF92(s0)
    nop
    xori    v0, v0, 1
    sb      v0, -0xF92(s0)
@@n5:
    lbu     v0, -0xF05(s0)
    nop
    beqz    v0, @@n6
    ori     v0, v1, 0x20
    sh      v0, -0x7710(at)
@@n6:
    jal     skip_pad
    nop
    lh      v0, -0xFA8(s0)
    nop
    blez    v0, @@n7
    addiu   v0, v0, -1
    sh      v0, -0xFA8(s0)
@@n7:
    lui     t1, hi(skip_vars)
    lbu     t2, lo(skip_vars + SKIP_ON)(t1)
    lbu     t1, lo(skip_vars + SKIP_CNT)(t1)
    lhu     v0, -0xFA6(s0)              ; tick counter
    lbu     v1, -0xF08(s0)
    sb      zero, -0xF6B(s0)
    addiu   v0, v0, 1
    sh      v0, -0xFA6(s0)
    beqz    t2, @@swap                  ; fast-forward off: every tick is shown, swap every tick
    xori    t1, t1, SKIP_RATE - 1
    bnez    t1, @@noswap                ; on: swap only before a shown tick, so the hidden ticks draw into the
    nop                                 ; back buffer and the shown tick displays the last finished one
@@swap:
    xori    v1, v1, 1
    sb      v1, -0xF08(s0)
@@noswap:
    lw      ra, 0x1C(sp)
    lw      s1, 0x14(sp)
    lw      s0, 0x18(sp)
    jr      ra
    addiu   sp, sp, 0x20

;; v0 = current draw buffer: base (0x800CF098) + index (0x800CF0F8) * 0xE660. Clobbers v1, at (keeps a0-a3).
btl_buf:
    lui     at, 0x800D
    lbu     v0, -0xF08(at)
    lw      v1, -0xF68(at)
    ori     at, zero, 0xE660
    multu   v0, at
    mflo    v0
    jr      ra
    addu    v0, v0, v1

;; v0 = 1 when this tick is not drawn. Called after the OT clear of every frame.
skip_tick:
    la      t0, skip_vars
    lui     at, 0x800D
    lbu     v0, BTL_PHASE(at)
    lbu     v1, BTL_AUTO(at)
    lbu     t1, SKIP_ON(t0)             ; (loaded before the branch: a load in its delay slot would be read too
    or      v0, v0, v1                  ; early at @@turn, which made AUTO turn the fast-forward on silently)
    bnez    v0, @@turn
    lbu     v0, SKIP_CNT(t0)
    sb      zero, SKIP_ON(t0)           ; command menu without AUTO: the fast-forward ends with the turn / AUTO
    move    t1, zero
@@turn:
    beqz    t1, @@show
    addiu   v0, v0, 1
    sltiu   at, v0, SKIP_RATE
    beqz    at, @@show
    nop
    sb      v0, SKIP_CNT(t0)
    ori     v0, zero, 1
    jr      ra
    sb      v0, SKIP_HIDE(t0)
@@show:
    sb      zero, SKIP_CNT(t0)
    sb      zero, SKIP_HIDE(t0)
    jr      ra
    move    v0, zero

;; After the pad read: START toggles the fast-forward during a turn; new presses of hidden ticks are
;; collected and handed to the next shown tick.
skip_pad:
    la      t0, skip_vars
    lui     at, 0x8010
    lhu     v1, -0x7710(at)             ; new presses
    lui     v0, 0x800D
    lbu     a0, BTL_PHASE(v0)
    lbu     v0, BTL_AUTO(v0)
    nop
    or      v0, v0, a0
    andi    a0, v1, SKIP_BUTTON
    beqz    v0, @@keep                  ; command menu (no AUTO): START stays as it was
    nop
    beqz    a0, @@keep
    lbu     v0, SKIP_ON(t0)
    xori    v1, v1, SKIP_BUTTON         ; START consumed
    xori    v0, v0, 1
    sb      v0, SKIP_ON(t0)
@@keep:
    lbu     v0, SKIP_HIDE(t0)
    lhu     a0, SKIP_LATCH(t0)
    beqz    v0, @@flush
    or      a0, a0, v1
    sh      a0, SKIP_LATCH(t0)          ; hidden tick: keep them
    jr      ra
    sh      zero, -0x7710(at)
@@flush:
    sh      zero, SKIP_LATCH(t0)
    jr      ra
    sh      a0, -0x7710(at)             ; shown tick: everything since the last shown tick

;; ">>" icon while the fast-forward is on: two POLY_F3 per draw buffer, linked first into the OT entry of the
;; text sprites (buffer + 0xE65C).
skip_icon:
    la      t0, skip_vars
    lbu     v0, SKIP_ON(t0)
    lui     at, 0x800D
    beqz    v0, @@ret
    lbu     v1, -0xF08(at)
    ori     a0, zero, 0xE65C
    addu    a0, s1, a0                  ; a0 = OT entry (s1 = draw buffer, from btl_frame)
    la      a1, skip_prims
    sll     v0, v1, 5
    sll     v1, v1, 3
    addu    v0, v0, v1
    addu    a1, a1, v0                  ; a1 = first triangle (40 bytes per buffer)
    addiu   a2, a1, 20                  ; a2 = second
    lui     t1, 0x00FF
    ori     t1, t1, 0xFFFF
    lui     t2, 0x0400                  ; 4 words
    lw      v0, 0(a0)
    and     v1, a2, t1
    or      v1, v1, t2
    sw      v1, 0(a1)                   ; first -> second
    and     v1, v0, t1
    or      v1, v1, t2
    sw      v1, 0(a2)                   ; second -> old list
    nor     t1, t1, zero
    and     v0, v0, t1
    lui     t1, 0x00FF
    ori     t1, t1, 0xFFFF
    and     v1, a1, t1
    or      v0, v0, v1
    sw      v0, 0(a0)                   ; entry -> first
@@ret:
    jr      ra
    nop

.align 4
skip_vars:
    .byte   0, 0, 0, 0
    .halfword 0, 0

skip_prims:                             ; buffer 0, buffer 1
    skip_tri 0
    skip_tri 9
    skip_tri 0
    skip_tri 9
.endarea

;; Results window (0x80098CF4: opens the window, then frames until any new press): the fast-forward ends there, so
;; the ">>" icon is gone. s0 is saved by its prologue and set later; the called window functions keep it.
.org 0x80098D30
    lui     s0, hi(skip_vars)           ; delay slot of jal 0x800AB650 (was nop)
.org 0x80098D38
    sb      zero, lo(skip_vars + SKIP_ON)(s0) ; delay slot of jal 0x800A9CEC (was nop)
.endif                                  ; QOL60
