"""E0 entry 4."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Nanjo: There are no decent books in here... The library at my home is far superior."],
    1: [
        "Mark: What do you need in the library for? More importantly, let's go visit her" + P('ぎ'),
        "Mark: I mean, let's go get examined!"
    ],
    2: [
        "Yukino: Those two in the corner seem to be making fun of Akuma-kun...",
        "Yukino: But I think Akuma-kun is a bit better simply because he doesn't act all high and mighty."
    ],
    3: [
        "Kurouri: ...Ah, <FF0F>あ-kun. Hehehe, I'm currently investigating the Seven Wonders of the school.",
        "Kurouri: Want me to tell you? Hehehe, maybe later..."
    ],
    4: [F6('い') + "Kurouri Tsutomu<FF03>Known as Akuma-kun. Occult expert who is often wrong."],
    5: [
        "Student: That guy gets called \"Akuma-kun\", but he's always saying things that miss the mark.",
        "Student: My knowledge of the occult is steps above his. I can't teach it to an amateur, though."
    ],
    6: [
        "Student: Even demons must have ones they get along with and ones they don't.",
        "Student: If demons that hate each other were to run into one another,",
        "Student: wouldn't that cause a huge problem?"
    ],
    7: [
        "Student: You see that guy over there, Akuma-kun? He fell over during PE class again today.",
        "Student: We all had a good laugh! He can't do push-ups at all! I feel so bad for him!"
    ],
}
REVIEW = {
    1: "Mark corrects himself from saying visit (Sonomura) to going to the exam.",
}

if __name__ == '__main__':
    apply('E0', 4, BOXES, REVIEW)
