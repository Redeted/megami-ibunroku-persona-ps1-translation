"""E0 entry 49 - Holding cell: Mark and Brown, then the demon police."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Mark: Who are you, jerk! Locking me up in a place like this... I won't let you off easy!"],
    1: [
        "Brown: S-stop it, Mark! What are you gonna do, making them angry?",
        "Brown: It'd be better to butter them up here..."
    ],
    2: ["Brown: Huh?"],
    3: [
        "Maki: Aaah, found you! Inaba-kun! Were you okay?",
        "Maki: ...Huh? Uesugi-kun's here too!"
    ],
    4: ["Nanjo: Heh." + P('な') + " A cage suits a monkey quite well..."],
    5: ["Mark: You jerk, Nanjo! You're late, damn it! ..." + P('み') + " ..." + P('み') + " ..." + P('ぎ') + " Sonomura?"],
    6: ["Brown: What, it's just you guys..." + P('ゆ') + " I see, did you miss the great me that much, huh?"],
    7: ["Maki: Hey, hey, Uesugi-kun, why are you trying to butter us up?"],
    8: ["Brown: Ugh..."],
    9: [
        "Nanjo: Most likely he mistook us for other people. Well, we are allies, so there is no need to butter us up.",
        "Nanjo: Good for you, Uesugi?",
        "Nanjo: ...More importantly, why are you here?",
        "Nanjo: I thought only Inaba was being held captive..."
    ],
    10: ["Maki: That can wait, later, later! Let's hurry and let them out!"],
    11: [
        "Brown: Even the great me, you know, figured that no matter what, I couldn't beat Demons without a weapon.",
        "Brown: So I came here. And then I got caught along with Mark!"
    ],
    12: [
        "Mark: Shut up, Uesugi! You keep quiet!",
        "Mark: ...Sonomura! Why are you here?",
        "Mark: No, more importantly, you came all the way to a place like this. Is your body all right?!"
    ],
    13: ["Maki: Aw, even you, Inaba-kun, saying things that make no sense..." + P('な') + " I told you, I'm fine!"],
    14: ["Mark: I-I see..." + P('な') + " Then it's fine. Anyway..."],
    15: ["Brown: " + P('な') + "...Who's there?"],
    16: ["Inspector: " + P('な') + " Inabaaa, you mustn't go outside on your own, you know..."],
    17: ["Police Officer: " + P('な') + " It's not allowed, you know..."],
    18: ["Mark: Octopus geezer! Even for a joke, you're going too far, aren't you? I didn't do anything, y'know."],
    19: ["Nanjo: No, something is strange! Inaba..." + P('み') + " These guys are...!"],
    20: ["Police Officer: Inspector, this guy broke out of jail, you know. He's a violent criminal, you know."],
    21: ["Inspector: A violent criminal gets the death penalty, huh..."],
    22: ["Mark: There's a nasty stink..." + P('な') + " Don't tell me...!!"],
    23: ["Demon Officer: Death penalty, death penalty! Death penalty, death penalty, death penalty! Death penaaalty, ehehehehe!"],
    24: ["Demon Inspector: That's right! You guys, get 'em!"],
    25: ["Used the \"Holding Cell Key\"..."],
}
REVIEW = {
    9: "人まちがい: read as Brown mistaking them for other people (Nanjo's guess)",
    12: "split into three pages for the original FF02 mid-page",
    23: "Japanese plays 死刑 (kanji) vs しけい (hiragana) vs しけぇ; English cannot show the script difference",
    24: "ヤローども rendered 'You guys'; rough tone (bastards) is toned by context",
}

if __name__ == '__main__':
    apply('E0', 49, BOXES, REVIEW)
