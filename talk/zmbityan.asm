;; =============================================================
;; TALK/ZMBITYAN.BIN - Demon negotiation: ZMBITYAN
;; =============================================================

;; --- In-place string replacement ---
; .org TALK_ZMBITYAN_STRING_ADDR
;     strpad EXAMPLE_STR, 12

;; --- Relocated string (overflow: append past EOF) ---
; .org TALK_ZMBITYAN_EOF_ADDR
; new_string_label:
;     .string LONG_EXAMPLE_STR
;
; .org TALK_ZMBITYAN_POINTER_LUI_ADDR
;     li a1, new_string_label
