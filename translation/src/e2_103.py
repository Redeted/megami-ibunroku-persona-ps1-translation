"""E2 entries 103-143 - party chatter variants (Maki/Brown/Ayase/Mark/Elly), school NPCs under the demon crisis."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

pm = P('み'); pn = P('な'); pg = P('ぎ'); pt = P('た'); pk = P('キ')

E103 = {
    7: [
        "Clerk: ..." + pt + " Even demons won't come into the store, right?" + pn + " I have to keep the shop open... Open every day of the year, after all..." + pm + " Welcome!"
    ],
}

E104 = {
    0: ["Maki: Do you have business with the doctor?" + pm + " Hey, let's get out of here quick..."],
    1: [
        "Brown: Do we really have to go to the abandoned factory? A grubby place like that doesn't suit me!"
    ],
    2: [
        "Brown: Do we really have to beat Kandori? He ran away, so isn't that good enough?"
    ],
    5: ["Mark: We gotta hurry and chase that Kandori bastard...!!"],
    7: ["Ayase: Why does SEBEC have to be so heavily guarded?"],
    8: ["Ayase: SEBEC really was a crazy place..."],
}

E105 = {
    0: [
        "Maki: Hey, hey, Inaba-kun is at the police station, right? Let's hurry and go save him!"
    ],
    1: ["Maki: Um, we were going to the abandoned factory, right?"],
    2: ["Maki: We have to hurry and chase Kandori!"],
    3: [
        "Brown: Still, what a lame shop! If it were me, I'd renovate it into an open-air cafe!"
    ],
    4: [
        "Nanjo: That shopkeeper seems to suspect us. But we who possess such strange power, are we still truly human?",
        "Nanjo: What do you think?"
    ],
    7: ["Ayase: <FF0F>あ, you like this kind of thing! Aww, it's cute!"],
}

E106 = {
    0: ["Maki: The owner here is good at business, isn't he."],
    1: [
        "Brown: It was my first time in a jail cell! I was a little nervous, but looking back it was pretty fun!"
    ],
    3: [
        "Mark: I've got lots I wanna say to Kandori. Anyway, that guy's the one I won't forgive."
    ],
    4: [
        "Elly: We are going to the abandoned factory, correct? I never paid attention to such a place before..."
    ],
    5: [
        "Elly: We must hurry and chase Mr. Kandori..." + pm + " We cannot leave him be!"
    ],
    6: [
        "Ayase: That's right, we're storming SEBEC, so we should at least bring medicine!"
    ],
    7: [
        "Ayase: We gotta chase Kandori..." + pn + " Who knows what that guy will do?"
    ],
}

E107 = {
    0: ["Maki: Hmm, Elly is popular, huh..."],
    1: [
        "Brown: Let me tell you, I have fans by the dozen, enough to sweep up and throw away!"
    ],
    4: [
        "Mark: While we're doing this, I wonder if the abandoned factory's passage will get crushed?"
    ],
    6: [
        "Ayase: That guy's an idiot! Kirishima isn't such a pushover!"
    ],
    7: ["Yukino: Eriko's fearlessness is amazing, isn't it."],
    8: [
        "Customer: Oh, there you are, I was looking for you! You shouldn't wander around!",
        "Customer: With demons showing up, it's scary, right? I was thinking of protecting you!"
    ],
    9: [
        "Elly: Thank you very much for that.",
        "Elly: But I have more knowledge about Demons than you, and can protect myself, so no" + pt + " thank" + pt + " you!"
    ],
}

E109 = {
    0: [
        "Maki: Everyone's talking about my mother, but" + pm + " who is that?"
    ],
    2: [
        "Mark: I wonder if Sonomura still can't remember her mom. Seems like there are circumstances."
    ],
    3: [
        "Elly: After healing the wound, let us hurry to the abandoned factory.",
        "Elly: But can we truly enter SEBEC from such a place?"
    ],
    4: ["Elly: We must hurry and chase Mr. Kandori...!"],
    5: [
        "Brown: Me, I almost got a scar on my face in the last battle!",
        "Brown: Man, I almost made all fifty thousand Brown fans nationwide sad!",
        "Brown: Me, I'm just so" + pn + " ve" + pt + " ry" + pt + " lucky! *"
    ],
    6: ["Ayase: We won't get shots, right? Ayase hates shots."],
}

E110 = {
    0: ["Maki: I don't want to stay here much longer."],
    1: [
        "Brown: Isn't there somewhere I can shine more? Am I standing out properly?"
    ],
    4: [
        "Elly: I suppose the Demons appearing in town is also SEBEC's doing."
    ],
    5: ["Ayase: Ugh, I hate the smell of disinfectant."],
}

E111 = {
    0: [
        "Maki: Inaba-kun is surely waiting for us to come. Let's hurry and go to him."
    ],
    1: [
        "Maki: We were going to the abandoned factory, right? But..." + pm + " what is SEBEC?",
        "Maki: A company name? Was there such a thing in this town...?"
    ],
    2: ["Maki: Let's hurry and chase Kandori!"],
    3: [
        "Brown: Heh, finally getting into the groove. From now on I'll show you Brown's true power!"
    ],
    4: [
        "Nanjo: Uesugi seems to have already forgotten that he was rescued."
    ],
    5: [
        "Nanjo: Do you not think Sonomura is acting strangely? Hmm..."
    ],
    6: ["Mark: Is it really okay to keep the shop open? Don't blame me if demons get you!"],
    7: ["Elly: Come to think of it, I too have heard about an odd shop before."],
    8: [
        "Ayase: A shop opening just at a time like this is definitely weird."
    ],
    9: [
        "Customer: About that odd shop on this shopping street, it looks like it's about to open. What kind of shop could it be?"
    ],
    10: [
        "Customer: They say that odd shop on this shopping street is open for business. Western-style music can be heard from inside.",
        "Customer: Hmm, I wonder if it's members-only. I'd like to go in."
    ],
}

E114 = {
    1: [
        "Brown: I love the bread here, you know~" + pm + " Ah, this is no time for that?"
    ],
    5: [
        "Ayase: But, like, if a convenience store sold guns and stuff, wouldn't that be scary?"
    ],
}

E128 = {
    0: [
        "Teacher: <FF0F>あ, hey! Go patrol the school for a bit! I can't leave here because I have to grasp all the information!"
    ],
}

E129 = {
    0: [
        "Student: Senpai, \"Kido-san\" seems to have gone outside a moment ago!",
        "Student: And I finally had a chance to talk to him!"
    ],
}

E130 = {
    0: [
        "Toro: Demons are scary, but I think this is a chance. If I show Ayase-san a good side of me, she might come to l-" + pm + " like me" + pn + ", don't you think" + pn + "?"
    ],
    2: [
        "Student: Toro's dangerous. His eyes are gone.",
        "Student: He's still pestering Ayase-san, apparently.",
        "Student: That type gets scary when they get obsessed."
    ],
}

E131 = {
    0: [
        "Student: Hey, the school's guardian deity the principal talked about was real after all!",
        "Student: I mean, demons don't come into the school, right?"
    ],
    1: [
        "Student: Shut up..." + pm + " Guardian deities, demons... Is that guy half asleep?"
    ],
}

E132 = {
    0: [
        "Tadashi-kun: Ah! <FF0F>あ, what's it like outside? You went out, right? Is our bald guy alive?"
    ],
    1: [
        "Tamaki-chan: Hmm~ You're scared, aren't you? Why not go see for yourself? Coward Tadashi!"
    ],
    2: [
        "Tadashi-kun: S-Stupid! I'm n-not scared of demons! You're way scarier! You all-muscle girl!"
    ],
    3: [
        "Tamaki-chan: What did you say! You coward! Coward coward coward coward coward coward coward!"
    ],
    4: [
        "Tadashi-kun: Gah! You muscle girl! Muscle girl muscle girl muscle girl muscle girl! ...H-Hard to say..."
    ],
    5: [
        "Tadashi-kun: *Wheeze* *Wheeze*..." + pk + " Honestly, what a girl with no charm. You think so too, <FF0F>あ?"
    ],
    6: [
        "Tamaki-chan: *Pant* *Pant*..." + pk + " ...Hey, <FF0F>あ-kun, I'll give you this.",
        "Tamaki-chan: It's something I used at my old school for certain reasons... This time it's not me, it's your turn. I have a feeling."
    ],
    7: [
        "Tamaki-chan: <FF0F>あ-kun, there are demons you can talk to. Remember that defeating them isn't the only way."
    ],
    8: [
        "Boy Club Member: Tamaki-chan is amazing! Just now she named one demon after another walking outside!",
        "Boy Club Member: This one's useful, that one won't join us, and so on. By the way, what's a \"companion\"?"
    ],
    11: [
        "Girl Club Member: Those two were fighting so it felt like the usual atmosphere, but... something huge is happening right now, isn't it."
    ],
    12: ["Received a \"Rapier\"!"],
}

E133 = {
    0: [
        "Student: Hey, isn't this the haunted house's curse after all? Since they built a building there, some spirit must be angry!" + pm + " A warlord from the Sengoku era or something, surely!"
    ],
}

E134 = {
    0: [
        "Student: Lucky!" + pm + " Now I don't have to go to cram school! Ah, but I can't go home either...",
        "Student: If there were an exit with no guard, I could slip outside..."
    ],
    1: [
        "Student: That idiot doesn't recognize the seriousness of this at all!",
        "Student: Forget taking exams, our lives might end right here!"
    ],
}

E138 = {
    0: [
        "Student: This commotion will be over before the school festival, right?",
        "Student: It'd suck if the festival got canceled in the confusion!"
    ],
    1: ["The door to the storeroom is locked..."],
    2: [
        "Teacher: Oh, <FF0F>あ! You're still in a place like this!",
        "Teacher: We're closing the gym, so go to the school building. I haven't heard of demons entering the school yet, but it wouldn't be strange if they came in anytime.",
        "Teacher: ..." + pm + " You" + pg + " what's with that mask...?" + pg + " Ah, no, it can't be. Anyway, get out quickly."
    ],
}

E139 = {
    0: [
        "Student: I thought the art club was having a streak of hardship, and now this. It wasn't the art club that's cursed, it was the whole school.",
        "Student: Hahaha" + pn + " what a relief..." + pm + " Boo-hoo-hoo-hoo."
    ],
}

E140 = {
    0: [
        "Student: This is definitely a curse! The haunted house's curse! They should've stuck to SEBEC, but they dragged us in too! Geez, what a nuisance!"
    ],
    1: [
        "Student: Even with demons around, I get hungry..." + pm + " If you use the secret shortcut, you might be able to go out to eat something, dude.",
        "Student: ..." + pn + " But it's still scary, dude!"
    ],
}

E141 = {
    0: [
        "Student: See, I told you so! SEBEC is making biological weapons!"
    ],
}

E142 = {
    0: [
        "Student: This has become a serious mess. No time to talk about gambling. When will it be resolved..." + pm + " ..." + pt + " Hey, wanna bet on when it'll be resolved?"
    ],
}

E143 = {
    0: [
        "Student: That dream really was a premonition. But it seems the blue room was unrelated..."
    ],
}

if __name__ == '__main__':
    for n, d in ((103, E103), (104, E104), (105, E105), (106, E106), (107, E107), (109, E109), (110, E110), (111, E111), (114, E114), (128, E128), (129, E129), (130, E130), (131, E131), (132, E132), (133, E133), (134, E134), (138, E138), (139, E139), (140, E140), (141, E141), (142, E142), (143, E143)):
        apply('E2', n, d, {})
