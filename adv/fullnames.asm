;; =============================================================
;; ADV.BIN - item names as full-name markers (slps_005.00/fullnames.asm)
;;
;; 0x80067C00 = string-to-map copy (a0 = glyph bytes, a1 = GsBG map cell, a2 = glyph offset, a3 = max count). Item
;; names reach it from the item-name helper 0x80090164 (40 callers) and from inlined copies of that helper (equipment
;; list redraw 0x800914E4 ...): fn_adv_copy (kernel RAM) turns those copies into one marker cell that the resident cell
;; sorter expands into the full proportional name; any other string is copied as before.
;; =============================================================

.org 0x80067C00
    lui     t9, 0x8006                          ; was andi v0, a3, 0xFFFF
    j       fn_adv_copy                         ; was beq v0, zero, 0x80067C44
    ori     t9, t9, 0x7C0C                      ; was nop. t9 = copy + 0xC (the plain path returns there)

;; Persona status page bar: proportional arcana + full Persona name (drawer cell-advance, page function, name object)
    persona_bar_hooks 0x80065C60, 0x80070144, 0x800B2170

;; The Velvet Room Persona page (0x8009F8E8: fusion result preview, owned Personas, Persona compendium) fills the
;; same bar itself, not through 0x80070144, so after the name object was re-pointed to fn_bar_cells it drew an empty
;; name (only the arcana). Same treatment here: clear 16 cells of fn_bar_cells, full name through fn_bar_name,
;; proportional arcana through fn_bar_fill.
.org 0x8009F954                                 ; clear the name string
    lui     a0, (fn_bar_cells >> 16) + ((fn_bar_cells >> 15) & 1)
    addiu   a0, a0, fn_bar_cells & 0xFFFF       ; was 0x800B2114
    jal     0x8008F5B4
    ori     a1, zero, 16                        ; was 10
.org 0x8009FB40                                 ; master record branch (s3 = record of id s5 >> 6)
    jal     fn_bar_name
    sra     a1, s5, 6                           ; Persona id
    nop
    nop
    nop
    nop
.org 0x8009FB84
    jal     fn_bar_fill                         ; arcana (was 0x8008F730, same arguments)
.org 0x8009FE38                                 ; owned-Persona branch (s4 = stock entry, id at +0x18)
    jal     fn_bar_name
    lbu     a1, 0x18(s4)                        ; Persona id
    nop
    nop
    nop
    nop
.org 0x8009FE7C
    jal     fn_bar_fill                         ; arcana

;; ANALYZE demon page bar: proportional race + full demon name (name fill jal, name object)
    analyze_bar_hooks 0x8009903C, 0x800BA11C

;; Message-box name inserts (text interpreter 0x800666DC, jump table 0x800643F0..): <FF09> item, <FF0A> skill and
;; <FF0C> Persona printed the 10-glyph record name ("ST INCENSE", "Seimen Kon" in the Velvet Room gift speech).
;; They now print the full name from fn_btl_buf (kernel RAM, battle-only otherwise; fn_buf is busy with the menu
;; markers on screen). A handler leaves 0xC(s1) = the last parameter byte, s2 = the glyphs (FF-terminated),
;; 0x35(s1) = max glyphs, flags |= 0x4001, and goes to the reader 0x80066CF0.
.org 0x8006712C                                 ; <FF09 lo hi>: 13 words (to 0x80067160)
.area 0x80067160 - 0x8006712C
    lbu     s0, 0(s2)
    addiu   s2, s2, 1
    sw      s2, 0xC(s1)
    lbu     v0, 0(s2)
    lui     a1, (fn_btl_buf >> 16) + ((fn_btl_buf >> 15) & 1)
    sll     v0, v0, 8
    or      s2, s0, v0                          ; item id
    move    t6, s5                              ; fn_item_text clobbers v0, v1, at, t3, t5, s5
    jal     fn_item_text                        ; title-cased full name at a1, FF-terminated
    addiu   a1, a1, fn_btl_buf & 0xFFFF
    move    s5, t6
    j       adv_ins_go
    nop
.endarea

.org 0x80067160                                 ; <FF0A id>: 11 words (to 0x8006718C)
.area 0x8006718C - 0x80067160
    sw      s2, 0xC(s1)
    lbu     a1, 0(s2)
    lui     a0, (fn_btl_buf >> 16) + ((fn_btl_buf >> 15) & 1)
    jal     skill_name_copy                     ; 15 glyphs, blank-padded; a0 = the end
    addiu   a0, a0, fn_btl_buf & 0xFFFF
    j       adv_ins_trim
    nop
.endarea

.org 0x800671C4                                 ; <FF0C id>: 16 words (to 0x80067204)
.area 0x80067204 - 0x800671C4
    sw      s2, 0xC(s1)
    lbu     a1, 0(s2)
    lui     a0, (fn_btl_buf >> 16) + ((fn_btl_buf >> 15) & 1)
    jal     persona_name_copy                   ; 16 glyphs, blank-padded; a0 = the end
    addiu   a0, a0, fn_btl_buf & 0xFFFF
adv_ins_trim:                                   ; a0 = end of a blank-padded name: FF after its last real glyph
    lbu     v0, -1(a0)
    nop
    beqz    v0, adv_ins_trim
    addiu   a0, a0, -1
    ori     v0, zero, 0xFF
    j       adv_ins_go
    sb      v0, 1(a0)
.endarea

.org 0x800662EC                                 ; rest of the dead function behind party_count_fix_adv
.area 0x80066324 - 0x800662EC                   ; (build/partynames_adv.asm, 0x800662D4 + 0x50)
adv_ins_go:
    lui     s2, (fn_btl_buf >> 16) + ((fn_btl_buf >> 15) & 1)
    addiu   s2, s2, fn_btl_buf & 0xFFFF
    ori     v0, zero, FN_BUF_SIZE - 1
    sb      v0, 0x35(s1)
    lw      v0, 0(s1)
    nop
    ori     v0, v0, 0x4001
    j       0x80066CF0
    sw      v0, 0(s1)
.endarea
