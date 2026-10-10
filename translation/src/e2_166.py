"""E2 entries 165-171 - SEBEC floor chatter; the other-world Himeno, Saeko, student council, Reiji's fans."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

p = P('ほ'); pm = P('み'); pn = P('な'); pg = P('ぎ'); pt = P('た')

E165 = {
    10: [
        "Scientist: At this rate, the valuable experiment data will be ruined! Ahh, my precious research...!"
    ],
}

E166 = {
    0: ["Maki: What kind of company is SEBEC, anyway?"],
    1: ["Maki: Let's hurry and chase Kandori!"],
    2: [
        "Nanjo: Kandori and I never got along since the first time we met at a party.",
        "Nanjo: It would have been good had I noticed his scheme then."
    ],
    3: [
        "Mark: We might die, you know" + pm + " I don't care, but the thought of my old hag" + pm + " I mean my mom crying is so annoying..."
    ],
    4: [
        "Elly: I wonder what will happen next. Hee hee, I look forward to it!"
    ],
    5: ["Elly: Let us hurry and chase Mr. Kandori!"],
    6: [
        "Brown: Let's hurry and go crush that Kandori guy! Idiot, there's no way I'm scared" + pt + ", no" + pt + " way, right?"
    ],
    7: [
        "Brown: Hurry and..." + pm + " Kandori... Do we really have to chase him...?"
    ],
    8: [
        "Ayase: Ayase isn't scared or anything" + pg + " but still, it's kinda scary."
    ],
}

E167 = {
    0: [
        "Himeno: My father is going to get me a bodyguard so I won't be attacked by demons. Why don't you all get one too?" + pg + " ...Ah, it's impossible for you all, isn't it. Right, it costs money.",
        "Himeno: I'm sorry."
    ],
    1: [F6('う') + "Himeno Yuko<FF03>She was supposed to be a dutiful girl working part-time for her family's finances, but..."],
    2: [
        "Mark: ...That's Himeno, right? Am I seeing things? Was she that kind of person?"
    ],
    3: [
        "Himeno: Oh, Nanjo-kun. Are you still associating with those sorts of people?"
    ],
    4: ["Nanjo: ...It is not that I associate with them by choice."],
    5: [
        "Mark: Those sorts of people...?" + pm + " Those sorts of people means..." + pm + " us?"
    ],
    6: ["Brown: At least it's certainly not me!"],
    7: ["Ayase: No way! Was Himeno always this nasty?"],
    8: [
        "Elly: ..." + pn + " Those sorts of people...?" + pm + " I seemed to hear \"those sorts of people\" just now.",
        "Elly: I must have misheard, right?"
    ],
    9: [
        "Nanjo: Indeed, this lot is a bunch of hopeless fools and may be \"those sorts of people,\"",
        "Nanjo: ..." + pn + " but why does it irritate me when someone else says so..."
    ],
    10: ["Nanjo: What on earth..." + pm + " Did Himeno eat something bad?"],
    11: "=Mark: What do you mean,<FF03>\"that sort of people\"?!<FF03><FF02><FF01>",
    12: [
        "Brown: I too always think that I should be choosy about my friends, you know!"
    ],
    13: [
        "Elly: Having too little confidence is a problem too, but" + pm + " that is going a bit too far."
    ],
    14: ["Ayase: That's not Himeno! She wasn't a person like that!"],
    15: ["Himeno: Do you need something? Don't talk to me so casually!"],
    16: [
        "Student: Himeno is really unpleasant! Sonomura-san should stop being friends with someone like that."
    ],
    17: [
        "Student: The most popular, Sonomura-san, and the most disliked, Himeno-san..." + pm + " but the two are friends."
    ],
}

E168 = {
    0: [
        "Brown: Kozai was a real beauty, wasn't she... Hey, Mark, why don't you go get kidnapped in her place?"
    ],
    1: "=Nanjo: Kozai Chisato..." + pm + "<FF03>Missing here too, huh.<FF02><FF03>She must be truly hated<FF03>by the god of fate.<FF02><FF01>",
    2: "=Mark: Heh, Sonomura's good<FF03>at painting over here too.<FF03><FF02><FF01>",
    3: "=Elly: The girl in black...<FF03>She is mysterious.<FF03><FF02><FF01>",
    4: [
        "Ayase: Did Kozai really like Naito? He's totally not her type, you know.",
    ],
    5: [
        "Student: Sonomura-san's painting won a prize in a contest again. I'm proud of her, too."
    ],
    6: [
        "Student: In comparison, Kozai-san has never won a prize, and she got taken away by that girl in black. She's just unlucky."
    ],
    7: [
        "Student: Don't you know? Kozai-san was kidnapped by the girl in black. I feel so bad for Naito-kun, I can't bear to watch."
    ],
    8: [
        "Student: Maki-chan was close to Kozai-san, so she must be worried."
    ],
}

E169 = {
    0: ["Maki: Saeko-sensei is always gloomy, isn't she! It makes me gloomy too."],
    1: ["Brown: Huh? What happened to Saeko-sensei?"],
    2: [
        "Brown: Without that power of Saeko-sensei's, I get thrown off."
    ],
    3: ["Nanjo: Even Saeko-sensei is acting strangely..."],
    4: [
        "Nanjo: If Mayuzumi saw Saeko-sensei now, she would surely be disappointed."
    ],
    5: [
        "Mark: Huh?" + pm + " Hey, what's up, Saeko-sensei? If you say it's just overeating again, I'll get mad!"
    ],
    6: [
        "Mark: At least here we don't get made to do muscle training as punishment. Maybe this is better."
    ],
    7: [
        "Elly: For Saeko-sensei to be silent..." + pm + " Is she very angry about something?"
    ],
    8: [
        "Elly: Even with the same face, a different personality changes the atmosphere."
    ],
    9: ["Ayase: Ew, she's so gloomy."],
    10: ["Ayase: Our Saeko-sensei is prettier."],
    11: ["Reiji: ..." + pm + " Hmph. At least she's not noisy."],
    12: ["Natsumi-sensei: Oh, <FF0F>あ-kun. Did you get hurt somewhere?"],
    13: ["Mark: Oh, Natsumi-sensei!"],
    14: ["Saeko-sensei: ..............."],
    15: [
        "Brown: Ah, Saeko-sensei! Hello, long time no see! You're as beautiful as ever..."
    ],
    16: ["Ayase: Ah, it's Saeko-sensei! Sensei, it's Ayase! Do you recognize me?"],
    17: ["Elly: Oh, Saeko-sensei. I apologize for the trouble earlier..."],
    18: [
        "Nanjo: Saeko-sensei. It feels like it has been quite a long time."
    ],
    19: ["Mark: Ugh" + pg + " it's gloomy...!!"],
    20: [
        "Natsumi-sensei: I was so surprised earlier! But I heard you all helped me. Thank you!"
    ],
    21: ["Nanjo: Ugh" + pg + " how gloomy...!!"],
    25: [
        "Natsumi-sensei: When you're not feeling well, come to the nurse's office! * Now, let me take a look."
    ],
    26: ["Natsumi-sensei: There, that should do it. Don't lose to demons."],
}

E170 = {
    0: ["Brown: Huh? Wasn't he the student council president where I'm from?"],
    1: [
        "Nanjo: Someone else became student council president. A wise choice.",
        "Nanjo: ...But I sensed no sign of a president election?"
    ],
    2: [
        "Mark: Heh, serves him right! The previous president was all good at getting by but seems to have done nothing."
    ],
    3: ["Elly: A student council should be like this."],
    4: [
        "Ayase: Ayase doesn't like the previous student council president either. All talk and bossy!"
    ],
    5: [
        "Council Member: Not making me president, what are the people at this school thinking!",
        "Council Member: My dream was to leave my name in the school history as a great student council president..."
    ],
    6: [
        "Student Council President: Now that I'm president, I'll make it a great student council that works hard!"
    ],
    7: [
        "Council Member: The president's so enthusiastic, it makes us want to try hard too."
    ],
    8: [
        "Council Member: They say the president is aiming to be like a past president. Someone named Yamada or something like that."
    ],
}

E171 = {
    0: ["Maki: Kido..." + pm + " you're kind of scary..."],
    1: ["Nanjo: Pointless!"],
    2: ["Nanjo: Do you not think love is nothing but a delusion?"],
    3: [
        "Mark: Surely there's some girl who's quietly watching me from the shadows too, I bet..."
    ],
    4: [
        "Mark: So that girl was a Reiji fan... Ah," + pn + " I'm not jealous or anything!"
    ],
    5: ["Elly: ..." + pm + " Can one fall in love at first sight, I wonder."],
    6: [
        "Elly: ..." + pm + " I do not understand. There is no need to be so desperate."
    ],
    7: [
        "Brown: Hey hey hey hey, what the heck! Aren't you a fan of mine?"
    ],
    8: [
        "Brown: Hey hey hey hey, why him and not me?!"
    ],
}

if __name__ == '__main__':
    for n, d in ((165, E165), (166, E166), (167, E167), (168, E168), (169, E169), (170, E170), (171, E171)):
        apply('E2', n, d, {})
