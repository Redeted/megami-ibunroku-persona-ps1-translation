;; =============================================================
;; Address definitions and filename constants - single source of truth
;; Naming: OVERLAY_FUNCTION_PURPOSE_ADDR for addresses
;;         OVERLAY_FILENAME / OVERLAY_OUTPUT for binary filenames
;; Suffixes: _LUI_ADDR (pointer load), _WIDTH_ADDR, _COLUMN_ADDR
;; =============================================================

;; PS-X EXE files carry a 0x800-byte header before t_addr.
;; .open base = t_addr - header so file offset 0 lines up.
PSX_EXE_HEADER_SIZE equ 0x800

;; Shared overlay slot. ADV/BTLP/CASINO/DNG/S2D/NAME.BIN all load here;
;; file offset 0 is the overlay ID word. Runtime-confirmed for ADV.BIN
;; (99.6% of words match RAM); assumed identical for the others.
OVERLAY_SLOT_ADDR equ 0x800643C4

;; --- SLPS_005.00 - Main executable (resident), t_addr 0x80010000 ---
SLPS_FILENAME equ "original/SLPS_005.00"
SLPS_OUTPUT equ "build/SLPS_005.00"
SLPS_ADDR equ 0x80010000 - PSX_EXE_HEADER_SIZE
;; Free space: zero padding at the end of the EXE's data.
;; NOT YET VERIFIED as unused - set a write watchpoint on this range
;; during gameplay before relocating strings into it.
; WARNING: NOT free at runtime - 0x80055C34 is the CD-ready flag (hangs the game if overwritten). Do not use.
SLPS_FREE_START equ 0x80055C10
SLPS_FREE_END equ 0x80056000

;; --- FONT.BIN (resident at 0x801E0000, loaded once at boot) ---
FONT_FILENAME equ "original/FONT.BIN"
FONT_OUTPUT equ "build/FONT.BIN"
FONT_GLYPHS_ADDR equ 0x801E0000

;; --- VWF engine home: unreferenced SLPS_005.00 functions (tools/deadfuncs.py) ---
;; Verified: no jal/j, address word or lui pair to them on the disc, and no
;; hits from execution breakpoints in title, event, name entry, field and
;; hospital save states.
VWF_CODE_A_ADDR equ 0x8002E7BC           ; 0x8002E7BC + 0x8002E7FC
VWF_CODE_A_SIZE equ 0x8002EAA8 - VWF_CODE_A_ADDR
VWF_CODE_B_ADDR equ 0x800121B0           ; 4 functions
VWF_CODE_B_SIZE equ 0x80012484 - VWF_CODE_B_ADDR
VWF_DATA_ADDR equ 0x80021848             ; 2 functions
VWF_DATA_SIZE equ 0x80021AB8 - VWF_DATA_ADDR
VWF_TABLE_ADDR equ 0x8001D8D4            ; 2 functions
VWF_TABLE_SIZE equ 0x8001DAA4 - VWF_TABLE_ADDR
VWF_BTLP_CODE_ADDR equ 0x800124B4        ; 1 dead function (328 bytes)
VWF_BTLP_CODE_SIZE equ 0x800125FC - VWF_BTLP_CODE_ADDR
VWF_BTLP_CODE2_ADDR equ 0x8001EE84       ; dead fragment (284 bytes)
VWF_BTLP_CODE2_SIZE equ 0x8001EFA0 - VWF_BTLP_CODE2_ADDR
VWF_NAME_CODE_ADDR equ 0x80015510        ; dead function (252 bytes): vwf_name_map (typed names -> narrow English)
VWF_NAME_CODE_SIZE equ 0x8001560C - VWF_NAME_CODE_ADDR

