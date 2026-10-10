"""E0 entry 68 - Aki and Tesso."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Maki: Ah! There she is!"],
    1: ["Girl in Black: Ah! The ones who got in Papa's way!"],
    2: ["Maki: Put the school back the way it was! If you don't, I'll spank you until your bottom swells to twice its size!"],
    3: [
        "Girl in Black: Nooo way~! Aki only listens to what Papa says!",
        "Girl in Black: Try it if you can, flat-chested woman!"
    ],
    4: ["Maki: Flat...?! That's it, I'm furious! What a hateful child!!"],
    5: ["Mark: Calm down, Sonomura. She's just a kid. Let's talk some sense into her..."],
    6: ["Aki: Shut up, little monkey! Monkey, monkey, monkey, monkey!"],
    7: ["Mark: ..." + P('ヒ') + " What the hell! You little brat~!"],
    8: ["Nanjo: Calm down, monkey."],
    9: ["Mark: Nanjooo!! You bastard~!! I'll kill you!!"],
    10: ["Aki: Ugh, you're so noisy! Perfect, just die right here!"],
    11: ["Aki: Nomoraka tanomamaa! Come out, Tesso!!"],
    12: ["Tesso: Tesso! Tesso! Ukkyuu!!"],
    13: ["Elly: Mark! This is no time to be playing around!"],
    14: ["Brown: Waah! In front, in front, in front!"],
    15: ["Ayase: Hey! Something weird showed up!"],
    16: ["Aki: Get them, Tesso!!"],
    17: ["Reiji: ...You guys are gonna die."],
}
REVIEW = {2: "ペンペン = spank", 3: "ペチャパイ = flat-chested", 11: "Aki's incantation kept as sound", 12: "Tesso's cry guessed"}

if __name__ == '__main__':
    apply('E0', 68, BOXES, REVIEW)
