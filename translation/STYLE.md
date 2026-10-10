# Style sheet (keep every agent's output consistent)

Rules in `TRANSLATION_GUIDE.md` win. This file records the choices made while translating, so
the next batch sounds like the last. Add to it whenever you decide something new.

## Voices (from the opening scene and the first-day scenes)

| speaker | label | voice |
|---|---|---|
| マーク (Inaba Masao) | `Mark:` | rough, impulsive teenager from a laundry family; contractions, "jerk", "geez", "man"; swears mildly, never stronger than the Japanese |
| 南条 | `Nanjo:` | arrogant, formal, precise; no contractions ("Let us...", "It is..."); addresses people as "you people", "you"; calls Mark "Inaba" |
| ゆきの | `Yukino:` | blunt, tough big-sister; short sentences, dry; "Hmm.", "Huh.", "Do what you like." |
| アヤセ | `Ayase:` | bubbly kogal; refers to herself as "Ayase"; "Yaaay!", stretched vowels, "~" |
| エリー | `Elly:` | polite, ladylike, curious; keeps odd English capitals the Japanese uses for her English words ("I'll Bet on Brown", "Fantastic!") |
| ブラウン | `Brown:` | show-off joker; "man", "heh heh", laughs written phonetically ("Pupupupu...") |
| 山岡 | `Yamaoka:` | very polite old retainer; calls Nanjo "the young master" (ぼっちゃま) |
| 麻希 | `Maki:` | gentle (check as scenes appear) |

Other speakers: use the glossary label (`Nurse:`, `Student:`, `College Girl:` ...). Unnamed boxes
(narration, descriptions) have no label.

## Conventions

- Speaker label format `Name: ` at the start; repeat it on every page of a box.
- Honorifics stay: `Nanjo-kun`, `Yukino-san`, `Maki-san`. Nicknames stay (Mark, Brown, Elly, Ayase).
- Names Japanese order when a full name is written (`Inaba Masao`); family name alone otherwise.
- Ellipsis: three dots `...` for `…`. Tilde `~` kept for sung/stretched endings. `!?` kept as in the Japanese.
- Quotes: Japanese 「」 -> `"` (inner `'`); never smart quotes.
- Intro/description cards: `Known as X.` (通称); Japanese parenthetical readings are dropped.
- Culture kept: zaibatsu, kogal, yen, school-club terms, `-dori` for streets (Joy-dori).
- Sound/exclamation equivalents of the same length ("Tch!", "Geh!" -> "Gah!", "Kyaa!").
- Pause codes (`<FF05>`) stay where the pause falls in the English sentence; ellipsis dots repeated per pause
  as in the Japanese (e.g. Brown's 14 pauses).
- Keep one box per Japanese box; only split into pages when the text needs more than 3 lines.
- The player name (`<FF0F>あ`) counts as 45 px in the width check (5 typed letters); a choice prompt (`<FF0E>`)
  always follows `<FF03>` (or a page start), even when the Japanese has none.
- Keep jokes and insults at the same strength; do not censor or soften.

## Open decisions (ask a human)

- Proper nouns with doubtful kanji: see `translation/NAMES_AUDIT.md`.
- SEBEC spelling vs the 2009 PSP release.