;; --- ADV.BIN - Overlay #7: field / events ---
ADV_FILENAME equ "original/ADV.BIN"
ADV_OUTPUT equ "build/ADV.BIN"
ADV_ADDR equ OVERLAY_SLOT_ADDR
;; dialogue text interpreter (0x800669AC) - runtime-verified
ADV_TEXT_STATE equ 0x800E1E4C              ; +0xA u16 pos (cell 0-59), +0xC read ptr
ADV_CELL_ACTIVATE equ 0x80067908           ; void(u16 pos)
ADV_UPLOAD_COUNT equ 0x800BC714            ; LoadImage queue count
ADV_UPLOAD_QUEUE equ 0x800BC748            ; LoadImage queue entries
ADV_NAME_EMIT_JAL_ADDR equ 0x80066DA0      ; jal glyph renderer (name chars)
ADV_NAME_ACTIVATE_JAL_ADDR equ 0x80066DAC  ; jal cell activate
ADV_NAME_POS_INC_ADDR equ 0x80066DC0       ; addiu v0,v0,1 (pos++)
ADV_TEXT_CLASSIFY_ADDR equ 0x800677BC      ; sltiu v0,a2,0x80 / beqz v0 (3 words)
ADV_TEXT_TWO_BYTE_ADDR equ 0x800677F8      ; two-byte glyph decode path
ADV_TEXT_WIDE_ARG_ADDR equ 0x8006783C      ; move a2,s0 (two-byte glyph arg)
ADV_TEXT_EMIT_JAL_ADDR equ 0x80067840      ; jal glyph renderer (text)
ADV_TEXT_ACTIVATE_JAL_ADDR equ 0x8006784C  ; jal cell activate
ADV_TEXT_POS_INC_ADDR equ 0x80067860       ; addiu v0,v0,1 (pos++)

;; --- BTLP.BIN - Overlay #5: battle ---
BTLP_FILENAME equ "original/BTLP.BIN"
BTLP_OUTPUT equ "build/BTLP.BIN"
BTLP_ADDR equ OVERLAY_SLOT_ADDR
;; text interpreter 0x8007C9E0 calls the glyph function 0x8007C754(struct, ptr) -> ptr here
BTLP_TEXT_EMIT_JAL_ADDR equ 0x8007CCD4
BTLP_TEXT_EMIT2_JAL_ADDR equ 0x8007CF80
;; battle skill menu (btlp/skill_menu.asm): 7 small-font text descriptors per set (x, y, ptr, count ...),
;; filled by three copy loops; English names use a 16-byte stride buffer in SLPS (SKILL_MENU_BUF)
BTLP_SKILL_DESC_A equ 0x800DD788       ; 7 x 12 bytes, ptr at +4, glyph count at +8
BTLP_SKILL_DESC_B equ 0x800DDD68       ; second set, same buffer

;; --- full-length skill names (tools/skills.py, slps_005.00/skill_names.asm) ---
SKILL_RECORDS_ADDR equ 0x80047D44      ; + id*0x14 (id 1-based)
SKILL_FIELD equ 10
SKILL_SPARE equ 0x11                   ; unreferenced record bytes +0x11..+0x13
SKILL_MAXLEN equ 15
SKILL_CODE_ADDR equ 0x80011FBC         ; unreferenced function (taken from tools/choices.py FREE)
SKILL_CODE_SIZE equ 0x800120A4 - SKILL_CODE_ADDR
SKILL_TAILS_ADDR equ 0x8004CE6F         ; affinity records 63-95 (unused 'リザーブ' slots, tools/affinity.py FREE)
SKILL_TAILS_SIZE equ 0x70               ; 105 bytes used (offsets are one byte)
AFF_FREE2_ADDR equ 0x8004CEE0            ; rest of the free affinity records: slps_005.00/aff_free.asm
AFF_FREE_END equ 0x8004D1A8              ; record 96 starts here
VWF_SMALL_MAP_LEN equ 0xD0
SKILL_MENU_BUF equ 0x8002C248          ; 7 x 16 bytes, unreferenced function (taken from tools/s2dnames.py SPILL)
SKILL_MENU_BUF_END equ 0x8002C2B8          ; 0x8002C2B8-0x8002C2F0: banner names (tools/banner.py)

