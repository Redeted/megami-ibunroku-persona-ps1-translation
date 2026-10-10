;; =============================================================
;; BTLP.BIN - battle skill menu header: full Persona name + "Cost" label
;;
;; Original: 0x800AC800 copies the 10-byte name from the party Persona record
;; (battle copy, s0 = 0x8005CDA8 + slot*0x48) to 0x800F819C; the header line
;; is Pr. (x -128), Lv. (-88), level (-72), name (-48, 10 glyphs),
;; しょうかんSP (+48, 7 glyphs), summon cost (+104, 3 glyphs).
;; Now: name by Persona id (+0x1E) through persona_name_copy into
;; PERSONA_HDR_BUF (16 glyphs at x -52), label "Cost" at +80, value at +112.
;; =============================================================

.org 0x800AC800                         ; name copy (0x800AC800..0x800AC838)
.area 0x800AC83C - 0x800AC800, 0
    lbu     a1, 0x1E(s0)                ; Persona id (not in the delay slot: load delay)
    la      a0, PERSONA_HDR_BUF
    jal     persona_name_copy
    nop
.endarea

.org BTLP_HDR_NAME_DESC
    .halfword -52                       ; x (was -48)
.org BTLP_HDR_NAME_DESC + 4
    .word PERSONA_HDR_BUF
    .byte PERSONA_MAXLEN

.org 0x800DD744                         ; label string (was しょうかんSP + FF, 8 bytes)
    .byte 0xA8, 0x3A, 0x3E, 0x3F, 0xFF  ; "Cost" (C + lowercase o s t = smallfont_lc.LC_CODES, moved 2026-10-05)
.org BTLP_HDR_LABEL_DESC
    .halfword 80                        ; x (was 48)
.org BTLP_HDR_LABEL_DESC + 8
    .byte 4                             ; glyphs (was 7)

.org BTLP_HDR_VALUE_DESC
    .halfword 112                       ; x (was 104)
