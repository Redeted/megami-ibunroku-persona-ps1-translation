"""E0 entry 92 - the gate monster in the subway."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Monster: Nggh, aaahh... Shrruuuu... ...Yo... gu... soto..."],
    1: [
        "Maki: Wait! That monster looks strong!",
        "Maki: Let's go to the shrine like Kurouri-kun said. Maybe we'll learn something!"
    ],
    2: [
        "Monster: I AM THE GATE AND THE KEY. Son of... Yo-gu... So-toh...",
        "Monster: To one WITHOUT QUALIFICATION TO PASS, the gate shall NEVER open... Fu... Fshruuu..."
    ],
    3: [
        "Nanjo: ...I won't be able to eat fish for a while. And it stinks terribly.",
        "Nanjo: <FF0F>あ, I am sorry, but we cannot beat this thing as we are now.",
        "Nanjo: Here we have no choice but to heed the advice of that shady man."
    ],
    4: [
        "Yog-Sothoth Jr.: One who bears the \"Hama Mirror\"...",
        "Yog-Sothoth Jr.: But if you do not defeat me, you cannot pass here?"
    ],
    5: ["Mark: I figured it'd come to this! <FF0F>あ, let's go!"],
    6: [
        "Elly: If we leave this monster alone, it may grow bigger than a stable.",
        "Elly: If we are to defeat it, it must be now!"
    ],
    7: [
        "Ayase: Are we really gonna beat this thing?",
        "Ayase: Ayase can't get into this look..."
    ],
    8: ["Brown: This guy's got lousy taste, huh... And he reeks of fish!"],
    9: [
        "Reiji: No time to sit around whining.",
        "Reiji: If we don't beat this thing, we can't meet that guy!"
    ],
}
REVIEW = {2: "魔物 speech is katakana pastiche of Yog-Sothoth; kept formal", 4: "speaker label from glossary"}

if __name__ == '__main__':
    apply('E0', 92, BOXES, REVIEW)
