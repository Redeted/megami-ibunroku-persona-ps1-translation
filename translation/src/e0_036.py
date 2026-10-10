"""E0 entry 36 - Akuma-kun talks about the Snow Queen."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: [
        "Kurouri: Ah, <FF0F>あ-kun. This recent incident is quite fascinating.",
        "Kurouri: It might even be the work of aliens...!" + P('み') + " Hehehe...",
        "Kurouri: No, it's true this time. You can trust me."
    ],
    2: [
        "Kurouri: You know the \"Snow Queen\", right? Yes, the fairy tale.",
        "Kurouri: It's the traditional play of St. Hermelin's drama club. Hehehe..." + P('ゆ') + "<FF03>Well, listen patiently.",
        "Kurouri: In that play, for some reason, it is customary for the \"Snow Queen\" to perform wearing a mask. And here is the main point.",
        "Kurouri: The truth is, that mask is cursed." + P('み') + " The students who played the \"Snow Queen\" wearing it have died unnatural deaths, one after another.<FF02><FF03>Interesting, isn't it?",
        "Kurouri: But you see, they say there was just one schoolgirl who didn't fall under this curse.",
        "Kurouri: I don't know who she is. If we knew that, it should provide some sort of hint..." + P('ぎ') + " Hehehe..."
    ],
    3: [
        "Student: Hey, you! You know something, don't you? Please, help me!"
    ],
    4: [
        "Student: Don't back people into a corner too much. If you anger a short-tempered guy, you never know what he'll do!<FF02>I bet demons are the same way."
    ]
}

if __name__ == '__main__':
    apply('E0', 36, BOXES)
