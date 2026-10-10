"""E0 entry 99 - back at the market."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Master: Oh, all of you together. You are back early."],
    1: ["Mark: Ah, that woman~! She sent us all the way back here!"],
    2: [
        "Maki: Did Chisato really mean it? Maybe someone was controlling her.",
        "Maki: That's it! She must be controlled by that girl Aki!"
    ],
    3: [
        "Nanjo: Kozai's eyes had life in them.",
        "Nanjo: At least to me, they did not look like the eyes of someone being controlled."
    ],
    4: ["Elly: Shall we meet her once more? Then everything will become clear."],
    5: ["Brown: Anyway, let's go see her one more time."],
    6: ["Ayase: Let's go see her again. Maybe Kozai thinks she went too far, too?"],
    7: ["Reiji: Anyway, staying here gets us nowhere. We have no choice but to go see her again."],
}
REVIEW = {}

if __name__ == '__main__':
    apply('E0', 99, BOXES, REVIEW)
