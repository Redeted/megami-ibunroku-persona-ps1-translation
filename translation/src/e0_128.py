"""E0 entry 128 - the compact is set into the pedestal; Kandori's trap."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Mark: Alright, <FF0F>あ, let's put that \"Half Compact\" into the pedestal."],
    1: ["Nanjo: ..." + P('で') + " Wait, <FF0F>あ."],
    2: ["Maki: Why, Nanjo-kun?"],
    3: ["Nanjo: ..." + P('で') + " No, it is nothing. Continue."],
    4: [
        "Mark: You're acting weird. Even weirder than usual.",
        "Mark: You've been like that for a while now."
    ],
    5: ["Nanjo: ...Do not mind it."],
    6: ["Mark: Tch!" + P('で') + " That's what he says. Go ahead, <FF0F>あ."],
    7: [
        "Maki: <FF07>あ-kun, Kandori and Aki are up there... We finally made it this far."
    ],
    8: ["Maki: What do we do! We have to get Mai-chan's compact back!"],
    9: ["Mark: Hurry up. All you have to do is put the compact into the pedestal."],
    10: ["Mark: Damn it! We've been completely played!"],
    11: ["Nanjo: Kandori... such a dirty trick..."],
    12: [
        "Nanjo: In any case, we had no choice but to move as he wished.",
        "Nanjo: Cunning, but a clever method."
    ],
    13: ["Reiji: ..." + P('で') + " Kandori... You're not getting away. I'll settle this grudge for sure."],
    14: ["Reiji: ..." + P('で') + " Dirty bastard, just like his old man..."],
    15: ["Elly: ...I have a bad feeling about this. Be careful, <FF07>あ."],
    16: [
        "Elly: As I thought... But nothing has happened to <FF07>あ, so I am relieved."
    ],
    17: ["Brown: <FF08>あ, it'd be bad if something happened, so be careful...", "Brown: Want me to switch with you?"],
    18: [
        "Brown: That's dirty! Is this allowed?!",
        "Brown: I'm really pissed off now!"
    ],
    19: ["Ayase: <FF0F>あ~, hurry up~!"],
    20: [
        "Ayase: So sneaky! Using people like that is the worst!",
        "Ayase: Guys like that are the most annoying!!"
    ],
    21: "=Place the Half Compact?<FF03><FF0E>　<FF01>",
    22: ["Mark: W-What's going on?"],
    23: ["Nanjo: Kandori must be unable to stop laughing."],
    24: ["Maki: What does this mean!?"],
    25: [
        "Nanjo: What Kandori wanted was that compact. If he cannot lay a hand on Mai,",
        "Nanjo: he can simply have someone else bring it. We were used as a pretext."
    ],
    26: [
        "Mark: What?! That bastard!!",
        "Mark: If you knew, say so!"
    ],
    27: ["Nanjo: If we did not do this, we could not meet him."],
    28: [
        "Maki: But why? He could just take the compact. Why does he need to let us in?"
    ],
    29: [
        "Nanjo: He is telling us to come. He must be quite confident."
    ],
    30: [
        "Mark: Making fools of us... Fine, interesting. I'll take the bait!",
        "Mark: Let's go, <FF0F>あ!"
    ],
    31: ["The door is firmly shut."],
    32: [
        "Maki: A haunted house, huh. I used to sneak in there a lot when I was little..." + P('キ') + " Huh... I... who was it that scolded me?"
    ],
    33: [
        "Mark: Still, to think Reiji is that bastard's younger brother, I was surprised.",
        "Mark: Now that you mention it, their eyes are kinda similar."
    ],
    34: ["Mark: Kido must be frustrated."],
    35: [
        "Nanjo: ...No, that is not it. But if we think of it this way... No, wait...",
        "Nanjo: Hm? I am busy right now."
    ],
    36: ["Elly: <FF07>あ, let us hurry to the Haunted House!"],
    37: ["Brown: The haunted house is south of here, right?"],
    38: ["Ayase: Hurry, hurry! We can't be dawdling! The haunted house was to the south, right?"],
    39: ["Reiji: Is this the time to be chatting?! Hurry up and chase that bastard!"],
}
REVIEW = {32: "幽霊屋敷 = Haunted House"}

if __name__ == '__main__':
    apply('E0', 128, BOXES, REVIEW)
