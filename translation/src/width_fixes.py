"""2026-10-04: lines of exactly 240 px broke in game (the engine wraps at 240, an explicit <FF03> then skips a
second line; found on the Nanjo card). tools/fix_width.py moved words automatically; the boxes below needed
a different wording or pagination. Same Japanese -> same English everywhere, so the replacements run on all TSVs.
"""
import glob
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
NL = '<FF03>'

REPLACE = [
    # Nanjo card (E0/0/43): 3 lines max; "Thorough" -> "Total" to fit (flagged)
    ("Known as Nanjo-kun. Nanjo zaibatsu" + NL + "heir. Thorough rationalist.",
     "Known as Nanjo-kun. Nanjo" + NL + "zaibatsu heir. Total rationalist."),
    # E0/7/1: "No," moved to the next page (the pause sits at the page end)
    ("wanna hurry up and go to Sono...<FF05><40><00> No,<FF02><FF04>Mark: no, I wanna go to the",
     "wanna hurry up and go to Sono...<FF05><40><00><FF02><FF04>Mark: No, no, I wanna go to the"),
    # E0/8/4
    ("have played Persona-sama before...", "played Persona-sama before..."),
    # casino help (shared by many entries)
    ("If the number of the selected card" + NL + "and the face-up card are the same," + NL + "it is a draw and you can try again.",
     "If the selected card's number is" + NL + "the same as the face-up card's," + NL + "it is a draw and you can try again."),
    # 2026-10-05: <FF0F> (player name) now counts 45 px (5 widest letters) in vwf_wrap; these four needed rewording
    ("Natsumi-sensei: You're awake,<FF03><FF0F>あ-kun. Welcome to the infirmary.<FF03>You had a cute sleeping face.<FF02>",
     "Natsumi-sensei: You're awake,<FF03><FF0F>あ-kun. Welcome to the<FF03>infirmary. Cute sleeping face.<FF02>"),
    ("<FF06><03>Takami Saeko<FF03><FF0F>あ's homeroom teacher. Bright and<FF03>very popular with the students.<FF02>",
     "<FF06><03>Takami Saeko<FF03><FF0F>あ's homeroom teacher.<FF03>Bright and popular with students.<FF02>"),
    ("Principal Oishi: My, <FF0F>あ-kun. Are you<FF03>all on a walk as well? Praying to<FF03>this guardian deity for everyone<FF02><FF04>"
     "Principal Oishi: to become fine<FF03>adults... that has been my daily<FF03>routine since I was young.<FF02>",
     "Principal Oishi: My, <FF0F>あ-kun.<FF03>Are you all on a walk as well?<FF03>I pray to this guardian deity<FF02><FF04>"
     "Principal Oishi: for everyone to<FF03>become fine adults... that has been<FF03>my daily routine since I was young.<FF02>"),
    ("Yukino: I wonder if the school is<FF03>okay...<FF03><FF0F>あ, let's hurry and get outside.<FF02>",
     "Yukino: I wonder if the school is<FF03>okay... <FF0F>あ, let's hurry<FF03>and get outside.<FF02>"),
    # 2026-10-05: a Japanese choice question of exactly 15 glyphs ends its line, so the options (<FF0E>) started on
    # the next line; the shorter English needs an explicit <FF03> before <FF0E> (else "right?Tha/t's the plan")
    ("You mean to beat SEBEC, right?<FF0E>", "You mean to beat SEBEC, right?<FF03><FF0E>"),
    ("It is an unavoidable choice!<FF03>Let us go!<FF0E>", "An unavoidable choice! Let us go!<FF03><FF0E>"),
    ("Trade coins for items?<FF0E>", "Trade coins for items?<FF03><FF0E>"),
]


def replace_all():
    n = 0
    for f in sorted(glob.glob(os.path.join(ROOT, 'translation', 'events', 'E?.tsv'))):
        s = open(f, encoding='utf-8').read()
        t = s
        for old, new in REPLACE:
            n += t.count(old)
            t = t.replace(old, new)
        if t != s:
            open(f, 'w', encoding='utf-8', newline=chr(10)).write(t)
    print('replaced', n, 'occurrences')


if __name__ == '__main__':
    replace_all()
    apply('E0', 38, {0: [
        "Student Council President: If I can just get through this, I will surely leave my name in school history "
        "as a great Student Council President...",
        "Student Council President: If you want to be of even a little use to the school, why don't you try "
        "resolving this incident?"]})
    apply('E0', 39, {8: [
        "Principal Oishi: I don't want to lose any more of my precious students ever again.<FF05><25><00>",
        "Principal Oishi: Please, take good care of yourselves."]})
    apply('E0', 42, {26: [
        "Nanjo: This is the gun. It seems that invoking a Persona consumes quite a lot of spirit.",
        "Nanjo: Inaba was exhausted by that and captured. If one is prepared, there is nothing to fear.",
        "Nanjo: Do not forget to equip it."]})
    import tl_lib
    tl_lib._flag('E0', 0, {43: "reworded to fit 239 px: 'Total rationalist' instead of 'Thorough rationalist' (徹底した合理主義者)"})
