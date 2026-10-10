;; =============================================================
;; Reusable macros
;; =============================================================

;; Write null-terminated string with zero-fill padding.
;; Triggers build error if string overflows slot_size.
;; The second argument to .area zero-fills remaining bytes automatically.
.macro strpad, str, slot_size
.area slot_size, 0x00
    .string str
.endarea
.endmacro
