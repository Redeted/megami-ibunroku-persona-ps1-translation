;; =============================================================
;; Per-overlay entry stubs for vwf_dialog_emit
;; (config blocks: vwf_dialog_cfg_data.asm)
;; =============================================================

.macro vwf_dialog_stub, name, cfg, path
name:
    lui     a0, ((cfg + 0x8000) >> 16) & 0xFFFF   ; %hi with addiu sign adjust
    addiu   a0, a0, cfg & 0xFFFF
    j       vwf_dialog_emit
    li      a1, path                    ; 0 = text path, 1 = name-insertion path
.endmacro

vwf_dialog_stub vwf_adv_emit, vwf_cfg_adv, 0
vwf_dialog_stub vwf_adv_name_emit, vwf_cfg_adv, 1
vwf_dialog_stub vwf_dng_emit, vwf_cfg_dng, 0
vwf_dialog_stub vwf_dng_name_emit, vwf_cfg_dng, 1
vwf_dialog_stub vwf_s2d_emit, vwf_cfg_s2d, 0
vwf_dialog_stub vwf_s2d_name_emit, vwf_cfg_s2d, 1
