"""E2 entries 4-11 - school NPC chatter."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

pm = P('み'); pg = P('ぎ'); pk = P('キ'); pn = P('な')

E4 = {
    3: [
        "Toro: I-I had a weird dream, you know! A girl said \"help me\"... Could it be a prophetic dream? Is there a girl waiting for me to save her?",
        "Toro: That's so" + pm + " cool..."
    ],
    4: [F6('い') + "Yokouchi Kenta<FF03>Nicknamed Toro. Loves to eat. Strong, but timid."],
    5: [
        "Student: I saw it! Toro confessed to Ayase-san and got turned down flat! But apparently he's still pestering her."
    ],
    6: ["The cafeteria lady seems to have gone home."],
}

E5 = {
    0: ["Nanjo: This is a story that does not interest me much."],
    1: ["Mark: At this age you long for older women, don't you."],
    2: [
        "Yukino: Geez, the sun's going to set. When on earth are we gonna get to the hospital?"
    ],
    3: [
        "Student: Natsumi-sensei, the school nurse, is so sexy and grown-up, isn't she!"
    ],
    4: ["Student: Ugh! N-Not that..." + pg + " Sorry, my bad..."],
    5: [
        "Student: But even if she's bad at cooking, she can just buy something at the convenience store."
    ],
    6: ["Student: Oh yeah? Then from now on get Natsumi-sensei to make your bento!"],
    7: ["Student: Come to think of it, Natsumi-sensei seems to have broken up with her guy! Why do you think?"],
}

E6 = {
    0: ["Nanjo: What a noisy woman..."],
    1: ["Mark: Hey" + pm + " <FF0F>あ, still not going to the hospital?"],
    2: [
        "Yukino: Yuka looks at a glance like she's not thinking about anything,",
        "Yukino: but I get the feeling she's deliberately not thinking."
    ],
    3: [
        "Student: You guys going to the hospital? The big one at the northeast edge of Mikage Town, right?",
        "Student: It's quite a walk. Well, good luck!"
    ],
    4: [
        "Student: Hey, what about Ayase? Weren't you guys with her?",
        "Student: We promised to go hang out, but she never shows up. I'm thinking of just going ahead without her!",
        "Student: Weird, she was looking forward to it, I thought! Ayase does this kind of thing a lot, you know!",
        "Student: Like, she's cold or something. I can't really tell what she's thinking."
    ],
}

E7 = {
    0: ["Tamaki-chan: Hey! Why are you dirtying the clubroom! Stupid Tadashi!"],
    1: [
        "Tadashi-kun: Ah~ I can't hear you. It's our business, isn't it~?",
        "Tadashi-kun: Geez, you're angry every day. You ugly Tamaki!"
    ],
    2: ["Tamaki-chan: What did you say! Such a vulgar thing, I'm tearing it off right now!"],
    3: ["Tadashi-kun: Hey! What are you doing to my goddess!"],
    4: [
        "Tamaki-chan: Goddess my foot! You pervert! Pervert pervert pervert pervert!"
    ],
    5: ["Tadashi-kun: Gah! You ugly! Ugly ugly ugly ugly ugly ugly ugly!"],
    6: [
        "Boy Club Member: Oh boy. These two are like this every day. Don't they ever get tired of it?"
    ],
    7: ["Tamaki-chan: *Huff* *Huff*..." + pk + " What? I'm kind of busy right now."],
    8: ["Tadashi-kun: *Wheeze* *Wheeze*..." + pk + " What is it? I'm busy right now, I said."],
    11: [
        "Nanjo: Honestly. The fools of our sports clubs... truly the height of arrogance."
    ],
    12: [
        "Mark: What a half-baked paint job. If you're gonna bomb graffiti, put more effort into it."
    ],
    13: [
        "Yukino: Leave them alone. They say people who fight are close, don't they?"
    ],
    14: [
        "Girl Club Member: Tamaki's a transfer student, but she's strong enough to place third in tournaments. But...",
        "Girl Club Member: she doesn't like to talk about her previous school. I wonder if something happened."
    ],
}

E8 = {
    0: [
        "Nanjo: Listening to talk about SEBEC is not very pleasant. More importantly, let us go to the hospital."
    ],
    1: [
        "Mark: Man, that brings back memories. The haunted house!",
        "Mark: I used to go play there a lot, and my old hag" + pn + " I mean my mom, would yell at me..."
    ],
    2: [
        "Yukino: It was about a year ago, wasn't it? That the SEBEC building was built where the vacant house was torn down..."
    ],
    3: [
        "Student: Know what? There are lots of weird rumors about the SEBEC building.",
        "Student: Like people hearing moaning voices or red eyes peeking from the windows...",
        "Student: They say it's the curse because it was built where the haunted house used to be."
    ],
}

E9 = {
    0: [
        "Nanjo: Honestly, we make many detours. At this rate, by the time the hospital exam finishes, the sun will have set."
    ],
    1: ["Mark: Behind the highway... that's straight north, right?"],
    2: ["Yukino: To think there are other trees like the one in the nurse's office..."],
    3: [
        "Student: I saw a beautiful tree in the woods behind the highway.",
        "Student: It looks just like the one in the nurse's office. It's a mysterious tree that makes you feel at ease just looking at it."
    ],
}

E10 = {
    0: [
        "Nanjo: We will be exam-takers soon, after all. I, of course, intend to pass my first choice with the top score."
    ],
    1: [
        "Mark: Hey, let's hurry to the hospital. Detours are bad, you know."
    ],
    2: [
        "Yukino: Are you thinking about your future path? I don't plan to take entrance exams, though."
    ],
    3: ["Student: I don't wanna go to cram school~ I wanna sleep at home all day~"],
    4: [
        "Student: You can't, you have to study. Let's meet up and go" + pn + " okay? How about the subway ticket gate?"
    ],
    5: [
        "Student: The subway..." + pn + " It's past Sun Mall to the north, then straight right, right?"
    ],
    6: [
        "Student: They say \"Persona-sama play\" lets you see your future self.",
        "Student: Maybe I'll look at my future self that way too... I wonder if I'll properly become a college student by this time next year..."
    ],
    7: [
        "Student: Geez, how pathetic! If you have time for \"Persona-sama play,\" you should study!",
        "Student: We promised to go to the same university together..." + pm + " You idiot!"
    ],
}

E11 = {
    0: [
        "Nanjo: You want to join the boxing club? But first we must have our hospital exams."
    ],
    1: ["Mark: Boxing's cool, huh! But it looks painful."],
    2: ["Yukino: ...Maybe I should diet too..."],
}

if __name__ == '__main__':
    for n, d in ((4, E4), (5, E5), (6, E6), (7, E7), (8, E8), (9, E9), (10, E10), (11, E11)):
        apply('E2', n, d, {})
