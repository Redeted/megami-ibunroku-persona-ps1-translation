"""E2 entries 171-172 - other-world school: Reiji's fans, the girl in black rumor."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

pm = P('み'); pn = P('な')

E171 = {
    9: [
        "Ayase: The boys at this school are all so childish. Ayase isn't interested."
    ],
    10: [
        "Ayase: Even if you call him mature... Kido is a bit different, isn't he."
    ],
    11: [
        "Reiji: What? That woman is glaring at me" + pm + " ...Did I do something?"
    ],
    12: [
        "Student: Ah, senpai... um" + pm + " I just saw a really cool person.",
        "Student: It's a face I've never seen, so maybe a transfer student... Ahh, who is that person...?"
    ],
    13: [
        "Student: ..." + pn + " Kya! Senpai, do you know that person? Hey, hey, introduce me!"
    ],
}

E172 = {
    0: [
        "Principal Oishi: Oh, <FF0F>あ-kun. ..." + pm + " Did something happen?",
        "Principal Oishi: Surely the girl in black hasn't appeared again!?"
    ],
    1: [
        "Nanjo: No, Principal. But a girl in black...?"
    ],
    2: [
        "Vice Principal Hanya: This is your first time hearing, Nanjo-kun? Actually, lately a girl in black clothes has been appearing at this school...",
        "Vice Principal Hanya: They say she controls demons."
    ],
    3: ["Elly: Demons here too...?"],
    4: ["Brown: Demons here too...?"],
    5: ["Ayase: Demons here too...?"],
    6: ["Mark: Demons here too...?"],
    7: [
        "Vice Principal Hanya: But there's no need to worry. We shall protect you students, Principal Oishi and I!"
    ],
    8: [
        "Mark: W-What the heck, that's creepy! Why is Vice Principal Hannya so nice!",
        "Mark: Anyway, we're going now!"
    ],
    9: ["Principal Oishi: <FF0F>あ-kun and the others! You're safe..."],
    10: [
        "Vice Principal Hanya: Oh, thank goodness... But what on earth was that? It seemed the inside of the school had been turned upside down..."
    ],
    11: ["Maki: It's okay, Sensei! We'll protect you!"],
    12: [
        "Vice Principal Hanya: Did you hear that, Principal! What consideration!",
        "Vice Principal Hanya: Principal, this too is the result of your wonderful education!"
    ],
}

if __name__ == '__main__':
    apply('E2', 171, E171, {})
    apply('E2', 172, E172, {})
