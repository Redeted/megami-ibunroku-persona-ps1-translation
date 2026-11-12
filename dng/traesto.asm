;; =============================================================
;; DNG.BIN - Emergency Exit (item 111, slps_005.00/emergency_exit.asm) and Traesto (skill 0x71): warp the party back
;; to the dungeon entrance, as on the PSP ("ダンジョンの入口にワープする"). The PS1 has no effect for Traesto.
;;
;; Entrance = where the party stood when the dungeon was entered FROM THE OVERWORLD (previous mode 2): recorded at the
;; first frame of the field input handler after the DNG entry (map file, floor, x, y, facing) in kernel RAM (fn_tr_vars), since the overlay is
;; reloaded after every battle. Usable only on that map file: dungeons entered otherwise (e.g. the Snow Queen route
;; towers, entered from the frozen school) never record an entrance, so the item / spell is greyed out there.
;;
;; Kama Palace (map 0x0F) and Mana Castle (0x12) are reached from an event scene / another map file, never from the
;; overworld (S2D place tables), but the PSP allows the item there (user's research, 2026-11-11): for these two the
;; arrival point is recorded when the DNG is entered from an event (previous mode 3) or from another dungeon file
;; (previous mode 0) AND the last dungeon map seen was a different one (TRV_LAST), so coming back from a room inside
;; the dungeon, or a battle, never moves the entrance. The record (and the Clean Salt timer) is kept in the save's
;; location sector (slps_005.00/entrance_save.asm, open_exe/entrance_load.asm): after Continue on a dungeon save the
;; entry records nothing (TRV_LOADED) and the saved entrance stays usable.
;;
;; Warp: the effect only sets "pending"; the next call of the step routine 0x8006A73C returns 2 (warp tile) and the
;; warp lookup 0x8006C90C is replaced for that call by a transfer record to the entrance (0x801F5350: map, x, y,
;; floor, facing; next mode 0 = DNG), which the main loop handles like the stairs (same-file reposition 0x8006826C).
;;
;; Hooks: DNG entry 0x80064D50, step 0x8006A73C, warp lookup call 0x800680A4, field-skill usable table 0x80064B34 and
;; effect table 0x80064ADC (entry 0x71; entry 0x70 = Estoma, dng/estoma.asm), item use 0x8008F06C (ids >= 0x68), no
;; target selection for the item (0x8007A41C, with Skull Pendulum / Core Shield) and for the Persona spell (0x8007D1C4
;; and 0x8007D448, with Mappa / Liftoma; Estoma too).
;; =============================================================

TR_STATE_PTR    equ 0x800A0D70          ; -> dungeon state (0x801F0000): +0x15A0 map, +0x15A2 floor, +0x15A4 x, +0x15A6 y, +0x15A7 facing
TR_SKILL        equ 0x71                ; Traesto
TR_ITEM         equ 111                 ; Emergency Exit (0-based item id; the menus pass id + 1)
ES_ITEM         equ 110                 ; Clean Salt (dng/estoma.asm)
ES_SKILL        equ 0x70                ; Estoma (slps_005.00/estoma_skill.asm, was the unused Trafuri)
TRV_VALID       equ 0
TRV_FRESH       equ 1
TRV_PENDING     equ 2
TRV_FLOOR       equ 3
TRV_MAP         equ 4                   ; u16
TRV_X           equ 6
TRV_Y           equ 7
TRV_DIR         equ 8                   ; transfer-record format (0x801F5355)
TRV_ES_TIMER    equ 9                   ; Clean Salt: moon phases left (dng/estoma.asm)
TRV_ES_DONE     equ 10                  ; Clean Salt: show "wore off" next
TRV_LAST        equ 11                  ; last dungeon map seen by the field handler + 1 (0 = none)
TRV_LOADED      equ 12                  ; set by Continue on a dungeon save (open_exe/entrance_load.asm)
TR_MAP_KAMA     equ 0x0F                ; Kama Palace
TR_MAP_MANA     equ 0x12                ; Mana Castle

.ifdef QOL60                            ; QoL build only (equ above: armips allows none inside .ifdef)

.org 0x80064D50                         ; DNG entry: addiu sp, sp, -0xE8 / sw ra, 0xE4(sp)
    j       dng_tr_entry
    nop

.org 0x8006A73C                         ; step routine: lui v0, 0x800A / lbu v0, 0x368(v0)
    j       dng_tr_step
    nop

.org 0x80067D64                         ; field input handler 0x80067D40 (every frame), after its prologue:
    j       dng_tr_idle                 ; lw v0, 0x1580(a1) / nop
    nop

.org 0x800680A4                         ; step result 2 (warp tile): jal 0x8006C90C
    jal     dng_tr_warp

.org 0x80064ADC + (TR_SKILL - 0x5F) * 4 ; field-skill effect table (0x8008F67C)
    .word   dng_tr_effect
.org 0x80064B34 + (TR_SKILL - 0x5F) * 4 ; field-skill usable table (0x8008F8CC)
    .word   dng_tr_usable
.org 0x80064ADC + (ES_SKILL - 0x5F) * 4 ; Estoma (dng/estoma.asm)
    .word   dng_es_effect
.org 0x80064B34 + (ES_SKILL - 0x5F) * 4
    .word   dng_es_skill_usable

.org 0x8007A41C                         ; item menu: ids 0xF / 0x12 skip the target selection (s1 = id + 1)
    jal     dng_tr_item_notarget
    nop
    bnez    v0, 0x8007A544
    nop

.org 0x8007D1C4                         ; Persona spell menu: 0x6F / 0x73 skip the target selection (v1 = skill)
    jal     dng_tr_skill_notarget
    nop
    bnez    v0, 0x8007D2FC
    nop
.org 0x8007D448                         ; the same check in the second spell-menu path (0x8007D440 state)
    jal     dng_tr_skill_notarget
    nop
    bnez    v0, 0x8007D598
    nop

.org 0x8008F06C                         ; item_use: id - 1 >= 0x68 had no effect (delay slot move s1, a0 kept)
    beqz    v0, dng_tr_item_hi

.org 0x8008F428                         ; item_usable 0x8008F400 (menu grey-out): id - 1 >= 0x68 was "no"
    beqz    v0, dng_tr_usable_hi        ; (delay slot sw s2, 0x18(sp) kept)

.org DNG_EXT2_ADDR                      ; second DNG extension (common/addresses.inc); dng/estoma.asm follows
.area DNG_EXT2_END - DNG_EXT2_ADDR
dng_tr_entry:
    addiu   sp, sp, -0xE8
    sw      ra, 0xE4(sp)
    la      at, fn_tr_vars
    sb      zero, TRV_PENDING(at)
    sb      zero, TRV_ES_DONE(at)       ; the "wore off" request is cleared with 0x800A0D90 (0x80064DA8)
    lbu     v0, TRV_LOADED(at)          ; first entry after Continue on a dungeon save: the entrance came from
    nop                                 ; the save (slps_005.00/entrance_save.asm), record nothing
    bnez    v0, @@go
    sb      zero, TRV_LOADED(at)
    lui     v0, 0x8005
    lw      v0, 0x5C54(v0)              ; previous mode (gp + 0x60)
    ori     v1, zero, 2                 ; overworld: FRESH = 1 (always recorded)
    beq     v0, v1, @@set
    ori     v1, zero, 1
    beqz    v0, @@set                   ; another dungeon file: FRESH = 2 (Kama Palace / Mana Castle only)
    ori     v1, zero, 2
    ori     t0, zero, 3                 ; event scene: FRESH = 2
    bne     v0, t0, @@go
    nop
@@set:
    sb      v1, TRV_FRESH(at)
@@go:
    j       0x80064D58
    nop

dng_tr_step:
    la      at, fn_tr_vars
@@pending:
    lbu     v0, TRV_PENDING(at)
    nop
    beqz    v0, @@orig
    nop
    jr      ra                          ; "stepped on a warp tile"
    ori     v0, zero, 2
@@orig:
    lui     v0, 0x800A
    j       0x8006A744
    lbu     v0, 0x368(v0)

;; field input handler: a queued warp is taken at once (as "step result 2", s0 = 2) instead of reading the pad
dng_tr_idle:
    la      at, fn_tr_vars
    lhu     t0, 0x15A0(a1)              ; current map
    lbu     t1, TRV_LAST(at)
    addiu   t0, t0, 1
    sb      t0, TRV_LAST(at)
    lbu     v0, TRV_FRESH(at)
    nop
    beqz    v0, @@queued
    ori     t2, zero, 1
    beq     v0, t2, @@record            ; from the overworld
    sb      zero, TRV_FRESH(at)
    beq     t0, t1, @@queued            ; same dungeon as before: back from a room inside it
    ori     t2, zero, TR_MAP_KAMA + 1
    beq     t0, t2, @@record
    ori     t2, zero, TR_MAP_MANA + 1
    bne     t0, t2, @@queued
    nop
@@record:
    move    v0, a1                      ; dungeon state (a1, from the handler prologue; a1 / a3 kept)
    lhu     t0, 0x15A0(v0)
    nop
    sh      t0, TRV_MAP(at)
    lhu     t0, 0x15A2(v0)
    nop
    sb      t0, TRV_FLOOR(at)
    lbu     t0, 0x15A4(v0)
    nop
    sb      t0, TRV_X(at)
    lbu     t0, 0x15A6(v0)
    nop
    sb      t0, TRV_Y(at)
    lbu     t0, 0x15A7(v0)
    la      t1, dng_tr_dir
    andi    t0, t0, 3
    addu    t1, t1, t0
    lbu     t0, 0(t1)
    nop
    sb      t0, TRV_DIR(at)
    ori     t0, zero, 1
    sb      t0, TRV_VALID(at)
@@queued:
    lbu     v0, TRV_PENDING(at)
    nop
    beqz    v0, @@input
    nop
    j       0x800680A4
    ori     s0, zero, 2
@@input:
    lw      v0, 0x1580(a1)
    j       0x80067D6C
    nop

dng_tr_warp:
    la      at, fn_tr_vars
    lbu     v0, TRV_PENDING(at)
    nop
    beqz    v0, @@lookup
    nop
    sb      zero, TRV_PENDING(at)
    lui     v1, 0x801F
    lhu     v0, TRV_MAP(at)
    nop
    sh      v0, 0x5350(v1)
    lbu     v0, TRV_X(at)
    nop
    sb      v0, 0x5352(v1)
    lbu     v0, TRV_Y(at)
    nop
    sb      v0, 0x5353(v1)
    lbu     v0, TRV_FLOOR(at)
    nop
    sb      v0, 0x5354(v1)
    lbu     v0, TRV_DIR(at)
    nop
    sb      v0, 0x5355(v1)
    lui     v1, 0x8005
    jr      ra
    sw      zero, 0x5C5C(v1)            ; next mode 0: DNG (same map file: repositioned)
@@lookup:
    j       0x8006C90C
    nop

;; 0x8008F8CC case: v1 = 1 when the entrance of this map file is known (and no warp is pending yet)
dng_tr_usable:
    la      at, fn_tr_vars
    lbu     v0, TRV_VALID(at)
    nop
    beqz    v0, @@no
    nop
    lbu     v0, TRV_PENDING(at)
    nop
    bnez    v0, @@no
    nop
    lhu     v0, TRV_MAP(at)
    lui     v1, TR_STATE_PTR >> 16
    lw      v1, TR_STATE_PTR & 0xFFFF(v1)
    nop
    lhu     v1, 0x15A0(v1)
    nop
    bne     v0, v1, @@no
    nop
    j       0x8008F974
    ori     v1, zero, 1
@@no:
    j       0x8008F974
    move    v1, zero

;; 0x8008F67C case: queue the warp (the party may be several members: idempotent)
dng_tr_effect:
    la      at, fn_tr_vars
    ori     v0, zero, 1
    j       0x8008F820
    sb      v0, TRV_PENDING(at)

;; item_use, id - 1 (a1) >= 0x68
dng_tr_item_hi:
    ori     v0, zero, ES_ITEM
    beq     a1, v0, dng_es_use
    ori     v0, zero, TR_ITEM
    bne     a1, v0, @@out
    ori     a0, zero, 0xFF
    ori     a1, zero, 0xFF
    jal     0x8008F67C
    ori     a2, zero, TR_SKILL
@@out:
    j       0x8008F3C4
    nop

;; item_usable, id - 1 (a0) >= 0x68 (s0 = 0 = result)
dng_tr_usable_hi:
    ori     v0, zero, ES_ITEM
    beq     a0, v0, dng_es_usable
    ori     v0, zero, TR_ITEM
    bne     a0, v0, @@out
    nop
    jal     0x8008F8CC
    ori     a0, zero, TR_SKILL
    move    s0, v0
@@out:
    j       0x8008F53C
    nop

dng_tr_item_notarget:                   ; s1 = item id + 1 -> v0 = 1: no target selection
    ori     v0, zero, 0xF
    beq     s1, v0, @@yes
    ori     v0, zero, 0x12
    beq     s1, v0, @@yes
    ori     v0, zero, TR_ITEM + 1
    beq     s1, v0, @@yes
    ori     v0, zero, ES_ITEM + 1
    beq     s1, v0, @@yes
    nop
    jr      ra
    move    v0, zero
@@yes:
    jr      ra
    ori     v0, zero, 1

dng_tr_skill_notarget:                  ; v1 = skill (kept) -> v0 = 1: no target selection
    ori     v0, zero, 0x6F
    beq     v1, v0, @@yes
    ori     v0, zero, 0x73
    beq     v1, v0, @@yes
    ori     v0, zero, TR_SKILL
    beq     v1, v0, @@yes
    ori     v0, zero, ES_SKILL
    beq     v1, v0, @@yes
    nop
    jr      ra
    move    v0, zero
@@yes:
    jr      ra
    ori     v0, zero, 1

dng_tr_dir:                             ; facing 0x15A7 -> transfer-record facing (inverse of table 0x80099D1C)
    .byte   3, 0, 2, 1
.align 4
.endarea
dng_tr_end:
.endif                                  ; QOL60
