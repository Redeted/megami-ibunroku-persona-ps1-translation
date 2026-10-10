"""E0 entry 20 - Hospital room, Maki wakes up."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: [
        "Doctor: Well then, I'll be going...<FF03>Make sure to go outside sometimes.",
        "Doctor: That's an important part of rehab too, you see."
    ],
    1: ["Nurse: That's right, Maki-san.<FF03>Let's go for a walk tomorrow."],
    2: ["Maki: ........."],
    3: [
        F6('う') + "Sonomura Maki<FF03>A classmate who's been hospitalized for a year.",
        "She's been in and out of hospitals since childhood." + F6('　')
    ],
    4: [
        "Doctor: Hm?<FF03>It seems the best medicine has arrived.",
        "Doctor: Well then, we'll excuse ourselves."
    ],
    5: [
        "Maki: <FF0F>あ-kun...<FF03>You all came...<FF03>Thank you.",
        "Maki: Inaba-kun, you were being considerate of me, weren't you."
    ],
    6: ["Nanjo: What is the meaning of this?"],
    7: [
        "Maki: Because when Inaba-kun visited me before, I said I wanted to see everyone...",
        "Maki: " + P('ス') + " Am I wrong?"
    ],
    8: [
        "Yukino: ...You're not wrong.<FF03>" + P('キ') + " How's it going? Feeling okay?"
    ],
    9: [
        "Yukino: ...You're not wrong.<FF03>" + P('キ') + " Himeno said she'd come by to return your book, too.",
        "Yukino: I think it was called \"Door to Paradise\"."
    ],
    10: [
        "Maki: I see... She didn't have to.<FF03>I've read it so many times, I have it memorized..."
    ],
    11: [
        "Yukino: Got it, I'll tell her when I see her.",
        "Yukino: " + P('キ') + " More importantly, how's it going? Feeling okay?"
    ],
    12: [
        "Maki: Yeah, I'm feeling a lot better than before.",
        "Maki: Maybe it's because I've been having good dreams lately...",
        "Maki: I don't really remember them well, though.",
        "Maki: A dream about a very kind man...<FF03>Like a father..."
    ],
    13: [
        "Yukino: Like that doctor from earlier?<FF03>He seems like a good doctor."
    ],
    14: ["Maki: ..." + P('ぎ') + " I hate him..."],
    15: ["Mark: Did he do somethin' to you!?"],
    16: ["Maki: It's not like that, but... I just hate doctors..."],
    17: [
        "Mark: Well, let's drop it.<FF03>Oh yeah! What about your mom?",
        "Mark: I think she works at SEBEC, right?"
    ],
    18: [
        "Maki: That woman is not my mom!<FF03>Her work is more important to her than me!",
        "Maki: " + P('ス') + " She doesn't care about me at all..."
    ],
    19: ["Mark: M-My bad..."],
    20: ["Maki: Ah... I'm sorry...<FF03>" + P('ス') + " Ngh?"],
    21: ["Maki: N... " + P('で') + " Nooooooooo!"],
    22: ["Mark: What's wrong!? Sonomura!<FF03>Hey!"],
    23: ["Yukino: This is bad! Get the doctor!"],
    24: ["Nanjo: ...Yamaoka."],
    25: [
        "Mark: This place...<FF03>smells like Sonomura...<FF03>" + P('キ') + " I'll find you for sure, Sonomura."
    ],
    26: [
        "Yukino: I'm worried about Sonomura too, but...<FF03>for now, let's head out into town.",
        "Yukino: I have a bad feeling about this."
    ],
    27: [
        "Yukino: <FF0F>あ,<FF03>what are we going to do about Sonomura's mom?",
        "Yukino: If we don't hurry, it'll be too late."
    ],
    28: [
        "Elly: ...<FF03>Is this Maki's hospital room?",
        "Elly: It feels... like a very lonely place..."
    ],
    29: [
        "A painting titled \"Door to Paradise\"<FF03>that Maki won an award for...",
        "Looking at it,<FF03>you can almost feel Maki's heartache..."
    ]
}

if __name__ == '__main__':
    apply('E0', 20, BOXES)
