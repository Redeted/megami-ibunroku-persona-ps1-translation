;; =============================================================
;; SLPS_005.00 - Estoma as a Persona skill, PSP style (2026-11-11)
;;
;; Skill id 0x70 (record 111, トラフーリ "Trafuri") becomes Estoma. Trafuri is not in the PSP skill table, and no PS1
;; Persona, demon (+0x14..+0x17 of the demon records) or item ever uses id 0x70; the PSP added Estoma as a new id
;; 243, which the PS1 table has no room for (243+ is other data). The data bytes become the PSP Estoma ones (= Traesto's
;; 66 00 11 FF 0A 00 FF: field-only, like Liftoma / Traesto). Effect: dng/traesto.asm (dungeon) and s2d/estoma.asm
;; (overworld) set the Clean Salt timer through the field-skill effect / usable tables. Name: tools/skills.py
;; (SKILLS.tsv 111), description: tools/descs.py (DESCS.tsv 110; Traesto's was a placeholder too, DESCS.tsv 111).
;;
;; Fusion: an item's type byte (name + 0x15, ADV 0x800A13D4) 0x00 means "teaches the skill at name + 0x16" (spell
;; stones); ADV 0x800A0710 writes it into the result's 7th skill slot (stock entry + 0x3A). Emergency Exit already has
;; 0x71 there (Traesto), Clean Salt gets 0x70 (Estoma), as on the PSP (both items teach their skill in fusion).
;;
;; Personas: the PSP adds Estoma / Traesto in one EMPTY slot of 7 Personas (PSP Persona table, 2026-11-09 research);
;; no skill is replaced and the 7th (fusion item) slot is untouched. Persona record skills: +0x20..+0x25.
;; =============================================================

ES_SKILL_ID     equ 0x70
ES_SKILL_REC    equ 0x80047D44 + ES_SKILL_ID * 0x14

.ifdef QOL60                            ; QoL build only (equ above: armips allows none inside .ifdef)

.org ES_SKILL_REC + 0x0A
    .byte 0x66, 0x00, 0x11, 0xFF, 0x0A, 0x00, 0xFF

.org 0x800451EC + 0x16                  ; Clean Salt (item 110): fusion / field skill
    .byte ES_SKILL_ID
.org 0x8004B0CC + 6 * 0x2C + 0x20 + 4 - 1 ; Cu Chulainn: Estoma
    .byte 0x70
.org 0x8004B0CC + 14 * 0x2C + 0x20 + 3 - 1 ; Urdr
    .byte 0x70
.org 0x8004B0CC + 40 * 0x2C + 0x20 + 2 - 1 ; Shouki
    .byte 0x70
.org 0x8004B0CC + 53 * 0x2C + 0x20 + 3 - 1 ; Byakko
    .byte 0x70
.org 0x8004B0CC + 52 * 0x2C + 0x20 + 2 - 1 ; Otohime: Traesto
    .byte 0x71
.org 0x8004B0CC + 54 * 0x2C + 0x20 + 4 - 1 ; Aonbarr
    .byte 0x71
.org 0x8004B0CC + 97 * 0x2C + 0x20 + 3 - 1 ; Quetzalcoatl
    .byte 0x71
.endif                                  ; QOL60
