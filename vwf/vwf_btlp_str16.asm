;; =============================================================
;; BTLP 16 px string renderer (0x8007BF44) -> shared VWF engine
;;
;; The command windows (CONTACT commands, "LV13 name" header, ...) draw each string with BTLP 0x8007BF44(a0 = descriptor,
;; a1 = string, FF / F5 end): one 16x16 glyph per cell, queued as a LoadImage (0x80066620(src, x, y, w, h), flushed at the
;; end of the frame AFTER a black clear of the whole texture area queued by the caller) to the texture slot
;; (x = descriptor.x * 2 + 0x380 + 4 * cell, y = descriptor.y + 0x150); the caller owns the sprites. This replacement
;; composes the string with the dialogue VWF engine (vwf_dialog_emit, config vwf_cfg_btlp with its own activate function and
;; a fake text state on the stack). The engine's 4-cell ring is reused, so every touched cell is copied into slot
;; (counter + P) of the game's own glyph ring (0x800EBE48, counter at 0x800EBE44) by btlp_str16_activate; when the string is
;; finished btlp_str16_flush queues one LoadImage per cell and advances the counter.
;; Text encoding as the other VWF paths: 00-7F kana glyph, 80-87 xx two-byte glyph, 88-E6 English, FF/F5 end.
;; Typed names (two-byte full-width / lowercase glyphs) are narrowed by vwf_glyph_map inside the engine.
;; =============================================================

;; hook: BTLP 0x8007BF44 = j btlp_str16
btlp_str16:
    addiu   sp, sp, -0x30
    sw      ra, 0x2C(sp)
    sw      s2, 0x20(sp)
    sw      s3, 0x1C(sp)
    move    s2, a1                      ; read pointer (the engine rewinds s2 when it hands a glyph back)
    la      s3, vwf_cfg_btlp
    sw      a0, BTCFG_STRUCT(s3)        ; descriptor
    la      t0, btlp_str16_activate
    sw      t0, VWF_CFG_ACTIVATE(s3)
    addiu   t0, sp, 0x10
    sw      t0, VWF_CFG_STATE(s3)       ; fake text state, pos halfword at +0xA
    sh      zero, 0x1A(sp)
    la      t0, vwf_dlg_state
    li      t1, -1
    sh      zero, DLG_PX(t0)
    sh      t1, DLG_LINE(t0)
    sh      t1, DLG_INIT(t0)
    sh      zero, DLG_LAST(t0)
@@loop:
    lbu     a2, 0(s2)
    li      t0, 0xFF
    beq     a2, t0, @@done
    li      t0, 0xF5
    beq     a2, t0, @@done
    addiu   s2, s2, 1
    sltiu   t0, a2, 0x88
    beqz    t0, @@go                    ; 88-FF English
    sltiu   t0, a2, 0x80
    bnez    t0, @@go                    ; 00-7F kana glyph
    nop
    lbu     t1, 0(s2)                   ; 80-87 xx two-byte glyph
    andi    a2, a2, 0x7F
    sll     a2, a2, 8
    or      a2, a2, t1
    ori     a2, a2, 0x8000
    addiu   s2, s2, 1
@@go:
    la      a0, vwf_cfg_btlp
    jal     vwf_dialog_emit
    move    a1, zero
    lhu     t0, 0x1A(sp)                ; pos: 15 or more = the engine wrapped to a second line
    nop
    sltiu   t0, t0, STR16_MAX_CELLS
    bnez    t0, @@loop
    nop
@@done:
    lw      a0, BTCFG_STRUCT(s3)        ; descriptor
    la      t0, vwf_dlg_state
    lhu     a1, DLG_LAST(t0)            ; last touched cell
    jal     btlp_str16_flush            ; queue the cells
    nop
    la      t0, btlp_activate           ; give the config back to the text interpreter hook
    sw      t0, VWF_CFG_ACTIVATE(s3)
    lw      ra, 0x2C(sp)
    lw      s2, 0x20(sp)
    lw      s3, 0x1C(sp)
    jr      ra
    addiu   sp, sp, 0x30

;; btlp_str16_activate(a0 = cell P): copy the cell the engine queued (BTCFG_ENTRY.src, a ring cell) into slot
;; (counter + P) of the game's glyph ring
btlp_str16_activate:
    lui     t5, 0x800F
    lw      t6, -0x41BC(t5)             ; glyph counter
    la      t1, vwf_cfg_btlp
    lw      t8, BTCFG_ENTRY(t1)         ; src
    addu    t6, t6, a0
    sll     t6, t6, 7
    addiu   t5, t5, -0x41B8             ; ring base 0x800EBE48
    addu    t6, t6, t5                  ; dest
    addiu   t9, t8, CELL_BYTES
@@copy:
    lw      t0, 0(t8)
    addiu   t8, t8, 4
    sw      t0, 0(t6)
    addiu   t6, t6, 4
    bne     t8, t9, @@copy
    nop
    jr      ra
    sw      zero, BTCFG_COUNT(t1)       ; queue consumed
