;; =============================================================
;; BTLP.BIN - Overlay #5: battle
;; =============================================================

;; --- In-place string replacement ---
; .org BTLP_STRING_ADDR
;     strpad EXAMPLE_STR, 12

;; --- Relocated string (overflow: append past EOF) ---
; .org BTLP_EOF_ADDR
; new_string_label:
;     .string LONG_EXAMPLE_STR
;
; .org BTLP_POINTER_LUI_ADDR
;     li a1, new_string_label

;; --- Battle FORM list (slots A-E, user slot 1, 2026-10-09): "フォーメーション" + letter ---
;; The list entry is built at 0x800ABC00: 8 glyphs copied from the template at 0x800D2868, then the slot letter stored at +8
;; (the entry is 9 glyphs wide; lists stop at an FF). English "FORMATION" does not fit, so: "FORM" + space, the letter moves to
;; +5 and the template carries the FF at +6.
.org 0x800D2868
    .byte 0xAB, 0xB4, 0xB7, 0xB2, 0x00, 0x00, 0xFF, 0x00       ; F O R M <blank> <letter> FF
.org 0x800ABC2C
    sb      v0, 5(s2)                                          ; was sb v0, 8(s2)
