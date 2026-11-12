;; =============================================================
;; BTLP.BIN - battle result screen: full name of the dropped item (slps_005.00/fullnames.asm)
;;
;; The result screen's ITEM line is layout entry 0x800DF7A8 (x, y, string 0x800F7DBC, max 10 glyphs) printed by the
;; fixed 8 px text drawer 0x80088E80; the item code copied the 10-glyph record name there (0x800AADE4..0x800AAE64,
;; id = 0x800F7EB8, 1-based). Now: fn_btl_drop writes the full name into fn_btl_buf (kernel RAM), the entry points
;; there with a 31-glyph limit, and the drawer's glyph x comes from fn_btl_x (proportional for that string only).
;; =============================================================

.org 0x800AADE4                                 ; v0 = id * 0x20, a3 = id (kept for the add-item call at 0x800AAE68)
    jal     fn_btl_drop
    srl     a0, v0, 5
    j       0x800AAE68
    nop

.org 0x80088F84                                 ; was sll v1, t0, 3 / addu v0, v0, v1
    jal     fn_btl_x
    nop

.org 0x800DF7AC                                 ; result layout entry: string, max glyphs
    .word   fn_btl_buf
    .byte   31

;; Battle messages ("Obtained <item>" ...): the item name insert (name setter 0x8007A920 kind 3, slot 0x800EBDE0 with
;; the 10-glyph uppercase record name) becomes the full title-cased name in fn_btl_msg (fn_btl_msg_item).
.org 0x8007A9DC                                 ; was j 0x8007A9FC / addiu a0, s0, 96
    j       fn_btl_msg_item
    nop

.org 0x8007CC18                                 ; text reader, item slot: was lui v0, 0x800F / addiu v0, v0, -16928
    lui     v0, (fn_btl_msg >> 16) + ((fn_btl_msg >> 15) & 1)
    addiu   v0, v0, fn_btl_msg & 0xFFFF

;; Battle ITEM list (FIGHT > ITEM): full proportional names. The filler 0x800ACF0C copies the 10-glyph record names
;; of the 12 listed items (id | count << 9 words at FN_BTL_IDS) into 10-byte slots at 0x800F81CC; layout 0x800DD828
;; (24 entries: 12 names, 12 counts) prints them with the text drawer 0x80088E80 (t4 = entry index, a2 = entry + 8).
;; fn_btl_ent (in the name-copy code that fn_btl_drop made dead, 0x800AADF4-0x800AAE68) runs at each entry start: an
;; entry 0-11 whose string equals the record name of the item listed in that slot is printed from fn_btl_buf with the
;; full name (fn_btl_drop; proportional through fn_btl_x, max glyphs through fn_btl_max). Anything else (other
;; layouts, the slots' other filler 0x800AD41C) does not match and prints as before. t7 is free in the drawer.
.org 0x80088F04                                 ; entry start: was lbu v0, 0(a2) / lw a3, -4(a2)
    jal     fn_btl_ent                          ; v0 must be loaded HERE: a load in fn_btl_ent's jr delay slot is not
    lbu     v0, 0(a2)                           ; visible to the "blez v0" at the return address (R3000 load delay)

.org 0x800890EC                                 ; glyph loop: was lbu v0, 0(a2) / nop
    jal     fn_btl_max
    nop

.org 0x800AADF4
.area 0x800AAE68 - 0x800AADF4
fn_btl_ent:
    lw      a3, -4(a2)
    sltiu   at, t4, 12
    beqz    at, @@ret
    sll     v1, t4, 1
    lui     at, (FN_BTL_IDS >> 16) + ((FN_BTL_IDS >> 15) & 1)
    addu    at, at, v1
    lhu     a0, FN_BTL_IDS & 0xFFFF(at)
    lui     at, FN_ITEM_NAMES >> 16
    andi    a0, a0, 0x1FF                       ; a0 = item id
    beqz    a0, @@ret
    sll     v1, a0, 5
    addu    v1, v1, at
    ori     a1, zero, 10
@@cmp:
    lbu     t8, FN_ITEM_NAMES & 0xFFFF(v1)      ; t8 (not v0: v0 = max glyphs from the hook's delay slot)
    lbu     at, 0(a3)
    addiu   v1, v1, 1
    bne     t8, at, @@ne
    addiu   a3, a3, 1
    addiu   a1, a1, -1
    bnez    a1, @@cmp
    move    t7, ra
    jal     fn_btl_drop                         ; fn_btl_buf = full name of a0 (keeps a2, a3, t*)
    lui     a3, (fn_btl_buf >> 16) + ((fn_btl_buf >> 15) & 1)
    addiu   a3, a3, fn_btl_buf & 0xFFFF
    jr      t7
    ori     v0, zero, 31
@@ne:
    lw      a3, -4(a2)
@@ret:
    jr      ra
    nop
.endarea
