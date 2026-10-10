"""E0 entry 52 - SEBEC building elevator."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Maki: Hee... So it became like this. Amazing, I'm kinda excited!"],
    1: [
        "Elly: As expected of a cutting-edge corporation.",
        "Elly: It is quite an elaborate mechanism."
    ],
    2: ["Brown: Whew~ But making something like this, what on earth are they doing?"],
    3: ["Ayase: Ayase was in a place like this!? That's seriously bad!"],
    4: ["Nanjo: Inaba! Are you trying to kill me!?"],
    5: ["Mark: Wahahahaha. My bad, my bad." + P('キ') + " Tch, you're tough as expected..."],
    6: ["Maki: Inaba-kun, <FF07>あ-kun, come down quickly."]
}
REVIEW = {
    3: "マジヤバじゃん translated as That's seriously bad!",
}

if __name__ == '__main__':
    apply('E0', 52, BOXES, REVIEW)
