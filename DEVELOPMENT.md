# Persona (SLPS-00500) English translation: developer notes

armips project for *Megami Ibunroku Persona: Be Your True Mind* (PS1, Japan).

## Build

```
python tools/build.py            # tables, VWF font, armips, patched disc image
python tools/build.py --qol      # separate enhancement build (60 fps 3D areas, qol/README.md) -> ../patched_qol/
python tools/build.py --psp ISO  # PSP-script variant (story + negotiations from the official PSP English) -> ../patched_psp/
                                 # combinable with --qol (-> ../patched_psp_qol/); see "PSP-script variant" below
python tools/build.py --no-disc  # assemble only (build/)
```

Inputs: `original/` (files extracted with `tools/extract.py`) and the original
`.bin` one directory up. Output: `build/` and `../patched/Persona-TL.bin/.cue`.

## PSP-script variant (`--psp`)

`tools/pspscript.py` reads the English of the official PSP release (*Shin Megami Tensei: Persona*, ULUS10432)
from the user's own ISO and puts it in place of the project's translation for the story events (E0-E3) and
the demon negotiations (TALK units and the player's answers). Nothing from the PSP is stored in the
repository: `original_psp/` (extracted files) and `psp_text/` (generated tables + `report.tsv`) are not
committed, and no PSP-variant patch is published.

- `extract ISO` -> `original_psp/`; `convert` -> `psp_text/events/E?.tsv`, `psp_text/talk/*.tsv`, `report.tsv`.
- Each PSP box keeps the control-code skeleton of the Japanese PS1 box (pauses, player-name tokens, choices,
  profile styles) and is re-wrapped to the PS1 box (239 px, 3 lines). PSP boxes are matched to PS1 boxes by a
  per-entry alignment (speaker, choice, name tokens, length, shared words): the PSP sometimes adds or drops a box.
- A box that cannot be converted or fails the normal QA keeps the project's English (`report.tsv` says why).
  `translation/psp_keep_ours.tsv` (ids such as `E3/11/32`, `SLIME/40`, `ANSWERS/7`) forces that per box.
- TALK units may get extra pages (`FFFB FFF7`) when the PSP line is longer than the Japanese page count allows;
  with `PERSONA_TEXT` set, `talktl.py` ignores page codes in its code comparison and `tstatus.py` skips the
  speaker-label rule (PSP names differ from the glossary).
- `review-prep` writes `psp_text/review/chunk_NN.tsv` (literal vs PSP line, unique pairs, scene order) for a
  semantic check (`psp_text/review/BRIEF.md`); `review-collect` merges the reviewers' `out_NN.tsv` into
  `psp_text/review/flags.tsv` and adds every MISMATCH id to `translation/psp_keep_ours.tsv`.

### Player patcher (`tools/psp_patch.py`)

Players get the variant without armips (Java + jPSXdec are fetched/checked by the tool for the movie step): `psp_patch.py --original JP.bin --patched Persona-TL(-QoL).bin
--psp PSP.iso` (README "Optional: the official PSP script"). It checks the inputs (original = first release by
size/CRC, patched = SLPS word 0x8002E7BC is `d0ffbd27`, PSP = `ULUS-10432` in UMD_DATA.BIN), extracts only
ADV/E0..E3 + TALK from the original into its own work folder (`PERSONA_ORIGINAL`; `original/` is never touched),
runs `pspscript.py extract/convert` (`PERSONA_PSP_FILES`, `PERSONA_PSP_TEXT`), the QA gates, `etext.py`,
`talk.py` and `etctalk.py` builds, applies `event_tables.asm` to the patched disc's SLPS_005.00 (only if the
event layout grew) and runs `build_disc.py` with the patched disc as the base. Verified 2026-10-11: release
`Persona-TL-QoL.xdelta` + patcher = the same 390 file contents as `build.py --qol --psp` (only FSECT.DAT differs:
the grown files sit at other sectors; game tables and ISO directory agree). About 20 s.

### PSP formats (ULUS10432)

