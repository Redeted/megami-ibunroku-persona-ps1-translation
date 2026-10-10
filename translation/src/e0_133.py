"""E0 entry 133 - Kandori appears with Aki; Reiji's past."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Maki: Someone's collapsed!"],
    1: ["Mark: K-Kido!!"],
    2: ["Mark: Hey, Kido! Hold on!"],
    3: ["Reiji: ..." + P('セ') + " Ugh... D-Damn..."],
    4: [
        "Kandori: Heh. Youth sometimes brings its own ruin...",
        "Kandori: It is a mistake young men who overestimate their power easily make."
    ],
    5: ["Mark: ..." + P('で') + " You bastard~"],
    6: ["Nanjo: Kandori... It has been a while."],
    7: ["Mark: You've been making fools of us, huh."],
    8: [
        "Maki: Aki! That man isn't your papa! You know that, right!?"
    ],
    9: ["Elly: This is the end of the line, Mr. Kandori."],
    10: ["Brown: You coward! All you ever use is dirty tricks!"],
    11: [
        "Ayase: Old man! Give the compact back!",
        "Ayase: Ayase is borrowing it!"
    ],
    12: ["Aki: Neener! Papa is Papa!"],
    13: ["Kandori: You have quite some nerve, boy."],
    14: ["Maki: Where's the compact? Give it back!"],
    15: ["Aki: Here it is!"],
    16: [
        "Kandori: At last, the two compacts have become one in my hands.",
        "Kandori: I thank you, boy."
    ],
    17: ["Nanjo: You! What do you intend to do with it!?"],
    18: ["Kandori: Show them, Aki."],
    19: ["Aki: Okay, Papa!" + P('ゅ') + " Nomoraka tanomamaa!"],
    20: ["Maki: What is this?" + P('ゅ') + " A mirror!?"],
    21: ["Kandori: This is the form of my ambition..." + P('ゅ') + " Behold its power!"],
    22: ["Reiji: ..." + P('で') + " Kandori" + P('で') + " Takahisa!" + P('で') + " This time... you're not getting away!"],
    23: [
        "Kandori: Do not call your brother's name so casually. Though you are a filthy concubine's child, the same Kandori blood flows in you.",
        "Kandori: Mind how you speak..." + P('ゅ') + " though saying so is useless. A stray dog's pup is a stray dog after all."
    ],
    24: ["Mark: Reiji, you... You're that bastard's brother!?"],
    25: [
        "Reiji: Shut up!!" + P('で') + " I'm Kido! Kido Reiji!!",
        "Reiji: The grudge of my mother, toyed with by your father and thrown away like a rag!!",
        "Reiji: This scar hasn't forgotten it!"
    ],
    26: ["Kandori: Hmph... How trivial. Take it up with our dead father's grave."],
    27: ["Reiji: Kandoriiiiiii!!"],
    28: ["Kandori: What a noisy stray dog... Aki, silence him."],
    29: ["Mark: Reiji!!"],
    30: ["Mark: You bastard~! You've been making fools of us!"],
    31: ["Maki: That's the one from before! Mai-chan's compact!?"],
    32: [
        "Maki: Aki! That man isn't your papa! You know that, right!?",
        "Maki: Give the compact back!!"
    ],
}
REVIEW = {23: "妾の子 = concubine's child", 25: "Reiji's scar and mother"}

if __name__ == '__main__':
    apply('E0', 133, BOXES, REVIEW)
