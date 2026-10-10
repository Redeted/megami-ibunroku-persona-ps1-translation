"""E0 entry 32 - At the school gate."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Elly: We have to bring Maki's mother here... She should still be at the shrine."],
    1: ["Elly: I am Kirishima Eriko. I have an injured person with me. Won't you open the gate?"],
    2: ["Guard: No! I can't let you in unless you say the password!"],
    3: ["Elly: ..." + P('た') + "I know. \"Walls have ears, I'm Mary\"..." + P('み') + " Will this do?"],
    4: ["Guard: All right, come in!"],
    5: [
        "Guard: No! I can't let anyone in!",
        "Guard: I mean, what if you guys are demons?!"
    ],
    6: ["Elly: The shrine is right nearby. Let's hurry up and go."],
    7: ["Yukino: <FF0F>あ, are you planning to leave Sonomura's mother all alone?"],
    8: ["Mark: Looks like they ain't plannin' on lettin' anyone in."],
    9: [
        "Nanjo: <FF0F>あ, Sonomura's mother was working for SEBEC, was she not?",
        "Nanjo: This is very suspicious."
    ],
    10: ["The school gate is firmly closed..."]
}

REVIEW = {
    3: "Pun on 'me ari' (has eyes) and Meari (Mary) in a Japanese proverb 'Walls have ears, doors have eyes'."
}

if __name__ == '__main__':
    apply('E0', 32, BOXES, REVIEW)
