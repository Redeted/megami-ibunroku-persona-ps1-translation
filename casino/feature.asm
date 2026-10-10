;; =============================================================
;; CASINO.BIN - Overlay #8: casino
;; =============================================================

;; --- In-place string replacement ---
; .org CASINO_STRING_ADDR
;     strpad EXAMPLE_STR, 12

;; --- Relocated string (overflow: append past EOF) ---
; .org CASINO_EOF_ADDR
; new_string_label:
;     .string LONG_EXAMPLE_STR
;
; .org CASINO_POINTER_LUI_ADDR
;     li a1, new_string_label