;; --- CASINO.BIN - Overlay #8: casino ---
CASINO_FILENAME equ "original/CASINO.BIN"
CASINO_OUTPUT equ "build/CASINO.BIN"
CASINO_ADDR equ OVERLAY_SLOT_ADDR

;; --- DNG.BIN - Overlay #4: dungeon ---
DNG_FILENAME equ "original/DNG.BIN"
DNG_OUTPUT equ "build/DNG.BIN"
DNG_ADDR equ OVERLAY_SLOT_ADDR
;; dialogue text interpreter: copy of ADV's (main path at ADV+0xFC2C).
;; Statically derived (jal targets consistent with base) - not yet run.
DNG_GLUE_ADDR equ 0x800A1200           ; extension of DNG.BIN behind the image (dng/vwf_script.asm)
DNG_TEXT_STATE equ 0x800E1E4C
DNG_CELL_ACTIVATE equ 0x80077534
DNG_UPLOAD_COUNT equ 0x800A072C
DNG_UPLOAD_QUEUE equ 0x800A0760
DNG_NAME_EMIT_JAL_ADDR equ 0x80076BD0
DNG_NAME_ACTIVATE_JAL_ADDR equ 0x80076BDC
DNG_NAME_POS_INC_ADDR equ 0x80076BF0
DNG_TEXT_CLASSIFY_ADDR equ 0x800773E8
DNG_TEXT_TWO_BYTE_ADDR equ 0x80077424
DNG_TEXT_WIDE_ARG_ADDR equ 0x80077468
DNG_TEXT_EMIT_JAL_ADDR equ 0x8007746C
DNG_TEXT_ACTIVATE_JAL_ADDR equ 0x80077478
DNG_TEXT_POS_INC_ADDR equ 0x8007748C

;; --- S2D.BIN - Overlay #6: 2D map ---
S2D_FILENAME equ "original/S2D.BIN"
S2D_OUTPUT equ "build/S2D.BIN"
S2D_ADDR equ OVERLAY_SLOT_ADDR
;; dialogue text interpreter: copy of ADV's (main path at ADV-0x820).
;; Statically derived (jal targets consistent with base) - not yet run.
S2D_TEXT_STATE equ 0x80101E4C
;; extension of S2D.BIN behind its last sector (RAM 0x800BA3C4..): English overworld boxes (tools/s2dscript.py SPILL = ..0x800BB200), then VWF glue code
S2D_GLUE_ADDR equ 0x800BB200
S2D_GLUE_SIZE equ 0x800BB8E8 - S2D_GLUE_ADDR
S2D_CELL_ACTIVATE equ 0x800670E8
S2D_UPLOAD_COUNT equ 0x800B92C8
S2D_UPLOAD_QUEUE equ 0x800B92FC
S2D_NAME_EMIT_JAL_ADDR equ 0x80066784
S2D_NAME_ACTIVATE_JAL_ADDR equ 0x80066790
S2D_NAME_POS_INC_ADDR equ 0x800667A4
S2D_TEXT_CLASSIFY_ADDR equ 0x80066F9C
S2D_TEXT_TWO_BYTE_ADDR equ 0x80066FD8
S2D_TEXT_WIDE_ARG_ADDR equ 0x8006701C
S2D_TEXT_EMIT_JAL_ADDR equ 0x80067020
S2D_TEXT_ACTIVATE_JAL_ADDR equ 0x8006702C
S2D_TEXT_POS_INC_ADDR equ 0x80067040

;; --- NAME.BIN - Overlay #9: name entry ---
NAME_FILENAME equ "original/NAME.BIN"
NAME_OUTPUT equ "build/NAME.BIN"
NAME_ADDR equ OVERLAY_SLOT_ADDR

