# Megami Ibunroku Persona: Be Your True Mind - English translation

Release notes for version 1.0.1, the translation build of 2026-10-11 (disc `patched/Persona-TL.bin`).

## Changes in 1.0.1

- Item names follow the official 2009 PSP names (consumables, spell stones, tablets, gems, Persona
  items), abbreviated to the 10-character field; spell stones read "AGIDYNE ST" instead of the bare
  spell name. Dialogue that names an item uses the same names (Life Stone, Rattle Drink, Balm of Life).
- QoL build: Persona summons and skill effects in battle play at double speed; voices and sounds keep
  their normal speed.

## Base image

| | |
|---|---|
| Game | Megami Ibunroku Persona: Be Your True Mind (Japan), SLPS-00500 |
| Image | `Megami Ibunroku Persona - Be Your True Mind (Japan).bin` (single-track BIN/CUE) |
| Size | 699,705,888 bytes |
| CRC32 | `360EB310` |
| MD5 | `c0f167dd5133e2a0f89f772852a4e978` |

The patch is built for this exact image. Other dumps or revisions are not supported.

## Approach

A literal translation, not a localization: names, places, honorifics (-san, -kun, -chan, -sama),
Japanese name order (family name first) and cultural references are kept as in the Japanese.
Skills, items, demons, Personas, races and arcana use the official ATLUS English names of the 2009
PSP *Shin Megami Tensei: Persona*, never the *Revelations: Persona* localization.

Text is drawn with a new variable-width font, so English fits the original dialogue boxes.

## What is translated

- Story: every event script box of both routes (SEBEC and Snow Queen), 7,344 boxes, including
  choices, character introduction cards, dungeon script boxes and story-battle dialogue.
- Negotiation: every demon conversation (all TALK files, including the Spell Card and refusal
  scenes), the player's answer lists, the CONTACT command window, personalities and prompts.
- Battle: command menus, skill / Persona / demon names, battle messages, ANALYZE, AUTO, FORM,
  level-up and status labels, Triangle help.
- Menus: items, equipment, skills with descriptions, Persona status pages (affinities, Type, MATK,
  MDEF), STATUS, EQUIP, CONFIG, MAP titles, save / load screens and memory-card messages.
- Velvet Room: fusion lists and results, Igor's messages (including the fusion accident line and
  the Persona gift speech), item addition.
- Overworld: location names, overworld dialogue, the casino (help, coin exchange, prize bar).
- Name entry: labels, and an English ABC page (A-Z, a-z and punctuation).
- Title screen and memory-card check graphics.
- Movies: the opening Zhuangzi quote (MV1C) re-drawn in English; English subtitles burned into the
  spoken movies (Philemon and Kandori speeches, MV11-MV17, MV1B); the epilogue poems of the school
  (MV25) and hospital (MV1E) endings.
- Endings: every epilogue and character profile page of all five ending scripts (SEBEC good ending
  and epilogue, SEBEC bad ending, both Snow Queen endings), checked in game.

## Known limitations (by design or by hardware limits)

- Short name fields: fusion lists, item / equipment lists and some inserted names show at most
  10 characters (UPPERCASE small font for items). Overworld location labels are 7-character
  abbreviations. Six long skill names are shortened to the 15-character battle menu limit.
- Elly's family name on the STATUS screen is "K. Eriko" (the name slot holds 8 letters).
- A few long dungeon story boxes are condensed to fit their fixed-size slot.
- Heart and star symbols in the Japanese are replaced (the font is ASCII only).
- The alien demon's "alien speech" keeps the original full-width digits.
- Staff credits: job titles were already in English; staff names stay in Japanese.
- Name entry: the Hiragana / Katakana / Kanji pages stay Japanese; use the ABC page.

## Playing notes

- Save states made with an earlier build of the patch are not compatible (the game keeps code
  and text in RAM). Use in-game memory-card saves when you switch to a new build.

## Separate enhancement build

The 60 fps "QoL" build (`python tools/build.py --qol`, `patched_qol/`) is a separate disc and is
not part of this translation release. It keeps the original game speed and draws extra in-between frames
in the 3D dungeons and the overworld. It also halves the random encounter rate, gives x2 EXP,
Persona points and money after battles, and plays Persona summons and skill effects in battle at double
speed (voices and sounds keep their normal speed). Recommended DuckStation setting for it: CPU overclock 180%,
which gives 60 fps in the dungeons and 30 fps in the overworld. See `qol/README.md`.
