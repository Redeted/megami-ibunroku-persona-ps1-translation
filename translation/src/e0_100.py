"""E0 entry 100 - the Queen turns the party to stone; the final choice; Naito and Kozai."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: [
        "Queen: Aaargh, damn it, more moles again!",
        "Queen: This mirror is handy, but getting this many moles from one wish is a scam!"
    ],
    1: ["Mark: Kozai!"],
    2: ["Queen: ..." + P('み') + " You came! So, my painting was better, wasn't it?!"],
    3: [
        "Maki: Chisato..." + P('ぎ') + " Stop it already...",
        "Maki: I understand that Chisato is better at painting," + P('ぎ') + " and besides, those moles..."
    ],
    4: [
        "Queen: Shut up! Don't say things you don't mean!",
        "Queen: You're probably thinking it serves me right!"
    ],
    5: ["Queen: More importantly, <FF0F>あ-kun, there's something I want to show you."],
    6: ["Maki: That's" + P('ょ') + " my painting...!"],
    7: [
        "Queen: Hey, <FF0F>あ-kun, you looked at the painting displayed in the exhibition room, didn't you?",
        "Queen: Which do you think is better, my painting or this damn Maki's painting?"
    ],
    8: ["Mark: Sonomura's painting is better, obviously!!"],
    9: ["Queen: I'm not asking a monkey like you!"],
    10: [
        "Queen: Mirror, mirror, hear Chisato's wish.",
        "Queen: Turn those monkeys" + P('み') + " into stone! Nomoraka tanomamaa!"
    ],
    11: ["Mark: Whoa!"],
    12: ["Nanjo: Ugh!"],
    13: ["Elly: Eek!"],
    14: ["Brown: Aaah!"],
    15: ["Ayase: Noo!"],
    16: ["Reiji: ......!"],
    17: ["Maki: Chisato, stop!"],
    18: ["Queen: Ahahahaha!! Stay like that and turn to stone!" + P('ぶ') + " ...Ah!"],
    19: [
        "Queen: Damn it! More moles have appeared!",
        "Queen: Stone was too lenient! I should've done something worse to them!"
    ],
    20: [
        "Queen: <FF0F>あ-kun, I'll give only you a chance.",
        "Queen: Which do you think is better, my beautiful painting or the painting Maki drew?",
        "Queen: Now, answer honestly!"
    ],
    21: "=How will you answer?<FF03><FF0E>に<FF01>",
    22: ["Mark: You idiot! Do you really think that?!"],
    23: [
        "Queen: Hehehe, ahahaha!",
        "Queen: How about that, Maki? <FF0F>あ-kun chose me!"
    ],
    24: ["Maki: ..." + P('み') + " ..." + P('み') + " ..." + P('み') + " ..." + P('み') + " ..."],
    25: ["Nanjo: We somehow managed to avoid turning to stone."],
    26: [
        "Aki: Geez, what are you doing, Queen!",
        "Aki: I told you to beat these guys!"
    ],
    27: ["Queen: I'm sorry, Angel. But I can't stand any more moles..."],
    28: ["Aki: Then if you beat them, Aki will give you your old face back!"],
    29: ["Queen: Really?!" + P('ぎ') + " ...Understood. I'll do it!"],
    30: ["Queen: I'm sorry, <FF0F>あ-kun. You're actually quite my type, though."],
    31: [
        "Queen: Mirror, mirror, hear Chisato's wish. Give me power!",
        "Queen: Nomoraka tanomamaa!"
    ],
    32: [
        "Mark: Serves you right! This guy ain't a weakling who bends to threats!",
        "Mark: ...Gah!"
    ],
    33: [
        "Queen: <FF0F>あ-kun.",
        "Queen: I thought you of all people would understand, but I was wrong about you.",
        "Queen: I'll repay this humiliation tenfold." + P('ぎ') + " Turn to stone with everyone else!"
    ],
    34: [
        "Aki: Eeew, you're still at it?",
        "Aki: Hey, Queen, if you beat these guys, Aki will give you your old face back!"
    ],
    35: [
        "Queen: Since the Angel says so, plans have changed.",
        "Queen: I'll defeat you with my own hands!"
    ],
    36: ["Naito: ..." + P('ぎ') + " You silly girl, Chisato. * Trust me more."],
    37: [
        "Kozai: But, Yosuke, I was anxious.",
        "Kozai: I kept thinking, what if Yosuke came to hate me?"
    ],
    38: [
        "Naito: Haha, you! There's no way I'd come to hate Chisato, right?",
        "Naito: Don't make such a sad face. Smile for me" + P('ぎ') + " okay, Chii-chan? *"
    ],
    39: ["Mark: " + P('ぎ') + " Chii-chan? *" + P('ぎ') + " Geez..." + P('ぎ') + " Looks like we're in the way. Let's go home, <FF0F>あ..."],
}
REVIEW = {36: "♥ replaced by *", 38: "ちいちゃん = Chii-chan", 39: "♥ replaced by *"}

if __name__ == '__main__':
    apply('E0', 100, BOXES, REVIEW)
