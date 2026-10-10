"""E0 entry 10 - Delinquents."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Nanjo: Now that I think about it, what about the hospital? Weren't we going there to get examined?"],
    1: ["Mark: <FF0F>あ, this guy keeps saying boring stuff. You listen to him."],
    2: ["Yukino: Inaba is picking fights with the other kids, how pathetic. I wonder what's bothering him..."],
    3: ["Student: Don't you think they should just tear down buildings they don't use? That kind of place is just for delinquents to..."],
    4: ["Mark: Keheh! Delinquents are so lame~!"],
    5: ["Student: Shut up! Like I was saying, it'll become a hangout for delinquents, right? I really hate that."]
}

if __name__ == '__main__':
    apply('E0', 10, BOXES)
