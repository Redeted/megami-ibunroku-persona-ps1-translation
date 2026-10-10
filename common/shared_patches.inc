;; =============================================================
;; Shared parametric macros for repetitive modifications
;; Call once per overlay with overlay-specific addresses
;; =============================================================

;; Dialogue VWF hooks. ADV, DNG and S2D carry copies of the same text
;; interpreter; this patches one copy to call the VWF engine through
;; its stub (vwf/vwf_dialog_cfg.asm).
;;   name_*: player-name insertion path   text_*: main text path
.macro vwf_dialog_hooks, stub, name_stub, name_emit, name_activate, name_inc, text_classify, text_two_byte, text_wide_arg, text_emit, text_activate, text_inc
    .org name_emit
        jal     name_stub               ; was jal <glyph renderer>
    .org name_activate
        nop                             ; was jal <cell activate>: engine activates cells
    .org name_inc
        addiu   v0, v0, 0               ; was pos+1: engine sets pos
    ; byte classification: two-byte only for 80-87 (was: any byte >= 0x80),
    ; so 88-E6 take the single-byte path as English VWF characters. That path
    ; then computes VRAM coords with a stale mask; the engine ignores them.
    .org text_classify
        xori    v0, a2, 0x80            ; was sltiu v0,a2,0x80
        sltiu   v0, v0, 8               ; v0 = 1 if 0x80 <= byte <= 0x87
        bne     v0, zero, text_two_byte ; was beqz v0,...; delay slot unchanged
    .org text_wide_arg
        ori     a2, s0, 0x8000          ; was move a2,s0: flag two-byte glyphs
    .org text_emit
        jal     stub
    .org text_activate
        nop
    .org text_inc
        addiu   v0, v0, 0
.endmacro
