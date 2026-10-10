"""E0 entry 14."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Reiji: You really ain't gonna let me through? " + P('オ') + "You bastards... are gonna die."],
    1: [
        "Man in Black: Don't make me repeat myself.",
        "Man in Black: Beyond this point is under SEBEC's control.",
        "Man in Black: If you do not follow instructions, we will shoot to kill."
    ],
    2: ["Mark: That idiot! He's gonna get killed!"],
    3: [
        "Mark: Hehehe, sorry 'bout this! This guy's a little crazy in the head.",
        "Mark: C'mon, let's go, you blockhead!"
    ],
    4: ["Reiji: Tch... You guys again."],
    5: ["Nanjo: Ho... Even you help people. No, truly a bolt from the blue."],
    6: ["Mark: Dumbass. Even with a guy like that, he's probably got a mom who'd be sad if he died."],
    7: ["Man in Black: You cannot pass beyond this point. The road is closed."],
    8: ["Man in Black: This is no place for children. Hurry up and evacuate somewhere."],
    9: ["Mark: Geez, that bastard... What is he doing?"],
    10: ["Nanjo: SEBEC... Kandori, what are you scheming?"],
    11: ["Yukino: I don't like this... So they aren't just an ordinary company."],
    12: [
        "Elly: What does this mean? I heard SEBEC was a top-tier company...",
        "Elly: They are no different from the Mafia."
    ],
    13: ["Elly: Oh? Isn't that the transfer student?"],
    14: ["Mark: Huh? Oh, it's Kido. What's he doing?"],
    15: [F6('い') + "Kido Reiji<FF03>Transferred here half a year ago.<FF03>Quiet and always acts alone." + F6('　')],
    16: [
        "Man in Black: Who are you people?",
        "Man in Black: Beyond this point is under SEBEC's control. Entry is forbidden."
    ],
    17: ["Mark: Hey, SEBEC... that's Sonomura's mom's company, right? What's going on here?"]
}

REVIEW = {}

if __name__ == '__main__':
    apply('E0', 14, BOXES, REVIEW)
