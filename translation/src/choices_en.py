"""English for the dialogue choice table (translation/strings/CHOICES.tsv, tools/choices.py).

Syntax: rows joined by <FF03>; cells of a 2-column row joined by `|` (padded by the build).
Run: python translation/src/choices_en.py   (fills the `en` column, then `python tools/choices.py build`)
"""
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import choices  # noqa: E402

EN = {
    0: "Yes<FF03>No",
    1: "Sure<FF03>No way",
    2: "I know<FF03>I don't know",
    3: "Start Game|Quit<FF03>Check Coins|Explanation",
    4: "No<FF03>Yes",
    5: "Game Rules|Controls<FF03>About Hands|Go Back",
    6: "Game Rules|Controls<FF03>Advice|Go Back",
    7: "Let's go together<FF03>Don't take them",
    8: "Lend a hand<FF03>Don't lend a hand",
    9: "Don't go outside<FF03>Go outside",
    10: "Don't open it<FF03>Open it",
    11: "Don't listen<FF03>Listen",
    12: "Fuse|Never Mind<FF03>Summon/Erase|Hear Story",
    13: "Don't run|It's safe<FF03>True, but...|Who knows",
    14: "For myself|No reason<FF03>For everyone|It just happened",
    15: "...Why, I wonder?<FF03>To find that answer",
    16: "Press the red button<FF03>Press the blue button",
    17: "Heal me<FF03>No business",
    18: "Fight Hariti<FF03>Don't fight Hariti",
    19: "Don't run!<FF03>Maybe so...",
    20: "Stay|To 8F<FF03>To 4F|To 1F",
    21: "Self Fusion|Guided Fusion<FF03>View Cards|Never Mind",
    22: "Queen's painting is better<FF03>Maki's painting is better",
    23: "Beginner|Intermediate<FF03>Persona|Advanced",
    24: "Start Game|Quit<FF03>Check Cards|Explanation",
    25: "Bet on Mark<FF03>Bet on Brown",
    26: "That's the plan<FF03>Not exactly",
    27: "I guess so<FF03>That's not true",
    28: "Yes, I do<FF03>No, I don't",
    29: "I do<FF03>I don't",
    30: "The old one's better<FF03>This is fine as is",
    31: "Register<FF03>Don't register",
}

REVIEW = {
    12: "合体/降魔/消去: Fuse / Summon(Evoke?) / Erase; 話が聞きたい = want to hear the story/talk",
    13: "うん安全だ -> It's safe, わからないぞ -> Who knows (column width limit)",
    20: "戻らない = Don't go back, shortened to Stay (column 1 is 64 px wide); 8F/4F/1F are floors",
    23: "Dropped 'Topics' (話) to fit column 2; 初心者/中級者/上級者 = Beginner/Intermediate/Advanced",
    28: "いる/いない: answers E0/67/35 \"Do you have someone dear to you?\" -> Yes, I do / No, I don't (user asked to decide)",
    29: "ある/ない: answers E0/67/39 \"You've got secrets too, right?\" -> I do / I don't",
    25: "マークにのる = side with / go along with Mark; user chose 'Bet on Mark / Bet on Brown' (2026-10-04)",
}

if __name__ == '__main__':
    rows = choices.read_tsv()
    with open(choices.TSV, 'w', encoding='utf-8', newline=choices.NL) as o:
        o.write('idx\tptr\tparams\tja\ten' + choices.NL)
        for r in rows:
            o.write('\t'.join(r[:4] + [EN.get(int(r[0]), '')]) + choices.NL)
    rv = os.path.join(ROOT, 'translation', 'review.tsv')
    have = open(rv, encoding='utf-8').read()
    with open(rv, 'a', encoding='utf-8', newline=choices.NL) as o:
        for k, why in REVIEW.items():
            if f'CHOICES\t{k}\t' not in have:
                o.write(f'CHOICES\t{k}\t0\t{why}' + choices.NL)
    print('filled', len(EN), 'choices')
