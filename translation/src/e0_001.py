"""E0 entry 1 - Agastya Tree (first save point)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Agastya Tree: Young one... It is good that you have come to me."],
    1: "=Agastya Tree:<FF03>Will you engrave<FF03>your record into me?<FF02><FF03><FF0E>\u3000<FF01>",
    2: ["Agastya Tree: Young one... Go forth with the utmost care."],
}

if __name__ == '__main__':
    apply('E0', 1, BOXES)
