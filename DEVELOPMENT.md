# Persona (SLPS-00500) English translation: developer notes

armips project for *Megami Ibunroku Persona: Be Your True Mind* (PS1, Japan).

## Build

```
python tools/build.py            # tables, VWF font, armips, patched disc image
python tools/build.py --qol      # separate enhancement build (60 fps 3D areas, qol/README.md) -> ../patched_qol/
python tools/build.py --no-disc  # assemble only (build/)
```

Inputs: `original/` (files extracted with `tools/extract.py`) and the original
`.bin` one directory up. Output: `build/` and `../patched/Persona-TL.bin/.cue`.

## Text encoding

| Bytes      | Meaning                                                        |
|------------|----------------------------------------------------------------|
| `00-7F`    | original glyph 0x000-0x07F (kana); `00` = blank                |
| `80-87 xx` | original glyph `((b & 7) << 8) \| xx` (all 2048 glyphs)        |
| `88-E6`    | **English VWF character** = ASCII + 0x68 (VWF boxes only)      |
| `FF xx`    | control code                                                   |

The VWF range is new: bytes 88-E6 were never valid lead bytes, so the
encoding is a strict superset and untranslated Japanese keeps working.

Tables (generated, do not edit): edit `tools/font_map.tsv`, run `tools/make_tbl.py`.
- `common/persona.tbl` - original encoding; ASCII aliases the full-width glyphs.
  For renderers without VWF (menus, battle, ...).
- `common/persona_vwf.tbl` - ASCII maps to 88-E6. For dialogue (ADV/DNG/S2D).

