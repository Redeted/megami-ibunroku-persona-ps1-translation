"""E1 entries 96-98 - Tower of Thanatos: Yuriko."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

p = P('ほ')

E96 = {
    0: ["Yukino: Suddenly in a weird place. What's this skeleton room?"],
    1: [
        "???: Yahoo! Everyone! Nice to meet you!! Welcome to my \"Tower of Thanatos\"!!",
        "???: Everybody! Are you having fun?! I'm everyone's idol,",
        "???: \"Yamamoto Yuriko\"-chan!! Nice to meet you!!"
    ],
    2: [
        "Nanjo: What kind of joke is this?? It may be none of my business, but please use proper Japanese.",
        "Nanjo: It is truly unpleasant."
    ],
    3: [
        "Brown: Yeaaah!! Y!" + p + " U!" + p + " R!" + p + " I!" + p + " K!" + p + " O! Yuriko" + p + "-chan!",
        "Brown: ..." + p + " ..." + p + " ..." + p + " ..." + p + " ..." + p + " ..." + p + " ..." + p + " ..." + p + " ..." + p + " ..." + p + " ...Wrong, what am I doing! Dammit! I got carried away!"
    ],
    4: [
        "Ayase: What? This airheaded girl? And she talks weird too. You're like, super weird!"
    ],
    5: [
        "Yuriko: Geez, what!? This weird girl!? Aah! Is it jealousy because Yuriko is cute?",
        "Yuriko: Being too cute is a bit of a sin" + p + ", huh" + p + "!",
        "Yuriko: Sorry, for being so cute! Kyahahahaha!!"
    ],
    6: [
        "Nanjo: ..." + p + " ..." + p + " ..." + p + " What is this!? What did you come out for!? We are in a hurry!",
        "Nanjo: So?" + p + " Are you saying you want to cross swords here?! We do not mind at all!"
    ],
    7: [
        "Elly: Oh..." + p + " No... What did you come out for? You?",
        "Elly: Are you saying you want to cross swords here? We do not mind at all."
    ],
    8: [
        "Yuriko: Geez, don't say such scary things, no no! I'm just gonna tell you how to open the door at the back of this room!",
        "Yuriko: So listen well! Yuriko-chan's How-to-Open-the-Door Lecture, just kidding!",
        "Yuriko: See, see, there are two candles on both sides of the door, right? If you put out the flame of either one, the door will open!",
        "Yuriko: So do your best and come to me! Bye-bye!"
    ],
    9: [
        "Yukino: Somehow... however I think about it, it smells like a trap.",
        "Yukino: She might be a pretty hard opponent to deal with, that Yuriko..."
    ],
    10: [
        "Yukino: I don't like this. The atmosphere of this tower... I can't put it well, but..."
    ],
    11: [
        "Yukino: Damn! We got had!! That Yuriko woman!",
        "Yukino: She looks like an idiot, but she's quite the schemer!"
    ],
    12: [
        "Ayase: What is she!? That airheaded girl? She's, like, super making light of life!! Like, super making light of people!! She really pisses me off!!"
    ],
    13: [
        "Nanjo: Honestly... Ayase alone being noisy is more than enough, and now the enemy boss is like that. This bodes ill."
    ],
    14: [
        "Brown: Hey, hey, between us, Yuriko-chan was pretty cute, wasn't she!!"
    ],
    15: [
        "Elly: What is frightening about that woman Yuriko is that I cannot tell what she is thinking.",
        "Elly: It seems she enjoys fighting us Battle and snaring us in Traps.",
        "Elly: As Yukino says, she seems to be an opponent who cannot be dealt with by the straightforward approach."
    ],
    16: "=Put out the candle's flame?<FF03><FF0E>　<FF01>",
    17: [
        "Yukino: Ugh?! W-" + p + " What" + p + " is this? My bod-" + p + " body... something is draining out of me" + p + "!",
        "Yukino: Waaaah!! Aaaaaah!!"
    ],
    18: [
        "Yuriko: Yay yay! You fell for it! You fell for it! Kyahahahahaha! Did you think you could pass for free?!",
        "Yuriko: Life is \"give and take\"! If you want to do anything in this tower, you have to give Yuriko-chan something! No no!",
        "Yuriko: Life is harsh, you know! So I've definitely taken your other self's life,",
        "Yuriko: Per-" + p + " son-" + p + " a-" + p + " " + p + " ...Bye bye! Kyahahahahaha!"
    ],
    19: [
        "Yukino: Damn it! What the hell!? That woman!! What is it? \"Took your other self's life\"? What does that mean?"
    ],
    22: ["You decided not to put out the candle's flame."],
    23: ["The candle is not lit."],
    24: ["The candle is lit."],
    25: ["It seems the door will not open unless you put out the flame of one of the candles."],
    26: ["The door now opens freely."],
    27: "=Open the door?<FF03><FF0E>　<FF01>",
}

E98 = {
    0: [
        "Yukino: What an obviously suspicious room. Only two treasure chests at the back of the room.",
        "Yukino: Surely it's a trap like the candle room. Let sleeping gods lie, as they say. Let's not touch them."
    ],
    1: [
        "Yuriko: Aww, how mean, how mean! Yuriko prepared a present for everyone who's working so hard, and you're ignoring it and leaving? No no~"
    ],
    2: ["Nanjo: Hmph. How transparent. It is surely a trap. Mayuzumi, do not engage."],
    3: [
        "Brown: P-Present? Y-Yukino-san, let's take it!",
        "Brown: They've always said, \"there's no villain among beautiful people,\" right? Let's trust Yuriko-chan!"
    ],
    4: [
        "Ayase: Hmm. It sounds like a trap, but it seems fun. It'd be kinda frustrating to run away here.",
        "Ayase: Ayase will at least hear her out!"
    ],
    5: [
        "Yuriko: Yippee! As expected of the girl who gets me best, you understand! Yuriko is happy!"
    ],
    6: ["Nanjo: Spare the nonsense. State your business. Your tone is unpleasant."],
    7: ["Elly: It is surely not a proper Gift. Listening is a waste."],
    8: [
        "Yuriko: Geez! Everyone's so not honest! You're happy, aren't you! Well, fine. Here goes the present explanation! Listen well!",
        "Yuriko: In one of these two treasure chests, there's the \"mirror fragment\" everyone loves!",
        "Yuriko: Yuriko-chan is generous enough to give you the chance to get it for free!",
        "Yuriko: But! There's only one chance! Of course, if you open the wrong chest, there's a penalty.",
        "Yuriko: How about it? How about it? Interesting, right! Do your best!",
        "Yuriko: Ahahahahahaha"
    ],
    9: [
        "Ayase: So it's a trap after all? But it's a chance! Let's just try it, everyone, like we've been tricked!",
        "Ayase: Ayase somehow feels like she's the only one who isn't lying.",
        "Ayase: Nothing to lose! Ayase will take responsibility! Let's open a chest!"
    ],
    10: [
        "Yukino: That Yuriko! She's toying with our lives in the palm of her hand! What an awful woman!"
    ],
    11: [
        "Ayase: I wonder why. That Yuriko girl seems like she's trying really hard. Ayase feels like that."
    ],
    12: [
        "Ayase: Kyaaah! That Yuriko is such a coward! Ayase is super mad!!"
    ],
}

if __name__ == '__main__':
    for n, d in ((96, E96), (98, E98)):
        apply('E1', n, d, {})