- Files: `PSP_GAME/USRDIR/pack/E0..E3.BIN` and `pack/talk/*.BIN` mirror the PS1 `ADV/E?.BIN` and `TALK/*.BIN`
  (same entry / unit counts: 224/224/240/128 entries, every TALK file unit for unit). `pack/E4.BIN` is 224 copies
  of an Agastya Tree save stub (ignored). `SYSDIR/BOOT.BIN` is blank and `EBOOT.BIN` encrypted: text that only
  lives in the PSP executable (choices, battle / negotiation prompts) would need a RAM dump and is not used.
- Text: u16 big-endian glyph codes, not compressed. `0000` space, `00E0-00F9` A-Z, `0101-011A` a-z,
  `00CF-00D8` 0-9, punctuation in `CHARS` (pspscript.py). Control codes are the PS1 ones (FF01 end, FF02 wait,
  FF04 new page, FF03 new line, FF05 pause, FF0E choice, FF07/FF08/FF0F player name) plus PSP-only codes:
  FF1B name FF03 = nameplate, FF18/FF19/FF1A = colour. Parameters take one word (the same bytes as the PS1
  parameter); the player-name codes take none on the PSP.
- E files: header = 256 little-endian (start, end) byte pairs. A PSP entry is scanned for runs of text words
  ending in FF01 (`e_boxes`).
- TALK: header u32[6] (`[0]` = 0x18, unit table at 0x18), byte stream (FFFD + 1 parameter byte, otherwise
  2-byte glyphs), FF03 = new line, FF02 FF04 = new page (PS1: FFF6, FFFB FFF7). The player's answer lines use the
  PS1 section-1 layout, but the table holds ABSOLUTE file offsets (PS1: offsets from the section start).

### Cases and how they are handled (build of 2026-10-11)

Story: 7122 of 7344 boxes from the PSP; talk: 12913 of 13282 units (474 with an added page); answers: 1870 of 1888.

