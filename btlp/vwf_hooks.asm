;; =============================================================
;; BTLP.BIN - negotiation text VWF hooks (engine: vwf/vwf_btlp.asm)
;; =============================================================
.org BTLP_TEXT_EMIT_JAL_ADDR
    jal     btlp_vwf_emit               ; was jal 0x8007C754 (glyph function)
.org BTLP_TEXT_EMIT2_JAL_ADDR
    jal     btlp_vwf_emit


;; 16 px string renderer (command windows, header) -> VWF (vwf/vwf_btlp_str16.asm)
.org 0x8007BF44
    j       btlp_str16
    nop

;; "LV13 <name>" header builder (0x8007C248..): the name used to be copied as 0x80 + byte pairs (typed lowercase = kana);
;; btl_name_copy (btlp/name_lowercase.asm) maps typed names like in the battle messages. a0 returns the FF position.
.org 0x8007C258
.area 0x8007C29C - 0x8007C258
    lui     a0, 0x800F
    addiu   a0, a0, -0x1448             ; name buffer
    move    a1, s2                      ; stored name
    jal     btl_name_copy
    li      a2, 8
    lui     v1, 0x800F
    addiu   v1, v1, -0x1448
    subu    s1, a0, v1                  ; s1 = bytes written (the code behind stores FF F5 at buffer + s1)
    j       0x8007C29C                  ; skip what is left of the old copy loop
    nop
.endarea
