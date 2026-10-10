;; =============================================================
;; Variable-width font engine - dialogue box (ADV / DNG / S2D overlays)
;;
;; The three field overlays carry copies of the same text interpreter.
;; Each hook calls a per-overlay stub (vwf_<ovl>_emit) that passes a config
;; block (vwf_dialog_cfg.asm) to the shared engine.
;;
;; The box is a GsBG map of 15x4 cells (16x16 px, 4bpp). Originally one
;; glyph = one cell. This engine keeps the map, VRAM layout and the
;; interpreter line/scroll logic, but composes glyphs at pixel granularity
;; into a ring of 4 cell buffers and uploads the cells it touched through
;; the overlay's LoadImage queue.
;;
;; Memory (see vwf/vwf_slps.asm): code, ring buffer and tables live in
;; functions of SLPS_005.00 that nothing references; the English glyphs
;; live in unused FONT.BIN glyph slots. No other RAM is used.
;;
;; Text encoding (a strict superset of the original, so untranslated
;; Japanese keeps working and both can be mixed):
;;   00-7F   original single-byte glyph (kana), drawn 16 px wide
;;   80-87xx original two-byte glyph, drawn 16 px wide; the patched
;;           interpreter passes these as (glyph | 0x8000)
;;   88-E6   English VWF character = ASCII + VWF_CHAR_BIAS
;;   FFxx    control code (handled by the interpreter)
;;
;; pos (state+0xA) is owned by the engine: after drawing it is set to
;;   line*15 + clamp(ceil(px/16), 1, 14)
;; so pos%15 == 0 only at a true line start (no spurious scrolls).
;; Wrapping reproduces the original (which wrapped after 15 glyphs, and the
;; Japanese script relies on it):
;;   - pen reaches the box width after a glyph -> pos = next line start
;;   - glyph does not fit -> pos = next line start and the character is
;;     handed back (read pointer rewound) so the interpreter re-reads it next
;;     frame, after running its own scroll checks for the new line.
;; English should still be pre-wrapped at word boundaries (tools/vwf_wrap.py).
;; =============================================================

;; --- config block layout (one per overlay, vwf_dialog_cfg.asm) ---
VWF_CFG_STATE           equ 0x0         ; text state struct; +0xA u16 pos (0-59)
VWF_CFG_ACTIVATE        equ 0x4         ; void(u16 pos): map index + GsCELL setup
VWF_CFG_UPLOAD_COUNT    equ 0x8         ; u32* number of queued LoadImage entries
VWF_CFG_UPLOAD_QUEUE    equ 0xC         ; 12-byte entries {u32 src; u16 x,y,w,h}

;; --- box geometry (identical in all three overlays) ---
DLG_TEXT_VRAM_X         equ 0x3C0       ; VRAM x (16-bit units) of cell column 0
DLG_TEXT_VRAM_Y         equ 0x100
DLG_BOX_COLS            equ 15
DLG_BOX_WIDTH_PX        equ (DLG_BOX_COLS * 16)
CELL_BYTES              equ 128         ; 16 rows x 8 bytes (4bpp)
RING_CELLS              equ 4           ; a glyph touches at most 3 cells

;; --- engine state (vwf_dlg_state) ---
DLG_PX                  equ 0x0         ; u16 pen x in the current line
DLG_LINE                equ 0x2         ; u16 current line (0-3), 0xFFFF = none
DLG_INIT                equ 0x4         ; s16 highest cell cleared in this line
DLG_LAST                equ 0x6         ; u16 last cell touched by this glyph
DLG_COLOR_MAIN          equ 0x8         ; u8 palette index of the glyph (default 2); the S2D overworld box uses 1
DLG_COLOR_SHADOW        equ 0x9         ; u8 palette index of the shadow (default 1); S2D: 2
DLG_SHADOW_DX           equ 0xA         ; u8 shadow x offset (default 2); S2D: 1

VWF_CHAR_BIAS           equ 0x68        ; byte = ASCII + bias (0x20 -> 0x88)
VWF_FIRST_BYTE          equ (0x20 + VWF_CHAR_BIAS)
VWF_GLYPHS              equ 95          ; ASCII 0x20-0x7E

COLOR_SHADOW            equ 1
COLOR_MAIN              equ 2

;; -------------------------------------------------------------
;; vwf_dialog_emit(a0 = config block, a1 = 1 if called from the
;;                 name-insertion path else 0,
;;                 a2 = single byte, or glyph | 0x8000)
;; Reached through a per-overlay stub in place of the original glyph
;; renderer, whose VRAM-coordinate arguments are ignored.
;; Clobbers a0-a3, t0-t9, v0-v1. Preserves s-registers.
;; Frame: 0x0C ra of vwf_dialog_draw, 0x10-0x2C saved registers.
;; -------------------------------------------------------------
vwf_dialog_emit:
    addiu   sp, sp, -0x30
    sw      ra, 0x2C(sp)
    sw      s5, 0x28(sp)
    sw      s0, 0x24(sp)
    sw      a1, 0x20(sp)                ; caller path (0 text, 1 name)
    sw      s1, 0x1C(sp)
    sw      s2, 0x18(sp)                ; caller s2 = script read pointer
    sw      s3, 0x14(sp)
    sw      s4, 0x10(sp)
    move    s5, a0                      ; s5 = config block
    andi    s4, a2, 0xFFFF              ; s4 = glyph code
    move    a0, s4                      ; typed names (stored as full-width Latin glyphs) -> narrow English;
    jal     vwf_glyph_map               ; the name reaches the engine through the normal text path (a1 = 0);
                                        ; a1 = 1 (inserted small-font names) is mapped first (slps_005.00/aff_free.asm)
    move    s1, s4                      ; s1 = glyph code as passed (two-byte flag for the wrap rewind)
    move    s4, v0

    ; --- line / column of the current cell ---
    lw      t0, VWF_CFG_STATE(s5)
    li      t2, DLG_BOX_COLS
    lhu     t1, 0xA(t0)                 ; pos
    nop
    divu    t1, t2
    mflo    s0                          ; s0 = line
    mfhi    t3                          ; t3 = col
    la      t4, vwf_dlg_state
    lhu     t5, DLG_LINE(t4)
    beqz    t3, @@new_line
    nop
    beq     t5, s0, @@same_line
    nop
