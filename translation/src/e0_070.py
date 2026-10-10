"""E0 entry 70 - Kurouri in the library; the black door."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: [
        "Kurouri: So you are the new visitors. I have heard about you from Naito-kun.",
        "Kurouri: You seem to be having a precious experience. I am most envious."
    ],
    1: ["Mark: ...Is that really Kurouri? He's talking normal, man!"],
    2: ["Elly: He is speaking normally... Are you truly Akuma-kun?"],
    3: ["Brown: Hey, where's your usual \"Hehehe\"? That's not very Akuma-kun of you!"],
    4: ["Ayase: Hey, with that face, don't talk so normally! It's even creepier!"],
    5: [
        "Kurouri: Hmm... The me on the other side must be quite a strange man.",
        "Kurouri: I would like to meet him once."
    ],
    6: ["Everyone: ..........."],
    7: ["Kurouri: Hmm, shall we get to the main subject, visitors?"],
    8: [
        "Nanjo: I hear you have been investigating the two worlds. What are your thoughts?",
    ],
    9: [
        "Kurouri: Every phenomenon in this world, though seemingly unrelated, is tied together by threads of causality.",
        "Kurouri: This black door that suddenly appeared is no exception. Only one who follows those threads can know the truth.",
        "Kurouri: And unfortunately... that does not seem to be my role."
    ],
    10: ["Nanjo: Our coming here was inevitable, and exposing everything falls to us... Is that it?"],
    11: [
        "Kurouri: I do not know who spun the thread, but think of it so.",
        "Kurouri: Now then, what is the name of the one who holds the end of the thread you must follow?"
    ],
    12: ["Maki: Kandori" + P('キ') + " Takahisa..."],
    13: [
        "Kurouri: Hmm, the name I was told. In fact, I knew beforehand that this incident would happen.",
        "Kurouri: It was a prophecy from a certain gentleman I met at the shrine..."
    ],
    14: ["Mark: A monkey gentleman? There ain't no gentleman or whatever in a monkey!!"],
    15: ["Nanjo: Enough! Somebody shut that monkey up!"],
    16: ["Mark: Ah! You bastard~! You bib-wearing freak!"],
    17: ["Reiji: ........." + P('キ') + " What a noisy bunch..."],
    18: ["Elly: Shut up! Stop it, both of you!"],
    19: ["Ayase: Yay~! Monkey, monkey!"],
    20: ["Brown: The monkey gentleman must be Mark's uncle or something!"],
    21: ["Maki: Hey, hey, Kurouri-kun. Was that a man in a mask?"],
    22: ["Kurouri: Y-Yes... He called himself Philemon... But more importantly, is this all right?"],
    23: [
        "Maki: It's fine, it's fine. This is how it always is!",
        "Maki: <FF07>あ-kun, let's go to Araya Shrine.",
        "Maki: I've met that man before, and he might know where Kandori is!"
    ],
    24: ["Maki: This door... It gives me a bad feeling..."],
    25: ["Mark: Damn it! I'll settle this someday!"],
    26: ["Nanjo: Honestly! Because of that fool, I forgot what I was going to ask!"],
    27: ["Reiji: ..." + P('で') + " I said don't mess with me."],
    28: ["Elly: The demon-kun of this world seems reliable. His appearance is a problem, though."],
    29: ["Brown: Akuma-kun, huh... This is funny in its own way, but it throws me off."],
    30: ["Ayase: Huh~? We're leaving already? You're the first guy to drag Ayase around this much."],
    31: [
        "Kurouri: With your vitality, you should be fine whatever difficulties you meet.",
        "Kurouri: You are a bit noisy, though..."
    ],
    32: [
        "Yosuke: Araya Shrine is in the same place as in our world. Please find some way to get back.",
        "Yosuke: And..." + P('で') + " if you happen to meet Chisato, please help her. I'm begging you."
    ],
    33: ["An eerie heartbeat can be heard from beyond the door..."],
    34: [
        "Kurouri: You seem curious. This door appeared suddenly at the same time as the disturbance a month ago.",
        "Kurouri: I have tried many things, but it will not budge.",
        "Kurouri: Well, if the threads of causality guide us, the door will open eventually."
    ],
    35: [F6('い') + "Kurouri Tsutomu<FF03>An occult maniac who is always wrong...<FF03>or so he should be..." + F6(0)],
}
REVIEW = {14: "サルの紳士 - Mark hears Philemon as monkey (Saru)", 16: "ヨダレかけ男 = bib man (Kurouri's drool bib)", 22: "Philemon name", 35: "card ending code check"}

if __name__ == '__main__':
    apply('E0', 70, BOXES, REVIEW)
