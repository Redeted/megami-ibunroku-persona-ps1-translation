;; =============================================================
;; SLPS_005.00 - Main executable (resident), t_addr 0x80010000
;; =============================================================

;; --- In-place string replacement ---
; .org SLPS_STRING_ADDR
;     strpad EXAMPLE_STR, 12

;; --- Relocated string (overflow: append past EOF) ---
; .org SLPS_EOF_ADDR
; new_string_label:
;     .string LONG_EXAMPLE_STR
;
; .org SLPS_POINTER_LUI_ADDR
;     li a1, new_string_label
