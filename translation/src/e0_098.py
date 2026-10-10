"""E0 entry 98 - the Harem Queen is Chisato Kozai."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Queen: It's been a while, Maki. <FF0F>あ-kun and the rest of you, welcome to my palace."],
    1: ["Maki: C-Chisato...!! So it really was you...!? How could this...!"],
    2: [
        "Mark: So it was her after all.",
        "Mark: Hey, <FF0F>あ, did Kozai always have that many moles on her face?",
        "Mark: She was always bragging that her skin was clear, wasn't she...?"
    ],
    3: [
        "Maki: Hey, Chisato! There must be some reason, right? Is the real Queen threatening you?",
        "Maki: Chisato being our enemy" + P('み') + " that's a lie, isn't it?"
    ],
    4: [
        "Queen: You're so stupid! Me, being threatened? Not at all!",
        "Queen: I'm here of my own will! The palace and this room are wonderful, aren't they?",
        "Queen: A girl in black clothes, an angel, lent me a mirror that grants any wish. I made all this with it."
    ],
    5: ["Mark: In black clothes..."],
    6: [
        "Mark: You mean Aki! Kozai, that kid ain't no angel!",
        "Mark: Besides, weren't you kidnapped?"
    ],
    7: [
        "Queen: At first I thought so too. But I was wrong.",
        "Queen: She was looking for a human who could master the mirror.",
        "Queen: And that was me, you see."
    ],
    8: [
        "Maki: ..." + P('み') + " I understand that Chisato is the Queen, so that's enough, right?" + P('み') + "",
        "Maki: Let's go home together! Naito-kun got hurt." + P('み') + " Chisato, you have to be with him..."
    ],
    9: ["Queen: He got hurt" + P('ゆ') + " ...Yosuke?"],
    10: [
        "Queen: ...Maki" + P('み') + " you know,",
        "Queen: I don't need Yosuke anymore. I don't even like him."
    ],
    11: ["Maki: Huh?"],
    12: ["Maki: What did you just say?"],
    13: ["Queen: I never liked Yosuke. Not from the start."],
    14: ["Maki: That's a lie! You were so proud of him. You said he was a wonderful boyfriend..."],
    15: [
        "Queen: You still don't get it? You really are stupid!",
        "Queen: I went out with Yosuke because I knew you liked him!",
        "Queen: At first Yosuke liked you, you know.",
        "Queen: I couldn't forgive that. Because I'm prettier than you!",
        "Queen: He should've liked me, right?",
        "Queen: So I seduced Yosuke. Then that simple idiot fell head over heels for me."
    ],
    16: ["Maki: That's... not true." + P('み') + " Chisato, don't joke like that..."],
    17: [
        "Queen: It's not a joke! It's all true!",
        "Queen: I'm better at painting too, yet you're the only one who gets fussed over!",
        "Queen: I've never liked you, from way back!",
        "Queen: I'm prettier, and I have talent for painting!",
        "Queen: So why do only good things happen to you?"
    ],
    18: [
        "Nanjo: So that is why you took Naito from Sonomura. And had the townspeople praise your paintings...",
        "Nanjo: ?" + P('ぎ') + " Wait, Kozai. This Sonomura is a different person from the Sonomura we know, you realize?"
    ],
    19: [
        "Queen: Shut up! Stay quiet, you outsider!",
        "Queen: Hey, Maki. You were laughing at me, weren't you, deep down?",
        "Queen: Wearing that \"I'm so kind\" face, you were secretly making fun of me!",
        "Queen: But I won't let you do that anymore! Now I'm above you in everything!"
    ],
    20: ["Mark: Aki..." + P('み') + " It's thanks to the mirror that girl in black gave you, ain't it?"],
    21: [
        "Queen: Shut up already!" + P('み') + " ...Hey, <FF0F>あ-kun, my paintings are wonderful, aren't they?",
        "Queen: Everyone praises them! They say they're much better than Maki's bad paintings!"
    ],
    22: ["Maki: Chisato, you hated me that much? I didn't know..."],
    23: [
        "Mark: Now I get why your paintings are bad!",
        "Mark: Your guts are rotten! Someone like that can't paint a good picture!",
        "Mark: Don't take painting lightly!"
    ],
    24: ["Queen: ..." + P('な') + " Wh..." + P('な') + " What did you say...?"],
    25: [
        "Nanjo: You do nothing but envy Sonomura, make no effort, and in the end make others obey by force.",
        "Nanjo: And you think that made you your ideal self? You are a naked king!",
        "Nanjo: Nobody truly means what they say. They are only flattering you because they fear you!"
    ],
    26: ["Queen: ..." + P('み') + " A naked king? Me?"],
    27: [
        "Mark: That's right, Kozai!",
        "Mark: You hurt Sonomura over a stupid complex! I won't forgive you, you bastard!",
        "Mark: Listen, I'll say it as many times as it takes. Your paintings are baaad!"
    ],
    28: [
        "Queen: Then go look at them again!",
        "Queen: If you can't understand my paintings, it's your fault, not mine!"
    ],
    29: [
        "Queen: Mirror, mirror, hear Chisato's wish. Throw them outside!",
        "Queen: ...Nomoraka tanomamaa!"
    ],
}
REVIEW = {8: "Maki switches to the Queen being Chisato; fine", 15: "Queen's bitter confession"}

if __name__ == '__main__':
    apply('E0', 98, BOXES, REVIEW)
