"""E1 entry 160 (rest) - the Sealing Gear trades with each party member."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

p = P('ほ')

E160 = {
    13: ["Yukino: Are those guys following us around?"],
    14: ["Yukino: I'll gladly take it."],
    15: ["Yukino: I already got mine."],
    16: [
        "Yukino: The number of Ambrosia is limited, so we have to choose carefully who gets a Sealing Gear."
    ],
    17: "=Yukino: Is it okay to<FF03>give it to me?<FF03><FF0E>　<FF01>",
    18: ["Yukino: You're the leader. I'll follow your judgment."],
    19: "=Are you sure?<FF03><FF0E>　<FF01>",
    20: ["Hee-Ho-kun: Hee-Ho!! It's a trade for \"Buffalo Beads\"!"],
    21: ["Obtained \"Buffalo Beads\""],
    22: ["Yukino: Thanks, I got it."],
    23: ["Ayase: She's totally under his thumb."],
    24: ["Ayase: Ayase got hers."],
    25: ["Ayase: Why is it a stuffed animal~? The worst!!"],
    26: ["Ayase: Sealing Gears are valuable, right?"],
    27: "=Ayase: Is it okay to take it?<FF03><FF0E>　<FF01>",
    28: ["Ayase: Tch!!"],
    29: "=So happy~ Seriously?<FF03><FF0E>　<FF01>",
    30: ["Hee-Ho-kun: Hee-Ho!! It's a trade for a \"Deer Mount\"!"],
    31: ["Obtained a \"Deer Mount\""],
    32: [
        "Ayase: Hey~ Why's it a stuffed animal~! I don't want something like this~!!"
    ],
    33: ["Nanjo: He has it rough too."],
    34: ["Nanjo: Yamaoka..."],
    36: ["Nanjo: I trust you realize that Ambrosia is a valuable item."],
    37: "=Nanjo: It's fine to trade<FF03>mine?<FF03><FF0E>　<FF01>",
    38: ["Nanjo: I shall leave the decision to you."],
    39: "=Then I will accept.<FF03><FF0E>　<FF01>",
    40: ["Hee-Ho-kun: Hee-Ho!! It's a trade for \"Tortoiseshell Glasses\"!"],
    41: ["Obtained \"Tortoiseshell Glasses\""],
    42: [
        "Nanjo: Th-" + p + " This is... Yamaoka's glasses!?",
        "Nanjo: Why... why are they in a place like this... Is it to protect me?",
        "Nanjo: Yamaoka..."
    ],
    43: ["Elly: Those Demons do not seem to be enemies."],
    44: ["Elly: I shall accept the Sealing Gear."],
    45: ["Elly: Thank you!"],
    46: [
        "Elly: Sealing Gears are valuable. I think it would be best to choose carefully who takes one."
    ],
    47: "=Elly: Am I all right?<FF03><FF0E>　<FF01>",
    48: ["Elly: Please think carefully."],
    49: "=Are you truly sure?<FF03><FF0E>　<FF01>",
    50: ["Hee-Ho-kun: Hee-Ho!! It's a trade for the \"Judgment Contract\"!"],
    51: ["Obtained the \"Judgment Contract\""],
    53: ["Brown: I sense a man's sorrow~"],
    54: ["Brown: Yeah~! Profit, profit!"],
    56: [
        "Brown: I'm the leader, so naturally I have the right to take one, you see."
    ],
    57: "=Brown: I'll take the one<FF03>for me<FF03><FF0E>　<FF01>",
    58: ["Brown: If you're changing your mind, now's the time."],
    59: "=Well, that's that then.<FF03><FF0E>　<FF01>",
}

if __name__ == '__main__':
    apply('E1', 160, E160, {})