;; --- OPEN.BIN - Title/opening data archive (seen resident at 0x80180000) ---
OPEN_FILENAME equ "original/OPEN.BIN"
OPEN_OUTPUT equ "build/OPEN.BIN"
OPEN_ADDR equ 0x80180000

;; --- EXE/ATLUS.EXE - Atlus logo EXE, t_addr 0x80080000 ---
ATLUS_EXE_FILENAME equ "original/EXE/ATLUS.EXE"
ATLUS_EXE_OUTPUT equ "build/EXE/ATLUS.EXE"
ATLUS_EXE_ADDR equ 0x80080000 - PSX_EXE_HEADER_SIZE

;; --- EXE/OPEN.EXE - Opening/title EXE, t_addr 0x80080000 ---
OPEN_EXE_FILENAME equ "original/EXE/OPEN.EXE"
OPEN_EXE_OUTPUT equ "build/EXE/OPEN.EXE"
OPEN_EXE_ADDR equ 0x80080000 - PSX_EXE_HEADER_SIZE

;; --- EXE/MOVIE.EXE - Movie player EXE, t_addr 0x80080000 ---
MOVIE_EXE_FILENAME equ "original/EXE/MOVIE.EXE"
MOVIE_EXE_OUTPUT equ "build/EXE/MOVIE.EXE"
MOVIE_EXE_ADDR equ 0x80080000 - PSX_EXE_HEADER_SIZE

;; --- EXE/END.EXE - Ending EXE, t_addr 0x80080000 ---
END_EXE_FILENAME equ "original/EXE/END.EXE"
END_EXE_OUTPUT equ "build/EXE/END.EXE"
END_EXE_ADDR equ 0x80080000 - PSX_EXE_HEADER_SIZE

;; =============================================================
;; Text data files (addresses are file offsets)
;; =============================================================

;; --- ADV/MES.BIN - Event script text (13 MB) - file offsets ---
MES_FILENAME equ "original/ADV/MES.BIN"
MES_OUTPUT equ "build/ADV/MES.BIN"
MES_ADDR equ 0

;; --- NAMEDT.BIN - Name data - file offsets ---
NAMEDT_FILENAME equ "original/NAMEDT.BIN"
NAMEDT_OUTPUT equ "build/NAMEDT.BIN"
NAMEDT_ADDR equ 0

;; --- TALK/ALIEN.BIN - Demon negotiation: ALIEN ---
TALK_ALIEN_FILENAME equ "original/TALK/ALIEN.BIN"
TALK_ALIEN_OUTPUT equ "build/TALK/ALIEN.BIN"
TALK_ALIEN_ADDR equ 0

;; --- TALK/BASKET.BIN - Demon negotiation: BASKET ---
TALK_BASKET_FILENAME equ "original/TALK/BASKET.BIN"
TALK_BASKET_OUTPUT equ "build/TALK/BASKET.BIN"
TALK_BASKET_ADDR equ 0

;; --- TALK/DOPPEL.BIN - Demon negotiation: DOPPEL ---
TALK_DOPPEL_FILENAME equ "original/TALK/DOPPEL.BIN"
TALK_DOPPEL_OUTPUT equ "build/TALK/DOPPEL.BIN"
TALK_DOPPEL_ADDR equ 0

;; --- TALK/ETC.BIN - Demon negotiation: ETC ---
TALK_ETC_FILENAME equ "original/TALK/ETC.BIN"
TALK_ETC_OUTPUT equ "build/TALK/ETC.BIN"
TALK_ETC_ADDR equ 0

;; --- TALK/GAKI.BIN - Demon negotiation: GAKI ---
TALK_GAKI_FILENAME equ "original/TALK/GAKI.BIN"
TALK_GAKI_OUTPUT equ "build/TALK/GAKI.BIN"
TALK_GAKI_ADDR equ 0

