"""E0 entry 11."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Yamaoka: Young master!"],
    1: [F6('い') + "Yamaoka<FF03>Nanjo family butler. Has looked after Nanjo since he was a child."],
    2: ["Nanjo: Y-" + P('み') + "Yamaoka..."],
    3: [
        "Yamaoka: Oh, my! " + P('み') + "To think young master Kei would come home from school with friends!",
        "Yamaoka: I-" + P('み') + "I am so happy~!"
    ],
    4: ["Mark: Young master" + P('た') + " Kei~?"],
    5: [
        "Nanjo: Y-Yamaoka! Haven't I told you time and time again to stop calling me that!?",
        "Nanjo: I am..."
    ],
    6: ["Mark: What's this \"I am\" stuff~?"],
    7: ["Nanjo: Ah, no..." + P('た') + " Shut up, Inaba!"],
    8: ["Nanjo: Yamaoka, anyway, that's enough for today! Go home ahead of me!"],
    9: ["Yamaoka: Oh, my! Are you going out with everyone, young master!"],
    10: ["Nanjo: I'm just going to the hospital! I said stop with the \"young master\"!"],
    11: ["Yamaoka: What! The hospital! Are you injured, young master!"],
    12: ["Yukino: Pfft..." + P('ぎ') + " Ahahahaha!"],
    13: ["Nanjo: I give up! Let's go, <FF0F>あ! Yamaoka, absolutely do not follow us!"],
    14: ["Nanjo: Yamaoka..." + P('ぎ') + " isn't here, right...?"]
}

REVIEW = {
    5: "Nanjo slips into 'boku', Mark pokes fun at it. Kept as 'I am...'",
    6: "Mark poking fun at 'boku'. Translated as 'I am'."
}

if __name__ == '__main__':
    apply('E0', 11, BOXES, REVIEW)
