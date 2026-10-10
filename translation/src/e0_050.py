"""E0 entry 50 - Mark/Brown join."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Brown: Wha- Wha- What was that just now!? W-Why is the great me... Wait, what is that?!"],
    1: ["Nanjo: Uesugi, you too..." + P('ゆ') + " However, out of everyone, why someone like this guy too..."],
    2: ["Mark: Then, I'll explain it to you. Got it? Listen well..."],
    3: [
        "Brown: Amaaaazing! So the great me was a hero of justice after all!",
        "Brown: Nah, I always thought there was something different about the great me since I was a kid!"
    ],
    4: [
        "Mark: You don't really get it..." + P('み') + " ...Well, whatever.",
        "Mark: " + P('た') + "Anyway, <FF0F>あ, I'm coming with you too. It's a bit worrying with just you guys, y'know."
    ],
    5: ["Nanjo: That is my line." + P('み') + " Inaba, hand over the \"security card\" to <FF0F>あ."],
    6: ["Mark: ...Can't be helped. Here, it's the \"security card\". Don't lose it."],
    7: ["Nanjo: Inaba, this is your gun. Do not shoot us by mistake."],
    8: [
        "Brown: Hey, hey, should the great me tag along with you too?",
        "Brown: It's a bit lacking in star power with just you guys, y'know.",
        "Brown: If the great me is there, the party'll tighten right up, right? What do you say, <FF08>あ!"
    ],
    9: ["Mark: ...What do you want to do? <FF0F>あ."],
    10: "=What will you do?<FF03><FF0E>き<FF01>",
    11: ["Brown: Okay! Since it can't be helped, the great me will lend you a hand! Wahahaha!"],
    12: [
        "Nanjo: Then, Uesugi. This is a gun for your use. Do not fire it recklessly.",
        "Nanjo: ...Where are you looking?"
    ],
    13: [
        "Brown: Ah, yeah?" + P('た') + " Really? You won't regret it?" + P('た') + " Ah, yeah...",
        "Brown: Then, the great me's gonna go to school or something." + P('た') + " ..." + P('な') + " Don't regret it!"
    ],
    14: ["Maki: Alright! So now that everyone's here... Where were we going again?"],
    15: [
        "Nanjo: Do not lose the \"security card\".",
        "Nanjo: Without this, we cannot enter what they call the loading bay from the abandoned factory."
    ],
    16: ["Mark: The octopus geezer turned into a Demon, man..." + P('み') + " It's all messed up now!"],
    17: [
        "Brown: \"Let's go!\"? Or maybe \"Perso~na!\"? Nah, nah, both are way too lame.",
        "Brown: As expected, something like \"Nice to meet'cha!\" is best!"
    ],
}
REVIEW = {
    10: "Choice prompt - '=What will you do?'"
}

if __name__ == '__main__':
    apply('E0', 50, BOXES, REVIEW)
