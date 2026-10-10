"""E0 entry 33 - Back inside the school."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Saeko-sensei: Are you all safe?!" + P('み') + " Th-" + P('た') + "Thank goodness..." + P('み') + " What happened to that person?!"],
    1: ["Yukino: I'll explain the details later! Hurry, to the infirmary!"],
    2: [
        "Saeko-sensei: You're right! <FF0F>あ, we're going to the infirmary!",
        "Saeko-sensei: Mayuzumi and Kirishima, go to the covered walkway by the gym.",
        "Saeko-sensei: Ayase and Himeno should be blocking up the hole in the wall, so go help them!"
    ],
    3: ["Yukino: We need to make sure demons can't get in, huh! Understood." + P('み') + " Let's go, Eriko!"],
    4: ["Elly: Yes, let's go!"],
    5: ["Saeko-sensei: All right, let's go!"],
    6: ["Saeko-sensei: Ah, <FF0F>あ!"],
    7: ["Student: Ah, <FF0F>あ-kun. Even if you come here, you can't go outside, you know?"],
    8: [
        "Student: Ah, you can't, <FF0F>あ-kun!",
        "Student: We were told by the teachers that we can't go outside right now!"
    ],
    9: [
        "Student: What if demons get in here? I don't even have a weapon...",
        "Student: I wonder if there's anything I can use as a weapon lying around in the archery club or something..."
    ],
    10: ["The door is firmly closed..."]
}

if __name__ == '__main__':
    apply('E0', 33, BOXES)
