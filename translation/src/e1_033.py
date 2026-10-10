"""E1 entries 13, 33-50 - Tower of Hypnos: sleepers, dream doors, dream worlds."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

p = P('ほ')
HEART = "*"

E13 = {
    7: ["Yukino: I've got a bad feeling. It's heavy like under the hospital. The air, I mean."],
    8: ["Yukino: Yuriko's gone, but this room still feels cold."],
    9: ["Ayase: So cold~ It's hitting my lower back~"],
    10: ["Ayase: I'm hungry~ How long will this life go on~?"],
    11: ["Nanjo: I want a better weapon."],
    12: ["Nanjo: The god of death... I would rather not equip a Thanatos Persona."],
    13: [
        "Brown: Wooo~ It's cold~ It's cold~",
        "Brown: It's colder in here than in other classrooms. Seriously."
    ],
    14: [
        "Brown: A-" + p + " Aaachoo!! Dammit!",
        "Brown: I wanna get the school back without ice already."
    ],
    15: ["Elly: The \"Tower of Thanatos,\" is it? Thanatos is the god of the underworld. I would not like to befriend him."],
    16: ["Elly: I can somewhat understand Yuriko-san's wish to stay beautiful."],
}

E33 = {
    0: [
        "Yukino: What's this? Someone's collapsed. T-Tadashi, Tamaki!? And Natsumi-sensei!",
        "Yukino: Why are they here... Weren't they at school? Cou-" + p + " Could it be!"
    ],
    1: [
        "Nanjo: So ordinary students have fallen victim at last...",
        "Nanjo: Sad as it is, we have no time to care for them. Today them, tomorrow us."
    ],
    2: [
        "Brown: Tadashi... Tamaki-chan... Natsumi-sensei... How cruel!",
        "Brown: Damn it! Snow Queen! I'll avenge all three of you..." + p + " I'll avenge..." + p + " I'll avenge them myself!"
    ],
    3: ["Tadashi-kun: Zzz zzz zzz... ...Ngah" + p + " ...mm-I-l..." + p + " ...Tamakichaaan!..."],
    4: [
        "Yukino: \"Ta... Tamakichan\"...? Sleep talking? Are they just sleeping!?",
        "Yukino: Geez... I worried for nothing."
    ],
    5: [
        "Nanjo: Wait, Mayuzumi. Even if they are only sleeping, it is abnormal for people who should have been at school to be here.",
        "Nanjo: It may be the Snow Queen's trap. It does no harm to be careful."
    ],
    6: [
        "Elly: The Tower of Hypnos... What Hypnos symbolizes is sleep...!",
        "Elly: Be careful, everyone! The three may have been put to sleep by the Snow Queen!"
    ],
    7: ["Tamaki-chan: Zzz zzzz... ...mnya mnya" + p + " ...love" + p + " ...you... mm... ta" + p + " ...da" + p + " ...mnya"],
    8: [
        "Ayase: But, but~ For people put to sleep by the Snow Queen,",
        "Ayase: they're all sleeping with such happy faces~!"
    ],
    9: [
        "Natsumi-sensei: Zzz" + p + " ...zzzz~ ...hee hee..." + p + " no good... ...eat" + p + " ...properly..."
    ],
    10: ["Ayase: ..." + p + " ..." + p + " I wonder what kind of dream they're having. Makes me want to pinch their noses."],
    11: [
        "Yukino: Even if they're just sleeping, we can't leave the three in a place full of monsters like this.",
        "Yukino: Let's wake them up before we go on."
    ],
    12: [
        "Yukino: Honestly, Natsumi-sensei is something else.",
        "Yukino: This is no different from sleeping..."
    ],
    13: [
        "Ayase: Hey, hey, Tadashi-kun is always yelling and noisy,",
        "Ayase: but sleeping like this he's pretty cute, huh."
    ],
    14: ["Ayase: Aah, so tired. Ayase is getting sleepy too."],
    15: [
        "Nanjo: If their lives are not in danger, there is no problem leaving them.",
        "Nanjo: We have no time. \"Time is money.\" Let us move on."
    ],
    16: [
        "Nanjo: ..." + p + " ..." + p + " ...!? No, no. If I relax even a little,",
        "Nanjo: I will fall asleep. I want to get out of this place quickly."
    ],
    17: [
        "Brown: Geez, geez. Scared me for nothing. They were just sleeping?",
        "Brown: Well, I figured from the start it was like that. Seriously."
    ],
    18: [
        "Brown: ..." + p + " ......" + p + " ........." + p + " ......" + p + " ........" + " ..." + p + " Gah!?",
        "Brown: W-What!? I-I wasn't sleeping or anything!! I-I was working out a strategy!!"
    ],
    19: [
        "Elly: If the reason the three are asleep is related to Hypnos,",
        "Elly: I do not think they will wake up by staying here like this."
    ],
    20: [
        "Elly: Keep a firm sense of self and do not fall asleep.",
        "Elly: That is the \"key\" to conquering this \"Tower of Hypnos.\""
    ],
    21: ["Tadashi-kun: Zzz zzz zzz... ngah..." + p + " guh..." + p + " guuu... I won't let go..." + p],
    22: ["Tamaki-chan: Zzz zzz zzz... zzz zzz... no more..." + p + " can't let g..." + p + " o..."],
    23: ["Natsumi-sensei: Zzz... zzz... zzz... zzz zzz... zzzz... ...don't" + p + " ...run" + p + " ...eat"],
    24: [
        "Natsumi-sensei: ..." + p + " ..." + p + " ..." + p + " ...! Owww, ow ow ow ow, my head... hurts...",
        "Natsumi-sensei: I have low blood pressure. Let me sleep a bit more! ..." + p + " ...Whatever, but be careful... ow ow..."
    ],
}

E34 = {
    0: [
        "Yukino: Dang, here too..." + p + " ..." + p + " ..." + p + " wait, what!",
        "Yukino: It's the teachers sleeping! Get it together, would you."
    ],
    1: [
        "Nanjo: Hm. The situation seems more serious than imagined.",
        "Nanjo: There is surely \"something\" putting the people of the school to sleep. We must find it first."
    ],
    2: [
        "Brown: Gaah! Pathetic! A student like me is working this hard,",
        "Brown: and what's with the teachers being this slack!? Seriously, come on."
    ],
    3: [
        "Vice Principal Hanya: Zzz... zzz..." + p + " Gh! Gaah..." + p + " grind grind grind..." + p + " grind... gh... hehe..." + p + " ghufufufufu..." + p + " hehe..."
    ],
    4: [
        "Ayase: Ew, this bald guy's sleeping and grinning. So gross!!"
    ],
    5: [
        "Nanjo: Hideous... I cannot bear to look. That such a man calls himself an educator, the world is truly at its end.",
        "Nanjo: But is the principal all right? He seems to be having quite a nightmare."
    ],
    6: [
        "Elly: Oh my! The principal is having a nightmare. He is sweating terribly.",
        "Elly: Is this also the Snow Queen's magic?"
    ],
    7: ["Principal Oishi: Zzz... zzz... Uh" + p + " ...mmm... ...but" + p + " ...that is..."],
    8: [
        "Yukino: Same as the last room. Neither of them looks like waking up whatever we do. What do we do?"
    ],
    9: ["Yukino: You're not planning to just leave the sleeping people like this, are you?"],
    10: ["Ayase: It's a chance, so shall we doodle on Hannya's bald head?"],
    11: [
        "Nanjo: Honestly...! Why did we enter the tower? To escape from the school, did we not?",
        "Nanjo: Then think of nothing else and go forward! There is much waste in your behavior."
    ],
    12: [
        "Brown: Hmm~" + p + " ...Mmm" + p + " ...Mmm" + p + " ...Mmm...!" + p + " Okay! As leader, I Great Brown order you!",
        "Brown: We move on! " + p + " ...But..." + p + " wait. Saving them and making them owe me a favor could be good too. What should I do?"
    ],
    13: [
        "Elly: Staying here like this only wastes time. Whether we wake the sleepers or conquer the tower,",
        "Elly: I think moving forward is what matters for us now."
    ],
    14: [
        "Vice Principal Hanya: Guooo..." + p + " guuu... ...copy practice..." + p + " hee..." + p + " hehee... ...shoes..." + p + " polish them..." + p + " ehehe..."
    ],
    15: ["Principal Oishi: Zzz... zzz... Ugh..." + p + " Uuuun... ...Uuun" + p + " ...Uuuun..."],
}

E40 = {
    0: ["Yukino: What's this place?"],
    1: ["Nanjo: Ugh. The sleepiness comes at us as if it had physical force."],
    2: [
        "Brown: H-Huh? I see! So this is the boss room?!",
        "Brown: Everyone, don't let your guard down! Just kidding."
    ],
    3: ["Ayase: Hey, hey, there's a super weird door in the back. Shall we go in?"],
    4: [
        "Nanjo: A suspicious-looking door. It would be wise not to approach carelessly.",
        "Nanjo: But thinking here only wastes time... What should we do?"
    ],
    5: [
        "Elly: It is a suspicious door, but I do not sense any evil presence.",
        "Elly: As Ayase says, entering may be an option."
    ],
    6: ["Yukino: Right! No use dithering here. Let's take a peek!!"],
    7: ["???: Ha ha ha. As spirited as ever, boys and girls."],
    8: ["A sweet wind blows in from beyond the door."],
    9: "=Go to the world of dreams?<FF03><FF0E>　<FF01>",
    10: [
        "Yukino: I don't like looking at other people's dreams. It feels like peeping."
    ],
    11: ["Ayase: If Ayase dreams, would she come to the dream world here, too?"],
    12: ["Nanjo: I have no business in such a place. Let us hurry on."],
    13: ["Brown: Other people's dreams are interesting and fun, huh. Kekeke..."],
    14: [
        "Elly: ...The world of dreams. Erie in DreamLand.",
        "Elly: \"Erie in Dreamland,\" a place like that. Hee hee..."
    ],
}

E48 = {
    0: ["Yukino: Huh? This is... the principal's office? Why is a place like this here??"],
    1: [
        "Vice Principal Hanya: Vice Principal Oishi. In other words, you mean that my educational policy as \"Principal\"",
        "Vice Principal Hanya: is mistaken. That is what you want to say, is it? \"Vice Principal\" Oishi?"
    ],
    2: [
        "Principal Oishi: No, Principal Hanya, that is not what I mean. It is just that I",
        "Principal Oishi: think the rule that students who are late three times must either be expelled or polish Principal Hanya's shoes until graduation is a bit much..."
    ],
    3: [
        "Nanjo: It appears this is the dream of the vice principal and the principal.",
        "Nanjo: Vice Principal Hanya has become \"Principal,\" and Principal Oishi \"Vice Principal.\"",
        "Nanjo: Most likely the principal was dragged into that vulgar vice principal's dream. That is about it."
    ],
    4: [
        "Brown: Huh? Vice Principal Hanya is \"Principal\"? Principal Oishi is \"Vice Principal\"?",
        "Brown: What's going on? Oh, I get it! This is Hanya and Oishi-sensei's dream!"
    ],
    5: ["Ayase: Eeh! Hannya the bald guy as principal? Super no way!"],
    6: [
        "Vice Principal Hanya: What did you say!? \"Vice Principal\" Oishi!",
        "Vice Principal Hanya: You, a mere \"vice principal,\" dare find fault with the wonderful rules I, \"Principal\" Hanya, came up with!!",
        "Vice Principal Hanya: Right! I've thought up a new rule! Ordinary teachers who find fault with the \"Principal's\" rules are fired! Fired, fired!",
        "Vice Principal Hanya: You're fired~!!"
    ],
    7: [
        "Principal Oishi: \"Came up with\"!? Principal Hanya!! Were you deciding the rules on a whim?"
    ],
    8: [
        "Nanjo: Pointless. Truly pointless. Unbearable to listen to.",
        "Nanjo: Is this the conversation of people calling themselves educators?"
    ],
    9: [
        "Elly: Vice Principal Hanya's desire-filled \"dream\" must be very powerful.",
        "Elly: To even pull Principal Oishi into his own dream..."
    ],
    10: [
        "Vice Principal Hanya: S-Shut up! What's wrong with deciding rules on a whim!?",
        "Vice Principal Hanya: Not to be spiritual about it, but I'm the greatest in this school! I'm a god, so to speak!",
        "Vice Principal Hanya: My voice is the voice of god! The will of the great universe! Understood!"
    ],
    11: [
        "Principal Oishi: Principal Hanya!! What do you think education is?",
        "Principal Oishi: In the first place..."
    ],
    12: ["Yukino: Let's wake them up quick. I can't stand listening to this."],
    13: [
        "Yukino: Still, it's one realistic principal's office.",
        "Yukino: If nobody said so, you wouldn't know it's a dream."
    ],
    14: ["Ayase: Ahh~ Let's hurry back to school. Ayase is tired!!"],
    15: [
        "Nanjo: We who peek into others' dreams have no right to say so, but",
        "Nanjo: being shown a person's naked desires like this is not pleasant."
    ],
    16: [
        "Brown: Whoo! Shall we take a rest at this reception set?",
        "Brown: Just kidding. A joke."
    ],
    17: ["Elly: Even a world of dreams is not such a Romantic world, is it."],
    18: ["Vice Principal Hanya: What! You're noisy! Later!!"],
    19: "=Pinch Vice Principal Hanya?<FF03><FF0E>　<FF01>",
    20: ["Principal Oishi: Later. I must persuade \"Principal\" Hanya."],
    21: "=Pinch Principal Oishi?<FF03><FF0E>　<FF01>",
    22: ["Vice Principal Hanya: W-What?"],
    23: ["Principal Oishi: A-Ah, my?"],
    24: ["Vice Principal Hanya: Get lost! Right now!! I'll make you polish shoes!!"],
    25: ["Principal Oishi: Now, go over there."],
}

E50 = {
    0: ["Yukino: This is... the fencing club room... Which me-" + p + " ans-" + p + " ..."],
    1: [
        "Tadashi-kun: T-Ta-Ta-Ta-Tamakichaaan! I love you! I really, really love you!!"
    ],
    2: ["Tamaki-chan: Tadashi... I love you..."],
    3: [
        "Nanjo: The dream of these two... They did nothing but fight in reality,",
        "Nanjo: but indeed, it seems they were a good example of \"those who fight are close.\""
    ],
    4: [
        "Brown: Bam! I'm super shocked! Tamaki-chan likes that Tadashi guy! Someone tell me it's a dream!!",
        "Brown: Wait, is this the dream? Huh? Is this reality and that the dream?"
    ],
    5: ["Ayase: No way! So those two really were in that kind of relationship!"],
    6: ["Tadashi-kun: Now, look into my eyes, my honey *"],
}

if __name__ == '__main__':
    for n, d in ((13, E13), (33, E33), (34, E34), (40, E40), (48, E48), (50, E50)):
        apply('E1', n, d, {})
