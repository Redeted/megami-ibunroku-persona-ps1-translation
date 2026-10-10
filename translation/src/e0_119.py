"""E0 entry 119 - Mai's bear disappears; the compact is dropped."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: [
        "Mai: Aah!! Mr. Bear! Mr. Bear died!",
        "Mai: Waaaaaah! Nobody is nice to Mai-chan!",
        "Mai: Be nicer to me!"
    ],
    1: ["Maki: She's gone... It feels like we did something bad..."],
    2: ["Nanjo: Honestly... It is because Inaba frightened her so strangely! We have lost a valuable source of information."],
    3: ["Elly: That Bear... was her only friend. And we..."],
    4: [
        "Brown: Magical girl indeed. That was close.",
        "Brown: Still... I kinda feel sorry for her."
    ],
    5: ["Ayase: Geez! It's because Inaba said something unnecessary!"],
    6: ["Mark: Can't be helped! I never thought it'd turn out like this..."],
    7: ["Nanjo: Hm? Something has dropped."],
    8: ["Maki: Ah! It's Mai-chan's compact!"],
    9: ["Mark: I see... She must've dropped it. It leaves a bad aftertaste, but let's borrow it."],
    10: ["Maki: Any wish can come true, right... Shall we have it carry us to the castle?"],
    11: ["Nanjo: Indeed. Inaba, try it."],
    12: [
        "Mark: Okay. It went like this, right?",
        "Mark: Nomoraka tanomama!"
    ],
    13: ["Maki: ..." + P('ほ') + " ..." + P('ほ') + " ..." + P('で') + " Nothing's happening."],
    14: [
        "Nanjo: I see, nothing is that easy. It can probably only be used by that child."
    ],
    15: ["Mark: Can't be helped. Let's walk."],
    21: ["Brown: Aww, what a shame! I've got so many wishes!"],
}
REVIEW = {}

if __name__ == '__main__':
    apply('E0', 119, BOXES, REVIEW)
