"""E0 entry 87 - the Hama Mirror and the subway demon."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Elly: Kandori... So he has come to this town as well."],
    1: ["Ayase: Kandori's here too? I've got a bad feeling about this!"],
    2: [
        "Brown: Kandori, huh...",
        "Brown: Even I, as great as I am, would really like to be spared from that guy."
    ],
    3: ["Reiji: Kandori... So he's come to this world." + P('ぎ') + " That saves me the trouble of searching."],
    4: ["Mark: He said there's a demon in the subway. And what was it..." + P('み') + " Ha..." + P('ぎ') + " Hama-no?"],
    5: [
        "Nanjo: The \"Hama Mirror.\" He said that with it we can cross to the east side.",
        "Nanjo: It seems Kandori was not satisfied with merely taking our town.",
        "Nanjo: I shall teach him that greed is the root of ruin."
    ],
    6: ["Maki: Even if you say that, I don't know. \"Hama Mirror\"..."],
    7: ["Nanjo: Hmm..." + P('み') + " The name seems familiar from somewhere... <FF0F>あ, what do you think?"],
    8: ["Maki: The wall dividing this town in two was only built recently. Before, we could go over there freely."],
    9: ["Nanjo: I cannot recall..." + P('ぎ') + " I am sure I heard the name \"Hama Mirror\" somewhere..."],
    10: ["Mark: \"Hama\" is a pretty old-fashioned name, ain't it?"],
    11: [
        "Brown: There's something that's bugging me.",
        "Brown: He said there's a \"monster\" in the subway, right?",
        "Brown: ..." + P('よ') + " I don't really mind not going to the east side, y'know... Just kidding..."
    ],
    12: [
        "Brown: The subway \"monster,\" huh...",
        "Brown: ..." + P('な') + " I see, so we're really fighting that guy after all..." + P('な') + " ...Boo-hoo-hoo..."
    ],
    13: [
        "Elly: Since ancient times, it has been believed that such a mirror has the power of \"Hama,\" that is, the power to break evil."
    ],
    14: ["Ayase: If the subway monster isn't a gross one, Ayase would be saved, y'know."],
    15: ["Ayase: ..." + P('な') + " We have to fight that monster? Waaah, I don't wanna!"],
    16: ["Reiji: Before you rely on others, why not think for yourself?"],
}
REVIEW = {4: "Mark stumbles on ハマノ (Hama no)", 5: "Hama Mirror name, glossary updated"}

if __name__ == '__main__':
    apply('E0', 87, BOXES, REVIEW)
