"""E0 entry 3."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["So you guys" + P('た') + " had that dream, too..." + P('ソ')],
    1: [P('み') + "It was truly" + P('み') + " a world-shattering experience." + P('ソ')],
    2: [P('み') + "Maybe this guy" + P('み') + " is having the same dream right now?" + P('ソ')],
    3: ["Natsumi-sensei: You're awake, <FF0F>あ-kun. Welcome to the infirmary. You had a cute sleeping face."],
    4: [F6('う') + "Yoshino Natsumi<FF03>St. Hermelin High school nurse. Not a very good cook."],
    5: ["Saeko-sensei: <FF0F>あ! Are you okay?!"],
    6: ["Saeko-sensei: Thank goodness you came to, <FF0F>あ! I was so worried when they said you collapsed!"],
    7: [F6('う') + "Takami Saeko<FF03><FF0F>あ's homeroom teacher. Bright and very popular with the students."],
    8: ["Saeko-sensei: I'm sorry, Natsumi-sensei, for my kids causing you trouble!"],
    9: ["Mark: Taking care of students is your job, so it can't be helped..."],
    10: [
        "Saeko-sensei: Hey, Inaba! Show a little remorse! " + P('ぎ'),
        "Saeko-sensei: ...Anyway, I heard the gist of it from Kirishima and Ayase.",
        "Saeko-sensei: I'm cancelling your chores for today." + P('み'),
        "Saeko-sensei: In exchange, go get examined at Mikage Hospital before you go home!"
    ],
    11: ["Yukino: You think we're crazy too, Sensei?"],
    12: [
        "Saeko-sensei: I can tell you're all sane just by looking at you.",
        "Saeko-sensei: ...But I want to make sure you didn't hit your head when you collapsed, just to be safe."
    ],
    13: ["Yukino: Even Saeko-sensei worries sometimes, huh. " + P('ぎ') + "Well, we'll go to the hospital."],
    14: [
        "Natsumi-sensei: Oh, speaking of Mikage Hospital,",
        "Natsumi-sensei: isn't there a student from your class admitted there?"
    ],
    15: ["Mark: ..." + P('み') + "You mean Sonomura."],
    16: [
        "Saeko-sensei: Right. Well, it's not exactly on the way, but you should go visit her.",
        "Saeko-sensei: She's been in the hospital for almost a year now. I'm sure she's lonely."
    ],
    17: [
        "Saeko-sensei: I asked you guys to prepare for the sports festival,",
        "Saeko-sensei: but why did you end up collapsing in an empty classroom?",
        "Saeko-sensei: It's only a month away, and we haven't prepared anything at all!",
        "Saeko-sensei: Should I just cancel it this year?!"
    ],
    18: ["Nanjo: It cannot be helped. Troublesome matters are best dealt with quickly."],
    19: [
        "Mark: Mikage Hospital, right? It's a pretty long walk from the school. It's way off to the northeast.",
        "Mark: First, we leave the school and go right.",
        "Mark: Then, we turn right at the main street..." + P('な') + " and take a left at the dead end!",
        "Mark: Well, " + P('み') + "if we wander around, we'll get there eventually."
    ],
    20: [
        "Yukino: I couldn't handle being in the hospital for a whole year. " + P('み') + "Let's all cheer her up!"
    ],
    21: ["Saeko-sensei: Hey!" + P('み') + " Just hurry up and get to Mikage Hospital!"],
    22: ["Agastya Tree: Young one... It is good that you have come to me."],
    23: "=Agastya Tree:<FF03>Will you engrave<FF03>your record into me?<FF02><FF03><FF0E>　<FF01>",
    24: ["Agastya Tree: Young one... Go forth with the utmost care."],
    25: [
        "Natsumi-sensei: I bought a new houseplant. What do you think? Nice, isn't it?",
        "Natsumi-sensei: They say plants grow well when you talk to them,",
        "Natsumi-sensei: so make sure you say hi to it sometimes, <FF0F>あ-kun."
    ],
}

if __name__ == '__main__':
    apply('E0', 3, BOXES)