;; --- TALK/HIHO.BIN - Demon negotiation: HIHO ---
TALK_HIHO_FILENAME equ "original/TALK/HIHO.BIN"
TALK_HIHO_OUTPUT equ "build/TALK/HIHO.BIN"
TALK_HIHO_ADDR equ 0

;; --- TALK/KEMONO.BIN - Demon negotiation: KEMONO ---
TALK_KEMONO_FILENAME equ "original/TALK/KEMONO.BIN"
TALK_KEMONO_OUTPUT equ "build/TALK/KEMONO.BIN"
TALK_KEMONO_ADDR equ 0

;; --- TALK/KOKURI.BIN - Demon negotiation: KOKURI ---
TALK_KOKURI_FILENAME equ "original/TALK/KOKURI.BIN"
TALK_KOKURI_OUTPUT equ "build/TALK/KOKURI.BIN"
TALK_KOKURI_ADDR equ 0

;; --- TALK/KOROU.BIN - Demon negotiation: KOROU ---
TALK_KOROU_FILENAME equ "original/TALK/KOROU.BIN"
TALK_KOROU_OUTPUT equ "build/TALK/KOROU.BIN"
TALK_KOROU_ADDR equ 0

;; --- TALK/KOSIKI.BIN - Demon negotiation: KOSIKI ---
TALK_KOSIKI_FILENAME equ "original/TALK/KOSIKI.BIN"
TALK_KOSIKI_OUTPUT equ "build/TALK/KOSIKI.BIN"
TALK_KOSIKI_ADDR equ 0

;; --- TALK/KOUMAN.BIN - Demon negotiation: KOUMAN ---
TALK_KOUMAN_FILENAME equ "original/TALK/KOUMAN.BIN"
TALK_KOUMAN_OUTPUT equ "build/TALK/KOUMAN.BIN"
TALK_KOUMAN_ADDR equ 0

;; --- TALK/KUTISAKE.BIN - Demon negotiation: KUTISAKE ---
TALK_KUTISAKE_FILENAME equ "original/TALK/KUTISAKE.BIN"
TALK_KUTISAKE_OUTPUT equ "build/TALK/KUTISAKE.BIN"
TALK_KUTISAKE_ADDR equ 0

;; --- TALK/KYOUKI.BIN - Demon negotiation: KYOUKI ---
TALK_KYOUKI_FILENAME equ "original/TALK/KYOUKI.BIN"
TALK_KYOUKI_OUTPUT equ "build/TALK/KYOUKI.BIN"
TALK_KYOUKI_ADDR equ 0

;; --- TALK/MAYOERU.BIN - Demon negotiation: MAYOERU ---
TALK_MAYOERU_FILENAME equ "original/TALK/MAYOERU.BIN"
TALK_MAYOERU_OUTPUT equ "build/TALK/MAYOERU.BIN"
TALK_MAYOERU_ADDR equ 0

;; --- TALK/POLUTAR.BIN - Demon negotiation: POLUTAR ---
TALK_POLUTAR_FILENAME equ "original/TALK/POLUTAR.BIN"
TALK_POLUTAR_OUTPUT equ "build/TALK/POLUTAR.BIN"
TALK_POLUTAR_ADDR equ 0

;; --- TALK/QSIRUBA.BIN - Demon negotiation: QSIRUBA ---
TALK_QSIRUBA_FILENAME equ "original/TALK/QSIRUBA.BIN"
TALK_QSIRUBA_OUTPUT equ "build/TALK/QSIRUBA.BIN"
TALK_QSIRUBA_ADDR equ 0

;; --- TALK/SINSI.BIN - Demon negotiation: SINSI ---
TALK_SINSI_FILENAME equ "original/TALK/SINSI.BIN"
TALK_SINSI_OUTPUT equ "build/TALK/SINSI.BIN"
TALK_SINSI_ADDR equ 0

;; --- TALK/SLIME.BIN - Demon negotiation: SLIME ---
TALK_SLIME_FILENAME equ "original/TALK/SLIME.BIN"
TALK_SLIME_OUTPUT equ "build/TALK/SLIME.BIN"
TALK_SLIME_ADDR equ 0

