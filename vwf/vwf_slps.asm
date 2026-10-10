;; =============================================================
;; SLPS_005.00 - home of the dialogue VWF engine
;;
;; The engine, its ring buffer and tables live in functions of the main
;; executable that no code or data on the disc references (found with
;; tools/deadfuncs.py; never executed in runtime breakpoint tests). The main
;; executable is resident, so this memory is never reused for anything else.
;; English glyph bitmaps live in unused FONT.BIN slots (font/vwf_glyphs.asm).
;; =============================================================

.include "vwf/vwf_btlp_defs.asm"

.org VWF_CODE_A_ADDR
.area VWF_CODE_A_SIZE
.include "vwf/vwf_dialog.asm"
.include "vwf/vwf_dialog_cfg.asm"
.endarea

.org VWF_CODE_B_ADDR
.area VWF_CODE_B_SIZE
.include "vwf/vwf_dialog_draw.asm"
.endarea

.org VWF_NAME_CODE_ADDR
.area VWF_NAME_CODE_SIZE
.include "vwf/vwf_name_map.asm"
.endarea

.org VWF_DATA_ADDR
.area VWF_DATA_SIZE
.align 4
vwf_dlg_ring:                           ; RING_CELLS x 16x16 4bpp cells
    .fill RING_CELLS * CELL_BYTES, 0
vwf_dlg_state:                          ; DLG_PX, DLG_LINE, DLG_INIT, DLG_LAST
    .halfword 0, 0xFFFF, 0xFFFF, 0
    .byte 2, 1, 2, 0                    ; DLG_COLOR_MAIN, DLG_COLOR_SHADOW, DLG_SHADOW_DX
.include "vwf/vwf_dialog_cfg_data.asm"
.endarea

.org VWF_TABLE_ADDR
.area VWF_TABLE_SIZE
vwf_font_index:                         ; u16 offset of each glyph inside FONT.BIN
    .incbin "font/vwf_index.bin"
vwf_font_width:                         ; u8 pen advance
    .incbin "font/vwf_width.bin"
.align 4
.include "build/name_vwf_tables.asm"    ; vwf_name_lc, vwf_name_sym (tools/name_grid.py)
.endarea

;; BTLP (negotiation text) hook code: unreferenced SLPS fragment
.org VWF_BTLP_CODE_ADDR
.area VWF_BTLP_CODE_SIZE
.include "vwf/vwf_btlp_activate.asm"
.endarea
.org VWF_BTLP_CODE2_ADDR
.area VWF_BTLP_CODE2_SIZE
.include "vwf/vwf_btlp.asm"
.align 4
.include "vwf/vwf_btlp_str16_act.asm"
.endarea
