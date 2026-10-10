"""E0 entry 40 - Mask box."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: "=There is a box sealed<FF03>with a talisman.<FF02><FF04>Will you open the box?<FF03><FF0E>こ<FF01>",
    1: ["Obtained \"Snow Queen Mask\"!"],
    2: ["There's nothing inside..."],
    3: ["There seems to be nothing here..."],
    4: ["Before you knew it, the door to the stage stopped opening..."]
}

if __name__ == '__main__':
    apply('E0', 40, BOXES)
