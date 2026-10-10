"""E3 entries 97-106 - Thanatos tower / Tartarus shop and treasure chest chatter."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

H = F6('う') + "*" + F6('　')

E97 = {
    4: "=It'll cost 6000 yen, okay?<FF03><FF0E>　<FF01>",
}

E98 = {
    1: [
        "Mariko: I'm thinking of interviewing a demon, but I don't have a tape recorder or a microphone. Hey, you don't suppose they sell them somewhere?"
    ],
    3: [
        "Yukino: At this level, even the things for sale are pricey."
    ],
    4: [
        "Ayase: The clothes that salesgirl is wearing are so cute! Ayase wants those too!"
    ],
    5: [
        "Nanjo: Amazing!! But everything is too expensive! Yet we cannot help but buy. This is truly a case of \"necessity knows no choice.\""
    ],
    6: [
        "Brown: Dehya~! I want this, I want that. But it's expensive! Hmm."
    ],
    7: ["Elly: What will that child do with the sales money?"],
}

E99 = {
    1: ["Yukino: Not that it matters, but the armor shop owner is gloomy."],
    2: ["Ayase: Hey~ This is lovely! " + H],
    3: [
        "Nanjo: Sturdy armor is generally heavy, which is a minor flaw."
    ],
    4: [
        "Brown: Man, I look good in whatever I wear. It takes forever to choose! Nahahaha"
    ],
    5: [
        "Elly: Where did this armor get sourced? Considering its origin is frightening."
    ],
}

E100 = {
    0: [
        "Yukino: Even as we stand here, time keeps passing. It's frustrating. Really, I start to think I'm powerless."
    ],
    1: [
        "Ayase: Working hard together with everyone for one purpose like this is kinda nice."
    ],
    2: ["Nanjo: Hey, how long do you intend to stay in a place like this?"],
    3: [
        "Brown: Sure, the school turning out like this is a problem, but I feel kinda excited, like I've been freed from boring everyday life!"
    ],
    4: [
        "Elly: The Tower of Thanatos, Tartarus... It is nearly Greek mythology."
    ],
}

E101 = {
    0: [
        "Yukino: Sometimes \"mirror fragments\" are in treasure chests! Let's check the chests as time allows."
    ],
    1: ["Ayase: Every time, it's thrilling to open a treasure chest, isn't it!"],
    2: [
        "Nanjo: Scavenging chests somehow does not look beautiful for a human. No, I do not mean you. It is purely a general observation. Yes."
    ],
    3: [
        "Brown: Hey, you, since you're always so quiet, honestly I thought you were a weirdo...",
        "Brown: But fighting alongside you, I get it now!! You're amazing!!",
        "Brown: You're about the second strongest after me, and second most reliable after me!",
        "Brown: I've got a new respect for you! Seriously!"
    ],
    4: [
        "Elly: I have gained a little respect for you. Even in a situation like this, you hold everyone together without a single complaint,",
        "Elly: a possessor of a strong Brave Heart."
    ],
}

E102 = {
    0: [
        "Yukino: Could this Tartarus be Yuriko's treasure vault? There sure are a lot of chests."
    ],
    1: [
        "Ayase: Hey... if we beat the \"Snow Queen\" and save Saeko-sensei, everything will be over, right? Everyone will go back to normal, and Ayase and the others can go home, right?"
    ],
    2: [
        "Nanjo: I am worried about Saeko-sensei, but also Inaba... I wonder if he is all right. He is a fool, after all. Damn, how frustrating!"
    ],
    3: [
        "Brown: Aaah!! The afterlife, huh, there's nothing in particular here. So boring!! Hey! Let's go back to the tower soon and go to Yuriko-chan!"
    ],
    4: [
        "Elly: Hee hee... Is it not strange? That five people who were not especially close ended up on an Adventure together,",
        "Elly: and that there is a part of me enjoying the situation. It is strange... truly."
    ],
}

E103 = {
    0: [
        "Yukino: Odd to say it in the afterlife, but... I hope we all get home safe."
    ],
    1: [
        "Ayase: Hey, hey, maybe there's a chest with a \"mirror fragment\" in it too!!"
    ],
    2: [
        "Nanjo: Still, the enemies here are strong. Without proper equipment, we cannot beat Yuriko."
    ],
    3: ["Brown: Cerberus was right, it's rough, this Tartarus..."],
    4: [
        "Elly: Checking every chest seems hard time-wise."
    ],
}

E104 = {
    0: [
        "Yukino: There's no end to it. There's a time limit too, so we might be in trouble if we don't draw a line somewhere."
    ],
    1: ["Ayase: Treasure chests, the more the merrier!"],
    2: [
        "Nanjo: I have gained a little respect for you through our battles so far. You are strong.",
        "Nanjo: And, as a matter of consultation, once we defeat the \"Snow Queen,\" when we go save Inaba, would you accompany us?",
        "Nanjo: I want every bit of fighting strength. Well, I will not force you. Think about it."
    ],
    3: [
        "Brown: Treasure chest! Yeah, they're great!! Gaah!! Treasure chests!!",
        "Brown: Even if you know the word, hardly anyone's actually seen, touched, or opened one!"
    ],
    4: ["Elly: Please also keep the Time limit somewhat in mind."],
}

E105 = {
    0: ["Yukino: Saeko-sensei... I hope she's okay. Damn, I have to hurry more..."],
    1: [
        "Ayase: What do we do!! To think Ayase's Persona would be gone! I hate it!!"
    ],
    2: [
        "Nanjo: I did not even know of the existence of Personas until now, but now that it is gone, it is quite painful."
    ],
    3: [
        "Brown: Damn it!! Fighting without a Persona... The enemies in this tower are strong! This is no joke!!"
    ],
    4: [
        "Elly: It seems this tower has a Law that anything done here costs a \"life\" as the price.",
        "Elly: In our case, it seems a \"Persona\" is lost instead of a \"life.\""
    ],
}

E106 = {
    0: [
        "Yukino: Not that it matters, but the treasure chests in the towers have odd shapes."
    ],
    1: [
        "Ayase: Somehow Ayase is hungry~ Isn't there a chest with food in it?"
    ],
    2: [
        "Nanjo: Medicine and items only have meaning if used. We must not let them become a \"waste of treasure.\""
    ],
    3: [
        "Brown: No amount of time is enough, really. Even as we stand here, the \"Eternal Night\" might come. Ugh."
    ],
    4: [
        "Elly: Eternal Night... What kind of world could it be? It is frightening..."
    ],
}

if __name__ == '__main__':
    for n, d in ((97, E97), (98, E98), (99, E99), (100, E100), (101, E101), (102, E102), (103, E103), (104, E104), (105, E105), (106, E106)):
        apply('E3', n, d, {})
