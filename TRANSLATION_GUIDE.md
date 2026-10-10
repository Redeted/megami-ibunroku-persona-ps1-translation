# Translation guide - Megami Ibunroku Persona (SLPS-00500)

Read this before translating or reviewing any text. Terms go in `glossary.tsv`.

## 1. Translation, not localization

- Translate what the Japanese says. Do not westernize, adapt or "fix" it.
- Keep names, places, organizations, food, holidays, currency (yen), school
  life, customs and cultural references exactly as they are in the Japanese.
  No substitutions (onigiri stays onigiri, not "sandwich").
- Keep honorifics: -san, -kun, -chan, -sama, -sensei, senpai, etc.
- Keep nicknames that the Japanese uses (マーク -> Mark, ブラウン -> Brown,
  エリー -> Elly): they are the characters' own nicknames, not localizations.
- Change something only if the Japanese text itself does (e.g. a character
  explicitly gives an English name or translates a word).
- Do not add, omit, censor, soften or intensify. Keep jokes, wordplay and
  insults; translate their meaning. No in-game translator notes; record
  explanations in the `notes` column of `glossary.tsv` instead.

## 2. Official terminology (Shin Megami Tensei / Persona)

For skills, spells, items, demons, Personas, arcana, status ailments, races,
system terms and recurring proper nouns, use ATLUS's official English names.
Reference order:
1. *Shin Megami Tensei: Persona* (PSP, 2009, Atlus USA) - the official
   translation of this same game. Do **not** use *Revelations: Persona*
   (PS1, 1996) terms or names: that release was westernized.
2. Other official ATLUS releases (Persona 2 PSP, Persona 3/4/5, mainline SMT).
3. No official term exists: translate literally and mark `source=project`.

Rule 1 overrides rule 2: an official release's westernized character or
place names are never used.

## 3. Names and romanization

- Name order follows the Japanese text (family name first when the full name
  is written, e.g. 南条 圭 -> Nanjo Kei). Change globally if the project decides
  otherwise.
- Romanize with Hepburn. The font has no macrons or accents: write long
  vowels without them (Nanjo, not Nanjō). Where the 2009 PSP release has an
  official spelling for a name from this game, use that spelling.
- One spelling per name everywhere. Check `glossary.tsv` first; add new names
  before using them.

## 4. Style and voice

- Match each character's register: Mark's and Brown's slang, Nanjo's
  arrogance, Yukino's toughness, Elly's mixing in of English words, and so on.
- Demons speaking in katakana or broken speech (e.g. the slime's オデ/オバエ)
  get a matching non-standard English voice. Keep each demon type
  consistent.
- Japanese fillers and sound effects (ハハ, フゥ, ヒック) become natural
  English equivalents of the same sound and length.
- Profanity: same strength as the original, no stronger, no weaker.

## 5. Formatting and technical limits

- **Characters**: VWF text supports printable ASCII only (0x20-0x7E). No
  smart quotes, accents, em dashes or Japanese punctuation in English lines.
  - 「」 and 『』 quotes -> `"` (quotation) or `'` inside a quotation
  - … -> `...`, ～/〜 -> `~`, ！？ -> `!?`, ・ -> space or `/` by context
- **Speaker labels** keep the original format: `マーク：` -> `Mark: `.
- **Line width**: 240 px per dialogue line. Wrap with
  `python tools/vwf_wrap.py "text"` and verify with `--check`.
  Do not end a line exactly at 240 px if a manual line break follows
  (it produces a blank line, as in the original).
- **Pages**: the box shows 3 lines and scrolls. Keep the original page
  breaks (`<FF02>` wait, `<FF04>` new page); prefer splitting a page with an
  extra `<FF02>` over letting it scroll many times.
- **Control codes**: keep every control code, in order and with its
  parameter bytes (e.g. `<FFFD><24>`), unless the code is purely a line break.
  Never translate or reorder `<...>` tokens.
- **Fixed-size fields** (menus, item and skill names, character names
  limited to 5 characters, ...): respect the field size. armips `strpad`
  fails the build on overflow. If an official name does not fit, use an
  official abbreviation if one exists, otherwise note it in the glossary
  and ask before abbreviating.
- Which table applies: dialogue (ADV/DNG/S2D) uses `common/persona_vwf.tbl`;
  everything else uses `common/persona.tbl` until it gets a VWF.

## 6. Consistency and review

- `glossary.tsv` is the single source of truth for terms. Look up before
  translating, add before introducing. Columns: `japanese`, `english`,
  `category`, `source` (`official-psp`, `official-other`, `game-text`,
  `project`), `notes`.
- Same Japanese line repeated -> same English line, unless context differs.
- Untranslated or uncertain lines are marked, never guessed silently.
- After inserting text, check it in the emulator (line width, page breaks,
  choices still selectable with Circle).
