;; =============================================================
;; S2D.BIN - Overlay #6: 2D map
;; =============================================================

;; --- In-place string replacement ---
; .org S2D_STRING_ADDR
;     strpad EXAMPLE_STR, 12

;; --- Relocated string (overflow: append past EOF) ---
; .org S2D_EOF_ADDR
; new_string_label:
;     .string LONG_EXAMPLE_STR
;
; .org S2D_POINTER_LUI_ADDR
;     li a1, new_string_label
