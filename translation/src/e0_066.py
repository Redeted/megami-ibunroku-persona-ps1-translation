"""E0 entry 66 - the party saves a student from a demon; Reiji appears."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Student: Eeek!! A demon!!"],
    1: ["Brown: Miss! Now that I'm here, you've got nothing to worry about!", "Brown: Go! <FF08>あ!"],
    2: ["Elly: Are you all right?! There is nothing to worry about anymore!"],
    3: ["Ayase: Ah! You okay?!", "Ayase: Hey, <FF0F>あ! What are you spacing out for?"],
    4: ["Maki: Ah! Are you okay?! Stop right there, demon!"],
    5: ["Demon: Oho, here they come, here they come. My fists thirst for blood tonight. I shall make blossoms of blood bloom to my heart's content."],
    6: ["Mark: Hey, you! Watch out! Get back!" + P('キ') + " ...Y-You're... Kido?!"],
    7: ["Reiji: You guys...? Get back... I'll kill this one."],
    8: [
        "Demon: Hoh, a spirited little boy. In honor of that spirit, I shall make you the first to be sacrificed.",
        "Demon: Regret your own immaturity in hell."
    ],
}
REVIEW = {}

if __name__ == '__main__':
    apply('E0', 66, BOXES, REVIEW)
