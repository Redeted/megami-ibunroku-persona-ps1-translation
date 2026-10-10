"""E0 entry 25 - Meeting Elly."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Elly: ...Was that Nike? The Goddess of Victory of Greece... That is me... I am that..."],
    1: ["Yukino: Eriko? Hey, are you okay?"],
    2: [
        "Elly: Nike... The archetype of the Angels of Christianity...",
        "Elly: That is me... I am that..."
    ],
    3: ["Mark: She's no good. She's lost it."],
    4: ["Yukino: Eriko! Pull yourself together!"],
    5: [
        "Elly: Ha!? I-I'm sorry. But I am fine now.",
        "Elly: I am an Angel that brings victory. From here on out, I shall protect you all!"
    ],
    6: ["Mark: ...Idiot. We have them too."],
    7: ["Elly: I-Is that so? I was not the only one chosen..."],
    8: ["Nanjo: Kirishima. You had the dream of the butterfly, did you not?"],
    9: ["Elly: How did you know? I have been seeing it often, I suppose, ever since we first played Persona-sama..."],
    10: ["Nanjo: As I suspected. So that dream is the cause..."],
    11: ["Mark: More importantly, what're you doing here? Is it like this outside too?"],
    12: [
        "Elly: Yes. It is already full of Demons. Moreover, we cannot leave the town.",
        "Elly: I have looked all around, but the school might be the only safe place."
    ],
    13: ["Yukino: The school is safe, then? <FF0F>あ, let's head back to the school."],
    14: [
        "Elly: Oh, that's right! Before that, let us go to the shrine.",
        "Elly: Maki's mother is injured and collapsed there."
    ],
    15: ["Mark: Hey! You should've said that sooner! <FF0F>あ, let's go help her."],
    16: ["Yukino: Let's help Sonomura's mother and hurry back to the school."],
    17: [
        "Nanjo: You people are too soft-hearted. Even so...",
        "Nanjo: Persona, and this bizarre incident... It is all too convenient... What is behind all this?"
    ],
    18: ["Mark: Sonomura... I'll definitely come save you..."],
    19: ["Elly: The shrine is not far from the school, after all. It is No problem!"]
}

if __name__ == '__main__':
    apply('E0', 25, BOXES)
