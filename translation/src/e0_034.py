"""E0 entry 34 - Infirmary."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Maki's Mother: And that is what happened."],
    1: [
        "Saeko-sensei: SEBEC, huh..." + P('み') + " But really, those kids!" + P('な') + " Hey, <FF0F>あ, I'm sorry to ask, but",
        "Saeko-sensei: could you go to the hole in the wall and tell Mayuzumi and the others to stop blocking it up?",
        "Saeko-sensei: Inaba and Nanjo might come back."
    ],
    2: ["Maki's Mother: I don't know what to say for causing everyone so much trouble..."],
    3: [
        "Saeko-sensei: Those guys know about the hole in the wall, right?",
        "Saeko-sensei: The school gate has been closed, so they won't be able to get in any other way."
    ],
    4: ["Agastya Tree: Young one... It is good that you have come to me."],
    5: "=Agastya Tree:<FF03>Will you engrave<FF03>your record into me?<FF02><FF03><FF0E>　<FF01>",
    7: [
        "Natsumi-sensei: Sonomura-san's mother's wounds aren't too bad. You can rest easy.",
        "Natsumi-sensei: How about you, <FF0F>あ-kun? Are you hurt? I'll take a look at you."
    ],
    8: ["Natsumi-sensei: There, you're all right now. Go carefully."]
}

if __name__ == '__main__':
    apply('E0', 34, BOXES)
