;; =============================================================
;; EXE/MOVIE.EXE - Movie player EXE, t_addr 0x80080000
;; =============================================================

;; --- In-place string replacement ---
; .org MOVIE_EXE_STRING_ADDR
;     strpad EXAMPLE_STR, 12

;; --- Relocated string (overflow: append past EOF) ---
; .org MOVIE_EXE_EOF_ADDR
; new_string_label:
;     .string LONG_EXAMPLE_STR
;
; .org MOVIE_EXE_POINTER_LUI_ADDR
;     li a1, new_string_label
