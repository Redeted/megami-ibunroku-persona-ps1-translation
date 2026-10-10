"""E1 entry 1 box 0."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: "=Ayase: Ow ow ow ow...<FF02><FF03>Hu" + P('そ') + "h?<FF03>Where are we?<FF02><FF01>",
}

if __name__ == '__main__':
    apply('E1', 1, BOXES, {})
