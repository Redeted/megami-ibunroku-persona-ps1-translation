"""E2 entry 23 - first day: classmates chatting at the school (shoe lockers)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P  # noqa: E402

BOXES = {
    0: ["Nanjo: You people are so slow." + P('み') + " Be brisk, like me!" + P('み')
        + " Youth ages easily, as they say..."],
    1: ["Nanjo: What is it, <FF0F>あ?!<FF03>Did you want something?!<FF03>If not, get lost!!!"],
    2: ["Mark: Nanjo's such a jerk.<FF03>He really ticks me off.<FF03>I'll get something on him someday."],
    3: ["Mark: Young Maaaster~!" + P('な') + "<FF03>Get it? \"Young Master\"~?" + P('な')
        + "<FF03>Bwa ha ha ha." + P('み') + " This'll be great!"],
    4: ["Yukino: Inaba and Nanjo are<FF03>both just kids."],
    5: ["Yukino: That old man, Yamaoka...<FF03>He really dotes on Nanjo,<FF03>doesn't he?"],
    6: ["Student: There was a weird old man standing by the school gate earlier. Creepy, huh?"],
    7: ["Student: Hey, hey, don't you think Nanjo-kun is kind of scary?",
        "Student: Like, he's cool, or rather calm and collected."],
    8: ["Student: Yo, <FF0F>あ! I heard you collapsed? Was it from studying too much?",
        "Student: " + P('み') + "...Nah, no way!"],
}

if __name__ == '__main__':
    apply('E2', 23, BOXES)