| Case | Count | Handling |
|---|---|---|
| PSP adds one box and drops another in the same scene (E3/11: "any love potions around here?" added, "your record is engraved" dropped) | few entries | Alignment by content, never by position; a PS1 box without a PSP match keeps ours (`unaligned`: E3/2/1, E3/11/33, E3/47/2, E3/88/0) |
| PS1 text box where the PSP plays a cutscene (girl in white, E0/0/34) | - | The PSP script still holds the box: converted like any other |
| PSP box uses button icons (`0x39 0x3A 0x3E 0x5B 0x60 0x62`), card suits (`0x204-0x207`) or yen (`0x4F`) | 91 (casino help E0/13, E0/16, E2/48 ...) | Ours kept: the icon order could not be confirmed and a wrong button would mislead |
| PSP box is only "......" or was left in Japanese on the PSP (E1/2 Agastya Tree) | 59 | Ours kept (`no text`: fewer than two letters) |
| PSP drops or adds the player's name (E0/21/8 "<hero>, let's go check it out!" -> no name) | 50 | Ours kept: the number of name codes must match the Japanese |
| PSP uses another part of the player's name (Natsumi E0/3/25 "Give it a try, <given name>"; the Japanese has the family name) | 211 family -> given, 2 nickname -> given | The PSP's code is used (FF0F family, FF07 given, FF08 nickname; the same codes on both, parameter byte from the Japanese); in this variant `tstatus.py` treats the three name codes as one class |
| PSP drops the coin / card counter ("Current Metal Cards: [n]") | 8 | Ours kept |
| Inline style symbol (Ayase's heart E1/10/10, Frog's impression E3/5/18) | 4 | Profile cards: style at the start, closing code at the end; a heart at the end reuses our suffix; other patterns keep ours |
| Choice the PS1 box does not have (E0/50/9) | 1 | Ours kept |
| Heading cards: profile cards ("Saeko Takami" / "Homeroom teacher for ...") and info cards ("Hiremon Stone") | 56 profile + info cards | Title kept on its own line as on the PSP (the PSP marks the page with bullet glyph `0x44`, the Japanese starts with a short line + line break; plain narration with the bullet is joined). When the own line would cost an extra page, "Saeko Takami, homeroom teacher for ..." (a comma, since ':' reads as speech; the first word is lowercased only if the PSP script uses it in lowercase elsewhere) (`titled`) |
| PSP word hyphenated across a line break ("part-" / "time") | 27 story, 24 talk | Joined without a space ("part-time"); stutters like "that-at-at-" are PSP text |
| Question + options on one page | - | The PS1 options need their own line: the question is limited to 2 lines there (`assemble`) |
| Pauses: PSP count differs or the order around name tokens differs | - | The Japanese pauses are placed at the nearest sentence end, between the same name tokens as in the Japanese |
| PSP lines are wider (about 45 vs 36 characters) | 85 boxes need one more button press than on the PSP (mostly the intro profile cards) | Accepted (user, 2026-10-11): the PSP wording is kept, the extra page is the PS1 box size |
| Speaker names before introductions ("Hat-wearing student" = Mark, "Ms. Saeko") | - | Accepted: PSP names; `tstatus.py` skips the glossary label rule in this variant |
| PSP directions that differ from the PS1 text (E2/9/1, E2/9/3, E2/47/6) | 3 | Ours kept (`psp_keep_ours.tsv`): players follow them on the PS1 map |
| TALK: PSP line longer than the Japanese page count allows | 474 units | Extra pages (FFFB FFF7) added. Verified in game 2026-10-11 (YOUEN 709 injected in place of 366: the box waits, the next page follows, the Yes/No decision appears) |
| TALK: where a page break goes (`page_split`) | - | Every split is scored: after a sentence (a pause code may follow) free, after a comma 3, mid-sentence 6, plus 1 per empty line on every page; no more "Oh, is that" / "so!" or a lone "hee-ho!" page |
| TALK: race + demon name ("I'm <FFF0> <FFF3>!" = "Night Pairika") | - | Never split across lines or pages (`glue`) |
| TALK/ETC: several speakers in one unit, PSP page split differs from the Japanese | 67 | Ours kept (`speaker pages`): redistributing pages would merge the speakers |
| TALK: still too long with 2 extra pages, or the PSP drops a demon-name insert (FFF3 / FFF0) | 164 + 88 | Ours kept |
| TALK: last unit of each file ("Dummy"; the PSP repeats the previous line there) | 28 | Ours kept |
| TALK: KOROU debug units 310-337 ("Adds 3 Eager."; PSP: "If this shows up, it's a bug.") | 7 | Ours kept (`psp_keep_ours.tsv`) |
| TALK/ETC card scenes where the PSP uses different portrait codes (Kali / Kwancha, Durga / Gdon) | 20 | Ours kept |
| Answers: one Japanese answer reused in several places and worded differently by the PSP | - | The PSP wording closest in meaning to ours is chosen, then the most frequent |
| Semantic review: 17282 unique pairs, Claude Haiku agents (calibrated: 6 of 7 planted misalignments caught, no false alarm) | 51 MISMATCH, 66 CHECK | MISMATCH -> `psp_keep_ours.tsv`; CHECK listed in `psp_text/review/flags.tsv` for a human (mostly deliberate PSP rewrites) |

### Terminology of the variant (`tools/psp_terms.py`)

Active only when `PERSONA_TEXT` is set (`build.py --psp`, `psp_patch.py`). Our own strings are aligned with the
official release: the overworld shrine "Araya" -> "Alaya" (`s2dnames.py`, `s2dscript.py` read the TSVs through
`psp_terms.fix`; `psp_patch.py` does the same same-length edit in place on the patched disc), and the movie
subtitles follow the PSP English *voice acting* (`fmv_subs.py`: Expel Mirror, Alaya Cavern, Demon Mirror,
"state your name"). The opening quote cards of MV1C come from `psp_terms.OPENING` (`fmv_opening.py` re-uses the
same card/band geometry, a `-` or `~` first character marks the attribution line). The PSP *text* itself says
"Devil's Mirror", so in-game text keeps that. `fmv_poems.py` (both variants): frames down to 1 % fade strength are
processed and the fade frames keep at most ~1 % contrast of the original strokes.

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
