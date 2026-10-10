"""E0 entry 116 - Aki's castle gate cannot be opened."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Maki: So this is your hideout! You won't get away anymore!"],
    1: [
        "Aki: Neeener! You can't go any farther than here! Unless you get that guy in the forest.",
        "Aki: But he doesn't have the courage, so nobody can get in the way of Aki and Papa!"
    ],
    2: ["Maki: Ah!!"],
    3: ["Maki: Aaargh, geez!! She got away again."],
    4: ["Nanjo: ........."],
    5: ["Mark: Damn, it doesn't budge."],
    6: ["Mark: Hey, Nanjo! Quit spacing out. Don't you have any ideas?"],
    7: ["Nanjo: That child set something into that pedestal."],
    8: ["Nanjo: Without a key that fits this half-moon-shaped hollow, we will not be able to enter."],
    9: [
        "Elly: Judging by her manner of speaking, someone else must be holding it."
    ],
    10: ["Brown: Ugh~ We've gotta look for something else again~?"],
    11: ["Ayase: Hey, open up already!"],
    12: [
        "Maki: When she said forest... she must mean the forest in the west. It used to be a beautiful flower garden...",
        "Maki: Now it's called the Lost Forest."
    ],
    13: ["Elly: Then let us go back. We must find the person who holds the key."],
    14: ["Brown: Ugh, we're going back? How about the leader keeps watch here? No good? Yeah, figured."],
    15: ["Ayase: Meowww~ We came all the way here and we're going back? The worst!!"],
    16: [
        "Mark: Can't be helped, let's go back.",
        "Mark: We gotta find that guy the brat mentioned."
    ],
    17: [
        "Maki: When the Lost Forest was a flower garden, a girl named Mai-chan often played there...",
        "Maki: Could she be the one?"
    ],
    18: ["Mark: So that brat really is Kandori's kid. She's just as infuriating as him."],
    19: [
        "Nanjo: ..." + P('で') + " <FF0F>あ, does that child's behavior not bother you somehow?",
        "Nanjo: I feel as though we are being made to dance."
    ],
    20: [
        "Elly: Still, that girl... She must care for Kandori so much..." + P('ス') + " I'm a little envious...",
        "Elly: Oh, I'm sorry. I said something strange..."
    ],
    21: ["Brown: Alright, alright, we'll go back. We'd be in trouble without the leader."],
    22: [
        "Ayase: Hey, <FF0F>あ~, carry me on your back~!",
        "Ayase: C'mon, you get to feel Ayase's warmth, okay?"
    ],
    23: ["Reiji: ..." + P('で') + " So that bastard's up there... He's not getting away. Wash your neck and wait..."],
    24: ["Reiji: ..." + P('で') + " Move aside, you guys. I'll smash it."],
    25: [
        "Mark: Wait, Reiji. It ain't something you can smash.",
        "Mark: You really do change when it comes to Kandori, huh. Well, I won't dig into it.",
        "Mark: Don't shoulder everything alone."
    ],
    27: [
        "Maki: ...Kido-kun, Inaba-kun's right. We're companions, aren't we?"
    ],
    28: [
        "Reiji: ..." + P('で') + " I don't intend to be chummy with you. Companions? It makes me sick.",
        "Reiji: Especially you, Inaba... Looking at you gives me the creeps."
    ],
    29: ["Maki: Kido-kun! Isn't that too much?!"],
    30: [
        "Mark: It's fine, Sonomura. Creeps or whatever, right now we've got no choice but to turn back together.",
        "Mark: We've got the same goal, after all. Let's go, <FF0F>あ."
    ],
    31: ["Maki: I don't get boys. It seems Inaba-kun likes Kido-kun."],
    32: ["Mark: What? \"Do you have a fever\"? What's that supposed to mean?"],
    33: [
        "Nanjo: To think Inaba stays silent after being told that." + P('サ') + " Heh heh...",
        "Nanjo: Perhaps he senses the same smell. He is a beast, after all."
    ],
    34: ["The door doesn't budge."],
    35: ["There is a half-moon-shaped hollow."],
}
REVIEW = {}

if __name__ == '__main__':
    apply('E0', 116, BOXES, REVIEW)
