"""E0 entry 19."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    10: [
        "Mark: Hey, what're you doing?",
        "Mark: Police? You mean that octopus geezer's place?",
        "Mark: Then it's west on Mikage-dori."
    ],
}

if __name__ == '__main__':
    apply('E0', 19, BOXES)
