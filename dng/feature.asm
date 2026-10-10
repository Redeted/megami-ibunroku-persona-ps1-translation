;; =============================================================
;; DNG.BIN - Overlay #4: dungeon
;; =============================================================

;; --- In-place string replacement ---
; .org DNG_STRING_ADDR
;     strpad EXAMPLE_STR, 12

;; --- Relocated string (overflow: append past EOF) ---
; .org DNG_EOF_ADDR
; new_string_label:
;     .string LONG_EXAMPLE_STR
;
; .org DNG_POINTER_LUI_ADDR
;     li a1, new_string_label
