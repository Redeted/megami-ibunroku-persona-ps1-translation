"""E3 entries 33-43 - the old wooden school wing, the Spiegel armor, Mariko, Hee-Ho elevator."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

p = P('ほ'); pk = P('き'); ps = P('そ')
H = F6('う') + "*" + F6('　')

E33 = {
    0: [
        "Hiho-ko-chan: Strike, strike, hee-ho!",
        "Hee-Ho-kun: This school doesn't have a sumo club, so I'm joining the boxing club!",
        "Hiho-ko-chan: Hey hey, sandbags shouldn't move.",
        "Hee-Ho-kun: Hee-ho? Is that about me??",
        "Hiho-ko-chan: Well, the boy in the fencing club got beaten up by a girl, didn't he?",
        "Hee-Ho-kun: Hee-Ho!! I see, girls are strong..." + p + " ..." + p + " be gen" + pk + "tle" + pk + " with" + pk + " me" + pk + " " + H
    ],
    1: ["Yukino: These guys again."],
    2: ["Ayase: Nice, being so close."],
    3: ["Nanjo: They are always doing a comedy routine."],
    4: ["Brown: So soothing~"],
    5: ["Elly: I wonder if Jack Frost has genders."],
}

E34 = {
    1: ["Yukino: What happened?"],
    2: ["Yukino: Going in again?"],
    3: ["Ayase: Huh? Feels like one person is missing..."],
    4: ["Ayase: It's glowing, but it's not warm."],
    5: ["Nanjo: Is everyone safe? What on earth was that..."],
    6: [
        "Nanjo: It seems that touching this teleports you to another place."
    ],
    7: ["Brown: Huh?? What was that?"],
    8: ["Brown: If you keep staring, your eyes hurt."],
    9: ["Elly: What has changed? Let us go outside and see!"],
    10: ["Elly: Is this something like a Warp Hole?"],
}

E35 = {
    0: ["Yukino: <FF0F>あ, are you hurt?"],
    1: ["Ayase: My hands are going numb~"],
    2: [
        "Nanjo: What is the structure of this building? I cannot believe it was originally a school."
    ],
    3: ["Brown: Phew~ Let's catch our breath. My legs are turning to sticks."],
    4: [
        "Elly: Both the Demons and the building's structure have become tougher."
    ],
}

E36 = {
    1: ["A small scrap of paper is stuck to the frozen floor."],
    2: "=Read it?<FF03><FF0E>　<FF01>",
    3: [
        "Dispose of the old protagonist costume used in \"The Snow Queen.\" It's dirty and looks like bad luck.",
        "The item is to the right of the vaulting box. Counting on you, freshman!!",
        "        From the Drama Club's star * the President"
    ],
    4: ["There is an antique costume among the junk."],
    5: ["Obtained the \"Spiegel Mask\""],
    6: ["Obtained the \"Spiegel Mail\""],
    7: ["Obtained the \"Spiegel Bein\""],
    8: ["Obtained the \"Spiegel Blade\""],
    11: ["Yukino: This one looks like it wants to say something..."],
    12: ["Yukino: We have to try hard for their sake too."],
    13: ["Ayase: If I cast Agi, will it melt~?"],
    15: [
        "Nanjo: \"Quiet the mind and even fire is cool\"" + p + " ..." + p + " ...How could I get cold?"
    ],
    16: ["Nanjo: A windfall. An unexpected find."],
    17: [
        "Brown: Damn it! Queen of the Night or whatever, I won't forgive her!!"
    ],
    18: [
        "Brown: If it's the protagonist's costume, it should fit great me perfectly" + p + " ..." + p + " Oh" + p + " my god~",
        "Brown: It doesn't fit~ Can't be helped. Out of the troupe leader's feelings, I might just let <FF08>あ have it. Just kidding."
    ],
    19: [
        "Brown: Huh?" + ps + " Hey! Look at what's at his feet. Something's fallen!",
        "Brown: A" + pk + " a" + pk + " a" + pk + " a" + pk + " a" + pk + " A 10,000-yen note!? If it's a 10,000-yen note, it's mine! Don't take it" + pk + " don't take it" + pk + " don't take it" + pk + " don't take" + pk + " it~!! I found it first~!!"
    ],
    20: ["Yukino: Same old greedy guy, aren't you!"],
    21: [
        "Brown: Aw, Miss Yukino, as if I'd pocket it. I'll present it to you properly, for real."
    ],
    22: ["Yukino: Idiot, I'm saying that's not 10,000 yen!"],
    23: ["Brown: Huh?" + p + " Oh~ It's true, boo-hoo..."],
    24: ["Ayase: Total idiot. You'll face judgment after death, for sure."],
    25: [
        "Brown: Gh" + p + " guh! Why do I have to hear that from Ayase~!?"
    ],
    26: ["Brown: Boo-hoo..."],
    27: ["Elly: Oh... here too."],
    28: ["Elly: You found something good."],
}

E37 = {
    0: ["Yukino: How did that woman climb up here?"],
    1: ["Ayase: Ah, look look~ My eyelashes are frozen~"],
    2: [
        "Nanjo: Usually she irritates me, but at times like this, having Ayase around is somehow a relief."
    ],
    3: ["Brown: I'm getting sleepy..."],
    4: [
        "Elly: No matter how far we go, the same scenery... Are we truly advancing?"
    ],
    5: [
        "???: Oh, hello. Nice to meet you. I'm Yabe Mariko of the \"Yamakumo Private High School Paranormal Phenomena Club\"! Pleased to meet you!",
        "???: Well, though it's an illegal club where I'm both president and the only member!",
        "???: My homeroom teacher won't approve setting up the club just because he says it's \"lame\"!",
        "???: Anyway, today I came to meet my comrade Kurouri-kun, but I never" + p + " thought" + p + " I'd get caught up in such an amazing paranormal phenomenon!",
        "???: I'm so lucky! Until just now I was exploring the three mysterious towers that suddenly appeared around the school!",
        "???: The towers are full of demons! I got tons of great photos! I'm going to submit those demon photos to a magazine!",
        "???: If the media recognizes it, maybe the teacher will approve the club too! Alright! I'll do my best!"
    ],
    6: [
        "Mariko: I've pretty much finished exploring the towers, so I climbed up this far, but... I'm a bit tired.",
        "Mariko: But this situation is exciting! \"The school's mysterious freezing!\" \"The revival of demons!\"",
        "Mariko: \"A mysterious tower and a school turned labyrinth!\"",
        "Mariko: Hey, what do you think?",
        "Mariko: I think it's a conspiracy by a secret society trying to rule the world with magic..."
    ],
}

E38 = {
    0: ["Hiho-ko-chan: Hee-ho!! Fourth floor, ma'am~"],
    1: ["Hee-Ho-kun: Hee-Ho! Hey, hey, you guys~"],
    2: "=Will you be our friend?<FF03><FF0E>　<FF01>",
    3: [
        "Hee-Ho-kun: Hee-Ho! 95 more and I'll have 100 friends!!",
        "Hee-Ho-kun: Is there anything I can do for my friends? Oh yeah!!"
    ],
    4: "=Shall I take you<FF03>to the upper floor?<FF03><FF0E>　<FF01>",
    5: ["Hiho-ko-chan: Tch."],
    6: ["Hee-Ho-kun: Hee-Ho! Then close your eyes for just a bit..."],
    8: ["Yukino: Another snowman. What's it doing this time?"],
    9: ["Ayase: It looks like it wants someone to talk to it."],
    10: ["Nanjo: Are they lonely?"],
    11: ["Brown: Looking at their mouths makes me want watermelon."],
    12: [
        "Elly: So there are friendly, curious individuals among Demons, too."
    ],
}

E39 = {
    0: ["Yukino: What's with this floor?"],
    1: [
        "Ayase: I've seen this classroom in the old framed photo hanging in the principal's office. This is the wooden school building from before the current building was built."
    ],
    2: [
        "Nanjo: As expected of Ayase, one lectured in the principal's office many times."
    ],
    3: [
        "Brown: The warmth of wood" + p + " the warmth of handcrafting" + p + " ..." + p + " ..." + p + " like hell there is" + ps + "!!",
        "Brown: There're drafts everywhere, it smells musty... I wanna take a hot bath~"
    ],
    4: [
        "Elly: An Antique building. If it were not such a time, I would like to look around leisurely."
    ],
}

E40 = {
    0: [
        "Yukino: Did the building change because the past Snow Queens spent their school life in the old building? Which means the demons' power is stronger than ever."
    ],
    1: ["Ayase: People in the old days held classes in classrooms like this~ Weren't they cold~?"],
    2: [
        "Nanjo: Mayuzumi is right. From here on, it is best to steel ourselves."
    ],
    3: [
        "Brown: What a bad feeling. It's an old building to begin with, and it's frozen, and the footsteps echo like crazy."
    ],
    4: [
        "Elly: They say old schools are steeped with memories spanning many generations. I only hope they do not exert a bad influence."
    ],
}

E41 = {
    0: ["Hiho-ko-chan: Hee-ho!! Fifth floor, ma'am~"],
    2: "=Shall I take you<FF03>to the lower floor?<FF03><FF0E>　<FF01>",
    6: ["Yukino: What kind of trick did this snowman use?"],
    7: ["Ayase: Whoa~ It's kind of creepy..."],
    8: [
        "Nanjo: It has turned wooden. Did the Queen of the Night haggle down the castle's construction costs?"
    ],
    9: ["Brown: Give me a break~ It's even colder here!"],
    10: ["Elly: This is..."],
}

E42 = {
    0: [
        "Yukino: The Queen of the Night called this frozen school an ice castle. It is indeed a castle. It's hard to storm and climb."
    ],
    1: [
        "Ayase: I've always been bad at mazes and mirror houses. Gah! So annoying!!"
    ],
    2: [
        "Nanjo: I am thinking of adopting a labyrinth into my family's security as well. What do you think?"
    ],
    3: [
        "Brown: Why is it so big!! Is there really a goal..."
    ],
    4: ["Elly: There is no turning back now."],
}

E43 = {
    0: [
        "Yukino: She's saying childish stuff again, Yuka. Well, no wonder."
    ],
    1: [
        "Ayase: Geez! Isn't there a handy spell that warps you to the Queen's room~!?"
    ],
}

if __name__ == '__main__':
    for n, d in ((33, E33), (34, E34), (35, E35), (36, E36), (37, E37), (38, E38), (39, E39), (40, E40), (41, E41), (42, E42), (43, E43)):
        apply('E3', n, d, {})
