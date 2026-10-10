"""E0 entry 39 - Principal and Vice Principal."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: [
        "Principal Oishi: <FF0F>あ-kun! You are safe. Thank goodness...!",
        "Principal Oishi: When I think about what could happen to my precious students... I..." + P('み') + " I get so worried..."
    ],
    1: [
        "Vice Principal Hanya: This is absolutely outrageous! If something were to happen at school, it would be the school's responsibility!",
        "Vice Principal Hanya: And we would be the ones punished!",
        "Vice Principal Hanya: Aaah, if only it had happened a little later, all the students would have gone home already...<FF02><FF03>I am so unlucky!"
    ],
    2: [
        "Principal Oishi: I heard you are looking into the \"Snow Queen\"." + P('ぎ') + "..." + P('な') + " I will tell you everything.",
        "Principal Oishi: You see, it was customary for the \"Snow Queen\" at this school to perform wearing a mask for generations.",
        "Principal Oishi: But the nasty rumors about that mask never ceased.",
        "Principal Oishi: At some point, people began to say that the Queen's mask was cursed.",
        "Principal Oishi: Even I didn't believe it until that day eight years ago...",
        "Principal Oishi: You see, the last person to play the \"Snow Queen\" was Saeko-sensei."
    ],
    3: [
        "Vice Principal Hanya: P-Principal!! What are you saying!"
    ],
    4: [
        "Principal Oishi: That time, eight years ago..." + P('み') + " Saeko-sensei lost her best friend.",
        "Principal Oishi: If only I had realized sooner..." + P('み') + " If I hadn't let them use that mask, that wouldn't have happened.",
        "Principal Oishi: ..." + P('な') + " We immediately held a memorial service for the mask and it's stored in the storehouse now, but...",
        "Principal Oishi: You must not bring up Saeko-sensei's painful past."
    ],
    5: [
        "Vice Principal Hanya: ..." + P('み') + "You there, the Principal is just joking! You shouldn't believe such a story!"
    ],
    7: [
        F6('い') + "Vice Principal Hanya<FF03>Known as Vice Principal Hannya. He is very strict, so his popularity with the students is quite low."
    ],
    8: [
        "Principal Oishi: I don't want to lose any more of my precious students ever again." + P('ゆ') + " Please, take good care of yourselves."
    ],
    9: [
        "Vice Principal Hanya: What is it, do you still need something? I am busy. Hurry up and get out!"
    ],
    10: [
        "Principal Oishi: The \"Snow Queen\" mask... I wonder if it has anything to do with this incident...?",
        "Principal Oishi: Probably not. But <FF0F>あ-kun, you must not go near the gymnasium storehouse."
    ]
}

if __name__ == '__main__':
    apply('E0', 39, BOXES)
