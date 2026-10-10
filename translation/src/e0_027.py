"""E0 entry 27 - Shrine butterfly."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Elly: This is the place. Maki's mother is... My, what a beautiful butterfly."],
    1: ["Yukino: Hey... Isn't there something strange about this butterfly?"],
    2: ["Mark: W-What's with this guy!?"]
}

if __name__ == '__main__':
    apply('E0', 27, BOXES)
