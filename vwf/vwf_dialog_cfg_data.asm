;; =============================================================
;; Per-overlay config blocks for vwf_dialog_emit
;; Layout: VWF_CFG_STATE, VWF_CFG_ACTIVATE, VWF_CFG_UPLOAD_COUNT,
;;         VWF_CFG_UPLOAD_QUEUE (see vwf_dialog.asm)
;; =============================================================

.align 4
vwf_cfg_adv:
    .word ADV_TEXT_STATE, ADV_CELL_ACTIVATE, ADV_UPLOAD_COUNT, ADV_UPLOAD_QUEUE
vwf_cfg_dng:
    .word DNG_TEXT_STATE, DNG_CELL_ACTIVATE, DNG_UPLOAD_COUNT, DNG_UPLOAD_QUEUE
vwf_cfg_s2d:
    .word S2D_TEXT_STATE, S2D_CELL_ACTIVATE, S2D_UPLOAD_COUNT, S2D_UPLOAD_QUEUE
; extra words behind the 16-byte config block
BTCFG_STRUCT            equ 0x10
BTCFG_COUNT             equ 0x14
BTCFG_ENTRY             equ 0x18        ; queue entry {u32 src; u16 x,y,w,h}
vwf_cfg_btlp:                           ; BTLP: state is set per call (vwf/vwf_btlp.asm)
    .word 0, btlp_activate, vwf_cfg_btlp + BTCFG_COUNT, vwf_cfg_btlp + BTCFG_ENTRY
    .word 0                             ; BTCFG_STRUCT
    .word 0                             ; BTCFG_COUNT
    .fill 12, 0                         ; BTCFG_ENTRY
