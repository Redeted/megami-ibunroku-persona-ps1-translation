"""E0 entry 144 - arrival back in the original world; Dr. Nicolai brainwashed."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Maki: Ugh... I feel sick~"],
    1: [
        "Mark: Bl..." + P('キ') + " Bleeeeargh! I got motion sick... <FF0F>あ,",
        "Mark: you're surprisingly tough..."
    ],
    2: [
        "Nanjo: *Cough*..." + P('キ') + " It is probably because of the forced transfer. We are lucky to have arrived in one piece."
    ],
    3: ["Reiji: Tch..." + P('で') + " What's wrong, Inaba... Pathetic."],
    4: ["Mark: ...Tch! Look in a mirror, Reiji. You're pale as a ghost. What are you, a zombie?"],
    5: [
        "Reiji: Heh... If you can joke, you're fine...",
        "Reiji: We don't have time to dawdle."
    ],
    6: ["Mark: Can you stand, Sonomura?"],
    7: ["Maki: Mm..."],
    8: ["Maki: Up we go!" + P('で') + " I'm fine now."],
    9: ["Nanjo: <FF0F>あ, that scientist is there."],
    10: ["Dr. Nicolai: Ugh... M-My head..."],
    11: ["Mark: Old man, you're alive!"],
    12: ["Maki: Something's wrong with him!"],
    13: [
        "Dr. Nicolai: Ugh..." + P('で') + " A HAMMER OF JUDGMENT UPON FOOLISH HUMANITY!",
        "Dr. Nicolai: HUMANITY NEEDS NO FUTURE!"
    ],
    14: [
        "Dr. Nicolai: DESTRUCTION! EXTINCTION!",
        "Dr. Nicolai: PERISH PERISH PERISH PERISH PERISHHH!! A HAMMER UPON HUMANITY!",
        "Dr. Nicolai: THE SONG OF PERDITIOOOOOOOON!"
    ],
    15: [
        "Mark: What the hell happened to you! Saying stuff like Kandori...",
        "Mark: Old man!"
    ],
    16: [
        "Kandori: That man is no longer anything more than my alter ego." + P('ヌ') + " No...",
        "Kandori: By now, people all over the world likely wish for humanity's extinction, just as I do."
    ],
    17: ["Maki: Kandori!?"],
    18: ["Mark: You bastard, what does that mean!"],
    19: ["Nanjo: You... With that mirror, you brainwashed the whole world's humanity!?"],
    20: ["Elly: Jesus... What a thing to do!"],
    21: ["Brown: What did you say!?"],
    22: ["Ayase: N-No way!?"],
    23: [
        "Kandori: All humans acting under a unified ideology... Do you not think it wonderful?",
        "Kandori: A feat no ruler could ever accomplish, I have achieved. I have transcended humanity."
    ],
    24: ["Nanjo: Nonsense!"],
    25: [
        "Kandori: Now just a single word, ordering them to kill one another, and it will be over...",
        "Kandori: A fitting end for foolish humanity. Nothing else will be harmed... Only humans will vanish from this planet."
    ],
    26: ["Maki: Why!? Why do you want to erase people!?"],
    27: ["Kandori: Heh... I would not think those words were yours..." + P('キ') + " Sonomura" + P('で') + " Maki-kun."],
    28: ["Maki: How do you know my name...!?"],
    29: [
        "Kandori: The mirror's power reaches all people. Even you are no exception.",
        "Kandori: Can you reach me? Heh heh..."
    ],
    30: ["Reiji: Bastard!!" + P('で') + " Let's go, <FF0F>あ."],
    31: ["Elly: Wait!"],
    32: ["Elly: Let us go, <FF07>あ!"],
    33: ["Brown: Wait up, you coward!!"],
    34: ["Brown: Dammit~ Everyone, follow me!"],
    35: ["Ayase: Wait just a minute!"],
    36: [
        "Ayase: <FF0F>あ! What are you spacing out for?",
        "Ayase: If we don't hurry, Ayase's future will be gone! Chase him already!"
    ],
    37: ["Mark: Sonomura, Elly, can you stand?"],
    38: ["Maki: Elly, are you okay?"],
    39: ["Elly: Ugh..." + P('で') + " Thanks, Maki. I am fine now."],
    40: [
        "Mark: Pathetic, Uesugi. Ain't you the leader? Get it together."
    ],
    41: [
        "Brown: I-I know that! I was just playing along! I'm fine, just watch!",
        "Brown: Nnnngh!"
    ],
    42: [
        "Brown: How's that! Leader is da Leader! Say it! Just kidding."
    ],
    43: ["Maki: Hee hee. Uesugi-kun is funny."],
    44: [
        "Brown: Right? Right? A super handsome guy with both looks and a sense of humor!",
        "Brown: My rival is Nakai of ZMAP! That knit-cap guy somewhere is nothing, nothing!",
        "Brown: Maki-chan, you get it~"
    ],
    45: ["Mark: What a simple guy..."],
    46: ["Nanjo: Well, as the saying goes, even a fool or a pair of scissors can be put to use."],
    47: ["Maki: Oh! There's someone! Ah, it's that old scientist."],
    48: ["Maki: Yuka, are you okay?"],
    49: ["Ayase: Urp!" + P('で') + " Bleeeeeeeh"],
    50: ["Mark: That's gross, hey."],
    51: ["Ayase: Shut up... Ayase's is clean!"],
    52: ["Maki: Here, Yuka, a handkerchief."],
    53: ["Ayase: ..." + P('で') + " Thanks, Sonomura."],
    54: ["Nanjo: For now, everyone seems all right."],
    55: ["Mark: That bastard... The crazy things he comes up with!"],
    56: [
        "Maki: Why..." + P('キ') + " Why does Kandori know me!?"
    ],
    57: [
        "Nanjo: ..." + P('で') + " I see. So that is how it is..." + P('キ') + " What a thing..."
    ],
    58: [
        "Reiji: ..." + P('で') + " Knowing that bastard, who knows what filthy tricks he's prepared..." + P('キ') + " Be careful."
    ],
    59: [
        "Elly: Kandori's last words bother me... And I have a headache...",
        "Elly: <FF07>あ..." + P('キ') + " Please do not do anything reckless," + P('で') + " okay?"
    ],
    60: ["Brown: Kandori! No brainwashing allowed! ...Get it? Hah."],
    61: ["Brown: <FF08>あ, this is where you laugh! Laugh, laugh! Dahahahaha..."],
    62: ["Brown: What... I'm not putting on a tough act or anything!"],
    63: ["Ayase: Hey, <FF0F>あ~, don't you have a headache?"],
    64: [
        "Dr. Nicolai: THE HOUR OF FINAL JUDGMENT! WHY WAS HUMANITY BORN?",
        "Dr. Nicolai: WE WHO CANNOT ANSWER THAT SHOULD PERISH!"
    ],
    65: [
        "Mark: Damn! Doesn't look like it's here!",
        "Mark: Where the hell did you go, Sonomura!"
    ],
    66: [
        "Nanjo: ........." + P('キ') + " To think such a system opens a path into people's hearts.",
        "Nanjo: As long as it exists, nothing good will come of it. We must destroy it at all costs."
    ],
    67: [
        "Reiji: ...That Sonomura. If we don't hurry, it'll be too late. Judging by how she looked."
    ],
    68: ["Elly: Shit! It is not here! We must hurry and search!"],
    69: ["Brown: Aargh, not here either! Where'd she go, Maki-chan?"],
    70: [
        "Ayase: Wrong! It's not here! Geez, why'd we come to a place like this?"
    ],
    71: [
        "Dr. Nicolai: Ugh... What on earth was I doing...?",
        "Dr. Nicolai: What! Such a thing!? I see... It seems I have done something terrible to you all.",
        "Dr. Nicolai: I too have a request. Please, by all means, save Sonomura's daughter.",
        "Dr. Nicolai: I will adjust the system and do everything to be able to go to her aid at any time!",
        "Dr. Nicolai: Afterward... I intend to accept any judgment. I beg you, boy!"
    ],
    72: [
        "Maki: <FF07>あ-kun! Where are you going!?",
        "Maki: We have to beat Kandori quickly!"
    ],
    73: [
        "Mark: <FF0F>あ! Where are you going!?",
        "Mark: Ain't you gonna save Sonomura!?"
    ],
}
REVIEW = {}

if __name__ == '__main__':
    apply('E0', 144, BOXES, REVIEW)
