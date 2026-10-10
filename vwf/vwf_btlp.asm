;; =============================================================
;; VWF for the BTLP negotiation / battle text box (overlay #5)
;;
;; BTLP's interpreter (0x8007C9E0) draws one 16x16 glyph per text cell with
;; its glyph function 0x8007C754(struct, ptr) -> ptr and adds one sprite per
;; cell. That function is replaced by btlp_vwf_emit, which feeds the shared
;; engine (vwf_dialog.asm). Differences to ADV/DNG/S2D, handled in
;; btlp_activate: cells are uploaded to VRAM at once (LoadImage + DrawSync;
;; BTLP resets its own queue every frame) and the sprite list is written here.
;; The text struct is not fixed: the caller passes it in a0 and the config is
;; filled in on every call.
;; Design notes: translation/BTLP_HOOK_PLAN.md
;; =============================================================

;; -------------------------------------------------------------
;; btlp_vwf_emit(a0 = text struct, a1 = read pointer) -> v0 = next pointer
;; Replaces the original glyph function at its two call sites.
;; Bytes 00-7F: original glyph; 80-87 xx: two-byte glyph; 88-E6: English.
;; -------------------------------------------------------------
btlp_vwf_emit:
    addiu   sp, sp, -0x20
    sw      ra, 0x1C(sp)
    sw      s2, 0x18(sp)
    la      t0, vwf_cfg_btlp
    addiu   t1, a0, BT_STATE_OFFSET
    sw      t1, 0(t0)                   ; config: text state
    sw      a0, BTCFG_STRUCT(t0)
    lbu     a2, 0(a1)
    addiu   s2, a1, 1                   ; s2 = pointer after the first byte
    sltiu   t2, a2, 0x88
    beqz    t2, @@go                    ; 88-FF: English VWF character
    sltiu   t2, a2, 0x80
    bnez    t2, @@go                    ; 00-7F: single-byte glyph
    nop
    lbu     t3, 0(s2)                   ; 80-87: two-byte glyph
    andi    a2, a2, 0x7F
    sll     a2, a2, 8
    or      a2, a2, t3
    ori     a2, a2, 0x8000
    addiu   s2, s2, 1
@@go:
    la      a0, vwf_cfg_btlp
    jal     vwf_dialog_emit
    move    a1, zero
    move    v0, s2                      ; the engine rewinds s2 if the glyph is handed back
    lw      ra, 0x1C(sp)
    lw      s2, 0x18(sp)
    jr      ra
    addiu   sp, sp, 0x20

