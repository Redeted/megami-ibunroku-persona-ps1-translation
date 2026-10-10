"""E0 entry 21."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Yukino: I wonder if Sonomura is okay..."],
    1: ["Mark: ..." + P('ょ') + " Dammit!"],
    2: ["Yukino: W-What!? An earthquake!?"],
    3: ["Mark: Wh-? It's a big one!"],
    4: ["Nanjo: ...It appears to have settled down."],
    5: [
        "Mark: Sonomura!",
        "Mark: Wh-What is this!? Th-The room is gone!?"
    ],
    6: [
        "Nanjo: Wha-!?",
        "Nanjo: What is the meaning of this! I am certain the Intensive Care Unit was there."
    ],
    7: ["Woman's Voice: Kyaa!!"],
    8: [
        "Yukino: A scream? From the floor below!",
        "Yukino: <FF0F>あ, let's go check it out!"
    ],
}

if __name__ == '__main__':
    apply('E0', 21, BOXES)
