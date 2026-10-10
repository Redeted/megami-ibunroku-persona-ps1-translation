"""E0 entries 176-185 - Araya Shrine butterfly, rock cave entrance, the voice of the self."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

E176 = {
    0: ["Maki: That butterfly again!"],
}

E177 = {
    0: [
        "Butterfly: Boy, inside the Rock Cave it will be just the two of you. Are you well prepared?",
        "Butterfly: Are your weapons and items ready?"
    ],
    1: "=Will you enter the Rock Cave?<FF03><FF0E>　<FF01>",
    2: [
        "Butterfly: Very well. Then I shall open the path to the Sea of Consciousness. A path has opened behind the shrine.",
        "Butterfly: Go."
    ],
    3: ["Butterfly: I see. Then come once you are ready."],
    4: ["Butterfly: Are you ready now?"],
    5: ["Butterfly: Do you wish to go elsewhere? Then rejoin your companions."],
    6: "=Rejoin your companions?<FF03><FF0E>　<FF01>",
    7: ["Butterfly: Come again when you are ready."],
    8: ["Butterfly: If you intend to go outside, do not forget to rejoin your companions."],
    9: ["Mark: Leave Sonomura... to you."],
    10: ["Nanjo: We will wait here. Do not overdo it."],
    11: ["Maki: Everyone, I'm going! <FF07>あ-kun, let's go!"],
    12: [
        "Mark: <FF0F>あ, just because you're alone with Sonomura, don't lose your head, got it!?"
    ],
    13: ["Maki: What are you talking about?"],
    14: ["Mark: N-Nothing! Right, <FF0F>あ? Heh heh heh, it's just guy talk."],
    15: ["Maki: That sounds kind of dirty. Well, whatever. <FF07>あ-kun, hurry, hurry! *"],
    16: ["Mark: Somehow... Sonomura looks happy."],
    17: ["Elly: ..."],
    18: ["Mark: Damn it! Why am I no good?"],
    19: ["Nanjo: Be careful. We do not know what is in there."],
    20: ["Nanjo: Where are you going? Well, I do not mind, but we do not have much time."],
    21: [
        "Maki: I'm happy... because I'm not alone. Because everyone, because <FF07>あ-kun is with me... Right!"
    ],
    22: ["Reiji: ...I wanna have a go at you someday. Don't die."],
    23: ["Reiji: Not going yet?"],
    24: [
        "Elly: Where are you going? I will follow wherever <FF07>あ goes, but..."
    ],
    25: [
        "Elly: Where are you going? I will accompany <FF07>あ anywhere, but..."
    ],
    26: ["Elly: <FF07>あ... Take care... I will be waiting..."],
    27: ["Elly: <FF07>あ... Be careful... I will be waiting..."],
    28: ["Brown: Say hi to the real Maki-chan for me!"],
    29: [
        "Brown: Huh? Not going yet? Ohh, I get it, you're scared, aren't you?"
    ],
    30: ["Ayase: <FF0F>あ, not going yet? Are you maybe scared?"],
    31: ["Ayase: <FF08>あ, not going yet? Are you maybe scared?"],
    32: ["Ayase: <FF08>あ, make sure you meet Sonomura properly!"],
    33: ["Ayase: <FF0F>あ, make sure you meet Sonomura properly!"],
}

E179 = {
    3: [
        "<FF08>あ's Voice: ...Here, you let a pitiful woman die.",
        "Can you say you never thought, as long as I'm saved, it's fine?"
    ],
    4: [
        "<FF08>あ's Voice: ...Here, with no regard for your own safety, you saved a pitiful woman..."
    ],
}

E180 = {
    1: ["<FF08>あ's Voice: ...Here, you tried to abandon an old man who was being used..."],
    2: ["<FF08>あ's Voice: ...Here, you chose the path of saving the old man over defeating Kandori..."],
}

E181 = {
    1: [
        "<FF08>あ's Voice: ...Did you truly think Kozai's painting was better?",
        "Can you say with confidence that you did not bend your claim out of fear of being turned to stone?"
    ],
    2: [
        "<FF08>あ's Voice: ...Refusing to yield to threats and asserting your true feelings...",
        "That is not an easy thing to do..."
    ],
}

E182 = {
    0: [
        "Mark: But, man, that voice is definitely Sonomura's mom's voice. Right?",
        "Mark: I don't know why she's dressed like that, but what if she's really her mom...?",
        "Mark: <FF0F>あ, don't fight her!"
    ],
    1: [
        "<FF08>あ's Voice: ...You do not have eyes that see the truth.",
        "You judge only by what you see and do not try to see with your heart..."
    ],
    2: [
        "<FF08>あ's Voice: ...You have the eyes of the heart.",
        "You do not only look with your eyes, you know the art of looking with your heart..."
    ],
}

E183 = {
    0: ["Kandori: Boy... I have not heard your answer. For what reason do you live?"],
    1: [
        "<FF08>あ's Voice: ...This man's soul was ill and lost.",
        "Yet you could not save a soul seeking salvation. Because your own soul is also lost."
    ],
    2: [
        "<FF08>あ's Voice: ...This man's soul was ill and lost.",
        "Yet you gave peace to this man's soul. Because there was no letter of doubt in your own soul."
    ],
}

E184 = {
    0: [
        "Maki: <FF07>あ-kun, you think so too, don't you!? You think I'm the worst woman, don't you!?"
    ],
    1: [
        "<FF08>あ's Voice: ...How did you answer her question?",
        "Could you not tell her not to run away because you know you are running too?",
        "Can you deny it? Me?"
    ],
    2: [
        "<FF08>あ's Voice: ...You answered her question. Yes, running is easy...",
        "If you keep running, you only add to the debt you owe yourself. You know that."
    ],
}

E185 = {
    4: "=It'll cost 5000 yen, okay?<FF03><FF0E>　<FF01>",
}

if __name__ == '__main__':
    for n, d in ((176, E176), (177, E177), (179, E179), (180, E180), (181, E181), (182, E182), (183, E183), (184, E184), (185, E185)):
        apply('E0', n, d, {})
