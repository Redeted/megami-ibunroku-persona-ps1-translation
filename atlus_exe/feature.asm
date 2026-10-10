;; =============================================================
;; EXE/ATLUS.EXE - Atlus logo EXE, t_addr 0x80080000
;; =============================================================

;; --- In-place string replacement ---
; .org ATLUS_EXE_STRING_ADDR
;     strpad EXAMPLE_STR, 12

;; --- Relocated string (overflow: append past EOF) ---
; .org ATLUS_EXE_EOF_ADDR
; new_string_label:
;     .string LONG_EXAMPLE_STR
;
; .org ATLUS_EXE_POINTER_LUI_ADDR
;     li a1, new_string_label
