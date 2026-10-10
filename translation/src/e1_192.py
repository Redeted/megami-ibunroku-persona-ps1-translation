"""E1 entries 160-195 - the masked girl, Mai, the masked boy."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

p = P('ほ')

E160 = {
    60: ["Hee-Ho-kun: Hee-Ho!! It's a trade for the \"Victoria Rune\"!"],
    61: ["Obtained the \"Victoria Rune\""],
    62: ["Brown: Dehyahya! A bourgeois-sounding name, fit for Great me."],
}

E192 = {
    0: [
        "Masked Girl: This is how I'm painting your future black. Do you know why?" + p + " Why do you get in my way?" + p + " Why can you endure the suffering?",
        "Masked Girl: You may have each other, and Saeko-sensei, and family..." + p + " people to rely on.",
        "Masked Girl: But I'm always alone. All I could do was watch everyone looking happy."
    ],
    1: ["Yukino: Don't tell me, you..."],
    2: [
        "Masked Girl: As if you could understand my feelings!! I'll destroy it..." + p + " I'll destroy the school!!"
    ],
    3: ["Yukino: Wait, Sonomura!!"],
    6: ["Yukino: Sonomura...?"],
    7: ["Yukino: Sonomura..."],
    8: ["Yukino: The paint isn't completely dry."],
    9: ["Ayase: Look at that painting. It's all black... It's kind of creepy."],
    11: ["Nanjo: An illusion?"],
    12: ["Nanjo: That cannot be. Sonomura should be outside the school."],
    13: ["Nanjo: Was someone here until a moment ago?"],
    14: ["Brown: Huh? Isn't that Maki-chan?"],
    15: ["Brown: Maki-chan has some sense, wearing a mask like that so boldly..."],
    16: [
        "Brown: Don't you guys understand art?",
        "Brown: What a magnificent piece of art, isn't it?"
    ],
    17: ["Elly: It may be the Queen's trap. Be careful!"],
    18: ["Elly: Maki cannot be here. Could it be a Demon...?"],
    19: ["Elly: Someone who was not frozen was here until a moment ago."],
}

E193 = {
    0: [
        "Girl in White: This is no time for this...",
        "Girl in White: Hey, have you seen me?"
    ],
    1: [
        "Ayase: ? What is this girl saying? Hey, little girl, why are you in a place like this? It's dangerous, go home."
    ],
    2: [
        "Nanjo: Ayase! There is no way an ordinary girl would be in a place like this!!",
        "Nanjo: What she says makes no sense either. She may not be human!!"
    ],
    3: [
        "Elly: Ayase! Can you not think a little calmly? There is no way a girl would be in a place like this! It is a Monster!!"
    ],
    4: [
        "Ayase: S-Shut up! Every little thing!",
        "Ayase: She seemed to be in trouble so I called out to her! Ayase isn't cold-blooded like you!"
    ],
    5: [
        "Girl in White: Mai-chan isn't lost, and isn't a demon either.",
        "Girl in White: More importantly, have you seen me?",
        "Girl in White: She's wearing the same clothes as you and a white mask."
    ],
    6: [
        "Yukino: One of our students? Sorry, but I don't know any student who wears a mask."
    ],
    7: ["Mai: I see."],
    8: ["Ayase: Ah!!"],
    9: ["Yukino: Hey, isn't that the one from before!!"],
    10: ["Mai: Eh!? Where was she? Tell me!!"],
    11: ["Yukino: A-Ah. On this floor. But I forgot exactly where."],
    12: ["Mai: Thank you!"],
    13: [
        "Yukino: A-Ah. It was somewhere like a stage on the eighth floor, I think. But she seems to have gone to a higher floor."
    ],
    14: ["Yukino: Who on earth is that girl..."],
    15: ["Ayase: I feel like she's not a bad girl, though..."],
    16: [
        "Nanjo: I feel I have seen that girl before.",
        "Nanjo: I wonder who she was."
    ],
    17: [
        "Brown: What a cutie~ If I check her out now, in ten years..."
    ],
    18: ["Elly: A girl in a place like this. She must be a Monster!"],
}

E195 = {
    0: [
        "Masked Boy: You are late. Have you met her yet?"
    ],
    1: ["Yukino: Her... What are you talking about?"],
    2: [
        "Masked Boy: She should be painting on the floor below. She is shutting the \"Door to Paradise\" in the black of despair."
    ],
    3: [
        "Yukino: Her... You mean the white-masked girl who was in the art room?"
    ],
    4: ["Masked Boy: What did she say?"],
}

if __name__ == '__main__':
    for n, d in ((160, E160), (192, E192), (193, E193), (195, E195)):
        apply('E1', n, d, {})
