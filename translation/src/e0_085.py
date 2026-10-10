"""E0 entry 85 - party chatter about the mask man and the butterfly; Maki dizzy."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Maki: That man in the mask... What on earth is he?"],
    1: ["Nanjo: I see. Sonomura, you said you have met that masked man before."],
    2: ["Mark: Why's there always a butterfly flying around, I wonder?"],
    3: ["Elly: This world is very interesting."],
    4: ["Brown: Meeting a creepy old guy like that? Ain't happy about it!"],
    5: ["Ayase: Ayase has seen that butterfly guy in a dream too."],
    6: ["Reiji: You're sure that butterfly has nothing to do with him?"],
    7: ["Mark: Nobody's here..." + P('ぎ') + " Did that Kurouri guy trick us?"],
    8: ["Nanjo: But the Kurouri of this world seemed trustworthy..." + P('み') + " What is that?"],
    9: ["Nanjo: ..." + P('と') + " Hey, Inaba. That butterfly..."],
    10: ["Elly: Oh, that butterfly. It was there when Maki's mother collapsed."],
    11: ["Ayase: Isn't it a pretty butterfly? Should we catch it and keep it?"],
    12: [
        "Brown: Nanjo, are you interested in butterflies or something?",
        "Brown: Are you the type who fills his room with butterfly specimens and grins at them?"
    ],
    13: ["Reiji: " + P('み') + " ...Could it be his trap?" + P('な') + " If it does anything the least bit strange, I'll catch it and crush it."],
    14: ["Maki: Oh no..." + P('ゆ') + " My vision..." + P('ゆ') + " is spinning...!"],
}
REVIEW = {}

if __name__ == '__main__':
    apply('E0', 85, BOXES, REVIEW)
