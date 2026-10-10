"""E0 entry 148 - Kandori's end; the truth about Maki's world."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: [
        "Kandori: Heh heh... That I should be defeated... You were right, Nanjo-kun.",
        "Kandori: I... could only live this way.",
        "Kandori: Perhaps I invited you here because I wanted someone to say that. Heh heh... Unsightly, but it feels good..."
    ],
    1: ["Nanjo: ..." + P('で') + " Where is the real Sonomura?"],
    2: ["Kandori: So you see through the mystery of the two worlds as well... As expected."],
    3: ["Maki: ...What does that mean, Nanjo-kun?"],
    4: [
        "Kandori: It means that you, and the world you lived in, are nothing but a product of a certain person's imagination, Sonomura Maki-kun..."
    ],
    5: ["Maki: Wh-What? What are you saying!? What does that mean!?"],
    6: [
        "Nanjo: ...You are probably the ideal form of the Sonomura Maki we know.",
        "Nanjo: And the town you live in is the world inside Sonomura Maki's heart... Is that right, Kandori?"
    ],
    7: [
        "Kandori: Exactly... Not only you. Mai and Aki are also Shadows within Sonomura Maki's heart.",
        "Kandori: They are nothing but her alter egos."
    ],
    8: ["Maki: No way..." + P('キ') + " That's absurd!!"],
    9: [
        "Nanjo: MAKI, MAI, AKI... A simple rearrangement of words.",
        "Nanjo: Sonomura must have been imagining a paradise of her own in her heart...",
        "Nanjo: modeled on the town as it was right before she was hospitalized."
    ],
    10: [
        "Mark: That's crazy... Then the police station being gone and the hospital turning into a castle...?"
    ],
    11: [
        "Nanjo: Because they are unnecessary in a paradise. One wants only what is convenient to oneself. Anyone would think so.",
        "Nanjo: Kozai and Naito being summoned must also be Sonomura's unconscious wish. She must have wanted the real versions of the boy she admired and her best friend."
    ],
    12: [
        "Kandori: The Deva System's activation experiment succeeded one month ago.",
        "Kandori: However, she and the system had been linked even before that.",
        "Kandori: Most likely her wavelength and the system's spiritually synchronized.",
        "Kandori: Fused with the power to interfere with dimensions, the paradise in her heart must have grown beyond imagination."
    ],
    13: ["Nanjo: And you made contact with the paradise's caretaker, Mai..."],
    14: [
        "Kandori: Mai... no, that Maki was lonely.",
        "Kandori: Her role was the ideal Maki: to provide you a world convenient to you and comfort the real Maki.",
        "Kandori: The rest is as you know."
    ],
    15: ["Maki: Liar! That's nonsense!!"],
    16: ["Kandori: Then meet the real you. She is inside this castle..."],
    17: [
        "Maki: I'm me! That... that's too cruel!"
    ],
    18: ["Mark: Sonomura!"],
    19: ["Elly: <FF07>あ! Let us go after her!"],
    20: ["Brown: <FF08>あ! This is bad, we gotta go after her!"],
    21: ["Ayase: This is bad, <FF0F>あ! Aren't you gonna chase her!?"],
    22: [
        "Reiji: Aren't you going after her? You're the only one who can save her."
    ],
    23: [
        "Kandori: Sonomura Maki... needs to know her true heart. Otherwise she will follow my footsteps...",
        "Kandori: Go to her..." + P('キ') + " She must not take the same road as me..."
    ],
    24: ["Nanjo: ..." + P('キ') + " A pitiful man."],
    25: ["Mark: <FF0F>あ! We gotta find Sonomura!"],
    26: ["Mark: This has gotta be a lie! It's too cruel for Sonomura!"],
    27: [
        "Nanjo: I had been thinking about it all along. When I reached the conclusion, even I was confused."
    ],
    28: [
        "Reiji: ..." + P('キ') + " I finally killed that bastard..." + P('キ') + " What is this emptiness?"
    ],
    29: ["Elly: Poor Maki... We must help her..."],
    30: ["Brown: Seriously...? What's gonna happen to Maki-chan?"],
    31: ["Ayase: I can't believe it... What's gonna happen to Sonomura? Hey!?"],
    32: ["Kandori's dead face is peaceful..."],
    33: [
        "\"Human life is fifty years. Compared to the realm of heaven, it is like a dream or an illusion.\"",
        "That is what is written..."
    ],
}
REVIEW = {33: "Atsumori verse (敦盛 人間五十年) rendered literally"}

if __name__ == '__main__':
    apply('E0', 148, BOXES, REVIEW)
