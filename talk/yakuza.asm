;; =============================================================
;; TALK/YAKUZA.BIN - Demon negotiation: YAKUZA
;; =============================================================

;; --- In-place string replacement ---
; .org TALK_YAKUZA_STRING_ADDR
;     strpad EXAMPLE_STR, 12

;; --- Relocated string (overflow: append past EOF) ---
; .org TALK_YAKUZA_EOF_ADDR
; new_string_label:
;     .string LONG_EXAMPLE_STR
;
; .org TALK_YAKUZA_POINTER_LUI_ADDR
;     li a1, new_string_label
