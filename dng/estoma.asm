;; =============================================================
;; DNG.BIN - Clean Salt (item 110, slps_005.00/emergency_exit.asm): Estoma, as on the PSP (item 384 casts skill 243
;; "Estoma"): no random battles against formations that are all weaker than the party leader, for a while.
;;
;; Encounter: once per step, 0x8007099C rolls rand() % divisor (QoL build: cooldown and divisors doubled, constants
;; only); on a hit a random cell picks a formation from the floor list and writes it to 0x801F5350 (0x80070B40). The
;; hook there skips the battle ("no encounter this step", the step routine returns 0, cooldown untouched) when the
;; strongest demon of the formation (table dng/estoma_levels.asm, tools/estoma.py) is below the leader's level
;; (party list 0x801F256C[0] -> battle struct 0x801F1BCC + n * 0x60, level +0x4B). Fixed-formation cells (bit 0x80,
;; 0x80070A68) and event battles are never skipped. The roll itself is unchanged, so with the QoL build the two
;; combine: half as many rolls, and weak formations among them are skipped.
;;
;; Duration: like Liftoma (16 moon phases = 256 steps): the step routine 0x80069754 advances the moon every 16 steps
;; and counts Liftoma down (0x801F29A9); the hook at 0x8006979C counts Clean Salt down (fn_tr_vars, kernel RAM, so it
;; also survives battles / floor changes; it is not saved). At 0 it raises the dungeon "wore off" message 0x800A0D90;
;; the message hook 0x8006C0D8 then shows message 0x100 ("<FF09 item> wore off", DNG 0x8009A18C) with the item id
;; set to Clean Salt (normally Core Shield 0x12, restored for every other message).
;; Use: dng/traesto.asm item hooks -> dng_es_use / dng_es_usable (greyed while active, like Liftoma); the Persona
;; spell Estoma (skill 0x70, slps_005.00/estoma_skill.asm) -> dng_es_effect / dng_es_skill_usable, same timer.
;; =============================================================

ES_PHASES       equ 16                  ; moon phases (16 steps each), Liftoma's duration
ES_FORMATIONS   equ 0x168               ; tools/estoma.py COUNT
ES_PARTY        equ 0x801F256C          ; party list (member index, 0xFF = empty)
ES_MEMBERS      equ 0x801F1BCC          ; battle structs, 0x60 bytes
ES_LEVEL        equ 0x4B
ES_MSG_ITEM     equ 0x8009A18E          ; u16 item id of message 0x100 (<FF09 12 00> wore off)
ES_CORE_SHIELD  equ 0x12

.ifdef QOL60                            ; QoL build only (equ above: armips allows none inside .ifdef)

.org 0x80070B40                         ; random formation: lui at, 0x801F / sh v1, 0x5350(at) (v1 = formation id)
    j       dng_es_pick
    lui     at, 0x801F

.org 0x8006979C                         ; moon phase tick, before the Liftoma count: lui v1, 0x801F / ori v1, 0x29A9
    j       dng_es_tick
    nop

.org 0x8006C0D8                         ; "wore off" message: lui v0, 0x801F / lbu v0, 0x29A8(v0)
    j       dng_es_msg
    nop

.org dng_tr_end
.area DNG_EXT2_END - dng_tr_end
dng_es_pick:
    sh      v1, 0x5350(at)
    la      t0, fn_tr_vars
    lbu     t1, TRV_ES_TIMER(t0)
    andi    v1, v1, 0xFFFF
    beqz    t1, @@back
    sltiu   t1, v1, ES_FORMATIONS       ; 0xFFFF (empty list slot) is out of range too
    beqz    t1, @@back
    nop
    la      t0, estoma_levels
    addu    t0, t0, v1
    lbu     t0, 0(t0)                   ; strongest demon of the formation
    lui     t1, ES_PARTY >> 16
    lbu     t1, ES_PARTY & 0xFFFF(t1)   ; leader
    nop
    sll     t2, t1, 1
    addu    t2, t2, t1
    sll     t2, t2, 5                   ; * 0x60
    la      t1, ES_MEMBERS + ES_LEVEL
    addu    t1, t1, t2
    lbu     t1, 0(t1)                   ; leader level
    nop
    sltu    t0, t0, t1
    beqz    t0, @@back
    nop
    j       0x80070D44                  ; return 0: no battle on this step
    move    v0, zero
@@back:
    ori     v0, zero, 0xFFFF            ; 0x80070B48: andi v1 / beq v1, v0 (retry an empty slot) / cooldown
    j       0x80070B48
    nop

dng_es_tick:
    la      t0, fn_tr_vars
    lbu     t1, TRV_ES_TIMER(t0)
    nop
    beqz    t1, @@liftoma
    addiu   t1, t1, -1
    sb      t1, TRV_ES_TIMER(t0)
    bnez    t1, @@liftoma
    ori     t1, zero, 1
    sb      t1, TRV_ES_DONE(t0)
    lui     at, 0x800A
    sb      t1, 0x0D90(at)              ; "effect wore off" pending
@@liftoma:
    lui     v1, 0x801F
    j       0x800697A4
    ori     v1, v1, 0x29A9

dng_es_msg:
    la      t0, fn_tr_vars
    lbu     t1, TRV_ES_DONE(t0)
    la      t2, ES_MSG_ITEM
    beqz    t1, @@other
    ori     t1, zero, ES_CORE_SHIELD
    sb      zero, TRV_ES_DONE(t0)
    ori     t1, zero, ES_ITEM + 1
    sb      t1, 0(t2)
    j       0x8006C0F0                  ; jal 0x80073E84(0x100)
    ori     a0, zero, 0x100
@@other:
    sb      t1, 0(t2)
    lui     v0, 0x801F
    j       0x8006C0E0
    lbu     v0, 0x29A8(v0)

;; item_use (a1 = id - 1 = ES_ITEM): start / refresh the timer (called per member: idempotent)
dng_es_use:
    la      at, fn_tr_vars
    ori     v0, zero, ES_PHASES
    sb      v0, TRV_ES_TIMER(at)
    j       0x8008F3C4
    nop

;; Persona spell Estoma (skill 0x70): field-skill effect table case (0x8008F67C; idempotent per member)
dng_es_effect:
    la      at, fn_tr_vars
    ori     v0, zero, ES_PHASES
    j       0x8008F820
    sb      v0, TRV_ES_TIMER(at)

;; field-skill usable table case (0x8008F8CC): v1 = 1 while no Clean Salt / Estoma is active
dng_es_skill_usable:
    la      at, fn_tr_vars
    lbu     v0, TRV_ES_TIMER(at)
    nop
    j       0x8008F974
    sltiu   v1, v0, 1

;; item_usable (a0 = id - 1 = ES_ITEM): s0 = 1 while no Clean Salt is active
dng_es_usable:
    la      at, fn_tr_vars
    lbu     v0, TRV_ES_TIMER(at)
    nop
    j       0x8008F53C
    sltiu   s0, v0, 1

.include "dng/item_name.asm"                ; dng_item_name (full item names; also in the base build)

estoma_levels:
.include "dng/estoma_levels.asm"
.endarea
.endif                                  ; QOL60

.ifndef QOL60                                   ; base build: only the full-name FF09 insert in the second extension
.org DNG_EXT2_ADDR
.area DNG_EXT2_END - DNG_EXT2_ADDR
.include "dng/item_name.asm"
.endarea
.endif
