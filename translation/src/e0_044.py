"""E0 entry 44 - After the first Persona fight; Maki and Nanjo on Personas and Kandori."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Maki: So that just now was a Persona? Persona... The power of the heart... The other me... huh..."],
    1: ["Nanjo: The meaning is 'mask' in Latin. It is the origin of the English 'personal' and 'individuality'."],
    2: ["Maki: In a person's heart, there are demons, and there are angels too... Is that what it means?"],
    3: [
        "Nanjo: Poetically speaking, yes. But an eye for an eye, a tooth for a tooth... a demon for a demon.",
        "Nanjo: I do not know the principle behind it, but it is useful."
    ],
    4: [
        "Maki: ...We can do it! We can do it!",
        "Maki: Let's defeat the cause of the demons overflowing and take back our town! Right!"
    ],
    5: ["Nanjo: Yes. For that purpose as well, we must rescue that idiot. Shall we go, <FF0F>あ?"],
    6: ["Maki: I won't let that girl do as she likes any longer! Right, <FF07>あ-kun!"],
    7: [
        "Nanjo: <FF0F>あ. In a sense, Kandori is more formidable than the demons.",
        "Nanjo: He is the one staging this situation, after all. Do not forget that."
    ],
    8: ["Maki: <FF07>あ-kun, where are you going? We've got to hurry and go save Inaba-kun!"],
}
REVIEW = {
    1: "Japanese: 英語のパーソナル 個性の語源 - read as the root of both 'personal' and 'individuality'; could also be 'personal, i.e. individuality'",
}

if __name__ == '__main__':
    apply('E0', 44, BOXES, REVIEW)
