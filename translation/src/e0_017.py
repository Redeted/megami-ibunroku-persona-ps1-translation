"""E0 entry 17."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Nanjo: Rather than 'antique'... it is simply filthy."],
    1: ["Nanjo: ...Hm?" + P('ぎ') + " Inaba, is he one of your hoodlum friends?"],
    2: [
        "Mark: What'd you say!?" + P('ぎ') + " ...Huh?",
        "Mark: A scar on the forehead... So they meant you... What're you doing here?"
    ],
    3: ["Reiji: Don't you guys come near here..." + P('ぎ') + " Or you'll die..."],
    4: ["Mark: What was that? Hey, hold it right there!"],
    5: ["Yukino: Stumbling around like that... What is he doing?"],
    6: [
        "Mark: You want something with our studio?",
        "Mark: Nobody's supposed to be here today."
    ],
}

if __name__ == '__main__':
    apply('E0', 17, BOXES)
