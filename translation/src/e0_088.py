"""E0 entry 88 - the Hama Mirror is found."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: [
        "Maki: This town isn't bad either, right? I think paradise is a place like this.",
        "Maki: It's ordinary, but every day is fun."
    ],
    1: [
        "Nanjo: I am curious about the person Kurouri mentioned...",
        "Nanjo: <FF0F>あ, do not forget to go to Araya Shrine."
    ],
    2: ["Mark: This place ain't any different from our town. Smells musty, too."],
    3: ["Elly: So this is the \"Hama Mirror.\" It is mystical and lovely!"],
    4: ["Brown: So this is the \"Hama Mirror\"..." + P('ゆ') + " Let's see, will it show my face?"],
    5: ["Ayase: So this is the \"Hama Mirror\"... Will it show Ayase's face? My skin's been a total mess lately..."],
    6: ["Reiji: This is the \"Hama Mirror\"? Some piece of junk."],
    7: ["The \"Hama Mirror\" gives off a divine atmosphere..."],
    8: ["Maki: Found it! This is the \"Hama Mirror,\" right!"],
    9: ["Elly: Wh-What is this...!"],
    10: ["Ayase: Eek! What's this!"],
    11: ["Brown: Whoa! What the heck!"],
    12: ["Reiji: !! What...!?"],
    13: ["Don't take it... Don't take it... You mustn't... Nooooo..."],
    14: [
        "Nanjo: What was that...! It looked like a little girl's face, and it said not to take \"this.\"",
        "Nanjo: Did she mean the \"Hama Mirror\"?"
    ],
    15: ["Mark: How should I know! We'd be in trouble without it!"],
    16: ["Maki: That face just now... It looked like Mai-chan..."],
    17: ["Mark: Here, <FF0F>あ. With this we can fight the monster in the subway, right?"],
    18: ["Obtained the \"Hama Mirror\"!"],
}
REVIEW = {13: "Mai's voice, wording guessed", 17: "ok"}

if __name__ == '__main__':
    apply('E0', 88, BOXES, REVIEW)
