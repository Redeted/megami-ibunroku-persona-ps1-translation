"""E0 entry 54 - SEBEC underground, second floor (Ayase awakens)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Ayase: Seriou~sly!?" + P('た') + " What was that just now~!" + P('た') + " Did Ayase beat them up?!"],
    1: ["Mark: So Ayase too..." + P('な') + " Just what in the world is going on?"],
    2: ["Nanjo: Hmph..."],
    3: ["Ayase: What? Ayase doesn't understand this at all!"],
    4: [
        "Nanjo: Then, I shall explain it to you.",
        "Nanjo: That said, what we know is fairly limited."
    ],
    5: ["Ayase: Hee..." + P('た') + " So, what are you telling Ayase to do with this power?"],
    6: ["Mark: Who knows."],
    7: ["Maki: For now, nothing will start even if we stay still here." + P('た') + " Let's go, let's go!"],
    8: ["Maki: Yuka as well. I kinda feel something fateful!"],
    9: ["Maki: It's kinda amazing... Like sci-fi..."],
    10: ["Nanjo: Is that \"Persona-sama game\" the cause..."],
    11: [
        "Nanjo: <FF0F>あ. If there is a suspicious mechanism up ahead, think carefully before you touch it!",
        "Nanjo: ...Good grief, that Inaba. Just remembering it now makes me angry!"
    ],
    12: ["Mark: Kinda feels like I'm being manipulated by someone. It's a bad feeling, man!"],
    13: ["Mark: Amazing... To think they'd build something like this. They're serious."],
    14: ["Ayase: I don't really get it. So many things happened so suddenly."],
    15: ["Ayase: Uu~, it's kinda gross..." + P('な') + " So there's something like that inside Ayase?"],
    16: [
        "Brown: Kuuh, it's great. This sense of tension!",
        "Brown: Look forward to the great me's exploits!"
    ],
    17: ["Elly: I am sure there are many Demons in the back. Hehehe..." + P('た') + " It is wonderful!"],
    18: ["Elly: We must hurry and chase Mr. Kandori!"],
    19: "=Will you ride the elevator?<FF03><FF0E>　<FF01>"
}
REVIEW = {
    10: "Persona-sama game",
    16: "Kuuh, it's great... - Kuuh as an excited grunt",
}

if __name__ == '__main__':
    apply('E0', 54, BOXES, REVIEW)
