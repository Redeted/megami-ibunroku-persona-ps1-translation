"""E0 entry 117 - the Lost Forest; party chatter."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Maki: It was a beautiful flower garden until a month ago..."],
    1: [
        "Maki: ..." + P('で') + " Ah, sorry... I was thinking about something...",
        "Maki: Come on, let's hurry to the castle!"
    ],
    2: ["Mark: This place was the police station in our world, right?"],
    3: ["Mark: Hey, let's hurry back to that weird castle."],
    4: [
        "Nanjo: This world must have been quite safe before the disturbance.",
        "Nanjo: There is not even a police presence."
    ],
    5: ["Nanjo: ..." + P('で') + " Sorry. Let me think for a while."],
    6: ["Reiji: ..." + P('で') + " You've got no business with me. Get going."],
    7: ["Reiji: ..." + P('で') + " You've got no more business here. Get going."],
    8: ["Elly: What a lonely forest."],
    9: [
        "Elly: <FF07>あ, are you hurt at all?",
        "Elly: Huh? Why am I suddenly asking? No reason..." + P('で') + " Do I seem strange when I say things like this?"
    ],
    10: ["Brown: Feels like a dangerous place."],
    11: [
        "Brown: That girl from before asked something pretty heavy...",
        "Brown: I'm kinda feeling blue."
    ],
    12: [
        "Ayase: <FF0F>あ~, it's been ages since Ayase saw this many trees~",
        "Ayase: Did you know this smell is called ozone?"
    ],
    13: [
        "Ayase: ..." + P('で') + " Hey, <FF0F>あ~, have you ever seriously thought about the \"future\"?",
        "Ayase: Ayase... " + P('ゅ') + " well, never mind... Forget it, such a heavy topic. Forget it, forget it."
    ],
}
REVIEW = {}

if __name__ == '__main__':
    apply('E0', 117, BOXES, REVIEW)