Both: control codes as `<FFxx>`, raw bytes `<xx>`, unnamed glyphs `<Gxxx>`.
`.string` terminates with FF01 (menu strings); dialogue uses `.stringn` with
explicit codes. Dialogue control codes seen so far: `<FF03>` newline,
`<FF02>` wait for button, `<FF04>` new page. Negotiation (TALK/*.BIN): `<FFF6>`
newline, `<FFF5>`/`<FFFC>` breaks, `<FFFD>` + 1 parameter byte.

## Dialogue VWF (text width)

Box: 3 visible lines x 240 px (was 15 full-width glyphs). English averages
~7 px/char, about 33 characters per line.

- Engine: `vwf/vwf_dialog.asm` (+ `vwf_dialog_cfg.asm` per-overlay configs).
  Keeps the original GsBG cell map, VRAM layout and scroll logic; composes
  glyphs at pixel level and owns the cell counter. Wrapping matches the
  original (auto-wrap at the box edge), so Japanese renders unchanged.
- Hooks: `common/shared_patches.inc` macro, applied in `adv/`, `dng/`, `s2d/`
  `vwf_hooks.asm` (10 words per overlay).
- Font: `font/spleen-8x16.bdf` (Spleen, BSD-2-Clause, `font/SPLEEN-LICENSE`),
  cropped to ink width by `tools/make_vwf_font.py`. Hand edits go in
  `font/vwf_overrides.txt` (`char X` + 16 rows of `.`/`#`). Preview:
  `font/vwf_preview.png`.
- Delivery: the engine, font and line buffers live at 0x801DB000-0x801E0000
  as a prefix of FONT.BIN (`vwf/vwf_blob.asm`); SLPS loads FONT.BIN 64 KB lower
  (`slps_005.00/vwf_font_load.asm`), glyphs stay at 0x801E0000.
- Word wrap English with the engine's metrics:
  `python tools/vwf_wrap.py "text"` / `--check "text"`.

Verified in-game (ADV): English, mixed Japanese/English, scrolling, choices,
original Japanese auto-wrap, blob intact through boot, FMV and the opening event.
DNG/S2D hooks are statically derived and not yet exercised at runtime.

## Event scripts (ADV/E0..E3.BIN)

816 entries, 7344 text boxes. Workflow: `python tools/etext.py dump` writes
`translation/events/E?.tsv` (`entry box ja en`); fill the `en` column (ASCII +
`<FFxx>` codes, one `<FF01>` at the end - appended if missing) and run
`python tools/build.py`. Rows with an empty `en` are left alone.

- Container: sector 0 = u16 cumulative sector offsets. Entry = u32 0x80100008,
  u32 end address, image loaded at 0x80100000 (body index = pointer - 0x80100000),
  max 0xFFF8 bytes. Image = map header + command stream (`FF op a b`, with a u32
  pointer after ops 55/22/26/54/...) + text boxes. `FF 55 00 00 <ptr>` shows the
  box at ptr; boxes end in `FF 01`; control codes inside text are `FF xx`, xx < 0x20,
  no parameters.
- `tools/efile.py` parses/rebuilds: boxes may grow or shrink; gaps (commands, data)
  move as blocks keeping their offset mod 4 (the interpreter reads operands with lw);
  every u32 pointer to a box or gap is remapped. A pointer into the middle of a box
  is only accepted while that box keeps its position and size. Self-test:
  `python tools/efile.py ADV/E2.BIN` (round-trip identical, 0 unsafe).
- The game does **not** read each file's sector 0: it uses copies embedded in
  SLPS_005.00 (0x8004DA70 E0, 0x8004DC34 E1, 0x8004DDF8 E2, 0x8004DFDC E3, index =
  script id & 0xFF; loader 0x800159EC). `etext.py build` regenerates them as
  `build/event_tables.asm` (included from main.asm) for every edited file.
- Fixed layout: `translation/layout.json` reserves a slot (sectors) for every entry
  (1.5x the original image + 1 sector, max 31). All four E files are always rebuilt at
  their final size and placed at fixed disc locations, so the sector tables and
  FSECT/FSIZE entries never change while translations fit their slots. If one does not,
  `etext.py build` warns; raise it with `python tools/etext.py layout --grow` (that
  changes the tables once and makes older save states stale).
- Translating: `python tools/etext.py dump` merges (keeps existing `en` rows), then write
  scenes as `translation/src/<file>_<entry>.py` using `tools/tl_lib.py` (`apply`, `P()`
  pause, `F6()` style switch; wraps to 240 px / 3 lines per page, reports every
  overflowing box) - or edit the TSV directly. Control codes with parameters must stay
  byte-identical to the Japanese: `FF05 xx 00` pause, `FF06 xx` style, `FF0F あ` player name.
- Save states: they carry resident code and tables in RAM. After a rebuild an old state
  needs `python tools/live_patch.py ../patched/Persona-TL.bin` and its chunks written to
  RAM (see the docstring); states saved on the current build need nothing.
- `tools/etext.py check` proves decode->encode is lossless for all boxes.
- Edited files are written to build/ADV/ and placed on the disc by build_disc.py
  (in place if they fit, otherwise appended); files with no edits are untouched.

## Disc image

`tools/build_disc.py` writes changed files in place when they fit, otherwise
appends them after the volume; it updates the ISO9660 records, the game's own
file table (`FNAME.DAT` order -> `FSECT.DAT` LBA / `FSIZE.DAT` size) and the
PVD, and regenerates EDC/ECC for every written sector.

## Tools

| Tool                     | Purpose                                        |
|--------------------------|------------------------------------------------|
| `tools/extract.py`       | extract files from the original image          |
| `tools/decode.py`        | dump game bytes as text (`--raw` round-trips)  |
| `tools/mipsdis.py`       | MIPS disassembly of a file range               |
| `tools/mipsconst.py`     | absolute addresses built by lui pairs          |
| `tools/ramdiff.py`       | build-vs-original diff as RAM writes (live tests) |
| `tools/efile.py`         | parse/rebuild ADV/E?.BIN event scripts           |
| `tools/etext.py`         | event text codec, TSV dump, build (+ SLPS tables) |
| `tools/mescodec.py`      | decoder for ADV/MES.BIN scene graphics            |
| `tools/talk.py`          | TALK/*.BIN negotiation: check / dump / build      |
| `tools/strscan.py`       | find FF01 strings in SLPS/overlays -> translation/strings |
| `tools/scan_text.py`     | disc-wide text inventory -> translation/TEXT_SOURCES.md |
| `tools/tstatus.py`       | QA (build gate), progress ledger, propagate, next |
| `tools/tl_lib.py`        | scene translation helper (`apply`, `P`, `F6`)     |
| `tools/live_patch.py`    | RAM patches for old save states                   |
| `tools/names_audit.py`   | translation/NAMES_AUDIT.md (speakers, proper nouns) |
| `tools/glyph_sheet.py`   | visual audit sheets of font glyph assignments     |
| `tools/blobcheck.py`     | check a RAM dump of the VWF blob for clobbering |

## Status

Translation complete (2026-10-09): see `RELEASE_NOTES.md` for what is covered and the known
limitations.
