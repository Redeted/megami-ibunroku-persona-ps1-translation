"""E0 entry 56 - Elevator room before Kandori."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Nanjo: Listen here, Inaba! From here on, do not recklessly touch anything we do not know the true nature of!"],
    1: ["Mark: I gooot it."],
    2: ["Nanjo: <FF0F>あ, then let us go."],
    3: ["Maki: Kandori... I wonder what kind of man he is."],
    4: ["Maki: Kandori..." + P('キ') + " Ah, sorry, it's nothing. More importantly, we have to hurry and chase him."],
    5: ["Mark: Geez, building something like this in our studio!"],
    6: ["Mark: Geez, man. I really liked this place, too. They totally ruined it!"],
    7: ["Nanjo: Somehow, with this lineup, we lack a sense of tension. I worry for our future, truly."],
    8: [
        "Nanjo: Hey, <FF0F>あ, is this the time to be wandering around!?",
        "Nanjo: If we do not find Kandori quickly, there is no telling what he might do."
    ],
    9: ["Elly: Actually, I have been interested in SEBEC for some time. I am looking forward to seeing what is inside!"],
    10: ["Elly: Where are we going? I believe the enemy is inside SEBEC, but..."],
    11: [
        "Brown: A-Alright, I'll let you take the lead.",
        "Brown: It'd be bad if the leader stood out too much, after all."
    ],
    12: [
        "Brown: Hey, hey, Kandori didn't escape outside, right?",
        "Brown: I understand the desire to run away, but we really have to give it our all here! So anyway, I'll leave the vanguard to you!"
    ],
    13: ["Ayase: Hey, hey, are we seriously going? Can't we just, like, not?"],
    14: ["Ayase: Ah, we're going home!? Ayase completely agrees!! Eh~, we aren't!?"],
    15: "=Will you ride the elevator?<FF03><FF0E>　<FF01>",
    16: ["It seems there is no longer a need to use the \"security card\"."],
    17: ["Maki: Come on, <FF07>あ-kun! Let's hurry!"]
}

REVIEW = {
    14: "Check if 'we aren't!?' sounds natural for 'え～　違うのぉ！？'"
}

if __name__ == '__main__':
    apply('E0', 56, BOXES, REVIEW)
