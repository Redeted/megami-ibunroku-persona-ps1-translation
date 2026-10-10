;; =============================================================
;; TALK/POLUTAR.BIN - Demon negotiation: POLUTAR
;; =============================================================

;; --- In-place string replacement ---
; .org TALK_POLUTAR_STRING_ADDR
;     strpad EXAMPLE_STR, 12

;; --- Relocated string (overflow: append past EOF) ---
; .org TALK_POLUTAR_EOF_ADDR
; new_string_label:
;     .string LONG_EXAMPLE_STR
;
; .org TALK_POLUTAR_POINTER_LUI_ADDR
;     li a1, new_string_label
