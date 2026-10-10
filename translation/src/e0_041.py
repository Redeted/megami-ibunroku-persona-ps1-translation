"""E0 entry 41 - Snow Queen story introduction."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Yukino: Hey, Inaba!<FF03>Wait!"],
    1: ["Ayase: We don't even know if that's<FF03>really Sonomura!"],
    2: ["Ayase: <FF0F>あ!<FF03>Listen to this~ That Inaba<FF03>is acting totally crazy~!"],
    3: [
        "Yukino: Inaba, Uesugi, and Eriko came back bringing an injured Nanjo with them.",
        "Yukino: And then, um..."
    ],
    4: [
        "Ayase: Sonomura came out from the school building. Isn't she in the hospital?",
        "Ayase: It's super weird!"
    ],
    5: ["Saeko-sensei: Inaba came back!?"],
    6: ["Yukino: Well..."],
    7: ["Saeko-sensei: ...Anyway, Sonomura went out with him too, right? We have to bring them back!"],
    8: [
        "Yukino: Hold on, sensei! If something happened to you now, what would happen to the rest of us?",
        "Yukino: We'll go!"
    ],
    9: ["Saeko-sensei: Well said, Mayuzumi!" + P('み') + " Thank you."],
    10: [
        "Saeko-sensei: Oh? <FF0F>あ," + P('み') + " what are you holding...?",
        "Saeko-sensei: That's..." + P('み') + " that mask...!!" + P('ょ') + " I see," + P('み') + " it was" + P('た') + " still here..." + P('み') + " Such a thing..."
    ],
    11: [
        "Saeko-sensei: Looking at this..." + P('ぎ') + " it reminds me of" + P('な') + " my high school days...",
        "Saeko-sensei: ...It's the mask that I wore when we put on a play called the \"Snow Queen\"."
    ],
    12: ["Ayase: It's a pretty mask, isn't it?"],
    13: [
        "Saeko-sensei: But you see, they say it's a cursed mask.",
        "Saeko-sensei: ...And it's only natural that they do." + P('み') + " Because of it," + P('ゆ') + " my friend..."
    ],
    14: [
        "Ayase: N-No way, sensei~ Don't scare us at a time like this~!",
        "Ayase: That mask is creeping me out. Just throw it away~!"
    ],
    15: [
        "Saeko-sensei: Ah... S-Sorry" + P('な') + " about that! It's just a silly legend, like you'll definitely die if you wear it.",
        "Saeko-sensei: But I wore it too, and I'm still alive and kicking like this, right?",
        "Saeko-sensei: So it's safer for me to be the one to go and bring them back!"
    ],
    16: [
        "Saeko-sensei: See, I have the goddess of luck watching over me." + P('み') + " ..." + P('く') + "..." + P('く') + "?",
        "Saeko-sensei: " + P('た') + "Ah..."
    ],
    17: ["Saeko-sensei: Kyaaah!"],
    18: ["Yukino: ...Sensei! What's wrong?!"],
    19: ["Ayase: Wha- What's happening~?!"],
    20: [
        'Once upon a time, there was a very wicked demon...' + P('み') + ' One day, the demon created a "mirror".',
        'Beautiful things' + P('た') + ' did not reflect well,' + P('た') + ' while ugly things' + P('た') + ' reflected clearly. It was the "Devil\'s Mirror".',
        'The demon tried to play a trick on God with this "mirror" and ascended to the heavens, but on the way, the "mirror" shattered.',
        'The "Devil\'s Mirror" became countless shards and scattered across the earth.' + P('み') + ' That was the beginning of everything.'
    ],
    21: [
        'Once upon a time, there was a boy and a girl who were good friends, named Kai and Gerda.',
        'However, one day, a shard of that "Devil\'s Mirror" entered Kai\'s heart and eye.',
        'Because of the "mirror shard", Kai\'s heart grew cold, and his eyes only saw the bad side of things.',
        'Eventually, he became a boy who even made fun of Gerda, who loved him very much.'
    ],
    22: [
        "One winter day, while it was snowing heavily...",
        "A large white sled appeared before Kai, who was sledding in the square.",
        "Kai was taken away by a beautiful woman riding in the white sled.",
        'In truth, this woman was' + P('み') + ' none other than the "Snow Queen" herself!',
        'And so, Kai was taken away to the "Ice Castle" of the "Snow Queen", far away in the northern world.'
    ],
    23: [
        "Learning of Kai's disappearance, Gerda was stricken with grief, but she resolved to set out on a journey to find him.",
        "Gerda overcame many hardships with the warm cooperation of the people she met.",
        "Gerda's devoted love for Kai and her courage to never give up...",
        '...finally led her to the "Ice Castle".'
    ],
    24: [
        "At the end of her journey, what Gerda saw was Kai, half-frozen and having forgotten even about Gerda.",
        "Gerda's hot tears melted the ice in Kai's frozen heart and warmly enveloped him.",
        "And then, the hot tears shed by Kai, who had returned to his senses through Gerda's tears...",
        '...washed away the "mirror shard" in his eye.',
        'The two of them left the "Ice Castle" hand in hand.',
        "Returning to their hometown, the two lived happily ever after."
    ]
}

if __name__ == '__main__':
    apply('E0', 41, BOXES)
