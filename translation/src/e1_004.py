"""E1 entries 4-9 - recruiting Nanjo, Elly and Kurouri; Brown and Toro; Toro's confession."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

E4 = {
    18: ["Ayase: Actually..."],
    19: [
        "Nanjo: Hm, I understand. If we save Saeko-sensei from this Snow Queen or whatever, the school will return to normal?"
    ],
    20: "=Surely you do not expect<FF03>me to help?<FF03><FF0E>き<FF01>",
    21: [
        "Nanjo: It cannot be helped.",
        "Nanjo: If you insist that much, I will not refuse to help. Chasing after Sonomura and the others comes after that."
    ],
    22: [
        "Nanjo: It cannot be helped.",
        "Nanjo: If you insist that much, I will not refuse to help. Chasing after Sonomura and the others comes after that.",
        "Nanjo: Come to think of it, I heard there was a commotion in the cafeteria. There may be some clue."
    ],
    23: [
        "Nanjo: Naturally. I will look for a way out of here in my own manner."
    ],
}

E5 = {
    0: ["Elly: How is it, Kurouri-kun?" + P('ほ') + " Have you found anything?"],
    1: [
        "Kurouri: Hehehehe... Of course, Kirishima-san.",
        "Kurouri: This is" + P('ほ') + " ..." + P('ほ') + " ..." + P('ほ') + " ..." + P('ほ') + " ..." + P('ほ') + " not the work of a cold front! No, really."
    ],
    2: ["Elly: ..."],
    3: [
        "Kurouri: Heeey, sorry...",
        "Kurouri: I don't know anything~ Because, well~ It isn't in any book."
    ],
    4: [
        "Elly: Oh... I see. Then I shall investigate on my own. This door also interests me."
    ],
    5: ["Elly: It says \"Tower of Nemesis\" in Greek letters."],
    6: ["Kurouri: Nemesis? Hmm~ Greek rice scoops? Hmmmm~"],
    7: ["Elly: Nemesis is the god who symbolizes vengeance."],
    8: [
        "Yukino: Hey, Kurouri looks like he knows about demons and the occult. Wouldn't he be pretty useful?",
        "Yukino: I think it'd be good to have someone like that in the party."
    ],
    9: [
        "Nanjo: Hm, a good idea. Indeed, we are currently ignorant of demons.",
        "Nanjo: Know the enemy and know yourself, and you will not fear a hundred battles. Even the art of war says to know the enemy first."
    ],
    10: [
        "Ayase: Ehh~ But, well. To put it mildly, he's not my type~",
        "Ayase: Ayase passes."
    ],
    11: [
        "Yukino: That's putting it mildly? And whether he's your type doesn't matter right now.",
        "Yukino: Well, he does look unreliable, though."
    ],
    12: [
        "Ayase: Hey, hey, what about Kirishima? She'd probably translate if we met foreign demons."
    ],
    13: [
        "Yukino: Come to think of it, she does know about that stuff. Yeah, maybe she'd be good."
    ],
    14: [
        "Elly: What have you been talking about?",
        "Elly: I did not mean to eavesdrop, but my name came up, so I was curious."
    ],
    15: [
        "Yukino: Oh, no. Good timing. We were just saying there's someone who seems to know about demons. Actually..."
    ],
    16: [
        "Elly: Oh! So that is why the school is wrapped in ice. How interesting.",
        "Elly: I like stories with Monsters and Ghosts, but...",
        "Elly: to think they would become reality one after another like this."
    ],
    17: "=Somebody has to do something<FF03>soon.<FF03><FF0E>き<FF01>",
    18: [
        "Elly: OK!",
        "Elly: Let us search for the \"Fragments of the Demon's Mirror\" to save Saeko-sensei."
    ],
    19: [
        "Elly: OK!",
        "Elly: Let us search for the \"Fragments of the Demon's Mirror\" to save Saeko-sensei.",
        "Elly: Come to think of it, I heard something happened in the cafeteria. Have you gone to see?"
    ],
    20: ["Elly: If there is anything I can help with, please do not hesitate to say so."],
}

E6 = {
    0: [
        "Brown: H-Hey, Toro! I'm sorry I hid the food from you, so",
        "Brown: please, don't eat any more! It's a waste!!"
    ],
    1: [
        "Student: Sorry. I thought if you found it, you'd eat it all.",
        "Student: We have to manage it properly. The school is in trouble right now! Please understand."
    ],
    2: [
        "Toro: S-Shut up~!! Everyone's making a fool of me!",
        "Toro: You were going to split up the food behind my back! Damn it, I'll eat it all out of spite!!"
    ],
    3: [F6('い') + "Yokouchi Kenta<FF03>Nicknamed Toro. Loves to eat. Strong, but timid." + F6(0)],
    4: [
        "Brown: It's precious food! You'll go berserk from a broken heart and we'll all starve to death together?",
        "Brown: Aah, is my glorious life supposed to end like this? Dying together with a fat guy..."
    ],
    5: [
        "Toro: Aaaaaaaaaaaaah D-D-D-D-D-Don't call me faaaaat!!",
        "Toro: Daaaamn iiiit! I'll eat before I starve! Eat and eat and multiplyyyy!",
        "Toro: I'll watch everyone drop, flop flop flop flop flop! Uha uha uha uha uha uhaaa"
    ],
    6: [
        "Student: H-Hey... His eyes are gone, this guy. What do we do, Brown?"
    ],
    7: [
        "Brown: W-What do we do, you ask? Damn it, Ayase! This is because you turned him down!!"
    ],
    8: ["Ayase: Heyyy~! Why is it Ayase's fault~!?"],
    9: ["Yukino: No choice. Let's put him to sleep."],
    10: [
        "Toro: Uhaha uhaha uhaaa It's no use~",
        "Toro: I have a Demon given to me by the butterfly!",
        "Toro: I'm no longer a lump of meat, Ayase-san. Uha uha uha uha uha uhaaa"
    ],
    11: ["Brown: A demon-sama~? This guy's bad. The shock of heartbreak made him go nuts."],
    12: ["Elly: What!? Could it be a Persona...?"],
    13: ["Student: I'll go get a teacher! Keep an eye on him until then!"],
    14: ["Toro: Uha uha uha uha uha uha, no matter how many of you there are, you can't stop me~"],
    15: [
        "Nanjo: Calm down, Yokouchi!",
        "Nanjo: When the town returns to normal, I will let you eat your fill of dishes made by our chef!"
    ],
    16: [
        "Ayase: Toro! Why are you doing this!",
        "Ayase: This makes it look like Ayase is the bad guy!!"
    ],
    17: [
        "Toro: Aaah, my Ayase-san! If you'll go out with me, I'll help only you!",
        "Toro: I'll save your share of the food for you~",
        "Toro: Uha uha uha uha uha uhaaa"
    ],
    18: ["Ayase: Rejected." + P('み') + " The worst." + P('み') + " Pass."],
    19: [
        "Toro: Uoooooooooooooh! Damn damn damn! A loser like me, a loser like meeeee!"
    ],
    20: [
        "Yukino: H-Hey, don't provoke him! Yuka's too blunt!",
        "Yukino: You said harsh things when he confessed, too, didn't you!?"
    ],
    21: [
        "Ayase: Not really~ I just told the truth. Like this" + P('ほ') + " ..." + P('ほ') + " ..."
    ],
    22: [
        "Brown: Big sis! This time, you gotta use your power to knock him senseless, or he won't wake up!"
    ],
    23: [
        "Yukino: Who're you calling big sis! Geez, you're such a smooth talker.",
        "Yukino: That's the last resort. For now let's buy time until the teacher comes!",
        "Yukino: Hey, Uesugi! Don't just stand there spacing out, help us out already!!"
    ],
    24: ["Brown: Dehyahyahyahya! I'll follow you to the ends of the earth."],
    25: [
        "Brown: Boo-hoo-hoo! What a thing to say to him!!",
        "Brown: It's not too late! Apologize! Go apologize!!"
    ],
    26: [
        "Nanjo: It is no wonder Yokouchi is angry. Truly, \"the mouth is the root of calamity,\" as they say...",
        "Nanjo: You went too far, Ayase! Apologize!"
    ],
    27: [
        "Ayase: Ehh~!? Did I go too far?",
        "Ayase: Hey, Toro, did it hurt to hear the truth?"
    ],
    28: [
        "Toro: Ugh... Ayase-san, you are...",
        "Toro: The price for hurting my pure heart is steep~",
        "Toro: Demon-sama, Demon-sama, please come out!",
        "Toro: Come out and punish the people who made fun of me!!",
        "Toro: ...Bimbur..." + P('ほ') + " Bambur..........." + P('ほ') + " Bambobbun.........................."
    ],
    29: [
        "Brown: Hey hey hey hey hey, what are you chanting, Toro?",
        "Brown: Doing that won't do anything, you know, this ain't a manga..."
    ],
    30: [
        "Ayase: ? What are you chanting?",
        "Ayase: Even in high school, stop dreaming of \"Demon-sama\" and..."
    ],
    31: ["Toro: Ugh... uuugh... uuuu... I'm being born~!!"],
}

E7 = {
    0: ["Ayase: So what's this important talk? Ayase is busy right now!!"],
    1: [
        "Toro: A-A-Ayase-san... U-Um um um um um um",
        "Toro: I'm sorry for calling you out like this."
    ],
    2: [
        "Ayase: What, you're so slow. If there's nothing, I'm going home!",
        "Ayase: Later."
    ],
    3: [
        "Toro: W-Wait! I'll say it, I'll say it, I'll say it.",
        "Toro: ...Is that okay?"
    ],
    4: ["Ayase: Hurry up and finish! I'm meeting someone!!"],
    5: ["Toro: ......................Ayase-san.................. ...I" + P('み') + " ...I..."],
    6: ["Ayase: I?"],
    7: [
        "Toro: I love yoooooooou! I really" + P('ぶ') + " love yoooooooou!!",
        "Toro: P-Pl-Please go out with me!!",
        "Toro: I'll definitely make you ha-" + P('つ') + " hap-" + P('つ') + " happy!" + P('つ') + " I'll d-do it!",
        "Toro: *Huff* *Puff*"
    ],
    8: [
        "Ayase: ..." + P('つ') + " ..." + P('つ') + " ..." + P('つ') + " ..." + P('つ') + " ..." + P('つ') + " ..." + P('つ') + " ..." + P('つ') + " ..." + P('つ') + " Say that kind of thing after you look in a mirror.",
        "You're a pass for me.",
        "Well, Ayase's going now."
    ],
    9: [
        "Toro: W-Wait!! Why a pass? What's wrong with me?"
    ],
    10: [
        "Ayase: You're fat and slow, you only smile no matter what people say to you, you always wear the same shirt,",
        "Ayase: I've only ever seen you sleeping, reading manga, or eating. What's even fun for you?",
        "Ayase: Everything about you is no good! Ayase doesn't get it."
    ],
    11: [
        "Toro: H-How cruel... Then... what's fun for Ayase-san?",
        "Toro: Don't you laugh even when you're not having fun, or go along with everyone even if you think it's dumb?",
        "Toro: Are you afraid of being alone?"
    ],
    12: [
        "Ayase: S-Shut up! You're a lump of meat, so don't talk like you know anything!"
    ],
    13: ["Toro: A lump... of meat..."],
}

E9 = {
    0: ["Brown: Fugaaa~?? Someone came out of me, hello."],
    1: ["Ayase: What was that just now..."],
    2: ["Nanjo: That? We decided to call it a Persona."],
    3: ["Elly: At least for now, it does not seem to be an enemy."],
    4: ["Yukino: We've got another companion."],
    5: ["Brown: Companion?"],
    6: [
        "Ayase: What's that supposed to mean? <FF0F>あ, Mayuzumi and the others... Don't tell me they're all that, y'know, that thing?"
    ],
    7: [
        "Nanjo: I do not know what that thing is, but there is one thing we certainly have in common."
    ],
    8: [
        "Yukino: Yeah. Ever since that weird dream, we seem to be able to call that... Persona, was it?"
    ],
    9: [
        "Elly: For some reason, only those who saw that butterfly in a dream seem to have gained power.",
        "Elly: It also seems to have some connection with this demon trouble."
    ],
    10: [
        "Ayase: Eek! Toro used a Persona too! Did he also dream of a butterfly?"
    ],
    11: [
        "Nanjo: Yes. Probably.",
        "Nanjo: That must be how he became able to use a Persona."
    ],
    12: ["Elly: Yes. Probably."],
    13: [
        "Ayase: Whaaaaat!? No wayyyyy! I can't believe iiiit!!",
        "Ayase: Then, then, will something go pee" + P('そ') + " pee" + P('そ') + " pee" + P('そ') + " out of Ayase's belly too!?"
    ],
    14: [
        "Elly: " + P('つ') + " ..." + P('つ') + " ..." + P('つ') + " I do not think so. Like a Knife, it all depends on how you use it.",
        "Elly: Depending on usage, it can help people or hurt them. In other words, it is the character of the one who holds it."
    ],
    15: [
        "Nanjo: I disagree. Even the same power can be used differently by each person.",
        "Nanjo: Dynamite has the power to kill people, but it can also open tunnels.",
        "Nanjo: In short, it is the character of the one who holds it. If one uses the power for desire, it is a case of getting what one deserves."
    ],
}

if __name__ == '__main__':
    for n, d in ((4, E4), (5, E5), (6, E6), (7, E7), (9, E9)):
        apply('E1', n, d, {})
