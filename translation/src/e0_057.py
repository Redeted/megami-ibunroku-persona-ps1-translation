"""E0 entry 57 - Encountering Kandori"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Takeda: Who goes there!? Children again? From where did you intrude!"],
    1: ["Kandori: This is a blunder, Takeda. First that brat earlier, and now this. Since when did our company become a day-care center?"],
    2: [
        "Nanjo: You have not changed, Kandori. Are you not acting a bit too arrogant for a fox borrowing a tiger's authority?",
        "Nanjo: President Saeki is aware of this current incident, I assume?"
    ],
    3: [
        "Kandori: Well, well. If it isn't the young master of the Nanjo Concern. That old man knows nothing.",
        "Kandori: More importantly, this will not do. Your mother will smack you for pulling a stunt like a petty thief.",
        "Kandori: Or perhaps it will be that senile butler of yours?"
    ],
    4: ["Nanjo: Silence! You... You are the only one I will never forgive!"],
    5: ["Mark: Old man, don't act like you've got this all figured out! I'm gonna make you pay!"],
    6: ["Maki: This guy is... Kandori...?"],
    7: ["Elly: This level of rudeness is just as I expected. A Heel must be exactly like this."],
    8: [
        "Brown: He looks surprisingly weak. <FF08>あ, I'll leave the big guy to you!",
        "Brown: A leader's gotta take down the boss, after all!"
    ],
    9: [
        "Ayase: Heey, old man! Could you stop treating us like kids? What's with rolling these balls around!?",
        "Ayase: You reek of old man! You look ancient!"
    ],
    10: [
        "Kandori: ..." + P('ょ') + " Undisciplined brats are no different from wild beasts.",
        "Kandori: Takeda, I do not mind if you kill them. Dispose of them. And try not to dirty the room."
    ],
    11: [F6('い') + "Takeda<FF03>Kandori's confidant.<FF03>A man who handles SEBEC's illegal operations." + F6('　')],
    12: [F6('い') + "Kandori Takahisa<FF03>An ambitious man serving as the SEBEC branch manager.<FF03>Dark rumors constantly surround him." + F6('　')],
    13: ["Mark: Bastard!! Where did he run off to!"],
    14: ["Nanjo: There are no traces of him leaving through the door. There must be another exit somewhere."],
    15: ["Maki: ...So that's Kandori... I've seen him somewhere..."],
    16: ["Elly: Is something wrong, Maki? You look a bit pale."],
    17: ["Brown: Hm? What's the matter, Maki-chan? You look so serious."],
    18: ["Ayase: What's wrong, Sonomura? You look super serious."],
    19: ["Mark: Hm? What's wrong, Sonomura? You look gloomy."],
    20: ["Maki: Eh? Y-Yeah. I'm fine, it's nothing. C-Come on, we have to hurry and chase him!"],
    21: ["Nanjo: There must definitely be another exit. I will keep watch outside. Find it quickly."],
    22: ["Mark: Still, I'm surprised those guys are Persona users, too."],
    23: ["Maki: Really, it's nothing. I just felt a little dizzy. Sorry for making you worry."],
    24: [
        "Elly: Kandori's Persona... A faceless god... A crawling chaos... A bizarre evil god with countless aliases...",
        "Elly: I suppose that makes it a symbol of a wicked heart."
    ],
    25: [
        "Brown: <FF08>あ, I didn't hear anything about them being Persona users too~!",
        "Brown: Isn't this super dangerous!?"
    ],
    26: ["Ayase: <FF0F>あ, get it together~. He got away, didn't he."],
    27: "=There is a switch.<FF03>Will you press it?<FF03><FF0E>　<FF01>",
    28: ["Mark: Bingo! Well done, <FF0F>あ!"],
    29: ["Nanjo: A hidden passage? He truly is a man who loves cheap tricks."],
    30: ["Maki: <FF07>あ-kun! Let's hurry and chase him!"],
    31: ["Brown: <FF08>あ, check if there are any traps."],
    32: ["Elly: <FF07>あ, you aren't injured or anything, right? If you are ready, let us go."],
    33: ["Ayase: We're seriously going? Ugh~, fine!"],
    34: [
        "Maki: He's the one who messed up our town... I will never forgive him!",
        "Maki: Eh...? Aha, it's nothing. Come on, let's go!"
    ],
    35: ["Mark: Alright, let's hurry up and tie the bastard down so we can put an end to this."],
    36: ["Nanjo: No doubt, whatever he cherishes for his cowardly ambitions is waiting up ahead."],
    37: ["There is no longer a need to press the switch."]
}

REVIEW = {
    9: "Ayase calls Kandori ジジクサ～！ フケ顔！ (Reek of old man! You look ancient!)"
}

if __name__ == '__main__':
    apply('E0', 57, BOXES, REVIEW)
