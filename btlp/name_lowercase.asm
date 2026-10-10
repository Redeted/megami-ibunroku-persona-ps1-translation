;; =============================================================
;; BTLP.BIN - typed names and demon names in battle text (FFF9 etc.)
;;
;; 0x8007A86C(a0 = text buffer, a1 = stored name, a2 = max chars) copies a
;; stored small-font name (typed names, demon names) into a text buffer:
;; bytes >= 0x80 got a 0x80 prefix (two-byte glyph), the rest were copied as
;; single bytes. The name entry stores typed lowercase as the LOW byte of the
;; full-width glyph (ａ = 0x723 -> 0x23), so those came out as hiragana, and the
;; small-font blank / . / ' / - of the English demon names came out as a 16 px
;; space and kana. Replaced (the body moved to the unreferenced function at
;; BTLP_NAME_COPY_ADDR, tools/deadovl.py):
;;   name_sym pairs     -> the VWF byte itself (narrow space, . ' -)
;;   lowercase codes    -> 0x87 prefix (vwf_name_lc != 0), i.e. back to the
;;                         full-width glyph, which vwf_name_map turns into narrow English
;;   >= 0x80            -> 0x80 prefix (A-Z ... via vwf_name_map)
;; Clobbers v0, v1, a0, a1, a2, t0, t1, at (the original used v0 v1 a0 a1 a3 t0; all callers return right after).
;; =============================================================
.org 0x8007A86C
.area 0x8007A8D4 - 0x8007A86C
    j       btl_name_copy
    nop
.endarea

.org BTLP_NAME_COPY_ADDR
.area BTLP_NAME_COPY_SIZE
btl_name_copy:
    lbu     v1, 0(a1)
    li      v0, 0xFF
    beq     v1, v0, @@end
    addiu   a1, a1, 1
    blez    a2, @@end                   ; a2 = characters left (counts down; the original counted a3 up)
    addiu   a2, a2, -1
    la      t0, @@sym
@@sym_loop:
    lbu     t1, 1(t0)
    lbu     v0, 0(t0)
    beqz    t1, @@not_sym
    addiu   t0, t0, 2
    bne     v0, v1, @@sym_loop
    nop
    b       @@single
    move    v1, t1                      ; the VWF byte, stored as is
@@not_sym:
    andi    v0, v1, 0x80
    bnez    v0, @@prefix                ; >= 0x80: prefix 0x80
    li      t0, 0x80
    addiu   t0, v1, -0x23
    sltiu   v0, t0, 35
    beqz    v0, @@single
    lui     at, hi(vwf_name_lc - 0x23)
    addu    at, at, v1
    lbu     v0, lo(vwf_name_lc - 0x23)(at)
    nop
    beqz    v0, @@single                ; not a lowercase code: single byte
    li      t0, 0x87
@@prefix:
    sb      t0, 0(a0)
    addiu   a0, a0, 1
@@single:
    sb      v1, 0(a0)
    b       btl_name_copy
    addiu   a0, a0, 1
@@end:                                  ; v0 = 0xFF on both paths
    jr      ra
    sb      v0, 0(a0)
@@sym:                                  ; small-font code, VWF byte (ASCII + 0x68); 0, 0 ends
    .byte   0x00, ' ' + 0x68
    .byte   0x47, '.' + 0x68            ; ぽ cell = .
    .byte   0x51, 0x27 + 0x68           ; ゎ cell = '
    .byte   0xCC, '-' + 0x68
    .byte   0, 0
.endarea
