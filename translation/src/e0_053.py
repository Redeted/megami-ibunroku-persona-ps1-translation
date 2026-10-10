"""E0 entry 53 - SEBEC underground, first floor."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Ayase: Seriou~sly!? There's a guy who looks strong!"],
    1: [
        "Mark: Ayase, be careful!",
        "Mark: Leave this place to us, you stay hidden!"
    ],
    2: ["Maki: It's kinda amazing... Like sci-fi..."],
    3: [
        "Nanjo: <FF0F>あ. If there is a suspicious mechanism up ahead, think carefully before you touch it!",
        "Nanjo: ...Good grief, that Inaba. Just remembering it now makes me angry!"
    ],
    4: ["Mark: Amazing... To think they'd build something like this. They're serious."],
    5: ["Elly: I am sure there are many Demons in the back. Hehehe..." + P('た') + " It is wonderful!"],
    6: ["Ayase: Uu~, it's kinda gross..." + P('な') + " So there's something like that inside Ayase?"],
    7: "=Will you ride the elevator?<FF03><FF0E>　<FF01>"
}
REVIEW = {
    7: "Choice parameter space."
}

if __name__ == '__main__':
    apply('E0', 53, BOXES, REVIEW)
