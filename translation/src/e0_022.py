"""E0 entry 22."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: [
        "Men: M... Meaaat...",
        "Men: I waaant meeeaaaat!"
    ],
    1: ["Yukino: Wh-What's with these guys?"],
    2: [
        "Nurse: Th-The patients who were supposed to be dead suddenly started moving, and the old man who helped me...",
        "Nurse: Nooo!"
    ],
    3: [
        "Mark: Wh-!?",
        "Mark: So these guys are dead? Are you serious!?"
    ],
    4: ["Nanjo: Ya-" + P('セ') + " Yamaoka?"],
    5: ["Nanjo: Yamaoka!" + P('で') + " ..." + P('で') + " ..." + P('で') + " ..." + P('で') + " You bastards!! How dare you!!"],
}

REVIEW = {
    0: "zombie speech (にぐがぎだ = 肉が食いたい/肉がいい) interpreted as 'I waaant meeeaaaat!' - please check"
}

if __name__ == '__main__':
    apply('E0', 22, BOXES, REVIEW)
