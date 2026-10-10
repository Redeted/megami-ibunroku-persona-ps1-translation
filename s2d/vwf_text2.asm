;; =============================================================
;; S2D.BIN - VWF for the overworld dialogue box (second text interpreter, 0x8009B2F4)
;;
;; The overworld party comments / door texts are NOT printed by the interpreter that vwf_hooks.asm patches (0x80066F9C...),
;; but by the generic "text object" interpreter 0x8009B2F4 (also used for the arrival banner and the area labels). Its objects
;; are a grid of 16x16 cells (+0x1D8 columns, +0x1DA rows), one 8-byte sprite record per cell at +0x1C, cell pixels
;; uploaded through the queue function 0x80098EC8 to VRAM (+0x1C4,+0x1C6) + cell. The dialogue box is the 15x3 object.
;;
;; Patches:
;;   * glyph decoder 0x8009AE50: only 80-87 are lead bytes of two-byte glyphs (result | 0x8000, like the other overlays),
;;     so 88-E6 pass as single bytes = English VWF characters.
;;   * the glyph function 0x8009AF6C (one call site, 0x8009BA0C) is replaced by s2d_txt_put: 15x3 objects go through the
;;     shared engine (vwf_dialog_emit with a private config), every other object keeps the original function.
;;   * s2d_txt_activate (engine callback): uploads the composed cell and creates / reuses the cell's sprite record.
;; The engine's pos = object +0x12 (state = object + 8); the interpreter's own scroll / page logic is unchanged.
;; Colours of this box: main 1, shadow 2 at (+1,+1) (set in vwf_dlg_state for the duration of the call).
;; Code and config live behind the English boxes in the extension of S2D.BIN (tools/s2dscript.py SPILL).
;; =============================================================

S2D_TXT_PUT_ORIG        equ 0x8009AF6C
S2D_TXT_UPLOAD          equ 0x80098EC8          ; (src, x, y, w, stack+0x10 = h): queue a LoadImage
S2D_TXT_ATTR            equ 0x8002DF60          ; (a0, a1) -> sprite attribute halfword
S2DT_STRUCT             equ 0x10                ; config: text object
S2DT_COUNT              equ 0x14                ; config: queued entry count
S2DT_ENTRY              equ 0x18                ; config: queue entry {u32 src; u16 x, y, w, h}

;; --- decoder: 80-87 = two-byte glyph (flagged 0x8000), everything else single ---
.org 0x8009AE58
    addiu   v0, v0, -0x80
    sltiu   v0, v0, 8
    bnez    v0, 0x8009AE70
.org 0x8009AE70
    lbu     v0, 0(a0)
    addiu   a0, a0, 1
    lbu     v1, 0(a0)
    ori     v0, v0, 0x80                ; was andi v0,v0,0x7F
.org 0x8009BA0C
    jal     s2d_txt_put                 ; was jal 0x8009AF6C

.org S2D_GLUE_ADDR
.area S2D_GLUE_SIZE

s2d_txt_put:
    lh      t0, 0x1D8(a0)
    li      t1, 15
    bne     t0, t1, @@orig
    lh      t0, 0x1DA(a0)
    li      t1, 3
    bne     t0, t1, @@orig
    nop
    addiu   sp, sp, -0x30
    sw      ra, 0x2C(sp)
    sw      s0, 0x28(sp)
    sw      s1, 0x24(sp)
    sw      s2, 0x20(sp)
    move    s0, a0                      ; s0 = text object
    sw      a1, 0x1C(sp)
    la      t0, s2d_txt_cfg
    addiu   t1, a0, 8
    sw      t1, 0(t0)                   ; engine state = object + 8 (pos at +0xA = object +0x12)
    sw      a0, S2DT_STRUCT(t0)
    sw      zero, S2DT_COUNT(t0)
    lhu     t2, 2(a0)
    nop                                 ; load delay
    andi    s1, t2, 0x100               ; s1 = 1-flag: glyph comes from the name buffer (pointer +8), else script (+0xC)
    bnez    s1, @@buf
    lw      s2, 0xC(a0)                 ; s2 = read pointer after the glyph
    j       @@go
    nop
@@buf:
    lw      s2, 8(a0)
