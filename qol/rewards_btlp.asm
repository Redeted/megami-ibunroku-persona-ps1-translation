;; =============================================================
;; QoL (separate enhancement build): EXP, Persona points (P.P.) and money after a battle x2 (BTLP.BIN).
;; During the battle each defeated enemy adds its EXP to 0x800F746C, its P.P. to 0x800F70F0 and its money
;; to 0x800F83A4. At the end, 0x80097930 (one call per battle) splits the EXP and P.P. totals between the
;; party members (software floating point, weighted by what each member did), and the results routine
;; 0x800AAB90 prints the money total and adds it to the wallet 0x801F2674. Each total is multiplied by 2
;; (x << 1) when it is first read there; the later reads see the new value.
;; =============================================================
.definelabel BTLQ_ADDR, 0x800F8900              ; behind the BTLP image (ends 0x800F88F8), inside its last loaded
                                                ; sector (ends 0x800F8BC4); nothing references this range

;; EXP split: first read of the total (v0 / v1 hold a result that is stored right after: keep them)
.org 0x80097A38
    jal     btlq_exp
    nop                                         ; was lw a0, 0x746C(a0)

;; P.P. split: first read of the total (v0 / v1 are not used before the next call)
.org 0x80097A88
    jal     btlq_pp
    nop                                         ; was lw a0, 0x70F0(a0)

;; results: money total for the screen and the wallet
.org 0x800AAD70
    jal     btlq_money
    nop                                         ; was lw a1, -0x7C5C(a1)

.org BTLQ_ADDR
.area 0x60
btlq_exp:                                       ; a0 = EXP total * 2 (stored back)
    lui     t0, 0x800F
    lw      a0, 0x746C(t0)
    nop
    sll     a0, a0, 1
    jr      ra
    sw      a0, 0x746C(t0)

btlq_pp:                                        ; a0 = P.P. total * 2 (stored back)
    lui     t0, 0x800F
    lw      a0, 0x70F0(t0)
    nop
    sll     a0, a0, 1
    jr      ra
    sw      a0, 0x70F0(t0)

btlq_money:                                     ; a1 = money total * 2 (stored back)
    lui     t0, 0x8010
    lw      a1, -0x7C5C(t0)
    nop
    sll     a1, a1, 1
    jr      ra
    sw      a1, -0x7C5C(t0)
.endarea
