"""E0 entry 18."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: [
        "Maki: Huh, do they not stock weapons?",
        "Maki: That's weird~"
    ],
    1: [
        "Nanjo: Are you finished with your business?",
        "Nanjo: Now, will you finally take us to the hospital?"
    ],
    2: ["Nanjo: Heh heh. It is true that a convenience store has everything one needs for daily life."],
    3: [
        "Mark: So that person's Kido's mom... She's so elegant, man, that must be nice.",
        "Mark: Compared to her, my place is..."
    ],
    4: [
        "Mark: Huh, is this where Yukino works part-time?",
        "Mark: Oh wait, that's a different store."
    ],
    5: ["Elly: Even if you do not buy one, sometimes things lying around can be used as weapons."],
    6: ["Yukino: Kido Reiji is a weirdo, but his mother is a nice person."],
    7: ["Yukino: No matter if it's a convenience store, weapons are a bit of a stretch..."],
    8: [
        "Reiji's Mother: Oh, are you students from St. Hermelin?",
        "Reiji's Mother: That means you're at the same school as my son..."
    ],
    9: "=Reiji's Mother: His name is<FF03>Kido Reiji. Do you know him?<FF02><FF03><FF0E>い<FF01>",
    10: [
        "Reiji's Mother: Oh, you do? My, you're in the same class?",
        "Reiji's Mother: I see... That boy isn't very good at socializing, so..."
    ],
    11: "=Reiji's Mother: I know this is a<FF03>selfish request, but could you<FF03>please be friends with Reiji?<FF02><FF03><FF0E>あ<FF01>",
    12: ["Reiji's Mother: Oh, is that so..." + P('み') + " I am sorry for being so pushy."],
    13: [
        "Reiji's Mother: Oh, really?",
        "Reiji's Mother: Thank you so much!",
        "Reiji's Mother: Please come visit our house sometime!"
    ],
    14: [
        "Reiji's Mother: I see..." + P('み') + " With the way he dresses, it cannot be helped.",
        "Reiji's Mother: But he really is a kind, good boy.",
        "Reiji's Mother: Oh, that's right. It is not much, but please accept this..."
    ],
    15: [
        "Reiji's Mother: Please take care of my boy.",
        "Obtained a \"Chewing Soul\"."
    ],
    16: ["Reiji's Mother: Oh, students from St. Hermelin... Please take care of my son."],
    17: ["Clerk: Welcome!"],
    18: ["Clerk: We do not stock weapons here, but..." + P('み') + " Is that all right?"],
    19: [
        "Customer: Convenience stores these days have everything, don't they!?",
        "Customer: Don't you think it's strange they don't have weapons!?"
    ],
    20: [
        "Customer: Yes, exactly!",
        "Customer: You should answer to the consumers' needs!"
    ],
    21: [
        "Customer: Convenience stores these days have everything, don't they!?",
        "Customer: It's strange they don't have weapons! You think so too, right!?"
    ],
    22: [
        "Customer: Yes, precisely!",
        "Customer: Shouldn't you answer to the consumers' needs!?"
    ],
}

if __name__ == '__main__':
    apply('E0', 18, BOXES)
