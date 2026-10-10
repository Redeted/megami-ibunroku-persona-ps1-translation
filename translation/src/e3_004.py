"""E3 entries 4-10 - the clothing shop, apothecary frog, candy shop, scared students, casino."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

p = P('ほ')
H = F6('う') + "*" + F6('　')
HH = F6('う') + "**" + F6('　')

E4 = {
    3: ["Himeno: U-Um... Do you think they'd buy back a uniform?"],
    5: ["Shopkeeper: ...WELCOME..."],
    7: ["Yukino: Nothing but practical clothes. More like armor than clothing."],
    8: [
        "Yukino: Is this shopkeeper from Demon Mountain too, like the weapon shop across the way?"
    ],
    9: ["Ayase: Hey~ This is so cool! " + H],
    10: ["Ayase: Ahh~ Did I gain weight lately~?"],
    11: ["Nanjo: The more expensive, the sturdier it seems."],
    12: [
        "Nanjo: How many times has this shop's armor saved our lives? Even if we are overcharged a bit, I cannot complain."
    ],
    13: [
        "Brown: Hey hey, what's with this shop selling crazy clothes at school! Well, whatever. School rules don't matter now."
    ],
    14: [
        "Brown: Even once the school's back to normal, I'm gonna come to school wearing clothes from here."
    ],
    15: [
        "Elly: Is that Armor? It is somewhat more reassuring than wearing no armor at all."
    ],
    16: [
        "Elly: If we died, their business would dry up. They certainly stock fine goods."
    ],
}

E5 = {
    0: ["Boy Student: Huh~? What's this song~!?"],
    1: [
        "Boy Student: This shop kills the tension. And it's rough outside."
    ],
    2: [
        "Shopkeeper: Hello. Thank you for always looking after my great-grandchild.",
        "Shopkeeper: I'm watching from the afterlife. Uhyahyahyahya"
    ],
    3: ["Shopkeeper: Oh my, it's cold outside, isn't it."],
    4: [
        "Yukino: What's with that old guy? Where's the afterlife, hey? And why's there a pharmacy at school anyway...?"
    ],
    5: ["Yukino: Where did this shop spring up from?"],
    6: ["Ayase: Kyaaah! Frogs!! So pretty~ " + HH],
    7: ["Ayase: I want this frog~ Papa, buy it for me, buy it~ " + H],
    8: ["Nanjo: Why is there a pharmacy...?"],
    9: ["Nanjo: Is this a legitimate shop?"],
    10: ["Brown: Hanajin Z... Looks like it works like crazy."],
    11: [
        "Brown: Maybe I should buy it all up before the school returns to normal. Hanajin Z..."
    ],
    12: ["Elly: Nothing but suspicious medicine... I wonder if it is harmless to the body."],
    13: [
        "Elly: Is there no more decent medicine that fits daily life?"
    ],
    14: [
        "Frog: Talking to a total stranger of a frog, you must be quite idle.",
        "Frog: In honor of that curiosity, I might just give you a sample recommended by Satomi Tadashi."
    ],
    15: [
        "Obtained \"Muscle Drinko\"",
        "Muscle Drinko, the essence of a frog's love.<FF03>Too many syllables."
    ],
    16: [
        "No wa" + p + " y, you seem to have more than me. To ask for even more, you're heartless. You'll surely face judgment after death.",
        "Feel free to die. No, seriously."
    ],
    17: [
        "Just kidding" + p + " You took three and not even one word of thanks?",
        "Surely you haven't" + p + " stolen little medals or travelers' clothes from other people's dressers, have you?",
        "Feel free to die. No, seriously."
    ],
    18: [
        "Frog: Oh my, so pretty~ " + H + "<FF02>An Ayase Yuka impression. No, seriously.",
        "..." + p + " ..." + p + " You're always so quiet. I'm providing laughs, and you look down at me silently with your hand on your hip?",
        "In respect of that unfriendliness, I might just give you a sample recommended by Satomi Tadashi."
    ],
    19: [
        "Obtained \"Hangonkou\"",
        "Hangonkou. Written in kanji it's \"Resurrection Incense.\" Very educational."
    ],
    20: [
        "Just kidding" + p + " After making me give you so much, can't you whisper even a word of love?",
        "You're old enough now, so you should learn a little about the subtleties of the hearts of men and women.",
        "In other words" + p + " frogs are girls. " + H
    ],
}

E6 = {
    0: ["Chemistry Teacher: Quite elaborate for a school festival stall. Impressive, impressive."],
    1: [
        "Chemistry Teacher: Selling expensive things for a school festival. Still, what an old-looking student."
    ],
    6: ["Yukino: Wasn't Senrinmando a penny candy shop?"],
    7: ["Yukino: Strange things for a penny candy shop."],
    8: ["Ayase: Wow! Pretty jewels! Hey Papa, buy it, buy it~ " + H],
    9: ["Ayase: I could look at shiny things all day and never get tired~ " + H],
    10: [
        "Nanjo: What is this shop? Dagashiya? Ah" + p + " you mean the buck-toothed comedian."
    ],
    11: ["Nanjo: Penny candy is odd, is it not?"],
    12: ["Brown: Hey hey, why's there a penny candy shop at school?"],
    13: ["Brown: Come to think of it, this shop's not cold."],
    14: ["Elly: Oh? It is not frozen here. Why is that?"],
    15: [
        "Elly: Only the shops around here seem to be in some other world. It is not cold at all."
    ],
}

E7 = {
    0: [
        "Girl Student: What do we do? There's no exit anywhere. We're trapped!!",
        "Girl Student: Demons will come eventually. Lots of demons will come and torture us to death!!"
    ],
    1: [
        "Girl Student: Even if you beat the Snow Queen, there are still other strong demons left, right!? It's over..."
    ],
    2: [
        "Girl Student: Who was it that said \"school is safe\"? I wanna go home..."
    ],
    3: [
        "Girl Student: Why still can't we get out? Do we just have to wait to freeze to death like this?",
        "Girl Student: I don't want that! I still have so much I want to do!"
    ],
    4: [
        "Satori-chan: It's over. We'll die someday anyway... It just comes a bit sooner, that's all.",
        "Satori-chan: We get to end our lives beautiful, so we should thank the Snow Queen."
    ],
    5: [
        "Satori-chan: Keeping my eyes closed like this, it feels like everything has stopped breathing. It's so quiet.",
        "Satori-chan: Somehow... I'm getting sleepy... it seems..."
    ],
    6: [
        "Yukino: Gloomy bunch. Let's go quick, it's bringing me down too."
    ],
    7: ["Yukino: Still saying stuff like that. It's depressing, let's get out."],
    8: [
        "Ayase: To be honest, Ayase is anxious too. I make jokes, but...",
        "Ayase: Can we really save Saeko-sensei? We're still just high school students! What can we even do!?"
    ],
    9: [
        "Ayase: <FF07>　 is seriously strong, huh. Never says a word of complaint. Ayase respects that."
    ],
    10: [
        "Nanjo: Admitting defeat before acting... I will fight to the end! For my own future, too."
    ],
    12: [
        "Brown: Don't worry! With my burning gaze I'll melt the Queen's heart of ice."
    ],
    14: [
        "Elly: In extreme situations, a glimpse of people's true natures appears. Hee hee..."
    ],
}

E9 = {
    0: [
        "Yukino: Why a casino? Does it mean to run from reality and ruin yourself? Well, the details don't matter. Since we're here, let's play a little."
    ],
    1: [
        "Yukino: Why a casino? Does it mean to run from reality and ruin yourself? Well, the details don't matter. Since we're here, let's play a little."
    ],
    2: ["Ayase: A casino, huh... I'd have preferred a disco, though."],
    3: ["Ayase: Still wanna play~? Let's go already."],
    4: ["Nanjo: What is this place!"],
    5: [
        "Nanjo: You are the one managing the money, so refrain from wasteful spending."
    ],
    6: ["Brown: Uhyahyahyahya! I could stay all day and not get tired!"],
    7: [
        "Brown: Forget the Queen, whoosh! Let's blow off steam once in a while!"
    ],
    8: ["Elly: This is a school, is it not..."],
    9: [
        "Elly: Stretching our wings now and then is fine, but please do not forget our purpose."
    ],
    12: ["Boy Student: Yeah!! I'm on a roll today!!"],
    13: [
        "Boy Student: ...Lost everything. How will I live from tomorrow..."
    ],
    14: [
        "Afro-san: Yeeah! Shubidabada yow~",
        "Afro-san: When I was still catnip, Mom was in maternity.",
        "Afro-san: When I was still a thigh, Dad's wallet was lonely.",
        "Afro-san: Do ya get it~? Dabashubiba yow~"
    ],
    15: [
        "Afro-san: Yeeah! Shubidabada yow~",
        "Afro-san: When I was still self-discipline, my sister was strawberry tanmen.",
        "Afro-san: You wouldn't get it, I bet~ Dabashubiba yow~"
    ],
}

E10 = {
    0: ["Yukino: <FF0F>あ! Be careful..."],
    1: "=Touch the orb of light?<FF03><FF0E>　<FF01>",
    2: ["Ayase: Hey! What did you do, <FF0F>あ!!"],
    3: ["Yukino: Whoa!!"],
    4: ["Yukino: What is this...?"],
    5: ["Yukino: What? I'm mentally prepared. Let's go quick!"],
    6: ["Ayase: Pretty..."],
}

if __name__ == '__main__':
    for n, d in ((4, E4), (5, E5), (6, E6), (7, E7), (9, E9), (10, E10)):
        apply('E3', n, d, {})
