# Megami Ibunroku Persona: Be Your True Mind — English Translation

A complete English translation of the original 1996 PlayStation release of *Megami Ibunroku Persona*
(Japan, SLPS-00500), with an optional enhancement patch.

<p align="center">
  <img src="screenshots/1.png" width="49%" alt="Item pickup"> <img src="screenshots/2.png" width="49%" alt="Dialogue">
  <img src="screenshots/3.png" width="49%" alt="Velvet Room"> <img src="screenshots/4.png" width="49%" alt="Dialogue choices">
  <img src="screenshots/5.png" width="49%" alt="Name entry"> <img src="screenshots/6.png" width="49%" alt="Dialogue">
</p>

## Features

- **Fully translated**: the whole story of both routes (SEBEC and Snow Queen), every demon
  negotiation, battles, menus, items, skills, the Velvet Room, the overworld, the casino, name entry,
  the save screens and all endings.
- **Subtitled movies**: English subtitles in the spoken movies; the opening quote and the epilogue
  poems redrawn in English.
- A literal translation that keeps the original names, places and honorifics, using the official
  terminology of the 2009 PSP release for skills, items, demons and Personas.
- **Optional enhancement patch (QoL)**:
  - smooth movement in the 3D dungeons (up to 60 fps) and the overworld (up to 30 fps), while the
    game's own speed stays the original;
  - Persona summons and skill effects in battle at double speed (voices and sounds keep their normal
    speed);
  - half the random encounter rate;
  - x2 EXP, Persona points and money after battles.

## What you need

Your own copy of the game, as a single-track BIN/CUE of the **first release**:

| | |
|---|---|
| File | `Megami Ibunroku Persona - Be Your True Mind (Japan).bin` |
| Size | 699,705,888 bytes |
| CRC32 | `360EB310` |
| MD5 | `c0f167dd5133e2a0f89f772852a4e978` |

The later **"Rev 1"** release (699,672,960 bytes) is **not supported**: the patch will refuse to apply.

## Patching (easy way)

1. Download a patch from the [Releases](../../releases) page:
   - `Persona-TL.xdelta` – the translation;
   - `Persona-TL-QoL.xdelta` – the translation plus the enhancement patch.
2. Apply it to your `.bin` with any xdelta patcher, for example
   [Delta Patcher](https://github.com/marco-calautti/DeltaPatcher), or on the command line:
   ```
   xdelta3 -d -s "Megami Ibunroku Persona - Be Your True Mind (Japan).bin" Persona-TL.xdelta Persona-TL.bin
   ```
3. Open the patched `.bin` in your emulator through a `.cue` sheet. The release does not ship one:
   use the `.cue` that came with your own copy of the game. Its `FILE` line must name the patched
   `.bin`, so either
   - give the patched file the original name (`Megami Ibunroku Persona - Be Your True Mind (Japan).bin`,
     in another folder or replacing the original), or
   - keep the name you chose (e.g. `Persona-TL.bin`) and change the `FILE` line of a copy of the `.cue`
     to match. The whole sheet is just:
     ```
     FILE "Persona-TL.bin" BINARY
       TRACK 01 MODE2/2352
         INDEX 01 00:00:00
     ```
   (Any online or tool-made `.cue` for a single-track BIN works as well.)

## Optional: the official PSP script (branch `psp-script`)

This branch adds one command that turns a disc you already patched with `Persona-TL.xdelta` (or
`Persona-TL-QoL.xdelta`) into a variant whose **story scenes and demon negotiations** use the English of
the official 2009 PSP release (*Shin Megami Tensei: Persona*) instead of this project's literal
translation. The opening quote and the movie subtitles get the PSP wording too. Menus, battles, items and the
QoL patch stay as in the patch you applied. The PSP text is read from **your own PSP copy** when you run the
command; it is not part of this project and no patch containing it is published.

**Why?**
Fun.

**How?**
The PSP version is a remake built on the same script structure as the PS1 game: the same event files, the same
scenes in the same order, and one list of lines per demon for the negotiations, with the same speakers,
choices and name tokens. The tool takes each PS1 box, finds the PSP box that belongs to it (matching speaker,
choices, name codes, length and shared words, since the PSP sometimes adds or drops a box), puts the PSP
English into the PS1 box's control-code skeleton and re-wraps it to the narrower PS1 text box. Boxes it cannot
match with confidence keep this project's translation.

**Is it the exact text?**
About 97% of the story boxes and 98% of the negotiation lines use the PSP text. The rest keep this
project's translation where the PSP line cannot be shown on the PS1 (button icons in the casino
help, lines without a PSP counterpart). It needs yet another playtest for both SEBEC and Snow Queen,
trying it myself.

### What you need, in addition to the steps above

