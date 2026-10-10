"""E1 entries 98-112 - Yuriko's treasure chests, Cerberus, Tartarus entrance."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

p = P('ほ')

E98 = {
    13: [
        "Nanjo: There are two kinds of traps. One is for surely killing the target.",
        "Nanjo: The other is to toy with the target and gradually instill fear.",
        "Nanjo: Yuriko's trap is surely the latter."
    ],
    14: [
        "Brown: This tower's traps are really nasty! A straightforward guy like me is in danger all over!",
        "Brown: No, seriously."
    ],
    15: [
        "Elly: For that Yuriko, this tower's Traps are a Game.",
        "Elly: Every time we advance, she hurts us just short of death, and sometimes even prepares a Gift, you see.",
        "Elly: Yuriko intends to Genocide us at the Last of the Game she hosts."
    ],
    16: "=Open this chest?<FF03><FF0E>　<FF01>",
    17: [
        "Ayase: Kyaaah?! Something... something is draining out of my body!"
    ],
    18: [
        "Yuriko: Ahahahahaha! Too bad, so sad!",
        "Yuriko: Well, as a penalty, I'll take your other self! Bye-bye!"
    ],
    19: [
        "Ayase: Kyaaah! What the heck! What the heck! What a cowardly jerk!",
        "Ayase: So frustrating! Ayase can't use her Persona anymore! What do I do!?"
    ],
    21: [
        "Ayase: Yay! Bingo!! Jackpot!",
        "Ayase: See, see, like Ayase said, just open the box and it was correct, right right?"
    ],
    22: [
        "Yuriko: Hmm, you seem to have good bad luck at least! OK! You win this game! Congrats!",
        "Yuriko: My room is just a little farther, so do your best!",
        "Yuriko: I'll give you a really lovely \"death.\" Well, I'll be waiting!"
    ],
    24: ["You decided not to open this chest."],
    25: ["The chest is empty."],
    26: ["Some kind of force is at work, so the chest cannot be opened."],
    27: [
        "Heh heh heh... What a pity. Time's up...",
        "Your desperate struggling was a perfect sideshow to make the arrival of the \"Eternal Night\" even more splendid.",
        "But the opening act ends here.",
        "Now the climax called the \"Eternal Night\" raises its curtain."
    ],
    28: [
        "Yukino: Wh-" + p + " Hey hey! What's started!? Don't tell me that Yuriko!",
        "Yukino: Did she cut the tower's time limit short as a \"penalty\"? What do we do! Ayase!!",
        "Yukino: You..." + p + " When you opened this chest, you said it! \"I'll take responsibility\"!",
        "Yukino: What do we do! That's why I said \"better not touch it\"!"
    ],
    29: [
        "Ayase: Eh? Ayase?" + p + " Is it Ayase's fault? No way?? Wait a sec!",
        "Ayase: Surely..." + p + " Ayase didn't think it'd turn into such a big deal...",
        "Ayase: Hee hee... I said \"I'll take responsibility\" on momentum, but...",
        "Ayase: Actually, Ayase didn't think about anything! It's Yuriko's fault... Ayase isn't to blame..."
    ],
    30: [
        "Yuriko: ...Kya ha... Kyahahahahahaha! Kyaaa hahahaha...",
        "Yuriko: Time's uuup! Game oooover! Just kidding!",
        "Yuriko: How?" + p + " How? Surprised, weren't you??",
        "Yuriko: Yuriko-chan's impression of the \"Snow Queen\" deserves an Academy Award, right? Kyahahahaha!",
        "Yuriko: You fell for it!" + p + " You fell for it! It's a joke" + p + " you know! Ahh, so fun!!",
        "Yuriko: Did you think it was over? Too bad! There's no \"mirror fragment\" in this chest" + p + " you know!",
        "Yuriko: See ya! Bye-byeee!"
    ],
    31: [
        "Ayase: Ayase is, like, so frustrated!! Aaah, geez!! Like, totally tricked!?",
        "Ayase: <FF0F>あ!! Why didn't you open the left chest! Take responsibility!",
        "Ayase: It's your fault! Ayase isn't to blame!"
    ],
}

E99 = {
    0: ["Yukino: What's this? It looks different from the rooms so far."],
    1: [
        "???: WHAT DID YOU COME HERE FOR? HUMANS... DID YOU COME HERE KNOWING THAT THIS IS THE ENTRANCE TO THE UNDERWORLD",
        "AND THAT I AM CERBERUS, THE WATCHDOG?"
    ],
    2: [
        "Nanjo: What is this beast? Does it intend to get in our way? If so, no mercy!"
    ],
    3: [
        "Brown: What's this guy? Trying to block my path? He's cocky.",
        "Brown: But he looks strong. Let's try \"talking\" for now! Ahem...",
        "Brown: \"Me in bad mood. Nuh, get out of way.\" Just kidding."
    ],
    4: [
        "Ayase: Hey, hey, Ayase and the others don't really plan to fight you.",
        "Ayase: We just wanna go past here, like. Is that no good?"
    ],
    5: [
        "Cerberus: Hmph. Beyond here is the world of death. A world where the souls of the dead gather.",
        "Cerberus: Can you have any business with you lot?"
    ],
    6: [
        "Nanjo: \"The world of the dead,\" is it? How interesting. This tower itself is already a \"hell\" where demons gather.",
        "Nanjo: We have nothing to fear anymore. And the secret of the Persona power we lost in the candle room is likely here.",
        "Nanjo: When Yuriko said then, \"I took your other self's life,\" she was referring to the loss of our Persona power.",
        "Nanjo: \"Taking life\" means \"death,\" the \"death of the other self\"... And this is the \"land where souls of the dead gather\"!",
        "Nanjo: Heh. It is obvious our \"other selves' souls\" are here!",
        "Nanjo: Hey, mutt! You are stalling us on Yuriko's orders, are you not? Let us through!"
    ],
    7: [
        "Elly: Heh heh. The secret of the Persona lost in the candle room earlier is likely here.",
        "Elly: When Yuriko said then, \"I took your other self's life,\" she was referring to the loss of our Persona.",
        "Elly: \"Taking life\" means \"death,\" the \"death of the other self,\" and this is the \"land where souls of the dead gather\"...",
        "Elly: Our \"other selves' souls\" are likely here.",
        "Elly: Hey! Cerberus!! You are stalling us here on Yuriko's orders, are you not?",
        "Elly: Quietly let us through! Otherwise..."
    ],
    8: [
        "Cerberus: Sharp intuition you have. That deduction is half right, half wrong.",
        "Cerberus: Indeed, the Personas you speak of are here. But I have nothing to do with Yuriko.",
        "Cerberus: I guard here by my own wish. The half-baked souls of the dead are not needed in the world of the dead I guard.",
        "Cerberus: Take them away as you please."
    ],
    9: [
        "Yukino: Got it. We'll go through. We won't lay a hand on you either."
    ],
    10: ["Yukino: The world of the dead, huh. Never thought I'd be going there while alive."],
    11: ["Ayase: It's kinda scary, the world after death!"],
    12: ["Nanjo: Not a place one wants to go willingly. Unless one has business, that is."],
    13: [
        "Brown: Whoa! The afterlife! When we get back, let's go on TV!",
        "Brown: \"Uesugi Saw It!! This Is the World After Death!\" Just kidding!",
        "Brown: Dehyahyahyahya!!"
    ],
    14: ["Elly: Hell, is it? How Lucky to see it while still alive!"],
    15: [
        "Cerberus: The demons of Tartarus are stronger than those of the tower.",
        "Cerberus: They hate the living, so be careful."
    ],
    17: "=Go to Tartarus?<FF03><FF0E>　<FF01>",
}

E112 = {
    0: [
        "Yukino: Even if it's my own, seeing it like this is strange. Personas, I mean."
    ],
    1: [
        "Ayase: When they said the afterlife, I thought it'd be scarier, but it's no big deal."
    ],
    2: [
        "Nanjo: A place where souls of the dead gather. Not a pleasant place, but in a sense also a solemn one.",
        "Nanjo: I feel as if my body is tightening."
    ],
    3: [
        "Brown: When I die, I'm 100 percent going to heaven! So this will be my last look at the scenery of the \"afterlife\"! Yeah yeah."
    ],
    4: [
        "Elly: It is a little different from the Image of Hell that we imagine. This place."
    ],
    5: [
        "Mariko: What is this place? On the surrounding walls, something like your spirit bodies appears now and then!",
        "Mariko: I took pictures perfectly, so I'll give them to you after developing! You rarely get a photo of your own ghost!"
    ],
    6: ["Your own Persona is here."],
    7: "=Return the Persona to yourself?<FF03><FF0E>　<FF01>",
    8: ["The lost power of the Persona is revived within you..."],
    10: ["Yukino's Persona is here."],
}

if __name__ == '__main__':
    for n, d in ((98, E98), (99, E99), (112, E112)):
        apply('E1', n, d, {})
