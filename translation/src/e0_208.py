"""E0 entries 208-217 - Pandora's door, the school, Pandora, the ending."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

E208 = {
    12: [
        "Chisato: I'm the one who should apologize...",
        "Chisato: You called us here because you thought of me as a best friend, didn't you?",
        "Chisato: And I betrayed that Maki. I'm the one who needs to be forgiven.",
        "Chisato: The positions are reversed."
    ],
    13: ["Maki: Chisato... Thank you..."],
    14: [
        "Chisato: Now, off you go. So I don't get in your way, I'll wait here.",
        "Chisato: When everything's settled... let's all go to an amusement park or something. Okay, Maki?"
    ],
    15: ["Maki: ...Yeah."],
    16: [
        "Mark: Heh heh... An amusement park, huh. Going back to being a kid ain't bad.",
        "Mark: Alright, let's get this over with!"
    ],
    17: ["Nanjo: Sonomura, open the door."],
    18: ["Maki: Okay."],
    19: ["Maki: Nomoraka tanomama..."],
    20: ["Reiji: Alright, let's go!"],
    21: ["Elly: It opened! Everyone, let's go!"],
    22: ["Brown: Alright! Let's go, everyone!"],
    23: ["Ayase: Yay! Let's hurry!"],
    24: [
        "Maki: Behind this door is the worst me... I can't lose. Never!"
    ],
    25: [
        "Mark: ...So this is the final stretch. Let's pump ourselves up, <FF0F>あ!"
    ],
    26: [
        "Nanjo: Come to think of it, those compacts may symbolize the three primary colors of light. A human heart can become any color.",
        "Nanjo: Which color one is dyed depends on oneself... Perhaps that is what it means."
    ],
    27: ["Reiji: Hurry up. I'll take care of all the small fry."],
    28: [
        "Elly: At last... Let us finish quickly and go to the amusement park together."
    ],
    29: [
        "Elly: At last. Let's finish quickly and go to the amusement park together!",
        "Elly: I want to ride the Ferris wheel with <FF07>あ."
    ],
    30: [
        "Brown: My blood's boiling!",
        "Brown: Anyone who gets in my way is gonna get my Persona, Wonderful Bomber!"
    ],
    31: [
        "Ayase: An amusement park, huh. Ayase wants Free Fall! I did it five times in a row before,",
        "Ayase: so next is ten in a row! Of course, <FF0F>あ's coming along too!"
    ],
    32: [
        "Ayase: An amusement park, huh. Ayase wants Free Fall! I did it five times in a row before,",
        "Ayase: so next is ten in a row! Of course, <FF08>あ's coming along too!"
    ],
    33: [
        "Chisato: Be careful. But... <FF0F>あ-kun, you're not one to be overlooked.",
        "Chisato: Looking at Maki's face, I can tell who she likes now at a glance."
    ],
    34: [
        "Chisato: Be careful. But... <FF0F>あ-kun, you're not one to be overlooked.",
        "Chisato: Looking at Maki's face, I can tell who she likes now at a glance. And what's more...",
        "Chisato: It seems it's not only Maki... You might have a hard time, <FF0F>あ-kun."
    ],
    35: ["Yosuke: Do your best. I can't be of any help, but I'm rooting for you."],
}

E210 = {
    4: "=It'll cost 8000 yen, okay?<FF03><FF0E>　<FF01>",
}

E212 = {
    0: [
        "Maki: Everyone at this school was imagined by the real me too, right?",
        "Maki: It feels complicated..."
    ],
    1: ["Mark: It's awfully quiet. I can't sense anyone."],
    2: ["Nanjo: The entrance to this Avidya realm is the library."],
    3: [
        "Reiji: This school and the town... once I killed Kandori, I had no use for them.",
        "Reiji: That's what I thought, anyway..."
    ],
    4: [
        "Elly: <FF07>あ, do you like school?",
        "Elly: I thought it was a boring place. But now I like it. Because it's where I met everyone..."
    ],
    5: [
        "Elly: <FF07>あ, do you like school?",
        "Elly: I thought it was a boring place. But now I like it, because it is where I met everyone."
    ],
    6: [
        "Brown: I like school quite a bit. I'm bad at studying, though.",
        "Brown: Studying isn't everything, anyway."
    ],
    7: [
        "Ayase: <FF0F>あ, do you like school? Ayase kinda likes it.",
        "Ayase: I get to do pretty much what I want."
    ],
    8: [
        "Ayase: <FF08>あ, do you like school? Ayase kinda likes it.",
        "Ayase: I get to do pretty much what I want."
    ],
}

E213 = {
    0: ["Pandora: Shhruu... Fshruruuuuuuuu..."],
    1: ["Maki: This is me too!? This is..." + P('キ') + " Pandora!!"],
    2: ["Nanjo: That is! What is behind it, is it the core of the Deva System!?"],
    3: [
        "Pandora: At last... at last you've come this far... Fshh... ruruuuuuu...",
        "Pandora: This is the \"Door to Paradise\" I finally obtained... Shruruu... I'll give it to no one... no one...",
        "Pandora: With it, I will create a paradise. A paradise where nothing exists..."
    ],
    4: [
        "Maki: No! That's not a \"Door to Paradise\"!",
        "Maki: That's \"Pandora's Box,\" which brings calamity to the world!"
    ],
    5: [
        "Pandora: Fshruruuuuuu... Everything is futile... All of it is futile...",
        "Pandora: You are futile... I am futile...",
        "Pandora: I need no futile things... Disappear... Fshruuaaaaaaaaah!"
    ],
}

E215 = {
    0: [
        "Pandora: Why do you not give up? Why can you be so strong?"
    ],
    1: ["Maki: You know the reason too, don't you?"],
    2: ["Reiji: Because we're not alone..."],
    3: ["Elly: Because it is not I, but We... Because we are not alone."],
    4: ["Elly: Because it's not I, but We... Because we're not alone."],
    5: ["Brown: Because we ain't alone."],
    6: ["Ayase: Because we're not alone!"],
    7: ["Mark: Heh heh... Besides, we believe in ourselves."],
    8: [
        "Nanjo: ...Humans cannot live alone. When it is hard, always look back.",
        "Nanjo: We are there."
    ],
    9: [
        "Maki: You and I are both parts of the same Sonomura Maki... a companion of everyone here.",
        "Maki: Let's stop this. Let's do our best together."
    ],
    10: ["Pandora: Thank you..."],
    11: ["Nanjo: It is over..."],
    12: ["Mark: Yeah..."],
    13: [
        "Maki: Everyone, thank you so much. This is goodbye, but...",
        "Maki: I will never forget."
    ],
    14: ["Mark: Hey! Goodbye, what..."],
    15: [
        "Maki: I'm the shadow of Sonomura Maki. I can't go with everyone...",
        "Maki: It was truly fun."
    ],
    16: ["Mark: Hey! Sonomura! Is that even allowed!" + P('キ') + " Whoa!!"],
    17: ["Maki: I'll send everyone back to the real world..."],
    18: ["Maki: <FF07>あ-kun... may I have a moment?"],
    19: [
        "Maki: Thank you... Please think of me once in a while.",
        "Maki: Goodbye... I love you..."
    ],
    20: ["<FF07>あ: ........."],
    21: ["Maki: Goodbye... everyone..." + P('キ') + " Goodbye... <FF07>あ"],
}

E216 = {
    0: ["Maki: And then, and then, <FF07>あ-kun was like..." + P('キ') + " ...What did you say!"],
    1: ["Elly: Really? My, hee hee hee..."],
    2: ["Elly: Really? Is that so? Hee hee hee..."],
    3: [
        "Nanjo: Good grief... They say you cannot put a door on people's gossip,",
        "Nanjo: but nothing is as noisy as girls' rumors."
    ],
    4: [
        "Maki: Oh! Speak of the devil! You're late! We got tired of waiting!"
    ],
    5: [
        "Mark: Sorry, sorry." + P('キ') + " Geez, I went through hell.",
        "Mark: I keep telling them neither me nor <FF0F>あ has a second button!",
        "Mark: They were searching for you like crazy too, Nanjo."
    ],
    6: ["Nanjo: A wise man avoids danger. Use your head."],
    7: ["Mark: Yeah, yeah, whatever you say."],
    8: ["Elly: You are all so popular, it must be hard."],
    9: ["Elly: You're all so popular, it must be hard."],
    10: [
        "Maki: S-Sorry to start right away, but this time I'll have you keep us company!"
    ],
    11: ["Elly: Let's go! Time will not wait for us!"],
    12: ["Elly: Let's go! Time won't wait for us!"],
    13: [
        "Inaba: Aww, they've already gone." + P('キ') + " Heh heh... It's like Sonomura's earlier incident was a lie..."
    ],
    14: ["Nanjo: Heh..." + P('キ') + " Pandora" + P('で') + " huh..."],
    15: ["Mark: What? You still saying that?"],
    16: [
        "Nanjo: What?" + P('で') + " I was only remembering what came out last from the \"box of calamities.\"",
        "Nanjo: Well, let's go, Mark."
    ],
    17: [
        "Mark: What's that supposed to mean?" + P('キ') + " Hey, you...",
        "Mark: Did you just say Mark? Hey!"
    ],
    18: [
        "Ayase: Huh~? Seriously? <FF08>あ? Super great, right?"
    ],
    19: ["Ayase: Huh~? Seriously? <FF0F>あ? Really?"],
    20: [
        "Ayase: Hmm~ <FF08>あ I get, but Inaba?"
    ],
    21: [
        "Ayase: Hmm~ <FF0F>あ I get, but Inaba?"
    ],
    22: [
        "Ayase: <FF08>あ, you remember, right? Free Fall ten times in a row!",
        "Ayase: We're riding till we throw up!"
    ],
    23: [
        "Ayase: <FF0F>あ, you remember, right? Free Fall ten times in a row!",
        "Ayase: We're riding till we throw up!"
    ],
}

E217 = {
    0: [
        "Mark: Oh? After all your complaining, you came anyway, huh."
    ],
    1: ["Reiji: Heh heh..."],
    2: ["Nanjo: What is it? You are creeping me out."],
    3: ["Reiji: Inaba, I hear you're afraid of heights."],
    4: ["Mark: W-Where'd you hear that!"],
    5: [
        "Reiji: Uesugi's been spreading it around, saying this is the last time.",
        "Reiji: Today I'll get to enjoy watching you scream and cry."
    ],
    6: [
        "Nanjo: Oho. This is good news. I shall observe closely as well."
    ],
    7: [
        "Mark: That bastard! He never does anything useful! What're you two laughing at!",
        "Mark: Forget it! I ain't going!"
    ],
    8: ["Maki: Sorry to keep you waiting! What's wrong, everyone?"],
    9: [
        "Nanjo: Just in time. Sonomura, <FF0F>あ.",
        "Nanjo: Inaba says he is canceling his plans. A pity, really."
    ],
    10: ["Maki: Huh! Why!? I was looking forward to it!"],
    11: ["Mark: Nanjo, you bastard..."],
    12: ["Reiji: Heh heh heh..."],
    13: ["Maki: Is it true, Inaba-kun?"],
    14: ["Mark: No... Well... I'll go... I'm going."],
    15: [
        "Maki: Yay! Chisato and everyone are waiting outside! Let's go, everyone!"
    ],
    16: ["Mark: Nanjo, Reiji! You'll pay for this!"],
    17: [
        "Reiji: Heh..." + P('キ') + " That Sonomura. It's like the earlier incident was a lie."
    ],
    18: ["Nanjo: Heh heh..." + P('キ') + " Pandora" + P('で') + " huh..."],
    19: ["Reiji: ...What? You still saying that?"],
    20: [
        "Nanjo: What?" + P('で') + " I was only remembering what came out last from the \"box of calamities.\"",
        "Nanjo: Well, let's go, <FF0F>あ."
    ],
    21: ["Reiji: Hey, what's that supposed to mean?"],
    22: ["Maki's Voice: Hurry up! <FF07>あ-kun!"],
    23: ["Mark: Oh? Here he comes. The poop-leaker."],
    24: [
        "Brown: Heh heh heh. You can only talk like that until today!",
        "Brown: Mark-kun, I hear you're terribly bad with heights? You pee-leaker!"
    ],
    25: [
        "Mark: Gah!" + P('キ') + " Y-You bastard! Where'd you hear that!"
    ],
    26: [
        "Brown: Heh heh heh. I heard it all from your mom!",
        "Brown: And it was in sixth grade, right!"
    ],
    27: [
        "Mark: That damn old hag!" + P('キ') + " Shut up!",
        "Mark: It's way better than crapping your pants in middle school!"
    ],
    28: [
        "Brown: Sixth grade or middle school, same thing. Heh heh heh.",
        "Brown: Today I'll get a good look at the pee-leaking scene!"
    ],
    29: [
        "Nanjo: These two... Where do they think they are!? Ugh... my head hurts..."
    ],
    31: [
        "Brown: Perfect timing! <FF08>あ, Maki-chan!",
        "Brown: Mark can't wait to ride Free Fall, he's itching to go!"
    ],
    32: ["Maki: Really? Then let's hurry!"],
    33: ["Mark: Uesugi, you bastard..."],
    34: ["Brown: Hee hee hee hee..."],
    35: [
        "Maki: What's wrong? Chisato and everyone are waiting outside! Come on, let's go!"
    ],
    36: ["Mark: Uesugi! You'll pay for this!"],
    37: [
        "Brown: Can't wait to see it!" + P('キ') + " Still, Maki-chan... It's like the earlier incident was a lie, huh."
    ],
    38: ["Nanjo: Heh heh..." + P('キ') + " Pandora" + P('で') + " huh..."],
    39: [
        "Brown: What? You still saying that? Same old sourpuss, huh."
    ],
    41: ["Brown: What's that supposed to mean? Hey, wait up!"],
}

if __name__ == '__main__':
    for n, d in ((208, E208), (210, E210), (212, E212), (213, E213), (215, E215), (216, E216), (217, E217)):
        apply('E0', n, d, {})
