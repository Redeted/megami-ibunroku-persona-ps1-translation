"""E1 entry 87 - Michiko defeated; Nemesis tower conquered."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

p = P('ほ')

E87 = {
    0: ["Yukino: Hmph! We... won! Want to keep going?"],
    1: [
        "Michiko: I-I, losing! Such... such a thing!!",
        "Michiko: And of all people, to humans like you... Oh!? Why is this happening?",
        "Michiko: Ohh!! Oooh!!"
    ],
    2: [
        "Nanjo: What a noisy woman. That you lost and we won is an undeniable reality.",
        "Nanjo: Making your hideous face even uglier and making a fuss will not change this reality.",
        "Nanjo: A loser should act like one and vanish from our sight at once... No, please vanish. I am begging you."
    ],
    3: [
        "Brown: Aah! Aaah!! Aaaah!!! You're so noisy! Geez, you!!!",
        "Brown: Listen? You got beaten by \"the super cool me and my friends\"!!",
        "Brown: Quit making noise like a sea lion's \"oh, oh\" and vanish from my sight! Okay? Okay?"
    ],
    4: [
        "Ayase: Yeah yeah, exactly, like! A hopeless super-idiot woman like you,",
        "Ayase: Ayase doesn't wanna see your face anymore, like?",
        "Ayase: Mm... I mean, just get lost already!"
    ],
    5: [
        "Michiko: Kyaaaaaah! Kyaaaaaaaaaaah!!",
        "Michiko: What! What!! What!!! What selfish and cruel humans you are!!",
        "Michiko: Five of you ganging up to bully me, who had done nothing, and gloating over it!!",
        "Michiko: Yes! Humans are always like that!! You too! And those on my room's walls, displaying their ugly faces, who bullied me for no reason long ago!",
        "Michiko: Can you understand? Using my excess money to win the seat of the \"Snow Queen\"!",
        "Michiko: Getting expelled a nasty girl who acted like the girlfriend beside the senior in the drama club I admired!",
        "Michiko: Bribing a teacher to bump up my grades a little! That is all I did!!",
        "Michiko: Yet the class idiots abused the frail me, badmouthed me behind my back, and shunned me...",
        "Michiko: The only one who kindly extended a hand to me was the \"Snow Queen's mask\"!",
        "Michiko: Only the \"Snow Queen's mask\" understood my sorrow and my misfortune!",
        "Michiko: Tell me, by what right do humans bully poor me?? Michiko... cannot understand at all!"
    ],
    6: [
        "Nanjo: That is... entirely your own fault!! You... truly threw away your life in the real world for that reason,",
        "Nanjo: and fell to being a lackey of the \"Snow Queen\" and a guardian of this tower?",
        "Nanjo: I am too appalled to speak."
    ],
    7: [
        "Elly: What? That is entirely your fault!! Truly, you... did you throw away your life in reality for such a reason",
        "Elly: and become a subordinate of the \"Snow Queen\"? Unbelievable... You really are quite strange."
    ],
    8: [
        "Michiko: Kyaaaaah!!! Even after hearing my tragic past, which cannot be told without tears,",
        "Michiko: you can still make fun of me? Michiko cannot believe it!",
        "Michiko: Enough!! It was impossible to ask poor-hearted people like you to understand the sorrow of a high-class me!",
        "Michiko: Hmph! Fine!! Just this once I shall let you say you won!!",
        "Michiko: But be prepared... When the thoughts of revenge swirling in my heart toward you are full once again, with time passed!",
        "Michiko: I shall show you hell again! Ohh, remember this!! I shall appear before you again and again!",
        "Michiko: Look forward to that time!! Now, good day! Ohohohohoho! Ohhhohohohohohohohoho!"
    ],
    10: ["Obtained 2 \"Ambrosia\""],
    12: [
        "Yukino: Matsudaira Michiko... If possible, I never want to meet her again.",
        "Yukino: Right! Toro and Kurouri... I wonder if they're okay? In the end Michiko never handed over the key!",
        "Yukino: When we go back to school, let's go check on those two. Now, let's go back!"
    ],
    13: ["The Tower of Nemesis has been conquered!"],
}

if __name__ == '__main__':
    apply('E1', 87, E87, {})
