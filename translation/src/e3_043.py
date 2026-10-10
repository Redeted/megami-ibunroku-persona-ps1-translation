"""E3 entries 43-88 - masked boy, the Eternal Night begins, Kumi's memories, Agasthya tree, Nemesis tower rooms."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

p = P('ほ'); pc = P('か')
H = F6('う') + "*" + F6('　')

E43 = {
    2: ["Nanjo: A size that rivals my own home. Impressive."],
    3: ["Brown: Phew~ Let's catch our breath."],
    4: [
        "Elly: I have been curious for a while... <FF07>あ, what are you fighting for?"
    ],
}

E44 = {
    0: ["Masked Boy: What is it?"],
    1: "=Do you wish to return<FF03>to the floor below?<FF03><FF0E>と<FF01>",
    2: [
        "Masked Boy: I see. Then aim for the top floor quickly. The Queen awaits."
    ],
    5: [
        "Masked Boy: Oho. At this late stage, you return to the starting point? Well, that is fine too."
    ],
    6: ["Yukino: What's he plotting?"],
    7: [
        "Ayase: Since he was kind enough to say that, let's ask him when we wanna go back."
    ],
    9: [
        "Brown: Hey hey, you're not gonna say we should go back after coming all this way, are you?"
    ],
    10: [
        "Elly: Be careful. It has not been determined that it is not a Demon."
    ],
}

E48 = {
    0: ["Elly: W" + p + " What!?"],
    1: ["Brown: Hey hey hey hey."],
    2: ["Ayase: N-" + p + " No! What is this!?"],
    3: [
        "Yukino: The \"Eternal Night\"!? Don't screw with me! You called yourself the \"Queen of the Night,\" didn't you? Come out from hiding!",
        "Yukino: Fight fair and square!!"
    ],
    4: [
        "Queen of the Night's Voice: Kukukuku... You too shall become an ice statue.",
        "Kurouri's Voice: Hiiii~ S-" + p + " Stop..." + p + " gh......"
    ],
    5: ["Elly: !! It is from inside the school building!"],
    6: ["Nanjo: That fiend! What is she doing inside the school building!?"],
    7: [
        "Queen of the Night's Voice: Ahahahaha... Come, come, if you don't run, you'll freeze, you will.",
        "Toro's Voice: Waaah, stop stop stop stop" + p + " stop it!",
        "Natsumi-sensei's Voice: Hey! Who" + p + " are you!?" + p + " Gyaaaaaaaaaaah" + p + " aaah" + p + " ......"
    ],
    8: ["Ayase: Toro? Natsumi-sensei!? No..." + p + " way......"],
    9: ["Yukino: Saeko-sensei!?"],
    10: [
        "Saeko-sensei: Nearly everyone in the school building has been frozen. Before the Queen returns, somehow at least you all..."
    ],
    11: ["Student's Ghost: Please, at least you all, escape!!"],
    12: ["Ayase: E-" + p + " Escape, but how!?"],
    13: [
        "Student's Ghost: With the last of our remaining power, we will send you outside the school building."
    ],
    14: [
        "Yukino: Us alone, tucking our tails and running away! We can't..."
    ],
    15: [
        "Saeko-sensei: She's coming back! There's no time!! Now, ready?",
        "Saeko-sensei: <FF0F>あ! I'm counting on you to look after everyone!! Everyone" + p + " survive..."
    ],
    16: ["Yukino: Sen" + pc + "sei" + pc + "ei" + pc + "ei" + pc + "ei" + pc + "!!"],
}

E65 = {
    4: "=It'll cost 1000 yen, okay?<FF03><FF0E>　<FF01>",
}

E66 = {
    1: [
        "Mariko: Huh? They don't sell film... Aah! Geez, the worst!"
    ],
    3: [
        "Yukino: From Demon Mountain? Then is this kid a demon too?"
    ],
    6: [
        "Brown: Dehya~ What is this kid, selling dangerous stuff. Well, whatever, such a petty matter."
    ],
    7: [
        "Elly: That child seems to be a merchant of death from the Demon world?"
    ],
}

E67 = {
    4: [
        "Brown: Oh oh, this looks like it's just right for me! Man, I look good in whatever I wear! Nahahaha"
    ],
}

E68 = {
    0: [
        "Yukino: The time limit is until the clock hands point to twelve, huh. Pretty strict."
    ],
    1: ["Ayase: Ever since coming to this tower, Ayase is super sleepy!"],
    2: [
        "Nanjo: That Snow Queen must be watching us collect \"mirror fragments\" from somewhere and sneering at us."
    ],
    3: [
        "Brown: Hey? Aren't you feeling sleepy or something? No, seriously."
    ],
    4: [
        "Elly: What kind of opponent do you suppose this Tower's Boss is?"
    ],
}

E69 = {
    0: [
        "Kumi's Father: ...Practicing for club activities this late, Kumi? What do you even go to school for?",
        "Kumi's Father: To study? Or to play?"
    ],
    1: ["Kumi: ......U-Um... But... I was chosen for the \"Snow Queen\"..."],
    2: [
        "Kumi's Father: Your mother told me. You got a score in the 70s on the last test.",
        "Kumi's Father: You get such low scores because you do nothing but play without studying."
    ],
    3: ["Kumi: ...But... the average was... ...eighty..."],
    4: [
        "Kumi's Father: Who do you think I work and earn money for, cutting back on the drinking and smoking I love and even stopping my weekend golf?",
        "Kumi's Father: To support you and your mother, isn't it?",
        "Kumi's Father: Kumi, you can go to school now because your father works up a sweat."
    ],
    5: ["Kumi: ............Yes."],
    6: [
        "Kumi's Father: Yet you, not even considering your father's hard work, don't study and lose yourself in things like club activities and playing around.",
        "Kumi's Father: It's your fault, Kumi, isn't it."
    ],
    7: ["Kumi: ............I'm sorry..."],
    8: [
        "Kumi's Father: Good, good. You understand, Kumi. Quit the club and study properly.",
        "Kumi's Father: Study more and more, get into a good company, and repay your father and me. Ha ha ha..."
    ],
}

E70 = {
    0: [
        "Kumi: ...Why does everyone blame me? What did I do? Whether I do something or do nothing, it's always... yes, always.",
        "Kumi: The world around me, the people around me, everyone, everyone is filled with malice and hostility... I feel like I don't have a shred of freedom.",
        "Kumi: In this space called reality, among the people living in this reality... maybe I'm not supposed to exist.",
        "Kumi: A world that gently surrounds me, people who gently surround me, everyone, everyone filled with goodwill and kindness. A world where I can live freely...",
        "Kumi: That's a dream, isn't it...",
        "Kumi: \"Dream\"? \"Dream\"... Heh... Only when I'm sleeping in bed like this...",
        "Kumi: Nobody complains to me... The only free world left to me. The \"world of dreams\"...",
        "Kumi: I wish I could just go to the world of dreams like this... To a \"world of dreams\" just for me, for me alone..."
    ],
}

E71 = {
    0: [
        "Agasthya Tree: Hoho. Young one, you seem quite tired. It would be fine to end your journey here for a while and rest.",
        "Agasthya Tree: However, I cannot record your journey. I am only keeping it until your next departure.",
        "Agasthya Tree: Do not forget that..."
    ],
    1: "=Agasthya Tree: Shall you<FF03>pause your journey?<FF02><FF03><FF0E>　<FF01>",
    2: ["Agasthya Tree: Young one... I shall keep the memory of your journey."],
}

E72 = {
    0: [
        "Yukino: We've come up quite far. We're near the finale. Gotta pull ourselves together!"
    ],
    1: ["Ayase: Ugh, I'm tired~ Geez! Isn't there an elevator or something?!"],
    2: [
        "Nanjo: Even if you obtain fine weapons and armor, it is a \"waste of treasure\" if you do not equip them. We must check from time to time."
    ],
    3: ["Brown: Gaah! I'm beat! Let's take a short breather."],
    4: [
        "Elly: We managed not to fall Asleep somehow. Let us go on without letting our guard down."
    ],
}

E82 = {
    1: [
        "Mariko: According to my investigation, aliens are involved in this \"school freezing incident\"!",
        "Mariko: Have you been abducted by a UFO in the past two or three days?"
    ],
    3: [
        "Yukino: Hey, why does the salesgirl have the same face at every weapon shop?"
    ],
    4: ["Ayase: Hey~ It smells like oil in here!"],
    5: ["Nanjo: Amazing!! Nothing but extremely maniacal goods."],
    7: [
        "Elly: Where in the Demon world did that child source these weapons?"
    ],
}

E83 = {
    1: [
        "Yukino: This tower has no time limit. Let's pick carefully and go."
    ],
    2: ["Ayase: Hey~ This is super cute! " + H],
    3: [
        "Nanjo: Buying good armor is like taking out insurance on one's life."
    ],
    4: [
        "Brown: Oh oh, this one's like it's telling me to wear it! There are indeed clothes suitable for a good-looking man, yeah. Nahahaha"
    ],
    5: ["Elly: Why do the armor shop owners all wear Masks, I wonder?"],
}

E84 = {
    0: [
        "Yukino: What a grandiose door. That showy feel is so Michiko, it makes me sick!"
    ],
    1: ["Ayase: I wonder if that Michiko girl has played the \"Snow Queen\" too."],
    2: [
        "Nanjo: Hmph! A door as unpleasant as that woman! Flashy only on the surface and seemingly empty inside!"
    ],
    3: ["Brown: I wanna take it home to my room! Yeah yeah, a cool door."],
    4: [
        "Elly: Umm... It is too obvious for a door meant as a Trap."
    ],
    5: "=Open the door?<FF03><FF0E>　<FF01>",
}

E85 = {
    0: [
        "Yukino: Hey, again! What is with this grandiose door!? Wasn't there a similar room before?"
    ],
    1: [
        "Ayase: Somehow we never reach the top floor! Ayase is tired!!"
    ],
    2: [
        "Nanjo: Damn! I sense the malice of that Michiko woman everywhere!!"
    ],
    3: [
        "Brown: Miss Yukino's right! There was a room like this downstairs too!"
    ],
    4: [
        "Elly: This tower seems much taller than it looks from outside. Is it my imagination?"
    ],
}

E86 = {
    0: ["Yukino: How awful! The oppressive feel of this tower!"],
    1: ["Ayase: I wonder if Toro and Kurouri are okay?"],
    2: [
        "Nanjo: This time even I shall be serious! I cannot forgive that Michiko!"
    ],
    3: [
        "Brown: Alright! Michiko's room must be near now! Time to check our equipment!"
    ],
    4: [
        "Elly: Phew, it is tiring both mentally and physically. Is this also Michiko's doing?"
    ],
}

E88 = {
    0: [
        "Mariko: I can hear screams and groans from the room next door! It must be a poltergeist!",
        "Mariko: Don't you know? It's a \"noisy spirit phenomenon\"!!"
    ],
    1: [
        "Yukino: No time limit is rather creepy. I think we'd better hurry."
    ],
    2: ["Ayase: This tower is, like, super creepy? Let's get out quick~"],
    3: [
        "Nanjo: But I dislike that Michiko woman! It is unpleasant! Truly unpleasant!!"
    ],
    4: [
        "Brown: Hey hey! This tower has no time limit, right? Let's take a break!",
        "Brown: Let's go easy! Easy breezy!"
    ],
    5: [
        "Elly: Shall we hurry on as much as possible? I have a bad feeling."
    ],
}

if __name__ == '__main__':
    for n, d in ((43, E43), (44, E44), (48, E48), (65, E65), (66, E66), (67, E67), (68, E68), (69, E69), (70, E70), (71, E71), (72, E72), (82, E82), (83, E83), (84, E84), (85, E85), (86, E86), (88, E88)):
        apply('E3', n, d, {})
