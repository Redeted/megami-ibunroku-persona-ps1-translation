;; =============================================================
;; TALK/TOILET.BIN - Demon negotiation: TOILET
;; =============================================================

;; --- In-place string replacement ---
; .org TALK_TOILET_STRING_ADDR
;     strpad EXAMPLE_STR, 12

;; --- Relocated string (overflow: append past EOF) ---
; .org TALK_TOILET_EOF_ADDR
; new_string_label:
;     .string LONG_EXAMPLE_STR
;
; .org TALK_TOILET_POINTER_LUI_ADDR
;     li a1, new_string_label
