"""E0 entry 160 - arrival in Child Maki's forest with Maki's mother; party chatter."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Maki's Mother: You all!? Are you alright!?"],
    1: [
        "Mark: Ow ow ow! That hurts~",
        "Mark: Huh?" + P('キ') + " I see... This compact brought us here."
    ],
    2: ["Nanjo: Ugh...!? Where are we!?"],
    3: [
        "Reiji: Looks like it worked..." + P('キ') + " This is... the forest where that white brat, the child Sonomura, was."
    ],
    4: ["Elly: Bingo!! This is Child Maki's forest!"],
    5: ["Brown: Hey, we did it!! This is that little Maki-chan's forest, right!?"],
    6: ["Ayase: Super lucky!! This is Little Sonomura's forest, right!?"],
    7: [
        "Maki's Mother: Why have you come back!? What happened to Kandori!?"
    ],
    8: ["Mark: Why are you here, ma'am!?"],
    9: [
        "Maki's Mother: I don't really know... After sending you off, I felt like I heard Maki's voice again.",
        "Maki's Mother: When I came to, I was here... Why did you come back?"
    ],
    10: ["Nanjo: Allow me to explain. In fact..."],
    11: [
        "Maki's Mother: ........." + P('キ') + " Surely not... Such a thing...",
        "Maki's Mother: Then Maki!? What will happen to Maki!?"
    ],
    12: [
        "Nanjo: If left alone, at best she will stay as she is for life, or worse..."
    ],
    13: [
        "Maki's Mother: No... Is there nothing that can be done!? This is too cruel!"
    ],
    14: [
        "Mark: Calm down, ma'am!! That's exactly why we came back!"
    ],
    15: ["Reiji: ..." + P('で') + " We won't let it end like this, so don't worry."],
    16: ["Elly: Don't worry. We will surely do something!"],
    17: [
        "Brown: It'll be fine! Trust us! Ride a mud boat and relax!"
    ],
    18: ["Nanjo: Big ship!"],
    19: ["Brown: Right, big ship, big ship! Totally okay! Dahahaha!!"],
    20: [
        "Mark: Nanjo... That's how he really is.",
        "Mark: And he said he'd made up a self..."
    ],
    21: [
        "Nanjo: Hm... This level of stupidity is natural talent.",
        "Nanjo: He does not look like someone who would be crushed by a mere bowel accident."
    ],
    22: ["Brown: Dahahaha!"],
    23: [
        "Ayase: Don't worry, Sonomura's mom! Ayase may not look it, but I'm reliable!"
    ],
    24: ["Maki's Mother: ...Thank you, everyone..."],
    25: ["Mai's Voice: Hu... *Sniff*..."],
    26: ["Maki's Mother: That was Maki's voice!? She's further in!"],
    27: [
        "Mark: Let's go!! Little Sonomura might know something!"
    ],
    28: [
        "Maki's Mother: Wait! Please take me with you! I am Maki's mother!",
        "Maki's Mother: I cannot leave my daughter alone when she is suffering!"
    ],
    29: [
        "Nanjo: ..." + P('キ') + " Very well. But this forest is dangerous. I cannot guarantee your life."
    ],
    30: ["Maki's Mother: I don't mind!"],
    31: [
        "Nanjo: There you have it. Let us go, <FF0F>あ. Let us let a mother meet her child."
    ],
    32: [
        "Mark: Heh heh... She's a good mom, ain't she? And pretty.",
        "Mark: My mom's... " + P('キ') + " just loud, but I hope she's alive!",
        "Mark: She ain't the type to go easy, though..."
    ],
    33: ["Mark: Come on, we gotta hurry or it's bad!"],
    34: [
        "Nanjo: A woman like her is what one calls a true mother... I do not even know my mother's birthday.",
        "Nanjo: Even at home, other than Yamaoka, everyone was practically a stranger. All I was given was money and things.",
        "Nanjo: <FF0F>あ, we will definitely let her meet Sonomura, even at the cost of our lives."
    ],
    35: [
        "Nanjo: Still, this incident gives me much to think about.",
        "Nanjo: I never even considered the existence of multiple selves... but I cannot help but admit it."
    ],
    36: [
        "Reiji: ..." + P('キ') + " That's what mothers are like... Kids just don't notice."
    ],
    37: ["Reiji: How long are you going to stay here? Aren't we going to the shrine?"],
    38: ["Elly: <FF07>あ..." + P('キ') + " Do I sound strange when I talk?"],
    39: "=Was it better before?<FF03><FF0E>ほ<FF01>",
    40: ["Elly: I see... Then I will speak politely."],
    41: [
        "Elly: Good! I was worried what if it seemed strange to you!",
        "Elly: <FF07>あ... Thanks..."
    ],
    42: ["Elly: Hurry up! We have to get to the shrine quickly!"],
    43: ["Elly: Hurry up! Let us hurry to the shrine!"],
    44: [
        "Brown: <FF08>あ! Don't think I'm the same as before! Big mistake!",
        "Brown: The me who's grown a size bigger is now Brown Mark 2!",
        "Brown: What? \"Lame\"? Then what should I do..."
    ],
    45: [
        "Brown: Next is the shrine, right? \"If you are in a hurry, go around!\"",
        "Brown: What? \"That's not what it means\"? Who cares, it's Great-me language!"
    ],
    46: [
        "Ayase: Hmm~ <FF0F>あ, you're actually a good guy when you look closely!",
        "Ayase: Shall I register you as a husband candidate?"
    ],
    47: "=Register?<FF03><FF0E>ま<FF01>",
    48: [
        "Ayase: Beep! Registered! From now on, work like a horse for Ayase!"
    ],
    49: [
        "Ayase: What!! Ayase isn't good enough for you!? Fine! Whatever!!",
        "Ayase: I'll work you even harder!!"
    ],
    50: [
        "Ayase: We're going to the shrine, right? With all this walking, maybe I lost a little weight?"
    ],
    51: [
        "Maki's Mother: I'm such a bad mother. When she's suffering, I can never do anything for her..."
    ],
    52: ["Maki: Next is the real me, huh. I wonder how many of me there are."],
    53: ["Elly: Child Maki... She is all alone in such a lonely place..."],
    54: ["Elly: Child Maki... She is all alone in such a lonely place, is she not..."],
    55: [
        "Ayase: <FF0F>あ, Little Sonomura is all alone in a place like this, right?",
        "Ayase: Ayase couldn't stand it."
    ],
    56: [
        "Ayase: <FF08>あ, Little Sonomura is all alone in a place like this, right?",
        "Ayase: Ayase couldn't stand it."
    ],
    57: [
        "The \"Broken Compact\" with the \"Mirror Shard\" set in it has become the \"Red Compact\"."
    ],
}
REVIEW = {44: "ブラウン・マーク２ pun; おれ様語 = Great-me language", 45: "急がば回れ literal"}

if __name__ == '__main__':
    apply('E0', 160, BOXES, REVIEW)
