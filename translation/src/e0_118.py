"""E0 entry 118 - Mai in the Lost Forest; the half compact."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Girl in White: W-Who is it?"],
    1: ["Mark: This kid! Ain't she the ghost from the archives? Ain't she one of that brat's friends!?"],
    2: ["Girl in White: ..." + P('で') + " Hu..."],
    3: ["Girl in White: Waaaaah!"],
    4: ["Maki: Hey, don't cry. You're Mai-chan, right?"],
    5: ["Girl in White: *Hic*..." + P('ス') + " Y-Yeah..."],
    6: [
        "Maki: ...!" + P('で') + " This girl has a half-moon-shaped compact!",
        "Maki: It looks a lot like mine..."
    ],
    7: [
        "Nanjo: That must be the key to the castle... But who on earth are these children...?"
    ],
    8: ["Maki: Hey, Mai-chan. You know a girl named Aki, right? Is she your friend?"],
    9: [
        "Mai: No, she's not! She's not my friend! That one is Mai-chan!",
        "Mai: She's a bad Mai-chan! Waaaaaaah!!"
    ],
    10: ["Maki: What do you mean by that!?"],
    11: [
        "Mai: *Sniff*... Mai-chan was lonely... Then Kandori came...",
        "Mai: And then, that one came out of Mai-chan and went away with Kandori.",
        "Mai: Mai-chan knows Kandori isn't Papa, but..."
    ],
    12: [
        "Nanjo: Another personality split off from a single person, then...",
        "Nanjo: What is that compact?"
    ],
    13: [
        "Mai: Mai-chan's treasure... Any wish comes true. Mai-chan made this town with it."
    ],
    14: ["Maki: No way!" + P('ス') + " That can't be..."],
    15: [
        "Elly: Surely not... that such a small girl is the Creator of this world..."
    ],
    16: ["Nanjo: The creator of the world is such a small child..."],
    17: [
        "Brown: Awesome~! Just like a magical girl!",
        "Brown: I want that thing!"
    ],
    18: ["Ayase: Seriously!? Give it to Ayase!"],
    19: [
        "Maki: Can't you use that compact to catch Aki and Kandori, or send everyone back to our world, or something?"
    ],
    20: [
        "Mai: I can't... Aki took half of it from Mai-chan...",
        "Mai: Mai-chan knows Aki does bad things with her half, but wishes get cancelled out.",
        "Mai: So Mai-chan hides here."
    ],
    21: [
        "Mark: But without that we can't meet Kandori. Could you lend it to us for a bit?"
    ],
    22: ["Mai: No way! Kandori wants it! It's this!"],
    23: ["Maki: Mai-chan... You mustn't run away."],
    24: ["Mai: Hu... *Sniff*... Why not?"],
    25: "=If I hide, I am safe, right?<FF03><FF0E>す<FF01>",
    26: [
        "Maki: That's right, <FF07>あ-kun is right. Running away solves nothing.",
        "Maki: You have to fight!"
    ],
    27: [
        "Maki: Come on, <FF07>あ-kun! Don't joke around. Running away solves nothing.",
        "Maki: That's why you fight."
    ],
    28: ["Mai: *Sniff*... Why?"],
    29: "=Why do you fight, big brother?<FF03><FF0E>せ<FF01>",
    30: [
        "Mark: Gaah! We ain't got time to dawdle! We have to hurry back to our world.",
        "Mark: There's someone we've got to save. Please, lend it to us!",
        "Mark: From the way things looked, she may already..."
    ],
    31: ["Mai: Already..." + P('キ') + " dead?"],
    32: [
        "Mark: I-Idiot! She's definitely alive!",
        "Mark: Anyway, look..."
    ],
    33: [
        "Mai: Big brothers and sisters, why are you alive?",
        "Mai: Isn't living painful?"
    ],
    34: ["Maki: Why, you ask..."],
    35: ["Mark: Uh..."],
    36: ["Nanjo: ..."],
    37: ["Elly: Why..."],
    38: ["Brown: ...That's heavy."],
    39: ["Ayase: ...What a creepy kid."],
    41: ["Mai: Why? Big brother."],
    42: "=Why are you alive?<FF03><FF0E>そ<FF01>",
    43: [
        "Elly: ...You are right, <FF07>あ is right.",
        "Elly: And if you live, there are fun things too."
    ],
    44: [
        "Brown: ...Yeah, that's right! <FF08>あ's right.",
        "Brown: If you live, there are fun things, too."
    ],
    45: [
        "Ayase: ...Yeah, <FF0F>あ might be right.",
        "Ayase: If you live, there are fun things, too."
    ],
    46: [
        "Elly: It has been a long while since I thought about this, but... there are fun things too..."
    ],
    47: [
        "Brown: Been a long time since I thought about this, but... there are fun things, too, huh..."
    ],
    48: [
        "Ayase: Been a long time since I thought about this... There're fun things too, but..."
    ],
    49: [
        "Nanjo: <FF0F>あ is right. If you live, good things happen too."
    ],
    50: [
        "Nanjo: What an unreliable fellow... Well, it is a difficult question, but if you live, there will be good things, too."
    ],
    51: [
        "Mai: I see..." + P('で') + " Still, Mai-chan can't lend out the compact she keeps here.",
        "Mai: I'm sorry."
    ],
    52: ["Mark: This is getting us nowhere!! Please, lend it to us."],
    53: ["Mark: If you still say no, I'll smack your butt, got it?"],
    54: [
        "Mai: Hu..." + P('で') + " No way!" + P('キ') + " Nomoraka tanomama!"
    ],
    55: ["Mai: Mr. Bear, help me!"],
    56: [
        "Mai: I see..." + P('で') + " If it's you, then...",
        "Mai: I'll lend you the compact."
    ],
    57: [
        "Mark: Alright! Thanks, Mai-chan!",
        "Mark: Let's make a wish right away and have it carry us to Kandori!"
    ],
    58: [
        "Elly: Thanks! Let us make a wish right away and have it carry us to Kandori."
    ],
    59: ["Brown: Yahoo! Now, what should I wish for?"],
    60: ["Ayase: She's so understanding! Um, what should Ayase wish for?"],
    61: [
        "Nanjo: Fools. What good is chasing personal gain?",
        "Nanjo: Have it carry you to Kandori."
    ],
    62: [
        "Mai: No. Only Mai-chan can use it.",
        "Mai: Also, the castle is Aki's house, so it won't listen to Mai-chan's wishes."
    ],
    63: ["Mark: Gah. Right, nothing's ever that easy."],
    64: ["Mark: Can't be helped. Let's go back to the castle."],
    65: ["Brown: Boo-hoo~ I had all kinds of wishes..."],
    66: ["Ayase: No way! Ayase had all kinds of wishes! The worst!"],
    67: [
        "Maki: <FF07>あ-kun, let me see that compact.",
        "Maki: Wow, it's only half, but it's the same as mine...",
        "Maki: Mine has no mirror, but this one has it in there properly."
    ],
    68: [
        "Mark: Well, wishes are something you make come true yourself.",
        "Mark: If everything went your way, the world would be boring."
    ],
    69: ["Nanjo: Kandori... What does he intend to do with that compact...?"],
    70: ["Reiji: ..." + P('で') + " You've got a pretty good mouth on you..."],
    71: [
        "Elly: When I was little, I too remember treating the mirror at home as a magic mirror and making wishes.",
        "Elly: Something like, may I become a pretty girl everyone likes..."
    ],
    72: ["Brown: Aww, what a shame! I've got so many wishes!"],
    73: ["Ayase: Aww, Ayase wants so many things! <FF0F>あ, buy them for me, okay?"],
    74: ["Mai: Please don't let Kandori take the compact."],
    75: ["It's locked."],
    76: ["Obtained the \"Half Compact\"!"],
}
REVIEW = {13: "Mai says she made this town", 54: "ノモラカ・タノママ kept as a sound"}

if __name__ == '__main__':
    apply('E0', 118, BOXES, REVIEW)
