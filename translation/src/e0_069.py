"""E0 entry 69 - after Aki flees; Yosuke asks them to come to the library."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: [
        "Aki: Aaah!! Damn it~! I'm telling Papa! Papa is strong!",
        "Aki: You guys are nothing, he'll beat you in one hit!!"
    ],
    1: ["Maki: Wait! ...Geez! She got away again."],
    2: ["Nanjo: ...Who on earth is that child...?"],
    3: ["Yosuke: Is everyone safe?!"],
    4: ["Maki: Yosuke-kun! Are you okay?!"],
    5: ["Yosuke: Yeah. Thanks to you guys, the school is back to normal.", "Yosuke: Thank you."],
    6: ["Elly: You are welcome."],
    7: ["Brown: Dahahaha! I only did what's natural! No thanks needed!"],
    8: [
        "Ayase: Geez, no matter how many lives I had, they wouldn't be enough.",
        "Ayase: Not that it does any good telling you."
    ],
    9: [
        "Yosuke: I'm really grateful. By the way... there's someone I'd like you to meet.",
        "Yosuke: Would you come with me?"
    ],
    10: ["Nanjo: Why?"],
    11: [
        "Yosuke: It's someone who's been looking after me since I came here. He believed what I said.",
        "Yosuke: He's been looking into the two worlds and all sorts of things. He might have found something by now."
    ],
    12: ["Mark: Hoh~ He actually took you seriously, huh? What kind of guy is he?"],
    13: ["Yosuke: Well, that's... You'll know when you meet him. Okay, I'll wait in the library!"],
    14: ["Elly: What is the matter with him? Well, anyway, let us go to the library."],
    15: ["Brown: H-Hey! Aww, he's already gone. Is that guy really hurt?"],
    16: ["Ayase: We're going somewhere again?! Let's rest a bit~!"],
    17: ["Mark: Then how about staying behind alone, Ayase?"],
    18: [
        "Ayase: ..." + P('で') + " Fine, I get it!",
        "Ayase: You idiot, Inaba! Masao monkey! Monkey monkey monkey!"
    ],
    19: [
        "Mark: Ah! You bastard! You just said monkey, didn't you? You said Masao, didn't you?",
        "Mark: Don't call me by that lame name!"
    ],
    20: ["Maki: Stop it, you two! Come on, <FF07>あ-kun, let's hurry to the library."],
    21: ["Mark: Don't mind it."],
    22: [
        "Mark: H-Hey... He went hopping off on one leg.",
        "Mark: Wanna go check? Hey, Reiji."
    ],
    23: ["Reiji: ..."],
    24: ["Mark: Man~! You really are no fun, huh? Lighten up and be happy a little."],
    25: ["Reiji: ..." + P('で') + " Don't mess with me..."],
    26: ["Mark: Well, whatever. Let's go then, <FF0F>あ."],
    27: ["Maki: Is he the one Yosuke-kun mentioned? If so, he's definitely in the library."],
    28: [
        "Nanjo: ..." + P('で') + " That girl calls Kandori her father. Is she truly his own child?",
        "Nanjo: This is the first I have heard of him having a child."
    ],
    29: ["Mark: That brat from before really pisses me off! Next time I see her, she's in for it!"],
    30: [
        "Mark: Geez, Ayase's got a foul mouth.",
        "Mark: Some guys are into that kind of thing, though. The world's a mystery."
    ],
    31: [
        "Mark: That Reiji guy's pretty twisted.",
        "Mark: Hey, let's you and me do something about him."
    ],
    32: ["Elly: " + P('で') + " Naito-kun has also lost someone dear to him, right? That must be painful..."],
    33: [
        "Brown: Kids are surprisingly cruel, y'know? They don't know how to hold back.",
        "Brown: What if somebody dies, I'm sayin'." + P('キ') + " Ah, she was out to kill from the start, so that's fine? Wahaha!",
        "Brown: Ooh, scary..."
    ],
    34: ["Ayase: I wanna go home~! Right now I should be getting into the groove at the club, for real~!"],
    35: ["Reiji: ..." + P('で') + " I told you not to mess with me."],
    36: [
        "Maki: Come to think of it... where did everyone in this world go?",
        "Maki: <FF07>あ-kun and Inaba-kun, everyone was here."
    ],
    37: ["Mark: As far as I can see, nothing's changed, but they say it's another world, huh."],
    38: ["Elly: ..." + P('で') + " Oh, I am sorry. I was lost in thought."],
}
REVIEW = {18: "Masao = Mark's real name 正男"}

if __name__ == '__main__':
    apply('E0', 69, BOXES, REVIEW)
