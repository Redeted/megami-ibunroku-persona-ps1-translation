"""E1 entries 65-73 - first mirror shard, the teachers, Kumi's boss room."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

p = P('ほ')

E65 = {
    8: [
        "Yukino: Yeah yeah yeah yeah!! I get it" + p + " I get it! Congratulations! Thanks for the meal!!",
        "Yukino: More importantly, could you two tell me just this? Then we won't bother you two anymore.",
        "Yukino: So, does either of you have a \"mirror fragment\"? It's very important."
    ],
    9: [
        "Nanjo: Hm, I did not expect much from the start, but for the time being,",
        "Nanjo: does either of you not have it? A \"mirror fragment.\""
    ],
    10: [
        "Elly: It is something we absolutely need now to save the school.",
        "Elly: Do you have any idea?"
    ],
    11: [
        "Tadashi-kun: ..." + p + " ..." + p + " ..." + p + " ..." + p + " ..." + p + " ..." + p + " ...Nope!",
        "Tadashi-kun: All I've got is a hand mirror for doing my hair. Will this do?"
    ],
    12: [
        "Tamaki-chan: ...Geez! Stupid Tadashi! Of course it won't do!",
        "Tamaki-chan: ..." + p + " ..." + p + " ..." + p + " ..." + p + " ..." + p + " ..." + p + " !",
        "Tamaki-chan: Is this the \"mirror fragment\" Mayuzumi-san means? It seems it was in my pocket at some point..."
    ],
    13: [
        "Tadashi-kun: ...Whaaat!? Tamaki-chan!! I... I didn't hear you had something like that...",
        "Tadashi-kun: I didn't hear about it!! Ahh! Between the two of us who vowed our love" + p + " even though" + p + " even though!",
        "Tadashi-kun: Keeping secrets!! How cruel, how cruel!"
    ],
    14: [
        "Tamaki-chan: ...Hey! I only just noticed it myself!",
        "Tamaki-chan: Don't say things that sound bad! ...Be quiet for a moment!",
        "Tamaki-chan: Here, take this if it's okay, <FF0F>あ-kun.",
        "Tamaki-chan: ...Hee hee. Do you remember me saying \"it's your turn this time\"?",
        "Tamaki-chan: That really came true, huh. But I'm sure you'll do fine. Good luck!"
    ],
    15: [
        "Tamaki-chan: ...Hey! I only just noticed it myself!",
        "Tamaki-chan: Don't say things that sound bad! ...Be quiet for a moment!",
        "Tamaki-chan: Here, take this if it's okay, <FF0F>あ-kun.",
        "Tamaki-chan: Sorry, this is all I can do to help...",
        "Tamaki-chan: I really wish Tadashi and I could go with you.",
        "Tamaki-chan: But as we are now, we would only get in your way.",
        "Tamaki-chan: Thank you for saving us. Good luck."
    ],
    16: ["Obtained a \"Mirror Fragment\""],
    17: [
        "Tadashi-kun: Hmm, I don't really get it, but do your best!",
        "Tadashi-kun: Leave Tamaki-chan to me!"
    ],
    18: [
        "Ayase: Yay! Super lucky!! Got a \"mirror fragment\"!",
        "Ayase: It was worth the detour into the Anti-Dream Realm!!",
        "Ayase: Hey, hey!! If Tamaki-chan and Tadashi-kun had \"mirror fragments,\"",
        "Ayase: maybe Natsumi-sensei has one too?? Shall we ask?",
        "Ayase: Hey, hey, Natsumi-sensei? Don't you have a \"mirror fragment\"?! Hey, sensei" + p + " sensei" + p + " Sensei!",
        "Ayase: What about the \"mirror fragment\"?! You're awake, aren't you! Sensei!"
    ],
    19: [
        "Natsumi-sensei: ...You're noisy. I have low blood pressure... ow ow ow, my head hurts.",
        "Natsumi-sensei: So? A mir" + p + " ror" + p + " frag..?" + "".join(" ..." + p for _ in range(8)) + " Don't have one! ...Good night... zzz"
    ],
    20: ["Ayase: Tch. So Sensei doesn't have one. Waking her was for nothing!"],
    21: ["Yukino: Still half asleep, huh. Those two. Well, whatever."],
    22: ["Yukino: Well then, shall we go take down the boss?"],
    23: [
        "Ayase: There were rumors that Tadashi-kun sometimes goes totally wild,",
        "Ayase: so that's what it was. Mmm, super passionate."
    ],
    24: ["Ayase: Mm, Ayase wants a hot relationship like that with somebody too!"],
    25: [
        "Nanjo: Do those two still think they are in the Anti-Dream Realm?",
        "Nanjo: I do not know why we woke them."
    ],
    26: [
        "Nanjo: We have wasted a great deal of time. Now there are no complaints.",
        "Nanjo: Let us hurry on. We" + p + " ell, it was not bad that all three were safe."
    ],
    27: [
        "Brown: Damn it! Tamaki-chan must still be half asleep!",
        "Brown: Why Tadashi, and not me? I have a little doubt!"
    ],
    28: [
        "Brown: Thanks to my great efforts, all three are safe! Wahahahaha!!",
        "Brown: I tell you, I have outstanding leadership qualities!!"
    ],
    29: [
        "Elly: It is not that Hypnos's magic" + p + " still remains, is it?",
        "Elly: Truly, \"thanks for the meal.\""
    ],
    30: [
        "Elly: By coincidence, Hypnos became the Cupid of Tadashi-san and Tamaki-san's love, did he not?"
    ],
    31: [
        "Tadashi-kun: Ah! Aah! How annoying! Getting in the way of other people's love,",
        "Tadashi-kun: what a rude person you are! Later!!"
    ],
    32: ["Tadashi-kun: You're done with your business, right? Could you leave us alone, please?"],
    33: ["Tamaki-chan: You're going to interrupt me and Tadashi? I won't forgive you!"],
    34: ["Tamaki-chan: Sorry. Right now I can only think about Tadashi."],
    35: ["Natsumi-sensei: Zzz" + p + " ...zzzz... ...hee hee..." + p + " how is it?... ...del" + p + " ...icious?..."],
    36: [
        "Natsumi-sensei: Uuugh!! My eyes are wide awake, but my head hurts so much.",
        "Natsumi-sensei: The dream was nice, though... Something very good was interrupted..."
    ],
}

E66 = {
    0: [
        "Yukino: You've finally woken up, teachers!! Are your bodies okay?"
    ],
    1: [
        "Vice Principal Hanya: Ma" + p + " Mayuzumi!! What is the meaning of this!? Where is this!?",
        "Vice Principal Hanya: Don't tell me" + p + " it's your doing!",
        "Vice Principal Hanya: You delinquents! What do you intend by locking us in a place like this?!",
        "Vice Principal Hanya: Damn it! Damn it!! I don't remember, but it was a good dream!",
        "Vice Principal Hanya: Aaah! What on earth is going on! Somebody explain!!",
        "Vice Principal Hanya: *Huff* *Huff* ...P-Principal, say something to these delinquents too!"
    ],
    2: [
        "Principal Oishi: Have you calmed down, Vice Principal? Then" + p + " ......" + p + " ......Mayuzumi-san, everyone,",
        "Principal Oishi: are you hurt? ..." + p + " ..." + p + " ..." + p + " ..." + p + " If not, good. By the way, where is this?",
        "Principal Oishi: I was having a very unpleasant dream..."
    ],
    3: [
        "Nanjo: It may be hard for you teachers to understand, but as a result, you were saved by us.",
        "Nanjo: We are not saying \"thank us,\" but it is also misplaced to complain to us. I hope you understand that.",
        "Nanjo: More importantly, teachers, do you know anything about a \"mirror fragment\"? It is important to us."
    ],
    4: [
        "Brown: Vice Principal Hanya, calling us delinquents is harsh! \"Great me\" and my friends worked so hard to save the t" + p + "w" + p + "o of" + p + " you" + p + "!!",
        "Brown: A word of thanks would be nice..." + p + " Well" + p + " fine" + p + " who cares! It's in the past!",
        "Brown: More importantly, teachers, do you know about a \"mirror fragment\"?",
        "Brown: It's an item that \"Great me\" and my friends absolutely need to become the heroes who save the school. Don't you know?"
    ],
    5: [
        "Vice Principal Hanya: A \"mirror fragment\"??? " + p + " Oh, this?",
        "Vice Principal Hanya: It was in my suit pocket before I knew it. Honestly! Thanks to this, the bottom of the pocket tore!",
        "Vice Principal Hanya: My daughter is starting a job this year, and I can't ask her to mend something like this...",
        "Vice Principal Hanya: *Cough!* " + p + " *Cough cough*!! Ahh..." + p + " well, that's not important.",
        "Vice Principal Hanya: Yes..." + p + " it's not important!!",
        "Vice Principal Hanya: By the way! What do you intend to do with such a thing?! It's surely nothing good!",
        "Vice Principal Hanya: No" + p + " no" + p + " no" + p + " no! I feel that giving you the \"mirror fragment\" will make things worse."
    ],
    6: [
        "Ayase: Kyaaah!! What" + p + " what" + p + " what" + p + " what! You bald Hannya!!",
        "Ayase: You don't even listen to what Ayase says! Don't suddenly say no!! Super mad!!",
        "Ayase: That's why everyone hates you, unlike the principal! Hurry up and hand over the fragment!",
        "Ayase: You bald" + p + " bald" + p + " bald" + p + " bald" + p + " bald! You bastard! Hand it over!",
        "Ayase: Hand it over!"
    ],
    7: [
        "Principal Oishi: Now, now, Ayase-san, you mustn't, as a girl, use such dirty words.",
        "Principal Oishi: Vice Principal, before scolding students outright, please try looking at things from the students' eyes first.",
        "Principal Oishi: Then you will know immediately whether a child is lying. Scold afterward.",
        "Principal Oishi: Vice Principal, I ask you as well. Please give these children the \"mirror fragment.\"",
        "Principal Oishi: Children trying to do something wrong would not have such sincere eyes."
    ],
    8: ["Vice Principal Hanya: ..." + p + " ......" + p + " .........Take it."],
    10: [
        "Nanjo: Hmph. You should have handed it over honestly from the start.",
        "Nanjo: At this school, only we are walking the truly right path."
    ],
    11: [
        "Elly: Sorry. But this is also important for us, no, for saving the school."
    ],
    12: [
        "Principal Oishi: I won't ask the reason now. I can tell you are doing something right, something that does you proud.",
        "Principal Oishi: But please, don't do anything reckless. Never do anything that would make those who worry about you sad.",
        "Principal Oishi: Now go. Good luck."
    ],
    13: [
        "Vice Principal Hanya: Hmph! I won't stop you anymore. Go on your own!",
        "Vice Principal Hanya: ..." + p + " ......" + p + " ............Hey, you lot!",
        "Vice Principal Hanya: If... if the school returns to normal, everyone gather in the principal's office!",
        "Vice Principal Hanya: I'll lecture you personally. You'll explain this situation to me in full then!",
        "Vice Principal Hanya: Be prepared!! I'll be waiting with the principal!",
        "Vice Principal Hanya: Be sure" + p + " to come! All of you!"
    ],
    14: [
        "Yukino: P-Principal..." + p + " Vice Principal...",
        "Yukino: Heh..." + p + " Leave it to us! We'll keep our promise! Yeah!" + p + " For sure!"
    ],
    15: [
        "Yukino: There's nothing left to do in this room, is there? We should hurry on, probably."
    ],
    16: ["Ayase: Hee hee! Now the vice principal will totally see Ayase and the others in a new light!"],
    17: [
        "Nanjo: Though not worthy of respect, they are our teachers for the time being. Well, it is best that they are safe."
    ],
    18: [
        "Brown: Alright! Now Vice Principal Hannya owes \"Great me\" a big one!",
        "Brown: Kekeke! He can't act so high and mighty anymore!!",
        "Brown: ..." + p + " ......" + p + " ............" + p + " I can't say that to Hannya, can I... He's scary, that vice principal!"
    ],
    19: ["Elly: Whatever the case, I am glad the teachers are safe."],
    20: [
        "Vice Principal Hanya: Hmm. Still, it was a good dream...",
        "Vice Principal Hanya: Aah, I'm so close to remembering! What kind of dream was it...?"
    ],
    21: [
        "Principal Oishi: Still, I was having an unpleasant dream. I don't even want to remember it."
    ],
}

E73 = {
    0: [
        "Yukino: Whoa?! S-Space?! What is this room?",
        "Yukino: !? Who are you...? You??"
    ],
    1: [
        "???: Um... Nice to meet you, everyone. I was entrusted by the Snow Queen with guarding this tower.",
        "???: My name is \"Hirose Kumi.\"",
        "???: Um... and, I've been ordered to kill you all...",
        "???: ...What do you say? I'm not very keen on it either, so how about you just surrender quietly and live happily with us in the world of dreams?",
        "???: ...I'll spare your lives."
    ],
    2: [
        "Nanjo: What is this? \"I am Hirose Kumi\"?",
        "Nanjo: A girl like you, the guardian of this tower?? Do not make me laugh!",
        "Nanjo: You seem to be wearing our school's uniform... Are you a student here? Which year?",
        "Nanjo: If you are teasing us with a bad joke, I will not forgive it!",
        "Nanjo: Answer! What are you doing here!?"
    ],
    3: [
        "Brown: Hey hey hey... She's wearing our uniform, but who is she?",
        "Brown: A cute girl like you is the boss here? Quit joking.",
        "Brown: Am I dreaming?"
    ],
    4: [
        "Ayase: What are you saying!? You four-eyes! Don't make fun of us!",
        "Ayase: There's no way a gloomy, super weak-looking girl like you is the boss!!"
    ],
    5: [
        "Kumi: Hee hee hee... I'd like you not to judge people by appearances.",
        "Kumi: I'll kill you right now... you fools.",
        "Kumi: It's always been like this... Nobody tries to listen to me!",
        "Kumi: People really are just a bunch of idiots...",
        "Kumi: Fine. Please disappear from my sight."
    ],
    6: ["Nanjo: What!? This killing intent!! Could she truly be... going to attack us??"],
    7: [
        "Elly: Oh... My... What a sinister aura... Is she truly!?",
        "Elly: Everyone! Here it comes!!"
    ],
    8: [
        "Kumi: Hee hee hee hee. \"Lord Hypnos\"... \"Lord Hypnos\"... My prince... \"Lord Hypnos!\" Defeat them!",
        "Kumi: They're bad people who came to bully me!"
    ],
    9: [
        "Yukino: P-Persona!? I see... So that's how it is. No holding back, everyone! Let's go!"
    ],
    10: [
        "Yukino: ...Hmph! This seems to be the goal. Right?! Miss \"Hirose Kumi\"!",
        "Yukino: Sorry to keep you waiting... Now, I'll give you a taste!"
    ],
    11: [
        "Kumi: You've finally made it this far...",
        "Kumi: Trapped in the frame of dull reality, not knowing, and not even trying to believe,",
        "Kumi: that a paradise named \"dream\" exists in this world... Fools......!"
    ],
    12: [
        "Nanjo: Who is the fool here...!? You walked a life that knew only how to run,",
        "Nanjo: and even ran away from the very act of running, you loser!",
        "Nanjo: There is nothing more to say! Come at us!"
    ],
    13: [
        "Brown: Kumi-chan... Fighting a cute girl like you...",
        "Brown: It's tough for me! But it can't be helped...",
        "Brown: For the school!",
        "Brown: For justice!",
        "Brown: For me to stand out!!",
        "Brown: Please get beaten!"
    ],
    14: [
        "Ayase: Hee hee! A bookworm like you!",
        "Ayase: If five of us gang up on you, it's a piece of cake!",
        "Ayase: Apologize while you can!"
    ],
    15: [
        "Kumi: What fools, judging others only by their appearance...",
        "Kumi: \"Lord Hypnos!\"",
        "Kumi: Help me!!",
        "Kumi: Defeat them!!"
    ],
    16: [
        "Nanjo: What! That is!? That is the one from the \"Anti-Dream Realm\"! Was he not a product of her dream?"
    ],
    17: [
        "Elly: Surely not!? Kumi-san's... Persona!?",
        "Elly: The Hypnos of the \"Anti-Dream Realm\" was not a product of Kumi-san's dream after all!"
    ],
    18: [
        "Kumi: \"Lord Hypnos!\"",
        "Kumi: Now, defeat those who came to bully me even in my dreams!!"
    ],
}

if __name__ == '__main__':
    for n, d in ((65, E65), (66, E66), (73, E73)):
        apply('E1', n, d, {})
