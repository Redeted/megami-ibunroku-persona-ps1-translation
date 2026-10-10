"""E0 entry 134 - the town vanishes; Kandori reveals the Mirror of Chaos."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Mark: W-What is that...? Could it be... our town...?"],
    1: [
        "Kandori: Indeed. Your town.",
        "Kandori: That is my new castle... Shall I name it \"Deva Yuga\"?",
        "Kandori: A fitting name to herald the arrival of a shining new age..."
    ],
    2: ["Elly: Oh my God..."],
    3: ["Brown: *Gulp*... The town's vanished..."],
    4: ["Ayase: No way... The people there... did they all die?"],
    5: ["Reiji: Ugh..." + P('で') + " You bastard..."],
    6: ["Nanjo: Kandori, you..."],
    7: ["Maki: ...Horrible."],
    8: [
        "Kandori: Heh heh..." + P('ゅ') + " Hahaha! This \"Mirror of Chaos\" is what I have sought!!",
        "Kandori: Magnificent... Unlike the puny compact, its effect is immense, as you see!",
        "Kandori: Without borrowing the power of the Deva System, I have obtained the power to transcend dimensions and realize my wishes!"
    ],
    9: [
        "Nanjo: I see... I am beginning to understand. The compact and the Deva System were merely stepping stones.",
        "Nanjo: And then..."
    ],
    10: [
        "Kandori: I shall become a god in the living world. The deed of a god is but one:",
        "Kandori: to wield the rod of judgment over foolish humanity!"
    ],
    11: ["Maki: I see, you..." + P('ゅ') + " You intend to kill all humans..."],
    12: ["Mark: Like hell we'll let you!"],
    13: ["Nanjo: We will not allow it!"],
    14: ["Kandori: Futile..."],
    15: ["Maki: Inaba-kun! Nanjo-kun!"],
    16: [
        "Kandori: I shall now return to the living world. Do you hate me? If you hate me, follow me...",
        "Kandori: after defeating this one!"
    ],
    17: ["Nanjo: Ugh..."],
    18: ["Mark: Y..." + P('で') + " You bastard..."],
    19: [
        "Kandori: What you desire is not easily obtained. But the joy of overcoming obstacles to grasp it is supreme...",
        "Kandori: Take it as a divine revelation!"
    ],
    20: ["Maki: Wait!"],
    21: [
        "Demon: Now then, showtime. I'll make you dance...",
        "Demon: a dance of death!!"
    ],
}
REVIEW = {1: "デヴァ・ユガ = Deva Yuga", 8: "混沌の鏡 = Mirror of Chaos"}

if __name__ == '__main__':
    apply('E0', 134, BOXES, REVIEW)
