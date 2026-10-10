"""E0 entry 24 - Hospital escape."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Yukino: <FF0F>あ! This person is still alive! Lend me a hand!"],
    1: ["Nanjo: <FF0F>あ! That nurse cannot be saved! If we dawdle, we will share her fate!"],
    2: ["Mark: Hey, <FF0F>あ! The monsters have made it this far!"],
    3: ["Nurse: I... I'm a goner... You kids... h-hurry up and run..."],
    4: ["Yukino: Don't give up!"],
    5: "=<FF0F>あ, hurry and lend me a hand!<FF03><FF0E>く",
    6: ["Yukino: Then grab that side!"],
    7: ["Mark: It's no good! They're coming!"],
    8: ["Elly: Oh, good day. My! Are there Demons here too?"],
    9: ["Yukino: Are you serious!? This person is still alive! Are you telling us to abandon her!?"],
    10: ["Nanjo: ...I did not want to leave Yamaoka behind, either!"],
    11: "=It is an unavoidable choice!<FF03>Let us go!<FF0E>け",
    12: ["Nanjo: Mayuzumi! Inaba! Let us go!"],
    13: ["Nanjo: Good grief... If you end up getting yourselves killed, I will not be held responsible."],
    14: ["Mark: What're we gonna do? Hurry up and decide!"],
    15: ["Yukino: We can't just abandon her! Lend me a hand!"],
    16: ["A demon's roar can be heard from down the hall!"]
}

if __name__ == '__main__':
    apply('E0', 24, BOXES)