;; --- TALK/SYOUJO.BIN - Demon negotiation: SYOUJO ---
TALK_SYOUJO_FILENAME equ "original/TALK/SYOUJO.BIN"
TALK_SYOUJO_OUTPUT equ "build/TALK/SYOUJO.BIN"
TALK_SYOUJO_ADDR equ 0

;; --- TALK/TENSI.BIN - Demon negotiation: TENSI ---
TALK_TENSI_FILENAME equ "original/TALK/TENSI.BIN"
TALK_TENSI_OUTPUT equ "build/TALK/TENSI.BIN"
TALK_TENSI_ADDR equ 0

;; --- TALK/TINPRA.BIN - Demon negotiation: TINPRA ---
TALK_TINPRA_FILENAME equ "original/TALK/TINPRA.BIN"
TALK_TINPRA_OUTPUT equ "build/TALK/TINPRA.BIN"
TALK_TINPRA_ADDR equ 0

;; --- TALK/TOILET.BIN - Demon negotiation: TOILET ---
TALK_TOILET_FILENAME equ "original/TALK/TOILET.BIN"
TALK_TOILET_OUTPUT equ "build/TALK/TOILET.BIN"
TALK_TOILET_ADDR equ 0

;; --- TALK/WORM.BIN - Demon negotiation: WORM ---
TALK_WORM_FILENAME equ "original/TALK/WORM.BIN"
TALK_WORM_OUTPUT equ "build/TALK/WORM.BIN"
TALK_WORM_ADDR equ 0

;; --- TALK/WTENSI.BIN - Demon negotiation: WTENSI ---
TALK_WTENSI_FILENAME equ "original/TALK/WTENSI.BIN"
TALK_WTENSI_OUTPUT equ "build/TALK/WTENSI.BIN"
TALK_WTENSI_ADDR equ 0

;; --- TALK/YAKUZA.BIN - Demon negotiation: YAKUZA ---
TALK_YAKUZA_FILENAME equ "original/TALK/YAKUZA.BIN"
TALK_YAKUZA_OUTPUT equ "build/TALK/YAKUZA.BIN"
TALK_YAKUZA_ADDR equ 0

;; --- TALK/YOUEN.BIN - Demon negotiation: YOUEN ---
TALK_YOUEN_FILENAME equ "original/TALK/YOUEN.BIN"
TALK_YOUEN_OUTPUT equ "build/TALK/YOUEN.BIN"
TALK_YOUEN_ADDR equ 0

;; --- TALK/ZMBITYAN.BIN - Demon negotiation: ZMBITYAN ---
TALK_ZMBITYAN_FILENAME equ "original/TALK/ZMBITYAN.BIN"
TALK_ZMBITYAN_OUTPUT equ "build/TALK/ZMBITYAN.BIN"
TALK_ZMBITYAN_ADDR equ 0

;; --- TALK/ZOMBIKO.BIN - Demon negotiation: ZOMBIKO ---
TALK_ZOMBIKO_FILENAME equ "original/TALK/ZOMBIKO.BIN"
TALK_ZOMBIKO_OUTPUT equ "build/TALK/ZOMBIKO.BIN"
TALK_ZOMBIKO_ADDR equ 0

;; --- TALK/ZOMB_MAN.BIN - Demon negotiation: ZOMB_MAN ---
TALK_ZOMB_MAN_FILENAME equ "original/TALK/ZOMB_MAN.BIN"
TALK_ZOMB_MAN_OUTPUT equ "build/TALK/ZOMB_MAN.BIN"
TALK_ZOMB_MAN_ADDR equ 0

