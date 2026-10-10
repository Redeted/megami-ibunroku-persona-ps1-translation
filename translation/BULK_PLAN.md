# Bulk translation plan (written 2026-10-06 after the text-source audit)

## 1. What is left (measured)

| family | size | status / how it is shown |
|---|---|---|
| Event scripts `ADV/E0..E3.BIN` | 5057 boxes left of 7344 = **4415 unique texts, ~181,000 JP characters** (E0 1881 boxes in 71 entries, E1 1118 / 53, E2 1411 / 137, E3 647 / 62) | dialogue VWF engine, verified in ADV/S2D; DNG path untested; 17 entries are empty placeholders |
| Negotiation `TALK/*.BIN` | **13085 units, 10290 unique, ~300,000 JP characters** (28 files, 370-740 units each) | BTLP text box VWF hook verified with test bytes only; **no real TALK English ever seen in game** |
| BTLP negotiation UI + character lines (FFF5 strings outside `btlmsg`) | ~200 strings, ~3,300 characters (`0x800C87DC-0x800CEE21`: prompt "悪魔から話しかけてきた！", 答える/無視する, per-character lines ...) | same BTLP text interpreter, translate with btlmsg-style tool |
| Dungeon in-room messages (`D0x/D??.BIN`) | ~12 distinct (door locked, shop closed ...) in ~15 places | DNG overlay dialogue engine (untested) |
| Done / not text | items, skills, Persona/demon names, races, affinities, menus, Config, equipment, fusion, save screens, load-game screens, battle messages/UI, story battles, casino, overworld names, dungeon floor names | |
| No game text found | ADV/BST, TYNSE, DVL, PER, KAGE, B/*, CD0/*, END.BIN, MOVIE/END/ATLUS.EXE, NAMEDT, CASINO.BIN, 2D/* (graphics, audio, data) | nothing to extract |

Total remaining: **~485,000 JP characters** (about 800,000 English characters, roughly 200k output tokens).

## 2. Cases that need a manual playthrough (cannot be verified offline)

Blocking (do first, they decide how the bulk text must be written):
1. **TALK negotiation text in the BTLP box**: translate ~20 units of one demon, then negotiate with it. Checks: 3-line pages,
   line width (15 cells = 239 px), `FFF6` newline / `FFFC` pause / `FFFB`/`FFF7` parameter pairs / `FFFD` branches, `FFF9` name tokens.
2. **BTLP negotiation prompts** (demon-initiated prompt and its options, the CONTACT result texts): translated in the same pilot.

Non-blocking (user-supplied states, can run while the bulk goes on):
3. Dungeon locked-door / shop-closed messages (DNG dialogue engine never tested).
4. Field menus not yet checked: MAGIC, FORM, STATUS pages, ANALYZE (field), ITEM > USE with targets.
5. Battle result screens: victory / EXP / level-up / game over; item use and Persona change in battle; ESCAPE messages.
6. Shops other than the casino exchange (convenience store / clinic menus).
7. Name entry errors and default names.
8. FMV subtitles (opening quote) and the ending credits: probably baked into video / bitmaps; decision needed after a look.
9. Remaining ADV menu strings listed in HANDOFF (spell-card / analyze menus at ADV 0x4DF18, 0x4EAF1).

## 3. How the bulk is done

* Unit of work = **part** (a group of entries / TALK files, ~10-15k JP characters, ~350 boxes or ~700 TALK units).
  Events: ~14 parts (E0 5, E1 3, E2 4, E3 2). TALK: ~12 parts of 2-3 demon files. Pilot part first.
* Translator: `agy-job start --tier pro --dir . --yolo --timeout 1700s` (the `s` unit is required), 2-3 jobs in parallel, ~100-150
  boxes per job. agy writes `translation/src/<file>_<n>.py` (events, same template as the existing ones) or a TSV (TALK), and a
  `REVIEW` dict with every line it is unsure about (puns, names, idioms, anything it had to guess).
* Gate per part, in this order: apply with `tl_lib.apply` (refuses width / code / label / charset errors) -> `tstatus propagate`
  -> `tstatus qa` -> **I review all flagged lines + a random 5% sample** (earlier batches: ~1-2% of boxes needed a fix) ->
  `python tools/build.py --no-disc` (layout round-trip) -> `python tools/build.py` (disc) -> **boot test** (see below).
* Boot test after every part: close DuckStation, build, `boot_game` the cue, run at normal/turbo speed ~60 s WITHOUT button
  presses (the intro cinematics loop if Start is pressed), screenshot must show the title screen; then `shutdown_system`.
  Structural check on top: re-parse the built E files / TALK files and compare every box with the TSV.
* Scene check by the user: one hard save near a translated scene per part (old save states are invalid after a rebuild).
* Disc size: relocated files are appended after the original volume (+5361 sectors now, about +10-15k more at the end, far below
  CD capacity). RAM limits: E entries load at 0x80100000, TALK files at 0x801C0000 (256 KB free): English fits.

## 4. Order

0. Pilot: TALK part of one demon (SLIME) + BTLP negotiation prompts + dungeon messages -> user tests the negotiation.
1. Events in story order of the parts already half done (E0 entries 50+), then E1, E2, E3 (file order is NOT story order; the
   user checks scenes as they come).
2. TALK files, biggest first, after the pilot proved the format.
3. Manual-playthrough items 3-9 in parallel.