- your patched `.bin` (`Persona-TL.bin` or `Persona-TL-QoL.bin`, made with the xdelta of release **v1.0.1**);
- your original Japanese `.bin` (the same file the xdelta was applied to);
- the US PSP release as an **ISO** (`ULUS10432`, about 820 MB; a `.cso` must be decompressed to `.iso`
  first, e.g. with [maxcso](https://github.com/unknownbrackets/maxcso) `--decompress`);
- [Python](https://www.python.org/) 3.10 or newer;
- [Java](https://adoptium.net/) (any recent JRE; it runs the movie encoder);
- the source code of **this branch**: `git clone --branch psp-script
  https://github.com/Redeted/megami-ibunroku-persona-ps1-translation`, or *Code -> Download ZIP* while the
  `psp-script` branch is selected on GitHub (the *Source code* zip of a release is the main branch and does
  not contain the tool);
- an internet connection the first time: the command installs the Python packages `opencv-python-headless`,
  `numpy` and `pillow` with pip and downloads [jPSXdec](https://github.com/m35/jpsxdec) 2.1 (3.7 MB, checked
  against a fixed SHA-256) into `tools/ext/jpsxdec/` if they are missing;
- about 2 GB of free disk space.

### Run it

In the source folder of this branch:
```
python tools/psp_patch.py --original "path/to/Megami Ibunroku Persona - Be Your True Mind (Japan).bin" --patched path/to/Persona-TL.bin --psp path/to/persona_psp.iso
```
This takes a few minutes (most of it re-encoding the movies) and writes `Persona-TL-PSP.bin` + `.cue` next
to the patched file (for `Persona-TL-QoL.bin`: `Persona-TL-QoL-PSP.bin`); `--out` chooses another name. Your
input files are not changed. The `.cue` paths of your images work as well. Load the new `.cue` in the emulator.

Notes:
- The PS1 text box is narrower than the PSP one: a few long lines take an extra button press.
- Memory-card saves work across the translation, QoL and PSP variants; save states do not.
- Building from source instead of patching: `python tools/build.py --psp path/to/persona_psp.iso`
  (with or without `--qol`), see DEVELOPMENT.md.

For technical questions, suggestions and very, very supportive messages: redeted@proton.me

## Playing

- Tested on [DuckStation](https://github.com/stenzek/duckstation).
- **For the QoL patch**, enable the CPU overclock: *Settings → Console → CPU Emulation*, enable clock
  speed control and set it to around **180%**. This gives 60 fps in the dungeons and a smooth 30 fps
  in the overworld. Without it the game still runs at its normal speed, just with fewer extra frames.
- Save states do not carry over between patch versions; use in-game memory-card saves when you update.

Known limitations (shortened names in some menus, untranslated staff names in the credits, …) are
listed in [RELEASE_NOTES.md](RELEASE_NOTES.md).

## Building from source

The repository contains the translation and all patches, but no game data: the build reads the files
from your own disc image.

Requirements:
- [Python](https://www.python.org/) 3.10 or newer, with `pip install capstone numpy opencv-python pillow`
- [armips](https://github.com/Kingcom/armips) 0.11: put `armips.exe` (or `armips`) in `tools/armips/`
  or on your PATH
- Optional, for the movie subtitles: Java and [jPSXdec](https://github.com/m35/jpsxdec) 2.1, unpacked so
  that `tools/ext/jpsxdec/jpsxdec.jar` exists. Without it the movies keep their Japanese text.

Build:
```
python tools/build.py --image "path/to/Megami Ibunroku Persona - Be Your True Mind (Japan).bin"
python tools/build.py --image "path/to/Megami Ibunroku Persona - Be Your True Mind (Japan).bin" --qol
```
Optional PSP-script variant (the official PSP English for the story and the negotiations, read from your own
*Shin Megami Tensei: Persona* PSP ISO; not distributed as a patch): add `--psp path/to/persona_psp.iso`
(with or without `--qol`); output `../patched_psp/` or `../patched_psp_qol/`.

The first run extracts the game files into `original/`. The results are written next to the
repository folder: `../patched/Persona-TL.bin/.cue` and `../patched_qol/Persona-TL-QoL.bin/.cue`.
A full build takes about 10 minutes.

Developer notes: [DEVELOPMENT.md](DEVELOPMENT.md), and the enhancement patch in [qol/README.md](qol/README.md).

## Legal

This is an unofficial, non-commercial fan translation. It is not affiliated with or endorsed by Atlus or any rights holder; *Megami Ibunroku Persona* and all related names and assets belong to their respective owners.

- The repository and the release patches contain **no game data**: the patches are xdelta differences that only work on a disc image you supply yourself. Use only an image created from media you own, where permitted by applicable law.
- Do not commit game binaries, CUE sheets, extracted disc files or save states to this repository (the `.gitignore` is a whitelist for that reason).
- `translation/*.tsv` list the original Japanese script lines next to the English text, as translation sources. They are quoted for the purpose of the translation only.
- Only the first release (SLPS-00500, 699,705,888 bytes) is supported; other revisions are not.

The tools, assembly sources and translation text written for this project are released under the [MIT licence](LICENSE).