;; --- battle small-font page: NOW PATCHED IN /B/BF.BIN (tools/btlfont.py); the VRAM-copy hook below was removed
;;     2026-10-05 (it copied garbage in overworld battles); 0x8001A4A8-0x8001A510 is free again ---
;; BTLP uploads its own small-font page (VRAM 960,256, from compressed battle data) without the redrawn a-z / . / '
;; cells; the field page (VRAM 896,256, patched on disc) is still in VRAM during battles, so its cell rows 0-2 are
;; copied over the battle page right after the upload.
BTLP_PAGE_LOAD_JAL_ADDR equ 0x80081E80  ; jal LoadImage (0x8002B810) in the BTLP TIM loader
GPU_LOAD_IMAGE equ 0x8002B810           ; LoadImage(rect, src)
GPU_MOVE_IMAGE equ 0x8002B8D8           ; MoveImage(rect, x, y)
BTLP_PAGE_FIX_ADDR equ 0x8001A4A8       ; 2 unreferenced SLPS functions (tools/deadfuncs.py)
BTLP_PAGE_FIX_SIZE equ 0x8001A510 - BTLP_PAGE_FIX_ADDR

;; --- battle banner names (tools/banner.py): pointer table 0x800D92F4 (347 words), pool 0x800D835C-0x800D92F4;
;; overflow strings in dead SLPS functions 0x8002C2B8-0x8002C2F0, 0x80026A10-0x80026A54, 0x80018B50-0x80018B88

;; --- full-length Persona names (tools/personas.py, slps_005.00/persona_names.asm) ---
PERSONA_RECORDS_ADDR equ 0x8004B0CC     ; + id*0x2C (id 1-based)
PERSONA_NAME equ 8
PERSONA_FIELD equ 10
PERSONA_SPARE equ 0x29                  ; unreferenced record bytes +0x29..+0x2B
PERSONA_MAXLEN equ 16
PERSONA_CODE_ADDR equ 0x80031878        ; 2 unreferenced functions (taken from tools/s2dnames.py SPILL)
PERSONA_CODE_SIZE equ 0x8003191C - PERSONA_CODE_ADDR
PERSONA_TAILS_ADDR equ 0x8001EA10       ; unreferenced function
PERSONA_TAILS_SIZE equ 0x8001EA4C - PERSONA_TAILS_ADDR
PERSONA_HDR_BUF equ 0x80012484          ; unreferenced function (48 B): 16 B header name buffer
;; battle skill menu header descriptors (x, y, ptr, count): Persona name, "Cost" label, summon cost value
BTLP_HDR_NAME_DESC equ 0x800DD74C
BTLP_HDR_LABEL_DESC equ 0x800DD80C      ; -> label string 0x800DD744 (しょうかんSP, 7 glyphs + FF)
BTLP_HDR_VALUE_DESC equ 0x800DD764

;; --- story-battle dialogue (tools/btlevt.py, btlp/btlevt_unpack.asm): BPE-packed strings + unpacker in their zone ---
BTLEVT_ZONE_START equ 0x800CFA14
BTLEVT_ZONE_END equ 0x800D0AE4
BTLEVT_UNPACK_ADDR equ (BTLEVT_ZONE_END - 0x360)  ; unpacker code, pair table, buffer (keep in sync with btlevt.TAIL)
BTLEVT_BUF_SIZE equ 256
;; PRS-CHG window (btlp/prschg_names.asm): NOW / SUB / SUB Persona names, 16 glyphs each, in the header buffer area
PRSCHG_BUF equ PERSONA_HDR_BUF          ; +0 NOW, +16 SUB, +32 SUB (48 bytes)
BTLP_PRSCHG_DESC equ 0x800DDD44         ; 3 descriptors x 12 bytes (x -96, y -4/8/20)
;; battle text name copy (btlp/name_lowercase.asm): unreferenced BTLP function (tools/deadovl.py)
BTLP_NAME_COPY_ADDR equ 0x800BD360
BTLP_NAME_COPY_SIZE equ (0x800BD3F8 - BTLP_NAME_COPY_ADDR)
