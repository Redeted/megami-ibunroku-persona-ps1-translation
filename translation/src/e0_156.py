"""E0 entry 156 - Trish price prompt (4000 yen)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    4: "=It'll cost 4000 yen, okay?<FF03><FF0E>　<FF01>",
}
REVIEW = {}

if __name__ == '__main__':
    apply('E0', 156, BOXES, REVIEW)
