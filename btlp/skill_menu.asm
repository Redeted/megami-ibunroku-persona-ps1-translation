;; =============================================================
;; BTLP.BIN - battle skill menu with full-length skill names
;;
;; Original: three loops copy 10 bytes of each skill name of the current
;; Persona into 0x800F7CB8 + slot*11 (byte 0 = FF marks an empty slot) and
;; two sets of 7 small-font text descriptors draw 10 glyphs from there.
;; Now: the copies call skill_name_copy (slps_005.00/skill_names.asm) into
;; SKILL_MENU_BUF + slot*16, the descriptors draw 15 glyphs from it.
;; Each replaced copy body may clobber v0 v1 a0 a1 a2 at (the original did);
;; the enclosing functions are non-leaf (ra saved on the stack).
;; =============================================================

;; --- descriptors: pointer + glyph count ---
.macro skill_desc, base
    .org base + 4
    .word SKILL_MENU_BUF
    .byte SKILL_MAXLEN
    .org base + 12 + 4
    .word SKILL_MENU_BUF + 16
    .byte SKILL_MAXLEN
    .org base + 24 + 4
    .word SKILL_MENU_BUF + 32
    .byte SKILL_MAXLEN
    .org base + 36 + 4
    .word SKILL_MENU_BUF + 48
    .byte SKILL_MAXLEN
    .org base + 48 + 4
    .word SKILL_MENU_BUF + 64
    .byte SKILL_MAXLEN
    .org base + 60 + 4
    .word SKILL_MENU_BUF + 80
    .byte SKILL_MAXLEN
    .org base + 72 + 4
    .word SKILL_MENU_BUF + 96
    .byte SKILL_MAXLEN
.endmacro

skill_desc BTLP_SKILL_DESC_A
skill_desc BTLP_SKILL_DESC_B

;; --- loop 1 (0x800AC8F8, menu build; t2 = FF offset, t3 = slot+1 after the increment) ---
.org 0x800AC908
    lui     at, hi(SKILL_MENU_BUF)      ; FF marker of the slot
    addiu   at, at, lo(SKILL_MENU_BUF)
.org 0x800AC924
    addiu   t2, t2, 16                  ; was 11
.org 0x800AC978                         ; copy body 0x800AC978..0x800ACA40
.area 0x800ACA44 - 0x800AC978, 0
    sll     a0, t3, 4
    lui     at, hi(SKILL_MENU_BUF - 16)
    addiu   at, at, lo(SKILL_MENU_BUF - 16)
    move    a1, v1                      ; skill id
    jal     skill_name_copy
    addu    a0, a0, at
    b       0x800ACA44
    nop
.endarea

;; --- loop 2 (0x800A5634; t1 = FF offset, a3 = slot) ---
.org 0x800A5634
    lui     at, hi(SKILL_MENU_BUF)
    addiu   at, at, lo(SKILL_MENU_BUF)
.org 0x800A5650
    addiu   t1, t1, 16                  ; was 11
.org 0x800A5654                         ; copy body 0x800A5654..0x800A5690 (0x800A5694 addiu t0 kept)
.area 0x800A5694 - 0x800A5654, 0
    sll     a0, a3, 4
    lui     at, hi(SKILL_MENU_BUF)
    addiu   at, at, lo(SKILL_MENU_BUF)
    move    a1, v1
    jal     skill_name_copy
    addu    a0, a0, at
.endarea

;; --- loop 3 (0x800ACC40; same shape as loop 2) ---
.org 0x800ACC40
    lui     at, hi(SKILL_MENU_BUF)
    addiu   at, at, lo(SKILL_MENU_BUF)
.org 0x800ACC5C
    addiu   t1, t1, 16                  ; was 11
.org 0x800ACC60
.area 0x800ACCA0 - 0x800ACC60, 0
    sll     a0, a3, 4
    lui     at, hi(SKILL_MENU_BUF)
    addiu   at, at, lo(SKILL_MENU_BUF)
    move    a1, v1
    jal     skill_name_copy
    addu    a0, a0, at
.endarea

;; --- empty-slot test (cursor movement): slot*11 -> slot*16 ---
.org 0x800A5328
    sll     v0, v1, 4
    nop
    nop
    nop
    lui     at, hi(SKILL_MENU_BUF)
    addiu   at, at, lo(SKILL_MENU_BUF)
