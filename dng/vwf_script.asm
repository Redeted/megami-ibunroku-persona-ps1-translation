;; =============================================================
;; DNG.BIN - VWF for the dungeon SCRIPT boxes (text inside the D0x/D??.BIN event records: locked doors, party / villain
;; speech, lever prompt ...). These are printed by the script interpreter 0x80073F90.., NOT by the E-file dialogue
;; interpreter that dng/vwf_hooks.asm patches. Found 2026-10-08 (lever prompt showed garbage with English bytes: every byte
;; with bit 7 set was a two-byte lead, 88-E6 included).
;;
;; Interpreter: byte < 0x80 (or 0x80-0x87 xx) -> glyph function 0x80074F34(glyph): converts the font glyph, uploads one 16x16 cell
;; to VRAM (0x140 + col*4, 0x18 + (line%3)*16), sets the cell's map entry (0x80075338), col++ (0x800A03F8); col >= 15 triggers
;; the newline routine 0x800750B8 (col = 0, line++ at 0x800A067C).
;; Patches:
;;   * lead-byte test: only 80-87 are two-byte glyph leads (88-E6 = English VWF bytes)
;;   * both calls of the glyph function (single byte / two-byte) go to dng_txt_put / dng_txt_put_wide, which run the shared
;;     engine (vwf_dialog_emit) with a private config and scratch state (pos = (line%3)*15 + col); afterwards col = engine pos
;;     (or 15 when the engine wrapped, so the interpreter's own newline logic runs on the next glyph). The read pointer s5 is
;;     handed to the engine as s2 (it rewinds it when a glyph does not fit).
;;   * dng_txt_activate (engine callback): LoadImage + DrawSync of the composed cell, then the cell's map entry.
;; The code lives in an extension of DNG.BIN behind the original image (bss of the overlay ends at 0x800A1124).
;; =============================================================
DNGS_COL                equ 0x800A03F8          ; word: cell in the line
DNGS_LINE               equ 0x800A067C          ; word: line counter (row = line % 3)
DNGS_NEWLINE            equ 0x800750B8
DNGS_SET_CELL           equ 0x80075338          ; (map base, attr, col, row, stack+0x10 = count)
DNGS_LOAD_IMAGE         equ 0x8002B810
DNGS_DRAW_SYNC          equ 0x8002B5E8
DNGT_COUNT              equ 0x10                ; config: queued entry count
DNGT_ENTRY              equ 0x14                ; config: queue entry {u32 src; u16 x, y, w, h}

.org 0x80074E4C
    addiu   v0, v1, -0x80                       ; v1 = the byte (loaded at 0x80073F90), was nop
.org 0x80074E50
    sltiu   v0, v0, 8                           ; was andi v0, a0, 0x80  (bnez at 0x80074E54 unchanged)
.org 0x80074E60
    jal     dng_txt_put                         ; was jal 0x80074F34
.org 0x80074EA0
    jal     dng_txt_put_wide                    ; was jal 0x80074F34
; the three string printers (0x800753AC, 0x80075428, 0x8007553C: choice lists, name parts, ...) take the same lead-byte test
; and call the entry points with the "menu" mode (no read pointer in s5 to maintain)
.org 0x800753EC
    jal     dng_txt_put_name                    ; was jal 0x80074F34 (delay slot addiu s1,s1,1 unchanged)
; 0x800753AC is only used for the name inserts FF08 (party), FF09 (item), FF0A (skill), FF0B / FF0C (demon): their bytes are small-font
; codes, so the engine gets the "name insertion" flag (a1 = 1: vwf_glyph_map maps them to the narrow English font)
.org 0x8007546C
    addiu   v0, v1, -0x80                       ; was nop (v1 = byte)
.org 0x80075470
    sltiu   v0, v0, 8                           ; was andi v0, a0, 0x80
.org 0x80075480
    j       dng_txt_menu_single                 ; was j 0x80075498 (delay slot move a0,v1 unchanged)
.org 0x80075498
    jal     dng_txt_put_wide_menu               ; was jal 0x80074F34
.org 0x800755A8
    addiu   v0, v1, -0x80                       ; was nop (v1 = byte)
.org 0x800755AC
    sltiu   v0, v0, 8                           ; was andi v0, a0, 0x80
.org 0x800755BC
    j       dng_txt_menu_single2                ; was j 0x800755D4 (delay slot move a0,v1 unchanged)
.org 0x800755D4
    jal     dng_txt_put_wide_menu               ; was jal 0x80074F34

; FF0A (skill name insert): the record only keeps the first 10 glyphs, skill_name_copy assembles the full name (up to 15 glyphs)
.org 0x8007420C
    j       dng_skill_name                      ; was j 0x80074234 (delay slot sll a0,a0,2 harmless)

.org DNG_GLUE_ADDR
dng_skill_name:                                 ; s5 = the skill id byte
    addiu   sp, sp, -0x20
    sw      ra, 0x1C(sp)
    lbu     a1, 0(s5)                           ; (never load a jal argument in the delay slot: the callee would see the old value)
    la      a0, dng_skill_buf
    jal     skill_name_copy                     ; clobbers v0, v1, a0, a1, a2, at
    nop
    la      a0, dng_skill_buf
    li      a1, 15
@@trim:                                         ; end the name at its last real glyph (the copy pads with blank glyphs)
    beqz    a1, @@go
    addu    t0, a0, a1
    lbu     t1, -1(t0)
    nop
    bnez    t1, @@go
    nop
    b       @@trim
    addiu   a1, a1, -1
@@go:
    addu    t0, a0, a1
    li      t1, 0xFF
    sb      t1, 0(t0)                           ; FF terminator (buffer is 16 bytes)
    jal     0x800753AC
    li      a1, 15
    lw      ra, 0x1C(sp)
    nop
    j       0x8007423C                          ; as the original after the name printer: next script byte
    addiu   sp, sp, 0x20
dng_txt_menu_single:
    jal     dng_txt_put_menu
    nop
    j       0x8007549C
    nop
dng_txt_menu_single2:
    jal     dng_txt_put_menu
    nop
    j       0x800755DC
    nop
dng_txt_put_wide_menu:                          ; a0 = two-byte glyph code, no read pointer
    ori     a0, a0, 0x8000
    j       dng_txt_go
    li      a1, 1
dng_txt_put_menu:                               ; a0 = single byte, no read pointer
    j       dng_txt_go
    li      a1, 1
dng_txt_put_name:                               ; a0 = single byte of an inserted name (small-font code), no read pointer
    j       dng_txt_go
    li      a1, 2
dng_txt_put_wide:                               ; a0 = two-byte glyph code
    ori     a0, a0, 0x8000
dng_txt_put:                                    ; a0 = single byte (kana glyph or English VWF byte), s5 = read pointer
    move    a1, zero
dng_txt_go:                                     ; a1 = 1: menu mode
    addiu   sp, sp, -0x30
    sw      ra, 0x2C(sp)
    sw      s0, 0x28(sp)
    sw      s1, 0x24(sp)
    sw      s2, 0x20(sp)
    sw      a0, 0x1C(sp)                        ; glyph code
    sw      a1, 0x18(sp)                        ; mode
    lui     s0, 0x800A
    lw      t0, 0x3F8(s0)                       ; col
    nop
    slti    t0, t0, 15
    bnez    t0, @@ok
    nop
    jal     DNGS_NEWLINE                        ; line full: the interpreter's own newline / scroll
    nop
@@ok:
    lw      t0, 0x3F8(s0)                       ; col
    lw      t1, 0x67C(s0)                       ; line
    li      t2, 3
    divu    t1, t2
    mfhi    t3                                  ; row
    li      t4, 15
    multu   t3, t4
    mflo    t5
    addu    t5, t5, t0                          ; pos = row * 15 + col
    la      s1, dng_txt_cfg
    sw      zero, DNGT_COUNT(s1)
    lw      t6, 0(s1)                           ; scratch state
    nop
    sh      t5, 0xA(t6)
    la      t7, vwf_dlg_state                   ; cells used by original (16 px) glyphs: keep the pen in step
    lhu     t8, DLG_PX(t7)
    sll     t9, t0, 4
    addiu   t8, t8, 15
    srl     t8, t8, 4
    sltu    t8, t8, t0                          ; ceil(px/16) < col ?
    beqz    t8, @@sync
    nop
    sh      t9, DLG_PX(t7)
@@sync:
    move    s2, s5                              ; read pointer (in/out)
    lw      t0, 0x18(sp)                        ; mode: 2 = name insert -> engine flag a1 = 1
    move    a0, s1
    sltiu   a1, t0, 2
    xori    a1, a1, 1
    jal     vwf_dialog_emit
    lw      a2, 0x1C(sp)
    lw      t0, 0x18(sp)
    nop
    bnez    t0, @@menu
    nop
    move    s5, s2                              ; rewound when the glyph did not fit
@@menu:
    lw      t6, 0(s1)
    li      t4, 15
    lhu     t5, 0xA(t6)                         ; new pos
    lui     s0, 0x800A
    divu    t5, t4
    mflo    t1                                  ; new row
    mfhi    t2                                  ; new col
    lw      t0, 0x67C(s0)
    li      t3, 3
    divu    t0, t3
    mfhi    t3                                  ; old row
    beq     t1, t3, @@same
    nop
    li      t2, 15                              ; wrapped
@@same:
    sw      t2, 0x3F8(s0)
    lw      ra, 0x2C(sp)
    lw      s0, 0x28(sp)
    lw      s1, 0x24(sp)
    lw      s2, 0x20(sp)
    jr      ra
    addiu   sp, sp, 0x30

;; dng_txt_activate(a0 = cell P): upload the cell the engine composed, set its map entry
dng_txt_activate:
    addiu   sp, sp, -0x38
    sw      ra, 0x34(sp)
    sw      s0, 0x30(sp)
    sw      s1, 0x2C(sp)
    li      t0, 15
    divu    a0, t0
    mflo    s0                                  ; row
    mfhi    s1                                  ; col
    la      t3, dng_txt_cfg
    lw      a1, DNGT_ENTRY(t3)                  ; src: ring cell queued by the engine
    sll     t4, s1, 2
    addiu   t4, t4, 0x140
    sh      t4, 0x18(sp)                        ; RECT x
    sll     t5, s0, 4
    addiu   t5, t5, 0x18
    sh      t5, 0x1A(sp)                        ; RECT y
    li      t6, 4
    sh      t6, 0x1C(sp)
    li      t6, 16
    sh      t6, 0x1E(sp)
    jal     DNGS_LOAD_IMAGE
    addiu   a0, sp, 0x18
    jal     DNGS_DRAW_SYNC
    move    a0, zero
    lui     t0, 0x800A
    lw      t1, 0xD7C(t0)
    lbu     a1, 0xDDC(t0)
    nop
    lw      t1, 0xC(t1)
    lui     a0, 0x8013
    addu    a0, t1, a0                          ; map base as in the original glyph function
    move    a2, s1
    move    a3, s0
    li      t2, 1
    jal     DNGS_SET_CELL
    sw      t2, 0x10(sp)
    la      t3, dng_txt_cfg
    sw      zero, DNGT_COUNT(t3)
    lw      ra, 0x34(sp)
    lw      s0, 0x30(sp)
    lw      s1, 0x2C(sp)
    jr      ra
    addiu   sp, sp, 0x38

.align 4
dng_skill_buf:
    .fill 16, 0
.align 4
dng_txt_cfg:                                    ; engine config (vwf_dialog.asm): state, activate, upload count*, upload queue*
    .word dng_txt_state, dng_txt_activate, dng_txt_cfg + DNGT_COUNT, dng_txt_cfg + DNGT_ENTRY
    .word 0                                     ; DNGT_COUNT
    .fill 12, 0                                 ; DNGT_ENTRY
dng_txt_state:
    .fill 16, 0
