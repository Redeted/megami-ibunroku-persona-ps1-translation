;; =============================================================
;; TALK/TINPRA.BIN - Demon negotiation: TINPRA
;; =============================================================

;; --- In-place string replacement ---
; .org TALK_TINPRA_STRING_ADDR
;     strpad EXAMPLE_STR, 12

;; --- Relocated string (overflow: append past EOF) ---
; .org TALK_TINPRA_EOF_ADDR
; new_string_label:
;     .string LONG_EXAMPLE_STR
;
; .org TALK_TINPRA_POINTER_LUI_ADDR
;     li a1, new_string_label
