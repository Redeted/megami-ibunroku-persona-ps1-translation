"""E0 entry 38 - Student Council."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: [
        "Student Council President: If I can just get through this, I will surely leave my name in school history as a great Student Council President...<FF02><FF03>If you want to be of even a little use to the school, why don't you try resolving this incident?"
    ],
    1: [
        "Student Council President: Old records? I sorted those out ages ago. It was a real pain, seriously.<FF02><FF03>What? You want me to show you the records? No, no way! Because it was a real pain!<FF02><FF03>You should go ask someone who looks like they know about the past!"
    ],
    2: [
        "Council Member: We council members are running around for everyone's safety, and yet...",
        "Council Member: The president has just been taking it easy here all by himself...",
        "Council Member: I knew it, we never should have made someone like him president!"
    ]
}

if __name__ == '__main__':
    apply('E0', 38, BOXES)
