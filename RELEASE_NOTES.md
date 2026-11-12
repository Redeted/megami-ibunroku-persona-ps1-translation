# Megami Ibunroku Persona: Be Your True Mind - English translation

Release notes for version 1.0.5-beta, the build of 2026-11-12. Notes of earlier versions are in their GitHub
releases.

## 1.0.5-beta

A beta: the new features are tested, but expect a few issues. When you report one, a save state from the same
patch helps a lot (save states only work with the exact patch they were made with).

### Patches

| Patch | Contents |
|---|---|
| `Persona-TL.xdelta` | The translation only. |
| `Persona-TL-QoL.xdelta` | The translation plus the enhancements below (60 fps, battle fast-forward, new items and skills, quit to the title screen). The game's balance is the original. |
| `Persona-TL-QoL-easy.xdelta` | The same as QoL, plus half the random encounter rate and x2 EXP, Persona points and money after battles. |

Up to 1.0.4 the single QoL patch had the halved encounters and the x2 rewards: they are now only in the easy patch.
Memory-card saves work with all three.

### New in the QoL patches

- **Battle fast-forward** (like the PSP skip): press **START** while a turn plays out, or while AUTO is running.
  A small ">>" appears at the top right and the battle runs about twice as fast: party, enemies, Persona summons,
  skill effects and damage numbers. It switches off by itself when the command menu comes back for your input,
  when you stop AUTO with Cross, and on the results screen; press START again to switch it off earlier. The battle
  itself is unchanged (only 1 out of 4 frames is shown). Loading effects from the disc is not faster.
- **Clean Salt and Emergency Exit**, two items from the PSP version, sold for 10,000 yen each in the Satomi
  Tadashi pharmacies (the drug store of Tadashi's dad, Sato-chan's store, and the one of Tadashi's uncle; in the
  Snow Queen route at the school pharmacy):
  - Clean Salt: for a while (16 moon phases), random battles with demons weaker than your party leader do not
    happen. Works in dungeons and on the town map.
  - Emergency Exit: in a dungeon, warps the party back to the tile where they entered. It works in the dungeons
    entered from the town map, the Kama Palace and the Mana Castle; elsewhere it is greyed out. The entrance is
    kept in memory-card saves.
- **Estoma and Traesto as Persona skills**, as on the PSP (each in a slot that was empty, no skill removed):
  - Estoma (same effect as Clean Salt): Cu Chulainn, Urdr, Shouki, Byakko.
  - Traesto (same effect as Emergency Exit): Otohime, Aonbarr, Quetzalcoatl.
  - Fusing with Clean Salt or Emergency Exit in the Velvet Room teaches Estoma or Traesto in the 7th skill slot,
    like the spell stones.
  - Field-only skills (Estoma, Traesto, Liftoma, Mappa) are greyed out and refused in battle.
- **Quit to the title screen**: GAME END at an Agastya tree now returns to the title screen instead of asking you
  to turn off the power.

### Translation fixes (all patches)

- Full names in the field menus: item, equipment, Persona, demon and skill names are no longer cut at 10 letters
  (shops, item and equipment menus, Velvet Room lists and results, dungeon menus, Persona status pages, ANALYZE).
  They are drawn with proportional spacing; the few longest names use a short form.
- Item and equipment names in mixed case ("Revival Bead" instead of "REV. BEAD"), following the official PSP names
  (e.g. Demon House, Magnadyne Stone, Verity Tablet, Kusanagi's Sword, Daybreak Greaves). Key items: Prison Key
  and Compact Half (dialogue updated too). Battle results show the dropped item with its full name.
- The heart symbols of the Japanese text are back, in the story and in the demon negotiations (they were written
  as `*` or dropped before), and no longer colour half of the letter before them.
- Velvet Room: the bottom bar of the Persona page (fusion preview, owned Personas) shows the full Persona name
  again (only the arcana was shown).
- Technical: the main executable grows by 3 sectors; a start-up stub copies the name code and data into unused
  BIOS RAM (0x8000EA00-0x8000FFC0).

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

- Short name fields: the field menus show full names, but some battle lists and inserted names still
  show at most 10 characters (UPPERCASE small font for items). Overworld location labels are 7-character
  abbreviations. Six long skill names are shortened to the 15-character battle menu limit.
- Elly's family name on the STATUS screen is "K. Eriko" (the name slot holds 8 letters).
- A few long dungeon story boxes are condensed to fit their fixed-size slot.
- Star symbols in the Japanese are replaced (the font is ASCII only); hearts are kept.
- The alien demon's "alien speech" keeps the original full-width digits.
- Staff credits: job titles were already in English; staff names stay in Japanese.
- Name entry: the Hiragana / Katakana / Kanji pages stay Japanese; use the ABC page.

## Playing notes

- Save states made with an earlier build of the patch are not compatible (the game keeps code
  and text in RAM). Use in-game memory-card saves when you switch to a new build.

## Separate enhancement build

The 60 fps "QoL" builds are separate discs and are not part of this translation release:
`python tools/build.py --qol` (`patched_qol/Persona-TL-QoL.bin`) and `python tools/build.py --easy`
(`patched_qol_easy/Persona-TL-QoL-easy.bin`). Both keep the original game speed and draw extra in-between frames
in the 3D dungeons and the overworld, play Persona summons and skill effects in battle at double speed (voices and
sounds keep their normal speed), add the START battle fast-forward and the PSP items and skills (Clean Salt,
Emergency Exit, Estoma, Traesto). The easy disc also halves the random encounter rate and gives x2 EXP, Persona
points and money after battles. With `--psp` each also exists with the PSP script (`patched_psp_qol/`,
`patched_psp_qol_easy/`). Recommended DuckStation setting for it: CPU overclock 180%,
which gives 60 fps in the dungeons and 30 fps in the overworld. See `qol/README.md`.
