"""E1 entries 149-160 - the Queen of the Night warns; Tomomi's farewell; Hee-Ho's trade."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

p = P('ほ')

E149 = {
    19: [
        "Queen of the Night: You fools who still haven't thrown away hope! I'll show you what I can do!",
        "Queen of the Night: I have not given up on the \"Eternal Night.\"",
        "Queen of the Night: From this castle of ice, from the peak of the castle, I shall make snow of despair fall.",
        "Queen of the Night: Kukuku..." + p + " Ahahahaha..."
    ],
    20: ["Ayase: Huh!?"],
}

E150 = {
    0: ["Ayase: What was that just now? What does it mean?"],
    1: [
        "Elly: The Snow Queen was the embodiment of Tomomi's bad side.",
        "Elly: By holding up the \"Demon's Mirror\" that reflects all evil, Tomomi" + p + " that is, the Snow Queen,",
        "Elly: came face to face with how corrupted her own heart had been."
    ],
    2: [
        "Nanjo: The Snow Queen symbolizes the dark part of Tomomi's heart.",
        "Nanjo: By holding up the \"Demon's Mirror\" that reflects all evil, Tomomi" + p + " that is, the Snow Queen,",
        "Nanjo: saw how tainted her own heart had been."
    ],
    3: [
        "Yukino: I see! Seeing her ugly self reflected in the mirror, Tomomi-san came to her senses.",
        "Yukino: That's why her Persona, the Queen of the Night, lost its place to go and started running wild."
    ],
    4: ["Elly: Most likely, that is about it."],
    5: ["Nanjo: Yes. That is probably about it."],
    6: [
        "Brown: Thanks for the explanation. Finally I get the situation, too.",
        "Brown: So what it means is, unless we beat that Night-whatever, we can't go home or take a hot bath!"
    ],
    7: ["Ayase: Hmm. So in the end we have to beat that Night-whatchamacallit too."],
    8: ["Saeko-sensei: You all... You've become so reliable in the short time I haven't seen you."],
    9: ["Ayase: We only got this far because everyone was with me. Ayase alone could never..."],
    10: [
        "Yukino: Yeah. Thanks to these guys," + p + " well..." + p + " I can't put it well, but I feel like I understood for the first time what it means that I'm alive."
    ],
    11: ["Ayase: Whoa, so cool~"],
    12: [
        "Yukino: S-" + p + " Shut up! Let's go, <FF0F>あ!",
        "Yukino: Queen of the Night or whatever, with this crew we've got nothing to fear!"
    ],
    13: ["Saeko-sensei: Heh... <FF0F>あ! I'm counting on you to look after everyone!!"],
    14: ["Yukino: W-" + p + " What!?"],
    15: ["Ayase: Hey! Look at that..."],
    16: ["Saeko-sensei: Tomomi!!"],
    17: [
        "Tomomi: Saeko-san..." + p + " everyone" + p + " Thank you. Thanks to you, I was able to regain a human heart.",
        "Tomomi: The figure of myself in the mirror" + p + " my own heart" + p + " was too ugly to look at straight..."
    ],
    18: [
        "Yukino: You're not the only one, Tomomi-san. Standing before that mirror, anyone would surely look ugly.",
        "Yukino: People with truly beautiful hearts are rare."
    ],
    19: [
        "Brown: In that respect, I'm as innocent as a young girl and pure as an angel" + p + " ..." + p + " Sorry."
    ],
    20: ["Ayase: Ayase's figure was probably some awful monster."],
    21: [
        "Tomomi: You all don't look like monsters now. That's right!",
        "Tomomi: You should keep carrying the \"Demon's Mirror\" from now on. It will surely protect you from calamity.",
        "Tomomi: As a mirror it would be hard to carry, though..."
    ],
    22: ["The \"Demon's Mirror\" turned into a shield."],
    23: ["Obtained the \"Spiegel Shield\"."],
    24: [
        "Tomomi: And, I don't know if it'll be useful... The costume worn by the heroines of past \"Snow Queen\" plays should be in the gymnasium storeroom.",
        "Tomomi: To strengthen the seal of the \"Snow Queen's mask,\" it should have been placed near the box."
    ],
    25: [
        "Yukino: Oh, good to know. I don't know where the storeroom is in the \"Ice Castle,\" but it seems worth looking for."
    ],
    26: [
        "Tomomi: Ah..." + p + " If only I could have met you sooner...",
        "Tomomi: So that no second or third me is born, I will watch over the school from heaven together with the past Queens.",
        "Tomomi: Thank you."
    ],
    27: [
        "Ayase: I'm the one who should be thanking you!",
        "Ayase: I realized that without noticing it myself, I've been hurting all kinds of people in all kinds of places!!",
        "Ayase: That a nuisance like Ayase increases the kids who can't trust others..."
    ],
    28: ["Tomomi: Heh heh heh heh..."],
}

E160 = {
    0: [
        "Hee-Ho-kun: Hee-Ho! I saw a girl wearing a weird mask on the upper floor!",
        "Hiho-ko-chan: She was saying something dangerous~ Like she'd smash the school or something~",
        "Hee-Ho-kun: That's bad, Hee-Ho! If the school gets smashed, what'll we do?",
        "Hiho-ko-chan: Work~!" + p + " Work till you sweat~!!" + p + " Support Hiho-ko for life~!!",
        "Hee-Ho-kun: It's cold..."
    ],
    1: [
        "Hiho-ko-chan: Going up? Hmm~ Well, good luck I guess.",
        "Hee-Ho-kun: Come to think of it, Hee-Ho! I saw a girl wearing a weird mask on the upper floor!",
        "Hiho-ko-chan: She was saying something dangerous~ Like she'd smash the school or something~",
        "Hee-Ho-kun: That's bad, Hee-Ho! If the school gets smashed, what'll we do?",
        "Hiho-ko-chan: Work~!" + p + " Work till you sweat~!!" + p + " Support Hiho-ko for life~!!",
        "Hee-Ho-kun: It's cold..."
    ],
    2: ["Hee-Ho-kun: Let's trade the Ambrosia you have for a Sealing Gear!"],
    3: "=Want to hear how?<FF03><FF0E>　<FF01>",
    4: [
        "Hee-Ho-kun: Hee-Ho! Huh? You have something good!",
        "Hiho-ko-chan: Hee-ho!! Really. You have Ambrosia.",
        "Hee-Ho-kun: Nice, nice! I want some too!!",
        "Hiho-ko-chan: Hey, hand it over! Hand it over!!",
        "Hee-Ho-kun: Um" + p + " ..." + p + " Hiho-ko-san, the teacher said grabbing things is wrong...",
        "Hiho-ko-chan: Hmm~ Humans are hard~ Then how about a trade?",
        "Hee-Ho-kun: Hee-Ho!! Let's trade the Ambrosia you have for a Sealing Gear!"
    ],
    5: [
        "Hiho-ko-chan: Apparently good things happen if you fuse a Sealing Gear with a demon.",
        "Hee-Ho-kun: I have five Sealing Gears. There are five of you.",
        "Hiho-ko-chan: One each, by the numbers.",
        "Hee-Ho-kun: Consider how many Ambrosia you have, and decide whose Sealing Gear to get.",
        "Hiho-ko-chan: Once decided, talk to the human who will get the Sealing Gear.",
        "Hee-Ho-kun: If you want your own Sealing Gear, talk to us!",
        "Hiho-ko-chan: Phew. Talking a lot is tiring~"
    ],
    6: ["Hee-Ho-kun: Hee-Ho!"],
    7: "=Trade for your Sealing Gear?<FF03><FF0E>　<FF01>",
    8: ["Hiho-ko-chan: Are you sure?"],
    9: "=No regrets?<FF03><FF0E>　<FF01>",
    10: [
        "Hee-Ho-kun: Hee-Ho!! Then it's a trade! Here, the \"Rosetta Stone\"!"
    ],
    11: ["Obtained the \"Rosetta Stone\""],
    12: ["Hee-Ho-kun: Then talk to the person you want to trade with!!"],
}

if __name__ == '__main__':
    for n, d in ((149, E149), (150, E150), (160, E160)):
        apply('E1', n, d, {})
