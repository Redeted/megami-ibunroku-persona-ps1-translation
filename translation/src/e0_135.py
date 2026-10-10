"""E0 entry 135 - the party recovers and resolves to go on to the Haunted House."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Mark: Hey, Kido! You alive!?"],
    1: ["Reiji: Ugh..." + P('で') + " Where's that bastard...?"],
    2: [
        "Mark: You idiot... That's why I said you couldn't do it alone." + P('キ') + " He's gone.",
        "Mark: He went to our world."
    ],
    3: ["Reiji: ..." + P('で') + " What are you doing...? Hurry up and chase him!"],
    4: ["Elly: But how...? We have no way to get back!"],
    5: [
        "Brown: It's impossible! There's no way we can beat a guy with a thing like that!",
        "Brown: Besides, how are we supposed to get back!?"
    ],
    6: [
        "Ayase: How are we supposed to get back!? Call a ride? Even if we got back...",
        "Ayase: There's nothing we can do about that! It's over..."
    ],
    7: [
        "Reiji: ..." + P('で') + " There's got to be some way... That bastard's the type.",
        "Reiji: He's toying with us, enjoying it..."
    ],
    8: ["Nanjo: Kido is right. There is surely a way... Heh, this is the first time we agree."],
    9: ["Reiji: ..." + P('で') + " I suppose."],
    10: ["Maki: ...Maybe that place. The one with rumors of people vanishing since long ago."],
    11: [
        "Mark: The haunted house! We used to sneak in there as kids and got our butts spanked by our moms..."
    ],
    12: ["Nanjo: A place that overlaps with SEBEC in our world... There is a possibility."],
    13: [
        "Elly: It is impossible! There is no proof at all!",
        "Elly: Besides, how can we fight an opponent with such power!?"
    ],
    14: [
        "Brown: It's impossible! No matter how hard we try, it won't work!",
        "Brown: It's always been like that..."
    ],
    15: ["Ayase: It's impossible! Why? Why does Ayase have to go through this!?"],
    16: [
        "Maki: Don't give up! It's everyone's world, everyone's future, isn't it?",
        "Maki: Is it okay? Letting someone else do as they please? Is it okay? To throw it away so easily? I can't stand that!",
        "Maki: I love this town! I love everyone! I love myself!",
        "Maki: I hate watching in silence while things I love are destroyed! That wouldn't be me!"
    ],
    17: [
        "Elly: ..." + P('ヒ') + " You are right. Nothing begins like this. Let us go.",
        "Elly: To protect those who are dear to us!"
    ],
    18: [
        "Brown: ..." + P('ゅ') + " Alright! The leader's back!",
        "Brown: The stronger the villain, the more the hero stands out! Let's go!"
    ],
    19: [
        "Ayase: ..." + P('ゅ') + " Well, fine. Ayase's future is at stake too.",
        "Ayase: Let's go! To the haunted house!"
    ],
    20: [
        "Mark: Things you love, huh... Looks like nobody's complaining.",
        "Mark: <FF0F>あ, let's go to the haunted house!"
    ],
    21: [
        "Mark: Damn! We wasted precious time.",
        "Mark: If we don't catch that bastard fast, something terrible will happen!"
    ],
    22: [
        "Reiji: ..." + P('で') + " There's got to be some way... That bastard's the type.",
        "Reiji: He's toying with us, enjoying it...",
        "Reiji: I won't give up! Not until I kill that bastard with my own hands."
    ],
    23: [
        "Mark: Sonomura... From here on it's our world's problem.",
        "Mark: It's fine now, go home."
    ],
    24: [
        "Maki: No! I can't stand just watching by myself!",
        "Maki: I love this town! I love everyone! I love myself!",
        "Maki: I hate watching in silence while things I love are destroyed! That wouldn't be me!"
    ],
    25: [
        "Nanjo: Heh... \"There is no word for failure in the dictionary of youth.\"",
        "Nanjo: Naive words from a predecessor, but shall we believe them?"
    ],
    26: [
        "Reiji: ..." + P('で') + " Hurry up! I'll look after myself!"
    ],
    27: ["Reiji: ........." + P('キ') + " Damn it! I'm Kido Reiji!"],
    28: ["Maki: To think a thing like that could be made with that compact..."],
    29: [
        "Mark: Kido, we'll come get you, so don't worry."
    ],
    30: ["Mark: You okay, Reiji?"],
    31: ["Reiji: ..." + P('で') + " Worry about yourself, not me."],
    32: [
        "Mark: Tch! That's nothing. I ain't gonna kick the bucket before you."
    ],
    33: ["Reiji: Heh..." + P('で') + " Big talk. Don't forget that line."],
    34: ["Mark: Damn right."],
    35: ["Mark: Hey, <FF0F>あ, Reiji finally started talking like a normal person."],
    36: ["Elly: One must not give in to weakness so easily."],
    37: ["Brown: Can't keep tucking our tails, right?"],
    38: [
        "Ayase: Right? If we leave it, Ayase's future boyfriend would die too, wouldn't he?"
    ],
}
REVIEW = {6: "アッシー = slang for a guy who drives girls around", 25: "青春の辞書に失敗の言葉無し = adapted Napoleon quote"}

if __name__ == '__main__':
    apply('E0', 135, BOXES, REVIEW)
