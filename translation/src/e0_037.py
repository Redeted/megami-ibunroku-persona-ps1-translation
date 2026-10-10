"""E0 entry 37 - Drama Club President and student."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: [
        "President: We're well past the point of worrying about the culture festival, aren't we?"
    ],
    1: [
        "President: When I say I don't know any play called the \"Snow Queen\", I mean I don't know it! You're so persistent!"
    ],
    2: [
        "Student: The President is the only one who knows about that play.",
        "Student: Huh? What play am I talking about? That's a secret."
    ],
    3: [
        "Student: This is a real problem, isn't it? What in the world is that thing?"
    ],
    4: [
        "Student: The \"Snow Queen\" role? Hmm, I don't know.",
        "Student: If there were some old records left, we might be able to find out by looking at them, but...<FF02><FF03>Even if I ask the President, she just gets mad..."
    ]
}

if __name__ == '__main__':
    apply('E0', 37, BOXES)