@@go:
    la      t0, vwf_dlg_state
    li      t1, 1
    sb      t1, 8(t0)                   ; main colour
    li      t1, 2
    sb      t1, 9(t0)                   ; shadow colour
    li      t1, 1
    sb      t1, 10(t0)                  ; shadow offset x
    la      a0, s2d_txt_cfg
    li      a1, 0
    jal     vwf_dialog_emit
    lw      a2, 0x1C(sp)
    la      t0, vwf_dlg_state
    li      t1, 2
    sb      t1, 8(t0)
    li      t1, 1
    sb      t1, 9(t0)
    li      t1, 2
    sb      t1, 10(t0)
    beqz    s1, @@script
    nop
    lw      t0, 8(s0)                   ; name buffer: rewound = the engine handed the glyph back
    nop
    beq     t0, s2, @@ret
    nop
    addiu   t0, t0, -2
    j       @@ret
    sw      t0, 8(s0)
@@script:
    sw      s2, 0xC(s0)
@@ret:
    lw      ra, 0x2C(sp)
    lw      s0, 0x28(sp)
    lw      s1, 0x24(sp)
    lw      s2, 0x20(sp)
    jr      ra
    addiu   sp, sp, 0x30
@@orig:
    andi    a1, a1, 0x7FFF              ; flagged two-byte glyph -> original glyph index
    j       S2D_TXT_PUT_ORIG
    nop

;; s2d_txt_activate(a0 = cell P): upload the composed cell, make sure cell P has a sprite record
s2d_txt_activate:
    addiu   sp, sp, -0x38
    sw      ra, 0x34(sp)
    sw      s0, 0x30(sp)
    sw      s1, 0x2C(sp)
    sw      s2, 0x28(sp)
    sw      s3, 0x24(sp)
    move    s3, a0                      ; P
    la      s0, s2d_txt_cfg
    lw      s1, S2DT_STRUCT(s0)         ; text object
    li      t0, 15
    divu    s3, t0
    mflo    t1                          ; row
    mfhi    t2                          ; col
    lw      a0, S2DT_ENTRY(s0)          ; src: ring cell queued by the engine
    lh      t3, 0x1C4(s1)
    sll     t4, t2, 2
    addu    a1, t3, t4                  ; x (16-bit units)
    lh      t3, 0x1C6(s1)
    sll     t4, t1, 4
    addu    a2, t3, t4                  ; y
    li      a3, 4
    li      t3, 16
    jal     S2D_TXT_UPLOAD
    sw      t3, 0x10(sp)
    sw      zero, S2DT_COUNT(s0)
    li      t0, 15
    divu    s3, t0
    mflo    t1
    mfhi    t2
    sll     t5, t2, 4                   ; x px
    sll     t6, t1, 4                   ; y px
    lhu     t7, 6(s1)                   ; sprite count
    move    t8, zero
    addiu   t9, s1, 0x1C
@@find:
    beq     t8, t7, @@append
    nop
    lh      t3, 4(t9)
    lh      t4, 6(t9)
    bne     t3, t5, @@next
    nop
    beq     t4, t6, @@done              ; the cell already has its record
    nop
@@next:
    addiu   t8, t8, 1
    j       @@find
    addiu   t9, t9, 8
@@append:
    sh      t5, 4(t9)
    sh      t6, 6(t9)
    lh      t3, 0x1C4(s1)
    lh      t4, 0x1C6(s1)
    andi    t3, t3, 63
    andi    t4, t4, 0xFF
    sll     t3, t3, 2
    addu    t3, t3, t5
    sb      t3, 0(t9)                   ; u
    addu    t4, t4, t6
    sb      t4, 1(t9)                   ; v
    sw      t9, 0x20(sp)
    lh      a0, 0x1C8(s1)
    lh      a1, 0x1CA(s1)
    lh      t0, 0x10(s1)
    nop                                 ; load delay
    addu    a1, a1, t0
    jal     S2D_TXT_ATTR
    nop
    lw      t9, 0x20(sp)
    lhu     t0, 6(s1)
    sh      v0, 2(t9)
    addiu   t0, t0, 1
    sh      t0, 6(s1)
@@done:
    lw      ra, 0x34(sp)
    lw      s0, 0x30(sp)
    lw      s1, 0x2C(sp)
    lw      s2, 0x28(sp)
    lw      s3, 0x24(sp)
    jr      ra
    addiu   sp, sp, 0x38

.align 4
s2d_txt_cfg:                            ; engine config (vwf_dialog.asm): state, activate, upload count*, upload queue*
    .word 0, s2d_txt_activate, s2d_txt_cfg + S2DT_COUNT, s2d_txt_cfg + S2DT_ENTRY
    .word 0                             ; S2DT_STRUCT
    .word 0                             ; S2DT_COUNT
    .fill 12, 0                         ; S2DT_ENTRY
.endarea
