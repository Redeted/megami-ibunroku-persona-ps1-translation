"""E0 entry 42 - Fake Maki at the school; Nanjo asks for help rescuing Mark from the police."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: [
        "Ayase: Hey, hey, <FF0F>あ! Kirishima went outside again, you know?",
        "Ayase: Ayase tried to stop her, but, like, you know she never listens, right? It's such a pain~",
        "Ayase: Is there really any place where you can get out of the town, for real?"
    ],
    1: ["Ayase: Heyyy. Are you guys serious? What can three people even do?"],
    2: ["Himeno: U-um... I think Mayuzumi-san is somewhere in the school. She said she was going to look for something to fill the hole..."],
    3: [F6('う') + "Himeno Yuko<FF03>Maki's friend. A plucky girl who<FF03>works part-time for the budget." + F6(0)],
    4: [
        "Ayase: Hey, if we fill this in, is this place really safe? Huh? Filling it in is cancelled?",
        "Ayase: Is that okay? Not filling it in?"
    ],
    5: ["Himeno: U-um... Be careful..."],
    6: ["Ayase: Heyyy. You're going too, <FF0F>あ?"],
    7: "=You mean to beat SEBEC, right?<FF0E>は<FF01>",
    8: ["Ayase: It's impossible, I'm telling you~ Stop it~"],
    9: ["Ayase: Oh, what, not that? Like, I guess it feels like we've at least gotta do something about the school, right~"],
    10: ["Maki: Oh! Yo, <FF07>あ-kun! What are you all doing?"],
    11: ["Himeno: Ah..." + P('で') + " Maki" + P('で') + "-chan...?"],
    12: ["Ayase: Huh?" + P('で') + " ...Could it be... Sono..." + P('で') + "mura?"],
    13: [
        "Maki: Could it be, nothing! Anyone can see it's everybody's idol, Sonomura Maki-chan, isn't it?",
        "Maki: What's wrong, Yuka?"
    ],
    14: ["Ayase: Nooo! <FF0F>あ, this one is weird! There's no way Sonomura would be this cheerful, right!?"],
    15: ["Maki: Yuka, what's wrong with you?" + P('キ') + " Huh? When did a hole like that open up? Ahh, it's <FF07>あ-kun's doing!"],
    16: ["Ayase: See, see? She's definitely weird! Besides, weren't you in the hospital!?"],
    17: ["Maki: Yuu-ukaa... If you don't knock it off, I'll get mad! Do you want to put me in the hospital that badly?"],
    18: ["Himeno: U-um..." + P('ょ') + " I think she's the real Maki-chan..."],
    19: ["Ayase: How can you even say that!? She's got to be a demon or something!"],
    20: ["Himeno: Ah..." + P('で') + " I'm sorry. But she has the compact that Maki-chan treasured, so..."],
    21: [
        "Maki: Hey, Yuka! Stop bullying Yuko!",
        "Maki: But Yuko... don't you seem different somehow?"
    ],
    22: ["Nanjo: <FF0F>あ! Wh-what!? Why is Sonomura here?"],
    23: ["Maki: Geez! Not you too, Nanjo-kun! Quit joking around! By the way, what's wrong? Why the panic?"],
    24: [
        "Nanjo: How rude. I am calm!" + P('ょ') + " In truth, that idiot... Inaba was captured by a demon at the police.",
        "Nanjo: He said we should get a weapon, so I went along with him, and this is what I get...",
        "Nanjo: Ordinarily I would leave him be, but that \"security card\" is in his possession.",
        "Nanjo: Lend a hand in the rescue."
    ],
    25: ["Maki: Inaba-kun was caught by a demon!? <FF07>あ-kun! We've got to go save him!"],
    26: [
        "Nanjo: This is the gun. It seems that invoking a Persona consumes quite a lot of spirit.",
        "Nanjo: Inaba was exhausted by that and captured. If one is prepared, there is nothing to fear.",
        "Nanjo: Do not forget to equip it."
    ],
    27: ["Maki: Persona...? I don't really get it, but whatever. Let's hurry and go!"],
    28: ["Maki: That Girl in Black again, huh... I've got to teach her a lesson! <FF07>あ-kun, let's hurry and go!"],
    29: ["Nanjo: <FF0F>あ, have you ever been to the police? It is in 3-chome, north of here."],
    30: ["Nanjo: <FF0F>あ! We do not have time to dawdle. Let us hurry."],
}
REVIEW = {
    7: "Japanese prompt is the fixed text of the yes/no choice (param glyph kept); Ayase asks if they are going to beat SEBEC",
    10: "Maki's greeting オッス rendered as 'Yo'; <FF07>あ君 kept as <FF07>あ-kun (name token + -kun)",
    24: "警察 here means the police station/building (box 43/3 explains it); kept literal 'the police' to match Maki's question in entry 43",
    29: "警察 kept literal 'the police' (see 24)",
}

if __name__ == '__main__':
    apply('E0', 42, BOXES, REVIEW)
