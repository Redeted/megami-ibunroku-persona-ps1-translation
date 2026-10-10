;; =============================================================
;; ADV/MES.BIN - Event script text (13 MB) - file offsets
;; =============================================================

;; --- In-place string replacement ---
; .org MES_STRING_ADDR
;     strpad EXAMPLE_STR, 12

;; --- Relocated string (overflow: append past EOF) ---
; .org MES_EOF_ADDR
; new_string_label:
;     .string LONG_EXAMPLE_STR
;
; .org MES_POINTER_LUI_ADDR
;     li a1, new_string_label
