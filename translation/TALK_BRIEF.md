# Brief for translating the demon negotiation scripts (TALK/*.BIN)

Read first: `TRANSLATION_GUIDE.md`, `glossary.tsv`, `translation/STYLE.md` (literal translation, no westernizing, official PSP names).

## What the text is
Megami Ibunroku Persona (PS1). In battle the party talks to a demon (CONTACT). Every party member has 4 contact commands (Persuade,
Taunt, Invite, Sing, Plead, Flatter, Lie, Cringe, Bribe, Pontificate, Condescend, Sarcasm, Dance, Stare, Brag, Pick up, Joke, Chat,
Startle, Horrify, Soothe, Abuse, Seduce, Cry, Threaten, Bully, Scold, Ignore, Scream, Prestidigitate ...). The demon answers with ONE
unit = ONE text page of at most 3 lines. The reply depends on the demon's personality (Wise, Foolish, Joyful, Gloomy, Bold, Timid,
Snappish, Haughty), the party member and how the demon feels (JOY / ANGER / FEAR / INTEREST), so a file contains many variations of
the same few ideas. The demon addresses the speaker directly. A file = one "voice" shared by several demons; keep that voice in
every unit (see the comments in the task for the file).

## Control codes (copy them; every one has a function)
* `<FFF6>` new line. At most 2 per unit (3 lines). `<FFFC>` short pause (keep the same number of them, move to a natural place).
* `<FFF5>` end of the page (the unit must end with it exactly once; a few units end with `<FFEF>`: keep what the Japanese has).
* `<FFFD>#` inserted by the tool in place of the real parameter character: write exactly `<FFFD>#` where the _ja file has it
  (position at the end of the speech, right before the end code).
* `<FFFB><FFF7>` pair: keep both, in that order, once each, where the Japanese has them (a long pause in the middle of the speech).
* Name insertions (the game replaces them with a name when it shows the text): `<FFF3>` = the demon's own name (e.g. "Ghost",
  up to 10 letters), `<FFF0>` = a second name (race name, up to ~6 letters), `<FFF9>` = the name of the party member talking (up to
  8 letters), `<FFF4>` item name, `<FFF2>` spell card name, `<FFF8>` a number. Use them like a name in English
  ("<FFF3> is happy", "You, <FFF9>!"); do not add spaces that are not needed. A demon that talks about itself in the third person
  in the Japanese (`<FFF3>` inside its own line) keeps doing so. A full-width space right after such a code in the Japanese is only
  padding: drop it.

## Hard limits (checked by `python tools/talktl.py check NAME`)
* A line is at most 239 pixels wide in the proportional font (about 30-34 letters); at most 3 lines. The Japanese uses up to 3 lines
  of 15 characters, so the English must be COMPACT: shorter sentences, fewer fillers, but keep the meaning, the tone and the
  attitude of the demon. If you had to cut content, put `REVIEW: shortened` in the note column.
* Only ASCII letters, digits, space and `! ? . , ' " - ~ : ; / ( ) & * +`. Japanese ellipsis `…` -> `...`; `！？` -> `!?`;
  quotes 「」 -> `"`. Sound effects and laughter as in the Japanese ("Nyahahaha!").
* Honorifics stay (`-san`, `-kun`). Do not invent names.

## Deliverable
Edit ONLY `translation/work/talk_<NAME>_en.tsv` (tab separated, UTF-8, first line `unit<TAB>en<TAB>note`), one row per row of
`translation/work/talk_<NAME>_ja.tsv` (same `unit` number, in the same order; these are the unique Japanese texts). Run
`python tools/talktl.py check <NAME>` and fix every reported problem until it prints 0 problems and 0 missing. Put `REVIEW: <why>`
in the note column for puns, lines you are unsure about, names you had to guess, shortened lines. Do not edit any other file.
Finish with one line: units done / REVIEW count.

## Addendum: the player's ANSWER lines (`translation/work/talk_ANS_ja.tsv`, 1888 unique texts)
These are the replies the PLAYER's party member can give when a demon asks something or reacts: two (sometimes more) options are
shown in a small window, one per line, e.g. `そんなことないよ` / `やっぱりそう思う？` ("That's not true" / "You think so too, right?"),
`はい`, `いいだろう`, `やめる`, `さらに歌う`, `ざけんじゃないよ！`. Each speaker has a personality: Maki gentle, Mark rough and
impulsive, Nanjo arrogant and formal, Ayase bubbly kogal, Yukino blunt, Brown cocky show-off ("おれ様"), Elly polite, the
protagonist plain; infer the speaker from the tone of the Japanese. Keep them SHORT: at most 215 px (about 24 letters) per line and
at most 2 lines (`<FFF6>` = new line), same control codes as the Japanese (`<FFF5>`/`<FFEF>` at the end, `<FFFC>` pauses). The same
Japanese text has the same English everywhere (the file is already de-duplicated). Output `translation/work/talk_ANS_en.tsv`
(`unit<TAB>en<TAB>note`), check with `python tools/talktl.py ans-check` until 0 problems and 0 missing.
