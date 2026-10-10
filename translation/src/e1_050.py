"""E1 entries 50-65 - Tower of Hypnos: dream worlds, Kumi and Hypnos."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

p = P('ほ')

E50 = {
    7: ["Tamaki-chan: Yes! * I understand, my darling..."],
    8: [
        "Nanjo: I have no intention of speaking ill of these two, but I cannot bear to watch...",
        "Nanjo: In many ways."
    ],
    9: [
        "Elly: T-They look so happy... It feels wrong to speak to them."
    ],
    10: [
        "Tadashi-kun: See, can you see yourself in my eyes?",
        "Tadashi-kun: And I can see myself in your eyes... Ahh... we are one!"
    ],
    11: [
        "Tamaki-chan: Ah, Tadashi is in my eyes. *",
        "Tamaki-chan: Ahh, I can see myself in Tadashi's eyes... We've become one!"
    ],
    12: [
        "Yukino: ............... Phew... Let's have them continue after they wake up.",
        "Yukino: Let's wake them quickly."
    ],
    13: ["Yukino: Being inside someone else's dream is uncomfortable after all. Somehow."],
    14: ["Ayase: So those two had a flavonoid relationship. So enviable."],
    15: ["Nanjo: \"No, no\" means \"yes,\" as they say. Hmph, men and women are interesting..."],
    16: [
        "Brown: Uuugh... Please! Leave heartbroken me alone for a while...",
        "Brown: Ahh... Tamaki-chan..."
    ],
    17: [
        "Elly: Judging from this clubroom, I would never imagine this is the \"Anti-Dream Realm.\""
    ],
    18: [
        "Tadashi-kun: Ah! Ahh! You're noisy! And I was in a good part!",
        "Tadashi-kun: What a rude person you are!"
    ],
    19: "=Pinch Tadashi-kun?<FF03><FF0E>　<FF01>",
    20: ["Tamaki-chan: You're noisy. I won't forgive you for getting in the way!"],
    21: "=Pinch Tamaki-chan?<FF03><FF0E>　<FF01>",
    22: ["Tadashi-kun: H-Huh? What?"],
    23: ["Tamaki-chan: Eh? W-Why?"],
    24: ["Tadashi-kun: Could you just leave us alone~?"],
    25: ["Tamaki-chan: Go somewhere. I'll get angry."],
}

E51 = {
    0: ["Yukino: Why is there a convenience store in a dream?"],
    1: ["Natsumi-sensei: Hey, what do you want to eat tonight?"],
    2: ["Teacher's Boyfriend: You, of course! Just kidding! Nahahaha"],
    3: [
        "Nanjo: Oh, Natsumi-sensei's dream. Then that must be the man she broke up with recently.",
        "Nanjo: Not as good as I am, but a decent man. He looks stupid, though."
    ],
    4: [
        "Brown: Huh? Isn't that the boyfriend Natsumi-sensei broke up with the other day?",
        "Brown: Well, he's not as good as me, but he's pretty decent."
    ],
    5: [
        "Ayase: Kyaa! Sensei's boyfriend is super cool!",
        "Ayase: Ayase wants a boyfriend like that, too~"
    ],
    6: [
        "Natsumi-sensei: Oh, you're always joking! So, what do you want to eat? Hurry and decide.",
        "Natsumi-sensei: Let's go home quickly and eat our bento."
    ],
    7: [
        "Teacher's Boyfriend: Huh? Eh? Didn't you say you'd let me eat your \"home cooking\" today?"
    ],
    8: [
        "Nanjo: Hey, hey. Surely Natsumi-sensei does not intend to feed a man a convenience store bento",
        "Nanjo: and call it \"home cooking\"? That is a misuse of the language, sensei."
    ],
    9: [
        "Elly: Natsumi-sensei... Surely she does not intend to feed him a bento bought here",
        "Elly: and call it \"home cooking\"? The use of the language is wrong... sensei."
    ],
    10: [
        "Natsumi-sensei: Yes, I did say that. When we get to my place, I'll properly warm it up in the microwave, \"myself.\"",
        "Natsumi-sensei: How about this \"Surprise Cosukisu Cutlet Bento\"? It's a new product! Doesn't it look delicious!",
        "Natsumi-sensei: Hey, let's get two of these! Okay? Okay?"
    ],
    11: [
        "Teacher's Boyfriend: ......Ah... Ahh... Anything's fine... My chest is kind of full...",
        "Teacher's Boyfriend: Nahaha..."
    ],
    12: [
        "Yukino: I can't watch this, in many ways. Let's wake them quickly and move on."
    ],
    13: ["Yukino: Still, no wonder a guy would run away from a woman like that."],
    14: ["Ayase: Hey, hey, is the food here okay for Ayase and the others to eat?"],
    15: [
        "Nanjo: This place is eerier than a late-night convenience store with no clerks or customers."
    ],
    16: ["Brown: Can't we bring the stuff in this store back to the real world? What a waste..."],
    17: [
        "Elly: Great!! That the human power of dreaming could create such a Real space!",
        "Elly: This convenience store looks completely genuine!"
    ],
    18: [
        "Natsumi-sensei: Hey! What is it, you!",
        "Natsumi-sensei: If you do anything weird, I'm calling the police!!"
    ],
    19: "=Pinch Natsumi-sensei?<FF03><FF0E>　<FF01>",
    20: ["Teacher's Boyfriend: What the hell! You! You got business with us, huh!"],
    21: ["Natsumi-sensei: N-No way. What?"],
    22: ["Natsumi-sensei: Go away!"],
}

E53 = {
    0: [
        "Yukino: What!? This place has a different atmosphere from the rooms so far. Is this someone's dream too?",
        "Yukino: Huh? Someone's in the back!"
    ],
    1: ["???: ...Oh my... We have a guest... How unusual."],
    2: ["???: That's right... Shall we entertain them?"],
    3: [
        "Nanjo: What is this? She is wearing our school uniform. Is this her dream?"
    ],
    4: [
        "Brown: Whoa! What a cute girl! Huh!?",
        "Brown: What the heck! She's wearing our school uniform!!",
        "Brown: Did I, of all people, fail to check her out?"
    ],
    5: [
        "Ayase: Hey, you. What class are you in, and who are you? Are you locked up here too?"
    ],
    6: [
        "???: Hee hee. Why are you all here?",
        "???: This is a dream of mine, by me, for me alone.",
        "???: Yes, the dream of me, \"Hirose Kumi,\" entrusted by the Snow Queen with guarding this \"Tower of Hypnos.\"",
        "???: Barging into someone else's dream with muddy feet. What rude people. Right, Lord Hypnos?"
    ],
    7: [
        "Hypnos: That's right, Kumi. Someone else's dream is one thing, but entering Kumi's dream,",
        "Hypnos: what presumptuous fools.",
        "Hypnos: What shall we do, Kumi? If it's alright with you, I'll punish them a bit."
    ],
    8: [
        "Nanjo: The lord of the tower? Then you are the ones who put the people of the school to sleep and lock them in the \"Anti-Dream Realm.\"",
        "Nanjo: Why not simply kill them? Why such a roundabout method?",
        "Nanjo: What are you plotting by confining human souls in the \"Anti-Dream Realm\"!?"
    ],
    9: [
        "Elly: The lord of the tower? Then you are the ones who put the people of the school to sleep and confine them in the \"Anti-Dream Realm.\"",
        "Elly: It should be easy for you to kill them all.",
        "Elly: For what purpose do you confine people's souls in the \"Anti-Dream Realm\"!?"
    ],
    10: [
        "Kumi: ...Heh... Hee hee hee... Asking such a thing, of all things...",
        "Kumi: Can't be helped. You too are unfortunate people forced to live in the real world.",
        "Kumi: It's obvious, isn't it? People are happiest living in dreams.",
        "Kumi: People can never be happy in the real world...",
        "Kumi: I'm just teaching everyone that. Right, Lord Hypnos?"
    ],
    11: [
        "Hypnos: That's right, Kumi. Kumi did nothing wrong. It's all their fault.",
        "Hypnos: But it's understandable that they can't understand Kumi.",
        "Hypnos: They have no idea how painful the real world was for Kumi, or with what feelings she came to this world of dreams.",
        "Hypnos: Come, let's show them. How harshly Kumi was treated in the real world.",
        "Hypnos: And let's teach them! The wonder of the world of dreams!!"
    ],
    12: ["Yukino: Wh-What!? What is this!!"],
}

E54 = {
    0: [
        "Drama Club President: Hirose-san, you've hardly shown up to drama club practice lately.",
        "Drama Club President: What good is the one playing the \"Snow Queen\" not showing up to practice for the \"Snow Queen\" play?!",
        "Drama Club President: Everyone is working so hard, and you don't mind being the only one who doesn't come!?",
        "Drama Club President: Do you have any awareness as a member entrusted with an important role?!"
    ],
    1: [
        "Drama Club Member: That's right, Kumi. Being chosen as the \"Snow Queen\" over the president, and now this? Not cool.",
        "Drama Club Member: Don't tell me you're getting a big head over it?"
    ],
    2: [
        "Drama Club Member: But seriously, it's a problem if you don't come to practice at least a little.",
        "Drama Club Member: I can only fill in for your lines so much. What are you thinking, Kumi?"
    ],
    3: [
        "Kumi: ...Um... ...I... have to study... ...My grades... dropped... ...so my... parents... ...said forget... club... ...and study..."
    ],
    4: [
        "Drama Club Member: Whoa. As expected of the parents of the class's top grind! That's too much, Kumi.",
        "Drama Club Member: You got third in your year on the last test, too! What's the problem!"
    ],
    5: ["Kumi: ...Ah... because... it wasn't... first place..."],
    6: [
        "Drama Club Member: What's that! Is that sarcasm!? Don't get a big head just because you're a little smart!!",
        "Drama Club Member: If studying matters that much, just quit the club!!",
        "Drama Club Member: Frankly, you're a nuisance!"
    ],
    7: ["Kumi: ...I... ...I didn't mean... ...I..."],
    8: [
        "Drama Club President: Well, fine. So that is why you didn't come to club.",
        "Drama Club President: Hirose-san... are you looking down on me? No, on the club?",
        "Drama Club President: Do you understand how much trouble you cause people by not joining practice?",
        "Drama Club President: Do you truly understand how much trouble others suffer while you only attend to your own circumstances?",
        "Drama Club President: Hirose-san... what is your role right now within this group called the \"Drama Club\"?",
        "Drama Club President: If you cannot understand that, please leave this drama club."
    ],
    9: [
        "Drama Club Member: That's right! That's right! The president's right! Get out!",
        "Drama Club Member: You big-headed four-eyed monkey! A gloomy runt like you is unpleasant just by existing!"
    ],
    10: [
        "Drama Club Member: Sorry to say it, but the president has a point.",
        "Drama Club Member: Think carefully, Kumi. Which is more important, studying or youth? ...Or so I say."
    ],
    11: ["Kumi: ..............."],
}

E55 = {
    0: [
        "Yukino: Hmm............ So that's the \"reason\" you had to shut yourself in the world of dreams.",
        "Yukino: ...And so what?"
    ],
    1: [
        "Kumi: Y-You... You felt nothing seeing that? What kind of nerves do you have?",
        "Kumi: The Sn-Snow Queen... the mask understood my pain and sorrow right away...!!",
        "Kumi: You're the same as my father and those drama club people!",
        "Kumi: You've never tried to understand me from the start!"
    ],
    2: ["Hypnos: C-Calm down, Kumi! Calm down!!"],
    3: [
        "Nanjo: Honestly...! You ran into the world of dreams for such a trivial reason?",
        "Nanjo: I am speechless at the absurdity. Are you not making light of life?"
    ],
    4: [
        "Brown: Hey hey! Kumi-chan, don't you think you're taking life too seriously?",
        "Brown: ...I mean! Life is nothing but fun! Seriously! Let's go easy and breezy, like me!"
    ],
    5: [
        "Ayase: What's that! You just wanted to brag that you're good at studying!",
        "Ayase: Fine, Ayase is dumb! I can't believe this! Super mad!"
    ],
    6: [
        "Kumi: But... but......! What did I do? Whether I do anything or nothing!",
        "Kumi: Nobody says a kind word to me! I tried my best in my own way!",
        "Kumi: The people around me! The people around me! Right, Lord Hypnos!?",
        "Kumi: Right!? Isn't it so?! I'm not the one at fault, am I?"
    ],
    7: ["Hypnos: Of course! It's not Kumi's fault! The fault lies with..."],
    8: [
        "Nanjo: ...\"Other people\"? Hmph. Your way of life has been easy.",
        "Nanjo: You only had to run around blaming others for everything.",
        "Nanjo: And when you got tired of running, you play alone in a world of dreams?",
        "Nanjo: In the end you are a loser who fled to the world of dreams because you feared the real world and people."
    ],
    9: [
        "Elly: \"Other people,\" is it? Your way of life is easy, is it not?",
        "Elly: Blaming everything on others, complaining from a safe zone...",
        "Elly: Are you so afraid of dealing with other people?",
        "Elly: You really are a selfish and weak person."
    ],
    10: [
        "Kumi: W-Who do you think you are!? I'm happy now! I'm happy, I said!!",
        "Kumi: Only the Snow Queen's mask! Only Lord Hypnos! Saved me!",
        "Kumi: In the world of dreams, for the first time! For the first time! I got freedom!",
        "Kumi: Even if the world itself is a dream, the \"happiness\" in my heart is real!"
    ],
    11: [
        "Hypnos: Enough! It's enough... Kumi. Let's finish these guys.",
        "Hypnos: Then let's return to our happy dream, just the two of us."
    ],
    12: [
        "Yukino: Cut the tough act. This is the \"Anti-Dream Realm,\" isn't it?",
        "Yukino: Then you two here are phantoms created by the dream of \"Hirose Kumi,\" who's somewhere in the tower, right?",
        "Yukino: Which means if we pinch her awake, you two will vanish.",
        "Yukino: We'll wake you up right now! Rub your sleepy eyes, wash your necks, and wait for us to come!!"
    ],
    13: [
        "Yukino: That girl Kumi is the boss of this tower! So she'll have a fragment or two of the \"mirror,\" too."
    ],
    14: ["Ayase: Boo! Boo!! What a super annoying girl. Let's beat her quickly!"],
    15: [
        "Nanjo: What is with that woman! She is simply making light of life.",
        "Nanjo: I dislike that mistaken victim mentality of \"I alone am unhappy.\""
    ],
    16: [
        "Brown: Hmm... Life's tough, huh. I'm smart and have had it rough, so",
        "Brown: I kinda understand Kumi-chan's feelings."
    ],
    17: [
        "Elly: The \"Hypnos\" beside Kumi-san... I hope he is only an illusion of the ideal \"prince\" born of Kumi-san's dream, a product of imagination."
    ],
    18: [
        "Kumi: W-What! If you lay a hand on me, Lord Hypnos won't stay silent!"
    ],
    19: ["Hypnos: Don't touch Kumi! Insolent fools!"],
    20: "=Pinch Kumi?<FF03><FF0E>　<FF01>",
    21: ["Kumi: Ugh... How dare you! You'll remember this!!"],
    22: [
        "Kumi: G-Good call. If you had pinched me, it would have been terrible for you."
    ],
    23: ["Nothing seems to be there."],
}

E65 = {
    0: [
        "Tadashi-kun: ...It's okay. No matter what happens, I'll protect you.",
        "Tadashi-kun: So..." + p + " so believe in me and follow me! Tamaki! I love you!!"
    ],
    1: [
        "Tamaki-chan: We always fought, but it was because I was worried about Tadashi.",
        "Tamaki-chan: You never understood my feelings... If left alone, you always do reckless things.",
        "Tamaki-chan: But thanks to that dream, I can finally be honest... Tadashi..." + p + " I love you!"
    ],
    2: [
        "Yukino: Oh ho. There they go again. Never get tired of it.",
        "Yukino: Well, this means all three woke up safely. Are your bodies alright?"
    ],
    3: [
        "Tadashi-kun: Ah! Aaah! And in a good part! Don't interrupt!",
        "Tadashi-kun: Right, Tamaki-chan?"
    ],
    4: ["Tamaki-chan: ...Mayuzumi-san, everyone... Why are you here?"],
    5: [
        "Nanjo: You do not remember anything? What blissful people.",
        "Nanjo: A complete waste of time, saving them was for nothing. I am too appalled to speak."
    ],
    6: [
        "Brown: Huh! What the heck! You're cold, Tamaki-chan!",
        "Brown: After I worked so hard to save you...",
        "Brown: You don't remember anything? That's kind of not cool, isn't it? I'm super sad."
    ],
    7: [
        "Tadashi-kun: Remember or not, we..." + p + " ..." + p + " ..." + p + " ...Huh?? Why are we in a place like this?",
        "Tadashi-kun: I think... I was having a good dream... and when I woke up, Tamaki-chan was in front of me...",
        "Tadashi-kun: Tamaki-chan was looking at me too..."
    ],
}

if __name__ == '__main__':
    for n, d in ((50, E50), (51, E51), (53, E53), (54, E54), (55, E55), (65, E65)):
        apply('E1', n, d, {})