@@new_line:
    sh      s0, DLG_LINE(t4)
    sh      zero, DLG_PX(t4)
    li      t5, -1
    sh      t5, DLG_INIT(t4)
@@same_line:
    lhu     s2, DLG_PX(t4)              ; s2 = px

    ; --- glyph source a0, row format a1 (0 = 14 narrow rows, 1 = 16 wide), advance s3 ---
    andi    t0, s4, 0x8000
    bnez    t0, @@wide                  ; two-byte glyph
    andi    t1, s4, 0x7FF
    sltiu   t0, s4, 0x80
    bnez    t0, @@wide                  ; single-byte original glyph
    nop
    addiu   t1, s4, -VWF_FIRST_BYTE     ; English VWF character
    sltiu   t2, t1, VWF_GLYPHS
    bnez    t2, @@ascii_ok
    nop
    move    t1, zero                    ; out of range -> space
@@ascii_ok:
    la      t3, vwf_font_width
    addu    t3, t3, t1
    lbu     s3, 0(t3)                   ; s3 = advance
    la      t3, vwf_font_index
    sll     t1, t1, 1
    addu    t3, t3, t1
    lhu     t1, 0(t3)                   ; offset of rows 1-14 inside FONT.BIN
    lui     a0, FONT_GLYPHS_ADDR >> 16
    addu    a0, a0, t1
    j       @@fit
    move    a1, zero
@@wide:
    sll     t1, t1, 5
    lui     a0, FONT_GLYPHS_ADDR >> 16
    addu    a0, a0, t1                  ; 16 rows x 2 bytes
    li      s3, 16
    li      a1, 1

@@fit:
    beqz    s2, @@draw                  ; a glyph always fits at the line start
    addu    t0, s2, s3
    sltiu   t0, t0, DLG_BOX_WIDTH_PX + 1
    beqz    t0, @@wrap_before
    nop
@@draw:
    jal     vwf_dialog_draw
    nop

    ; --- advance pen, set pos = line*15 + clamp(ceil(px/16), 1, 14) ---
    addu    s2, s2, s3
    la      t4, vwf_dlg_state
    sh      s2, DLG_PX(t4)
    sltiu   t0, s2, DLG_BOX_WIDTH_PX
    beqz    t0, @@next_line             ; line full: wrap like the original
    addiu   t0, s2, 15
    srl     t0, t0, 4
    bnez    t0, @@not_zero
    nop
    li      t0, 1
@@not_zero:
    sltiu   t1, t0, DLG_BOX_COLS
    bnez    t1, @@clamped
    nop
    li      t0, DLG_BOX_COLS - 1
@@clamped:
    li      t1, DLG_BOX_COLS
    multu   s0, t1
    lw      t3, VWF_CFG_STATE(s5)
    mflo    t2
    addu    t2, t2, t0
    j       @@return
    sh      t2, 0xA(t3)

    ; --- glyph does not fit: hand the character back, then wrap ---
@@wrap_before:
    lw      t0, 0x20(sp)
    lw      t1, 0x18(sp)                ; caller s2 = read pointer
    bnez    t0, @@rewind_name
    andi    t2, s1, 0x8000              ; original code: a mapped name glyph was two bytes in the text
    beqz    t2, @@rewind_text
    addiu   t1, t1, -1                  ; single-byte character
    addiu   t1, t1, -1                  ; two-byte character
@@rewind_text:
    j       @@next_line
    sw      t1, 0x18(sp)
@@rewind_name:
    lw      t3, VWF_CFG_STATE(s5)       ; name path: pointer direction flag
    lui     t4, 0x20
    lw      t5, 0(t3)
    nop
    and     t5, t5, t4
    beqz    t5, @@name_fwd
    addiu   t1, t1, -1
    addiu   t1, t1, 2                   ; reading backwards: undo the -1
@@name_fwd:
    sw      t1, 0x18(sp)
    lbu     t5, 0x35(t3)                ; remaining name characters
    nop
    addiu   t5, t5, 1                   ; the caller decrements it again
    sb      t5, 0x35(t3)

    ; --- pos = start of the next line (ring of 4) ---
@@next_line:
    addiu   t0, s0, 1
    andi    t0, t0, 3
    li      t1, DLG_BOX_COLS
    multu   t0, t1
    lw      t3, VWF_CFG_STATE(s5)
    mflo    t2
    sh      t2, 0xA(t3)

@@return:
    lw      ra, 0x2C(sp)
    lw      s5, 0x28(sp)
    lw      s0, 0x24(sp)
    lw      s1, 0x1C(sp)
    lw      s2, 0x18(sp)
    lw      s3, 0x14(sp)
    lw      s4, 0x10(sp)
    jr      ra
    addiu   sp, sp, 0x30
