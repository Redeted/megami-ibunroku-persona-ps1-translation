;; =============================================================
;; TALK/ZOMBIKO.BIN - Demon negotiation: ZOMBIKO
;; =============================================================

;; --- In-place string replacement ---
; .org TALK_ZOMBIKO_STRING_ADDR
;     strpad EXAMPLE_STR, 12

;; --- Relocated string (overflow: append past EOF) ---
; .org TALK_ZOMBIKO_EOF_ADDR
; new_string_label:
;     .string LONG_EXAMPLE_STR
;
; .org TALK_ZOMBIKO_POINTER_LUI_ADDR
;     li a1, new_string_label
