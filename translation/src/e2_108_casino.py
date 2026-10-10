"""E2 entry 108 - casino: the three party lines that were still Japanese (Maki, Brown, Ayase)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Maki: I've hardly ever been to a place like this before...<FF03>Hmm, it's interesting!"],
    1: ["Brown: I'm pretty confident when it comes to poker, y'know.<FF03>How about you let the great me play?"],
    5: ["Ayase: Ayase likes the slots here~<FF03>They're kinda unusual, you know."],
}
REVIEW = {}

if __name__ == '__main__':
    apply('E2', 108, BOXES, REVIEW)
