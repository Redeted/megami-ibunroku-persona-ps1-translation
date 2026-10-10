"""E3 entries 10-32 - the light orb, the infirmary, Toro recovers, the frozen students."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

H = F6('う') + "*" + F6('　')

E10 = {
    7: ["Ayase: What now, after all this? Did you get scared?"],
    8: [
        "Nanjo: They say beautiful things have thorns. Be careful!"
    ],
    10: [
        "Nanjo: I have been waiting. I came ahead to hand this over.",
        "Nanjo: It is a \"Purba Dagger,\" but it is awkward for me to use, so you can have it.",
        "Nanjo: I need no words of thanks. Instead, save the school as soon as possible."
    ],
    11: ["Received the \"Purba Dagger\""],
    12: [
        "Nanjo: It seems that touching this will teleport you to another place. Where you will be sent, I do not know."
    ],
    13: ["Brown: If you keep looking at it, you feel like you'll be sucked in."],
    15: [
        "Brown: You're late, geez. I have to keep an eye on Toro, so sorry, I can't go with you.",
        "Brown: As a substitute, you'll probably need this for something, so take it!",
        "Brown: It's a \"Scorch Tablet.\" I won it at the casino, but I have another one.",
        "Brown: No, no thanks needed! Now go do your best!"
    ],
    16: ["Received the \"Scorch Tablet\""],
    17: [
        "Brown: I have to keep an eye on Toro, so sorry, I can't go with you."
    ],
    18: ["Elly: Could it be Plasma?"],
    19: ["Elly: Now, let us go!"],
    20: [
        "Elly: So it was here after all. I came to hand this over. It is a \"Full Moon Tablet.\"",
        "Elly: I came across it by chance while searching for something in the library, and I thought it would be more useful in your hands."
    ],
    21: ["Received the \"Full Moon Tablet\""],
    22: ["Elly: What lies beyond the light, I wonder?"],
}

E11 = {
    0: [
        "Natsumi-sensei: Everyone safe? Let's see, let teacher take a look. " + H
    ],
    1: ["Natsumi-sensei: There, you should be fine now. Don't overdo it!!"],
    2: [
        "Natsumi-sensei: What? Staring at my face like that. Could it be... you fell for me?",
        "Natsumi-sensei: Speaking of falling, Ayase-san!"
    ],
    3: [
        "Natsumi-sensei: I heard Yokouchi-kun confessed to you? How did you turn him down!",
        "Natsumi-sensei: That boy's been strange lately. You need to put yourself in the other person's shoes when you speak!"
    ],
    4: [
        "Ayase: As expected! Words from someone good at getting dumped carry weight."
    ],
    5: [
        "Natsumi-sensei: ...... Now, back to work, back to work. Everyone safe? Let's see, let teacher take a look. " + H
    ],
    6: [
        "Natsumi-sensei: Haah~ I wonder if there's a good guy somewhere... ...... Now, back to work, back to work. Everyone safe? Let's see, let teacher take a look. " + H
    ],
    7: ["Maki's Mother: To think even the school has become like this."],
    8: ["Maki's Mother: Maki... please be safe."],
    9: [
        "Maki's Mother: If only Maki were bright and active like you all..."
    ],
    10: [
        "Maki's Mother: Nanjo-kun just left the room a moment ago. He said something about a classroom whose door was frozen shut."
    ],
    11: [
        "Student: Ow ow ow... I fell and hit my butt. Why is the hallway slippery!"
    ],
    12: [
        "Student: It seems something happened in the cafeteria. If I hadn't fallen and gotten hurt, I'd go see too. Ow ow ow..."
    ],
    13: [
        "Student: Hey, did you hear? To the left outside the nurse's office there's a flea market selling cool clothes, right?",
        "Student: Apparently the lineup has changed completely."
    ],
    15: [
        "Nanjo: I am worried about Inaba and Sonomura outside the school. We must beat the Snow Queen quickly."
    ],
    16: [
        "Nanjo: Wait for us, Inaba, Sonomura. Once we beat the Queen of the Night, we will head to SEBEC at once!"
    ],
    17: ["Nanjo: What, do you still have business with me?"],
    18: "=So you need my strength<FF03>after all?<FF03><FF0E>き<FF01>",
    21: [
        "Nanjo: I see. Then I shall look for a way out of here on my own."
    ],
    22: [
        "Nanjo: I shall look for a way out on my own. You beat the Snow Queen."
    ],
    23: [
        "Yukino: I hate doctors, but... if you're hurt or feeling unwell, don't push it, get Natsumi-sensei to look at you."
    ],
    24: ["Yukino: Everyone, are you in good shape?"],
    25: [
        "Ayase: Wasn't this Agasthya or something? They say it has mysterious power."
    ],
    26: [
        "Ayase: It's cold here too~ I wanna say goodbye to the cold already."
    ],
    27: ["Brown: Don't they have a love potion or something?"],
    28: ["Brown: Isn't there some medicine that makes you smarter?"],
    29: ["Elly: I am glad the nurse's office did not disappear."],
    30: [
        "Elly: To search for Maki, we must restore the school quickly."
    ],
    32: "=Engrave your record upon me?<FF03><FF0E>　<FF01>",
    33: [
        "Agasthya Tree: Young one... Your record is engraved upon me. Now, continue your journey."
    ],
}

E12 = {
    0: [
        "Toro: It can't be... only milk and cheese, and I don't even have the right to binge out of spite. And I can't eat dairy...",
        "Toro: Someone who knows that is plotting against me! Yes, surely!!",
        "Toro: Everyone in the world is laughing at my unhappiness! Ugh... uuugh... damn it~"
    ],
    1: [
        "Toro: Huh huh huh? Why was I sleeping in a place like this? Aw, everyone, it's embarrassing to look at me like that."
    ],
    2: ["Toro: Ugh... uuugh... Why does it always happen to just me..."],
    3: [
        "Toro: Ugh... uuugh... Why does it always happen to just me... Oh, I almost forgot. Kurouri-kun asked me to hand this over.",
        "Toro: When we came back from the tower, we found a glittering fragment.",
        "Toro: He's got terrible muscle pain and can't carry things, so I'm handing it over on his behalf."
    ],
    4: ["Obtained 2 \"Mirror Fragments\""],
    5: [
        "Toro: I'm not the only one suffering, huh. Ayase-san and you are doing your best too.",
        "Toro: Alright! I'll work hard too and learn to drink milk!!"
    ],
    7: [
        "Student: Suddenly frozen like that, is this the demons' doing too? I just looked and the food's running low. No wonder Toro panicked..."
    ],
    8: [
        "Student: Eh? Didn't I go call a teacher? I did! But nobody would deal with me. They said it'll heal on its own, or they're busy.",
        "Student: Well, anyway, I'm glad you're safe. The food is..."
    ],
    9: [
        "Student: Dumped by the girl he likes, forced to drink the milk he hates. Toro's unlucky today. Well, there are days like that."
    ],
    10: [
        "Student: The classroom that wouldn't open before, you know, down to the left outside here? The ice melted a bit and apparently you can get in now.",
        "Student: There's a rumor that a really beautiful sphere is floating there, but is it safe to approach?"
    ],
    11: [
        "Yukino: This is no time to waste time in a place like this! Let's go find someone reliable!"
    ],
    12: ["Yukino: Well, shall we head to the tower soon?"],
    13: [
        "Yukino: We have the \"mirror fragments,\" so let's go to the courtyard quick!"
    ],
    14: [
        "Yukino: Uesugi's not here. Wasn't he supposed to keep an eye on Toro? That guy, he ditched."
    ],
    15: ["Yukino: Doesn't it feel a little warmer?"],
    16: [
        "Ayase: Even the inside of the building is frozen! What a thing to do, that monster!!"
    ],
    17: [
        "Ayase: I wonder if Toro's okay~? Ah, no, I'm not worried or anything."
    ],
    18: ["Ayase: Let's hurry and get out."],
    19: [
        "Nanjo: What is that guy? Over a mere rejection! He will not amount to anything like that."
    ],
    20: [
        "Nanjo: That glutton had something come out of his belly, but is he all right now?"
    ],
    21: ["Nanjo: He seems to have grown in his own way."],
    22: [
        "Brown: Aaaa-choo! Ah, sorry, did it get on your clothes?",
        "Brown: Geez, I feel as blue as lettuce wilted in a fridge. I thought I'd have hot ramen, but the water won't even boil.",
        "Brown: On top of that, Toro, in spite over being dumped, went wild saying he'd eat everything in the cafeteria.",
        "Brown: So I hid everything except dairy in a hurry. We have no idea what'll happen, so as expected of me, huh?"
    ],
    23: [
        "Brown: The whole school's panicking and the teachers seem to have it rough.",
        "Brown: I don't know what trick you used, but thanks for calming things down.",
        "Brown: Well, I and one other will keep watch from here on, so ride easy like on a big ship."
    ],
    24: [
        "Brown: That Toro guy, I thought he suddenly disappeared, then he started saying nonsense about milk and torture.",
        "Brown: Well, I and one other will keep watch from here on, so ride easy like on a big ship."
    ],
    25: [
        "Brown: Persona, huh... Depending on how you use it, you could do anything."
    ],
    26: [
        "Brown: Personas are scary. I'm a lump of selflessness, so I'm totally fine, though."
    ],
    27: ["Elly: In this state, food is precious, too."],
    28: [
        "Elly: We had a terrible time because of Ayase. Honestly, that girl."
    ],
    29: [
        "Elly: A room with a beautiful sphere floating in it? It seems worth a visit."
    ],
    30: ["Elly: Let us hurry to the upper floor."],
}

E32 = {
    0: ["It's frozen over."],
    2: [
        "Yukino: I thought the numbers seemed low, and here they are... Wait for us, everyone! We'll save you soon!!"
    ],
    3: ["Ayase: How awful... What's so fun about doing this?"],
    4: ["Nanjo: Hm. The enemy has resorted to force as well."],
    6: [
        "Elly: They still seem to be breathing. The Eternal Night... so this is what it meant."
    ],
}

if __name__ == '__main__':
    for n, d in ((10, E10), (11, E11), (12, E12), (32, E32)):
        apply('E3', n, d, {})
