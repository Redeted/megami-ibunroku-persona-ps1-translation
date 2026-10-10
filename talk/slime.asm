;; =============================================================
;; TALK/SLIME.BIN - Demon negotiation: SLIME
;; =============================================================

;; --- In-place string replacement ---
; .org TALK_SLIME_STRING_ADDR
;     strpad EXAMPLE_STR, 12

;; --- Relocated string (overflow: append past EOF) ---
; .org TALK_SLIME_EOF_ADDR
; new_string_label:
;     .string LONG_EXAMPLE_STR
;
; .org TALK_SLIME_POINTER_LUI_ADDR
;     li a1, new_string_label
