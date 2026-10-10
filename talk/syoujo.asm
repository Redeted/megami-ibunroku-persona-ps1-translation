;; =============================================================
;; TALK/SYOUJO.BIN - Demon negotiation: SYOUJO
;; =============================================================

;; --- In-place string replacement ---
; .org TALK_SYOUJO_STRING_ADDR
;     strpad EXAMPLE_STR, 12

;; --- Relocated string (overflow: append past EOF) ---
; .org TALK_SYOUJO_EOF_ADDR
; new_string_label:
;     .string LONG_EXAMPLE_STR
;
; .org TALK_SYOUJO_POINTER_LUI_ADDR
;     li a1, new_string_label
