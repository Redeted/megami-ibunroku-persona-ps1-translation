;; =============================================================
;; BTLP.BIN - PRS-CHG window: full-length Persona names (NOW / SUB / SUB)
;;
;; Original (0x800ACAF0): copies 10 bytes of the current Persona's name from
;; the battle Persona record (+0x1F) to 0x800F81A8 and the member's other
;; Personas to 0x800F81B3 + 11*k (FF = empty slot); 3 descriptors draw 10
;; glyphs each. Now: names by Persona id (+0x1E) through persona_name_copy
;; into PRSCHG_BUF + 16*k, descriptors draw 16 glyphs.
;; persona_name_copy clobbers v0 v1 a0 a1 a2 at (the replaced copies did too);
;; the function is non-leaf (ra on its stack).
;; =============================================================

.org 0x800ACB08                         ; empty markers of the two SUB slots
    lui     a0, hi(PRSCHG_BUF + 16)
    addiu   a0, a0, lo(PRSCHG_BUF + 16)
.org 0x800ACB28
    lui     at, hi(PRSCHG_BUF + 32)
    sb      v1, lo(PRSCHG_BUF + 32)(at)

.org 0x800ACB3C                         ; NOW: 0x800ACB3C..0x800ACB74 (t2 = current record)
.area 0x800ACB78 - 0x800ACB3C, 0
    lbu     a1, 0x1E(t2)
    la      a0, PRSCHG_BUF
    jal     persona_name_copy
    nop
    lui     v1, 0x8006                  ; v1 = 0x8005CDA8 again (used at 0x800ACB88)
    addiu   v1, v1, -0x3258
    la      a0, PRSCHG_BUF + 16         ; a0 -> t0 at 0x800ACB8C: first SUB slot
.endarea

.org 0x800ACBD0                         ; SUB copy body 0x800ACBD0..0x800ACC0C (v1 = Persona slot, t3 = records + 0x1F)
.area 0x800ACC10 - 0x800ACBD0, 0
    sll     v0, v1, 3
    addu    v0, v0, v1
    sll     v0, v0, 3                   ; slot * 0x48
    addu    v0, v0, t3
    lbu     a1, -1(v0)                  ; Persona id (+0x1E)
    move    a0, t0
    jal     persona_name_copy
    nop
.endarea
.org 0x800ACC10
    addiu   t0, t0, 16                  ; was 11

.org BTLP_PRSCHG_DESC + 4
    .word PRSCHG_BUF
    .byte PERSONA_MAXLEN
.org BTLP_PRSCHG_DESC + 12 + 4
    .word PRSCHG_BUF + 16
    .byte PERSONA_MAXLEN
.org BTLP_PRSCHG_DESC + 24 + 4
    .word PRSCHG_BUF + 32
    .byte PERSONA_MAXLEN
