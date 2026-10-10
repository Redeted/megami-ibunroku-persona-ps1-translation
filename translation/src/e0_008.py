"""E0 entry 8 - Second floor empty classroom."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Nanjo: <FF0F>あ, it seems you have been mistaken for someone else."],
    1: ["Mark: Someone who sneaks into the empty classroom on the second floor... Do you know anyone like that?"],
    2: ["Elly: I was telling Saeko-sensei what happened. Brown seemed to have left a bit earlier, and there's no way Ayase could explain it properly all by herself, is there?"],
    3: ["Ayase: That Uesugi managed to ditch us, so Ayase and Kirishima explained it to the teacher! Seriously, Uesugi's only fast at times like this!"],
    4: ["Yukino: Eriko and Yuka didn't pass out, so they don't need to go to the hospital. But why did only we pass out? The ones who didn't pass out are the ones who have played Persona-sama before... Yuka, Eriko, and Uesugi, huh..."],
    5: ["Teacher: Oh, it's you, <FF0F>あ. Hey, I heard someone's been going in and out of the empty classroom at the far end of the second floor lately. It wasn't you, was it? Hmm?"],
    6: ["Teacher: If it isn't you, then who on earth has been going in and out of that classroom...?"]
}

if __name__ == '__main__':
    apply('E0', 8, BOXES)
