;; =============================================================
;; TALK/MAYOERU.BIN - Demon negotiation: MAYOERU
;; =============================================================

;; --- In-place string replacement ---
; .org TALK_MAYOERU_STRING_ADDR
;     strpad EXAMPLE_STR, 12

;; --- Relocated string (overflow: append past EOF) ---
; .org TALK_MAYOERU_EOF_ADDR
; new_string_label:
;     .string LONG_EXAMPLE_STR
;
; .org TALK_MAYOERU_POINTER_LUI_ADDR
;     li a1, new_string_label
