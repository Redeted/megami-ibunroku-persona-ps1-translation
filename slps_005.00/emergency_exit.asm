;; =============================================================
;; SLPS_005.00 - Emergency Exit (PSP item 385) in the unused item slot 111 (was "Last Mabble Pie", never given)
;;
;; Record = flags word (name - 4), name (10 glyphs, tools/items.py), +0xA battle skill, +0x16 field skill,
;; +0x18 sell price. Like Core Shield (flags 0x6040: used up after use, no target selection is handled in DNG):
;; field skill 0x71 = Traesto (dungeon effect: dng/traesto.asm), no battle use, sells for 5000 (buy 10000, PSP).
;; =============================================================
EE_NAME equ 0x8004520C
CS_NAME equ 0x800451EC

.ifdef QOL60                            ; QoL build only (equ above: armips allows none inside .ifdef)

.org EE_NAME - 4
    .byte 0xFF, 0x01, 0x40, 0x60
.org EE_NAME + 0x16
    .byte 0x71
.org EE_NAME + 0x18
    .word 5000

;; =============================================================
;; Clean Salt (PSP item 384: consumable, casts Estoma) in the unused item slot 110 (was "Last Abble Pie", never given)
;; Same flags as Emergency Exit (used up, no target selection in DNG), no battle use, no field skill: the dungeon
;; effect is dng/estoma.asm (item_use / item_usable hooks by id). Sells for 5000 (buy 10000, PSP).
;; =============================================================

.org CS_NAME - 4
    .byte 0xFF, 0x01, 0x40, 0x60
.org CS_NAME + 0x18
    .word 5000
.endif                                  ; QOL60
