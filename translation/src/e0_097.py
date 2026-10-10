"""E0 entry 97 - the Queen's paintings in the market; Chisato's painting."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Maki: It's a beautiful painting. But I don't really..."],
    1: ["Maki: ..." + P('る') + " Chisato..."],
    2: ["Maki: I wonder if this was for the best." + P('み') + " Hey, what do you think, <FF07>あ-kun...?"],
    3: [
        "Nanjo: I do not know much about paintings, but...",
        "Nanjo: Unlike Sonomura's paintings, this one has nothing that resonates in the heart."
    ],
    4: ["Nanjo: So it was Kozai... But how did she become ruler of this market?"],
    5: [
        "Nanjo: Fawning over Kozai while she is here, then saying whatever they like once she is gone...",
        "Nanjo: How quickly they change sides."
    ],
    6: [
        "Mark: This painting looks good at a glance, right? But that ain't enough.",
        "Mark: It ain't technique, it's heart. Corny, but that's what painting is about!",
        "Mark: This painting's all surface. The heart of whoever painted it ain't in it at all!"
    ],
    7: ["Mark: Kozai, why the hell are you helping out Aki? And leaving Naito behind..."],
    8: ["Mark: Maybe Sonomura ain't as down as we're worried she is. I hope that's the case."],
    9: ["Elly: I prefer Maki's paintings!"],
    10: [
        "Elly: A harem means a place where handsome men are gathered, does it not?",
        "Elly: But Kozai-san was supposed to have a boyfriend."
    ],
    11: ["Elly: Don't you think one can never tell what people are saying behind one's back?"],
    12: ["Brown: Paintings are boring~" + P('み') + " ...Yeah, seriously, it's a boring painting."],
    13: ["Brown: Did Kozai always have that many moles?"],
    14: [
        "Brown: That Kozai from before was kinda cute, maybe...",
        "Brown: Just kidding! Lies, lies! Of all people, Naito, though!"
    ],
    15: ["Ayase: Is that boy also a member of the Queen's harem~? No way, that's so unfair!"],
    16: [
        "Ayase: I bet Kozai had it rough too.",
        "Ayase: Try to understand that part, okay?"
    ],
    17: [
        "Ayase: Ayase wants that mirror too, but I wouldn't want any more freckles."
    ],
    18: [
        "Reiji: Whoever makes a stupid room like this must be a pretty childish person."
    ],
    19: [
        "Reiji: Isn't it weird to believe in something like friendship? That stuff's just for show."
    ],
    20: [
        "Reiji: Anyway, it's settled, isn't it? No need to stay long..."
    ],
    21: [
        "Young Man: This is a painting by Lady Queen. Awesome, isn't it?",
        "Young Man: Lady Queen has talent in painting, and she's beautiful, too!",
        "Young Man: She has lots of moles, and they're so pretty!",
        "Young Man: She once showed me a painting by an acquaintance of hers, and that one was awful!"
    ],
    22: [
        "Young Man: Who'd show people a stupid painting like this!",
        "Young Man: What's so great about a Queen!"
    ],
    23: ["There is a painting said to be drawn by the Queen." + P('な') + " ...The style looks familiar from somewhere."],
    24: ["Maki: ..." + P('み') + " This painting...!" + P('ぎ') + " This is a painting Chisato drew...!"],
    25: [
        "Mark: Chisato..." + P('な') + " Chisato Kozai? I heard she went missing!",
        "Mark: Kozai's painting is here, and they say it's the Queen's painting...?"
    ],
    26: ["Maki: Why?" + P('ぎ') + " Does that mean Chisato is being held captive" + P('み') + " by the Harem Queen...?"],
}
REVIEW = {}

if __name__ == '__main__':
    apply('E0', 97, BOXES, REVIEW)
