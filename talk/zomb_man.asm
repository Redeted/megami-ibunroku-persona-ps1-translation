;; =============================================================
;; TALK/ZOMB_MAN.BIN - Demon negotiation: ZOMB_MAN
;; =============================================================

;; --- In-place string replacement ---
; .org TALK_ZOMB_MAN_STRING_ADDR
;     strpad EXAMPLE_STR, 12

;; --- Relocated string (overflow: append past EOF) ---
; .org TALK_ZOMB_MAN_EOF_ADDR
; new_string_label:
;     .string LONG_EXAMPLE_STR
;
; .org TALK_ZOMB_MAN_POINTER_LUI_ADDR
;     li a1, new_string_label
