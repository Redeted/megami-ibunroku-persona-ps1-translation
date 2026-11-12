;; =============================================================
;; BTLP.BIN - field-only Persona skills cannot be cast in battle (2026-11-11)
;;
;; The battle skill list greys a skill whose record byte +0x0A has bit 0x80 clear (0x800AC938): Mappa (0x6F),
;; Estoma (0x70, slps_005.00/estoma_skill.asm), Traesto (0x71) and Liftoma (0x73). The confirm (0x800A35F8) only
;; refused Liftoma by id (buzzer, back to the list): the others were cast with no battle effect, and a Persona that
;; now learns Estoma / Traesto could crash the battle. The check now refuses every greyed skill, the same way.
;; Code: in place (0x800A35F8..0x800A3614, the old id test) + the unreferenced 8-word BTLP function 0x800B9F58
;; (tools/deadovl.py).
;; =============================================================

.org 0x800A35F8                         ; (delay slot of the copy loop above: harmless there)
.area 0x800A3618 - 0x800A35F8
    lui     at, 0x800F
    addu    at, at, s0
    lbu     a2, 0x6E04(at)              ; selected skill id
    lui     at, 0x8004
    sll     v1, a2, 2
    addu    v1, v1, a2
    j       btl_field_only
    sll     v1, v1, 2                   ; id * 0x14
.endarea

.org 0x800B9F58
.area 0x800B9F78 - 0x800B9F58
btl_field_only:
    addu    at, at, v1
    lbu     v1, 0x7D4E(at)              ; skill record + 0x0A (0x80047D44 + id * 0x14)
    ori     v0, zero, 0xA2              ; for the next test (0x800A362C)
    andi    v1, v1, 0x80
    bnez    v1, 0x800A362C              ; usable in battle: continue
    nop
    j       0x800A3618                  ; greyed: buzzer, stay in the list (was Liftoma only)
    nop
.endarea
