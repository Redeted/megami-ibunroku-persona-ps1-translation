"""E0 entry 93 - after the gate monster; Aki appears."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: [
        "Yog-Sothoth Jr.: Gu, gu, gu... You who have defeated me...",
        "Yog-Sothoth Jr.: Surely my master will be pleased with you. Now, go..."
    ],
    1: [
        "Aki: Oh, so that monster got beaten.",
        "Aki: Losing to people like you, how stupid!"
    ],
    2: ["Maki: Aki... chan! You came to do something again!"],
    3: ["Aki: Past here is Aki's house! If you come in, Aki won't let you out again!"],
    4: [
        "Nanjo: Even so, we are going in.",
        "Nanjo: We must defeat Kandori."
    ],
    5: [
        "Aki: ..." + P('ぎ') + " I won't let you do that, no way!",
        "Aki: If you come into Aki's house, I'll shut you in forever!"
    ],
    6: [
        "Mark: Idiot. Think I'd fall for the same trick twice?",
        "Mark: Now be a good girl, or I'll really punish you, got it?"
    ],
    7: [
        "Aki: Aki's not stupid! As proof, Aki thought up something really fun!",
        "Aki: ...The next opponent is a cuuute girl! Look forward to it!"
    ],
    8: ["Aki: Nomoraka tanomamaa!"],
    9: [
        "Maki: Aki-chan really is a cheeky girl.",
        "Maki: This time I'll catch her and scold her!"
    ],
    10: ["Maki: The cute girl she mentioned was Chisato..."],
    11: [
        "Nanjo: There is something that bothers me.",
        "Nanjo: ...No, I have no evidence. It is surely a mistake on my part."
    ],
    12: ["Nanjo: The demon that was here said \"master.\" Did it mean Aki?"],
    13: ["Mark: Right, let's hurry outside and look for Kandori!"],
    14: [
        "Mark: We're still wandering around in a place like this, huh.",
        "Mark: Hey, can we really save Sonomura like this?"
    ],
    15: ["Elly: I have never seen a Demon like that."],
    16: [
        "Elly: About the Demon that was here...",
        "Elly: It seemed almost as if it were testing our skill."
    ],
    17: ["Brown: Phew! Glad that monster's gone!"],
    18: ["Brown: This is a weird town..."],
    19: ["Ayase: Geez! Ayase is never fighting a guy like that again!"],
    20: ["Ayase: The town suddenly turning weird, demons starting to show up..." + P('ぎ') + " What happened to this town?"],
    21: ["Reiji: You're not taking what that brat says seriously, are you?"],
    22: ["Reiji: There's something I need Kandori to apologize for, no matter what..."],
}
REVIEW = {}

if __name__ == '__main__':
    apply('E0', 93, BOXES, REVIEW)
