"""E0 entry 35 - Corridors."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: [
        "Student: Akuma-kun is saying that the town went crazy because of a curse passed down at Hermelin.",
        "Student: To still be spouting that nonsense at a time like this... In a sense, I respect it."
    ]
}

if __name__ == '__main__':
    apply('E0', 35, BOXES)
