;; =============================================================
;; ADV.BIN - Overlay #7: field / events
;; =============================================================

;; --- In-place string replacement ---
; .org ADV_STRING_ADDR
;     strpad EXAMPLE_STR, 12

;; --- Relocated string (overflow: append past EOF) ---
; .org ADV_EOF_ADDR
; new_string_label:
;     .string LONG_EXAMPLE_STR
;
; .org ADV_POINTER_LUI_ADDR
;     li a1, new_string_label
