"""E0 entry 162 - the ideal Maki is persuaded to rejoin the party."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: [
        "Maki's Mother: Maki-chan... It's Mother!! Let's go home together!",
        "Maki's Mother: Look, everyone was worried and came all this way for you, you know!?"
    ],
    1: [
        "Maki: Don't come!! Everyone... why did you come!?",
        "Maki: You know what kind of girl I am, don't you?"
    ],
    2: [
        "Mark: Sonomura... It might be impossible to say don't worry about it, but...",
        "Mark: Everybody has feelings of envy for others, right? Me too.",
        "Mark: Besides, you were being used. It's Kandori who's to blame, ain't it?"
    ],
    3: [
        "Maki: How many times did I try to kill you all!? Why are you so kind!?",
        "Maki: Stop pitying me. Being pitied is more miserable... I should just die!"
    ],
    4: ["Mark: That ain't true!"],
    5: ["Nanjo: Spoiled brat..."],
    7: ["Elly: Maki..."],
    8: ["Brown: Maki-chan..."],
    9: ["Ayase: Sonomura..."],
    10: ["Maki: <FF07>あ-kun, you think so too, don't you!?"],
    11: "=You think I'm the worst<FF03>woman, don't you!?<FF03><FF0E>て<FF01>",
    12: [
        "Nanjo: Do not be spoiled!! Reap what you sow yourself!!",
        "Nanjo: If you want to die so badly, why have you not? Do not shout about things you cannot even do!"
    ],
    14: [
        "Nanjo: Pity? Don't make me laugh. Everyone came this far on their own because they can sympathize with you.",
        "Nanjo: Besides, do you think you live alone? Every person is kept alive by the people around them. That is exactly why there is responsibility.",
        "Nanjo: Your careless choice would leave an unfading wound in the hearts of many people.",
        "Nanjo: If you still want to die, do as you please. Forget everything that way. But we will not forget you, who were our companion."
    ],
    15: [
        "Nanjo: Come, let us go back. We will save Sonomura by ourselves. Giving up halfway is not in my nature."
    ],
    16: [
        "Maki: Wait!!" + P('キ') + " I'm sorry, everyone...",
        "Maki: Take me with you too..."
    ],
    17: ["Mark: Heh heh..." + P('キ') + " Of course! Welcome back, Sonomura!"],
    18: ["Reiji: Heh..."],
    19: ["Elly: Welcome back, Maki!"],
    20: ["Brown: Yeah! Welcome back, Maki-chan!"],
    21: ["Ayase: Welcome back! Sonomura!"],
    22: ["Maki: Everyone..." + P('キ') + " I'm home!"],
    23: ["Maki's Mother: Oh... Thank you, everyone... Thank you..."],
    24: [
        "Maki: Mama... I'm sorry... I was a bad girl...",
        "Maki: I remembered everything. I always wanted to see Mama. I was lonely and in pain on my own...",
        "Maki: I forgot Mama was working for my sake, and I resented her... I'm sorry..."
    ],
    25: ["Maki's Mother: It's alright... It's alright now. I'm sorry too, Maki-chan..."],
    26: ["Maki: Thank you, Nanjo-kun, <FF07>あ-kun... Really, thank you..."],
    27: ["Nanjo: ..." + P('キ') + " Sorry. I spoke rather harshly."],
    28: [
        "Mark: Nanjo... Are you embarrassed!? I see!",
        "Mark: You've never been thanked by anyone, being such a twisted guy."
    ],
    29: [
        "Nanjo: S-Shut up, Inaba! Honestly... Now, <FF0F>あ, let us go back!"
    ],
    30: [
        "Nanjo: <FF0F>あ is right. Reap what you sow yourself!!",
        "Nanjo: If you want to die so badly, why have you not? Do not shout about things you cannot even do!"
    ],
    31: [
        "Maki: I've woken up. Even if I'm just a dream, an illusion, a shadow, I'm still me.",
        "Maki: Besides, I have <FF07>あ-kun and everyone. Nothing is more reassuring than that."
    ],
    32: [
        "Mark: Well, I guess Nanjo's hair-splitting is useful once in a while."
    ],
    33: ["Nanjo: Hmph. Being thanked by people is an everyday matter for me."],
    34: ["Reiji: ...We can't stay all warm and fuzzy forever."],
    35: [
        "Elly: I'm glad... But, <FF07>あ, even if I became like that...",
        "Elly: I'm sorry, I said something strange." + P('キ') + " You would definitely save me, wouldn't you, <FF07>あ..."
    ],
    36: [
        "Elly: I am glad... But, <FF07>あ, even if I became like that...",
        "Elly: I am sorry, I said something strange." + P('キ') + " You would definitely save me, would you not, <FF07>あ..."
    ],
    37: ["Brown: *Sniff*... I'm crying along..."],
    38: [
        "Ayase: <FF0F>あ said such harsh things, Ayase wondered what would happen."
    ],
    39: [
        "Ayase: <FF08>あ said such harsh things, Ayase wondered what would happen."
    ],
    40: [
        "Maki's Mother: I do not know how to thank you all...",
        "Maki's Mother: Maki is a lucky girl to be surrounded by such warm friends. Truly, thank you..."
    ],
}
REVIEW = {}

if __name__ == '__main__':
    apply('E0', 162, BOXES, REVIEW)
