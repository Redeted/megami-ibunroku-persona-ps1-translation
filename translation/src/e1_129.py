"""E1 entries 129-147 - Yuriko's confession, the Snow Queen confrontation."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

p = P('ほ')
ps = P('そ')

E129 = {
    1: [
        "Yuriko: ..." + p + " ......" + p + " ........." + p + " ......",
        "Yuriko: You know, Yuriko-chan............ Truly..." + p + " truly..." + p + " the \"Snow Queen\"..." + p + " that kind of person...",
        "Yuriko: I hate her sooo much, you see.",
        "Yuriko: Yuriko-chan... it's all right like this......",
        "Yuriko: I played with everyone... chatted... fought as hard as I could... and then..." + p + " I got beaten...",
        "Yuriko: Yes..." + p + " it's fine like this..." + p + " ...Yuriko-chan is..." + p + " a \"human\"..." + p + " ...\"humans\" \"die\"...",
        "Yuriko: ...Yuriko-chan was stupid...so I didn't understand such an obvious thing..."
    ],
    2: [
        "Nanjo: What is this? Are you... crying" + p + "? Hmph... How transparent! What are you scheming this time?",
        "Nanjo: Did you think such fake crying could make us let our guard down?",
        "Nanjo: Stop making fools of people. And you, a subordinate of the \"Snow Queen,\" of all people, say you \"hate\" her?",
        "Nanjo: If you are going to lie, think of a better lie."
    ],
    3: [
        "Brown: Huh? Crying?",
        "Brown: Yuriko-chan... Even I, who am weak to a beautiful girl's tears, can see through that it's fake crying...",
        "Brown: You're probably plotting something again, but that's no good. You might be able to make others let their guard down,",
        "Brown: but you can't fool these eyes of mine! No, seriously.",
        "Brown: Besides, you, who worship the \"Snow Queen,\" say \"Yuriko-chan hates the Snow Queen\"? Hey hey... Is that a new party joke?",
        "Brown: Let's tell better lies, Yuriko-chan."
    ],
    4: [
        "Ayase: Hey..." + p + " Idiot! This girl is seriously crying! Can't you tell by looking?",
        "Ayase: That's why you never get a girlfriend! You just don't get girls at all!",
        "Ayase: You too, Mayuzumi! Don't say such harsh things, listen to what she has to say!",
        "Ayase: See, Ayase doesn't think this girl is that bad... I can't put it well..." + p + " but..."
    ],
    5: [
        "Yuriko: Than-" + p + " k you... Aya-" + p + " se-san, was it?",
        "Yuriko: While I was alive, Yuriko-chan wanted to be friends" + p + " with you.",
        "Yuriko: ...Yuriko-chan, you know... Truly..." + p + " I was scared.",
        "Yuriko: Chatting... playing a lot... lots of boys and friends who said they \"like\" Yuriko-chan... and kind Papa and Mama...",
        "Yuriko: Every day was so fun and happy... Ah, this must be my \"best time,\" I thought.",
        "Yuriko: And then suddenly... I got scared. If now is the \"best time,\" is the rest of my life just going downhill?",
        "Yuriko: That's right... Yuriko-chan thought: even if I keep living like this, I'll never have more happiness than this, will I?",
        "Yuriko: If I keep living like this, I'd become an adult... get old and ugly... and just die, I thought...",
        "Yuriko: I was so scared... so scared... I couldn't sleep at night.",
        "Yuriko: And then the \"Snow Queen\" mask used in the play... told Yuriko-chan: \"I'll make you stay as you are now forever.\"",
        "Yuriko: Before I knew it... Yuriko-chan was in this tower... forever and ever... alone... in this tower...",
        "Yuriko: Without Papa, without Mama, without friends... alone in this tower...",
        "Yuriko: Yuriko-chan was selfish! Even though I'm human, I asked for the impossible, \"I don't want to die, I don't want to get old\"!",
        "Yuriko: I was stupid! That's why the \"Snow Queen\" tricked me!! Because Yuriko was stupid!",
        "Yuriko: ...I was lonely! I wanted to end it! Yuriko-chan couldn't bear it anymore!!",
        "Yuriko: So when you came... Yuriko..." + p + " was happy! I could end it, no matter how! I didn't want to be alone anymore!",
        "Yuriko: So!" + p + " That's why!!"
    ],
    6: [
        "Nanjo: Hmph..." + p + " I see. So your terrifying fighting power was born of your selfish and willful heart of dependence.",
        "Nanjo: Your unmanageable sorrow and" + p + " regret grew in absolute solitude and time that could be called \"eternal\"... and changed...",
        "Nanjo: and in the end became limitless ferocity beyond your own belief" + p + ", is that it?",
        "Nanjo: That ferocious heart was the trigger for your eccentric words and deeds and for \"Thanatos\" powering up.",
        "Nanjo: What a nuisance! Well... I do not entirely fail" + p + " to understand how you feel."
    ],
    7: [
        "Elly: That abnormally enormous fighting power of yours was born of inexpressible sorrow, was it not...",
        "Elly: Despairing solitude and unmanageable sorrow gave birth to ferocity beyond your own belief.",
        "Elly: That sorrow and ferocity became mixed together, and that heart was the Trigger for your eccentric words and deeds and the Power up of your own Persona, \"Thanatos.\"",
        "Elly: Yuriko-san, you too were a victim of the \"Snow Queen\"..."
    ],
    8: [
        "Yuriko: But Yuriko-chan, thanks to everyone... can finally" + p + " end it, it seems...",
        "Yuriko: Thank you, everyone. Thanks to you, Yuriko-chan can properly, with a \"human's\"" + p + " feelings, die" + p + " it seems.",
        "Yuriko: Yuriko-chan, I-" + p + " I can't s" + p + " stay..." + p + " everyone..." + p + " truly..." + p + " thank you.",
        "Yuriko: Goodbye..."
    ],
    10: ["Obtained 3 \"Ambrosia\""],
    13: [
        "Yukino: Damn \"Snow Queen\"... Toying with people's lives, with their lives, for no reason! I can't forgive it!!",
        "Yukino: Yuriko..." + p + " We'll do it for you too! So rest easy..." + p + " ...and sleep."
    ],
    14: ["The Tower of Thanatos has been conquered!"],
}

E145 = {
    0: ["Yukino: <FF0F>あ! Hold up the mirror!!"],
    1: ["Ayase: N-" + p + " No way..."],
    2: ["Elly: Why...? What is going on?"],
    3: ["Brown: ..." + p + " ..." + p + " ..." + p + " ..." + p + " ? What? It just glowed?"],
    4: [
        "Ayase: That can't be! We all worked so hard to collect them," + ps + " the \"mirror fragments\"! H-Hey, let's hold it up once more!"
    ],
    5: ["Yukino: No way... O-Once more!!"],
    6: [
        "Snow Queen's Voice: Heh heh heh heh... Futile. Even if you thrust such a patchwork mirror at me, you lose."
    ],
    7: ["Nanjo: What did you say!"],
    8: ["Brown: Damn it!"],
    9: [
        "Snow Queen: Heh heh heh heh... Collecting fragments was well and good, but it seems there were not enough.",
        "Snow Queen: Now, come! Taste the nightmare that continues forever," + p + " the despair of the dark night" + p + " along with Saeko!!"
    ],
    10: ["Snow Queen: Gh... aah......"],
    11: ["Yukino: Did we get her!?"],
    12: ["Snow Queen: Gyaaaaaaaaah! My face! It's burning" + p + " aaaaaaah!!"],
    13: [
        "???: Daaamn yoooou... Whyyyyy...",
        "Whyyy" + p + " everyyyone..." + p + " Saeko-saaan" + p + " my bodyyyyy..."
    ],
    14: ["Ayase: Kyaaaaaaaaah!!"],
    15: ["Brown: Dehyaaaah!? Th-th-th-th-" + ps + " th-there it is!!"],
    16: ["Elly: Oh my..."],
    17: [
        "Saeko-sensei: You've all grown strong in a short time. You look like there's nothing you can't do.",
        "Saeko-sensei: I feel that you might do something for us now. Sever the mask's fate that tormented so many students!",
        "Saeko-sensei: I'm counting on you."
    ],
    18: [
        "Yukino: The Queen of the Night, huh... That guy said something like \"I'll make snow of despair fall from the castle's peak.\"",
        "Yukino: There may be a passage the Queen climbed up. Let's search for it!"
    ],
    19: [
        "Yukino: Just a little more... Just a little more and we can take back the school. Pull yourselves together and set out!!"
    ],
    20: [
        "Ayase: Doesn't it feel a little warmer? Maybe the Queen's power has weakened?",
        "Ayase: Oh yeah!! Maybe the doors that were frozen shut are fixed now!?"
    ],
    21: [
        "Ayase: Hey, let's hurry to the upper floor. If our stomachs get cold before we beat the Queen, we can't even fight!"
    ],
    22: [
        "Nanjo: A good deal of time has passed since Inaba and Sonomura went outside.",
        "Nanjo: We must settle this quickly. I am worried about the two."
    ],
    23: [
        "Brown: The Queen of the Night~? Like a Ginza bar madam. Doesn't look very strong.",
        "Brown: She'll be fine without me..." + p + " ..." + p + " Just kidding. Let's go!"
    ],
    24: ["Elly: To sever the mask's fate, we must defeat the Queen of the Night at all costs."],
}

E147 = {
    0: ["Ayase: We did it!!! " + F6('う') + "*" + F6('　')],
    1: ["Yukino: Saeko-sensei!!"],
    2: ["Yukino: Are you okay, Sensei? It must have been cold. Any injuries?"],
    3: ["Saeko-sensei: Thank you, I'm fine. More importantly," + p + " what about Tomomi?"],
    4: ["Brown: Tomomi? Who's that?"],
    5: ["Nanjo: Tomomi...?"],
    6: [
        "Saeko-sensei: Tomomi is..." + p + " the spirit that possessed the mask. One of the students the Snow Queen enchanted.",
        "Saeko-sensei: And also my best friend from my drama club days..." + p
    ],
    7: [
        "Yukino: S-" + p + " So... the Snow Queen who possessed Saeko-sensei was sensei's best friend..."
    ],
}

if __name__ == '__main__':
    for n, d in ((129, E129), (145, E145), (147, E147)):
        apply('E1', n, d, {})
