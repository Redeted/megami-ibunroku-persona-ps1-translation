;; BTLP 16 px string renderer: queue the finished cells (lives in the BTLP code fragment, see vwf/vwf_btlp_str16.asm)
;; btlp_str16_flush(a0 = descriptor, a1 = last touched cell): one BTLP_LQUEUE(src, x, y, 4, 16) per cell 0..a1 from the
;; glyph-ring slots filled by btlp_str16_activate, and the glyph counter advances by STR16_MAX_CELLS
btlp_str16_flush:
    addiu   sp, sp, -0x30
    sw      ra, 0x2C(sp)
    sw      s0, 0x28(sp)
    sw      s1, 0x24(sp)
    sw      s2, 0x20(sp)
    sw      s3, 0x1C(sp)
    move    s1, a0
    move    s0, a1
    lui     t2, 0x800F
    lw      t0, -0x41BC(t2)             ; glyph counter
    addiu   t3, t2, -0x41B8             ; ring base
    addiu   t4, t0, STR16_MAX_CELLS
    sw      t4, -0x41BC(t2)             ; reserve the whole string's slots
    sll     t0, t0, 7
    addu    s2, t3, t0                  ; slot 0 of this string
    move    s3, zero
@@queue:
    sll     t1, s3, 7
    addu    a0, s2, t1                  ; src
    lh      a1, 4(s1)
    nop
    sll     a1, a1, 1
    addiu   a1, a1, 0x380
    sll     t2, s3, 2
    addu    a1, a1, t2                  ; x
    lh      a2, 6(s1)
    li      t3, 16
    addiu   a2, a2, 0x150               ; y
    sw      t3, 0x10(sp)                ; h
    jal     BTLP_LQUEUE
    li      a3, 4                       ; w (16 px of 4bpp)
    sltu    t0, s3, s0                  ; more cells?
    bnez    t0, @@queue
    addiu   s3, s3, 1
    lw      ra, 0x2C(sp)
    lw      s0, 0x28(sp)
    lw      s1, 0x24(sp)
    lw      s2, 0x20(sp)
    lw      s3, 0x1C(sp)
    jr      ra
    addiu   sp, sp, 0x30
