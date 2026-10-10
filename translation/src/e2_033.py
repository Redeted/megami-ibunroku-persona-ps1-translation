"""E2 entries 33-45 - Mikage town NPC scenes (Kaneda, police, museum, Mark's mother, shops)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

pm = P('み'); pn = P('な'); pg = P('ぎ'); pj = P('じ'); pt = P('た')

E33 = {
    0: ["Kaneda: What do you want with my house? Don't tell me you came to steal my treasures!"],
    1: [F6('う') + "Kaneda Katsue<FF03>Mikage Town resident. Recently came into a sudden windfall." + F6('　')],
    2: [
        "Nanjo: Preposterous! To me, the old woman's \"treasures\" are nothing but junk.",
        "Nanjo: Putting on airs as an antique collector when she only buys things up with money is laughable!"
    ],
    3: [
        "Yukino: That old lady treats everybody like a thief. Don't bother with her."
    ],
    4: ["Mark: Let's just go, <FF0F>あ! This feels bad!"],
    5: [
        "Kaneda: Hmph. Kids like you couldn't possibly understand the value of my treasures! Now go home!"
    ],
    6: [
        "Kaneda: What are the police doing! I pay more taxes than most people!",
        "Kaneda: At a time like this, shouldn't they come to me first? If anything happens to my property, I'll sue!"
    ],
    7: [
        "Elly: Everyone pays taxes. I do not think there is any need to be arrogant."
    ],
    8: [
        "Kaneda: You stuck-up little girl, acting so high and mighty! Get off my land this instant!"
    ],
}

E34 = {
    0: [
        "Nanjo: Inaba seems to be acquainted with those police officers. He does not seem happy to see them, though."
    ],
    1: ["Mark: Yeah, well... so-so..."],
    2: ["Mark: Gah, <FF0F>あ! Don't take me to the police!"],
    3: [
        "Yukino: Look at Mark's face. By the way, aren't we going to the hospital?"
    ],
    4: [
        "Inspector: Oh, if it isn't Inaba. You are going to high school properly, I trust? You aren't causing the teachers trouble, are you?"
    ],
    5: ["Inspector: But I'm the one who took you in, so there's the matter of responsibility..."],
    6: ["Policewoman: Inspector, that's harsh. Inaba-kun is fine, right?"],
    7: [
        "Policewoman: You're Inaba-kun's friend, aren't you? I like him. Don't you think he's a good kid?"
    ],
}

E37 = {
    0: ["Nanjo: The archive room is beyond here. Are you going to look?"],
    1: [
        "Mark: Hmm, a receptionist, huh. Hmm..." + pg + " It sounds nice, though."
    ],
    2: [
        "Yukino: A field trip before going to the hospital for exams?" + pm + " ...Weirdo!"
    ],
    3: [
        "Receptionist: Welcome to the Mikage Local History Museum! Materials important to understanding local history are stored here."
    ],
}

E38 = {
    0: [
        "Nanjo: It has long been said that mirrors have spiritual power. Is that one supposed to have such power too?"
    ],
    1: [
        "Mark: You suddenly became studious, huh. It might snow."
    ],
    2: [
        "Yukino: It's a musty place, but the atmosphere isn't bad. Maybe that mirror is protecting it."
    ],
    3: [
        "Man: I came to see this museum's highlight, the \"Hama Mirror.\" Truly, how divine."
    ],
    4: [
        "Girl: They say the \"Hama Mirror\" was the only thing found at the ruins discovered half a year ago.",
        "Girl: The teacher said there's nothing else, so it's boring to go in."
    ],
}

E40 = {
    0: [
        "Mark's Mother: Mark-kun! You came at the perfect time!",
        "Mark's Mother: Mom is shopping, but the bags are heavy, so come along with me, Mark-kun!"
    ],
    1: [
        "Nanjo: Oho~..." + pj + " Is \"Mark-kun\" you? Hey, Inaba Masao..."
    ],
    2: [
        "Mark: S-Stop it, you old hag! I'm busy! Go over there!"
    ],
    3: [
        "Mark's Mother: Mark-kun! You mustn't call Mother an old hag!",
        "Mark's Mother: I was even going to buy you a shirt or something!"
    ],
    4: [
        "Yukino: \"Mark-kun,\" huh... A name as embarrassing as \"young master.\""
    ],
    5: ["Mark: Shut up, Yukino!"],
    6: [
        "Mark's Mother: Oh, your friends? But this shop is expensive, you know. Hey, Mark-kun, take a look at this!"
    ],
    7: ["Mark: It's nothing to do with me! Hey, <FF0F>あ! Let's go!"],
    8: [
        "Mark's Mother: Honestly, that boy..." + pm + " Everyone, please be nice to Mark-kun."
    ],
    9: ["Mark: Surely" + pn + " she's gone" + pn + " by now..."],
    10: [
        "Mark's Mother: Oh my, Mark-kun! You came back? Oh, perfect timing!"
    ],
    11: ["Mark: Uh-oh!" + pn + " She's still here! Let's get out, <FF0F>あ!"],
    12: ["Mark's Mother: Mark-kun!"],
    13: ["Mark: Gah!!" + pm + " M-Mom!"],
    14: ["Mark: Hey..." + pm + " There's nobody here...!"],
    15: [
        "Mark: You're hiding around here, right? It's me, Masao. I'm not a demon.",
        "Mark: It's okay, come out. I'll take you home."
    ],
    16: ["Mark: M" + pn + "om..." + pn],
    17: [
        "Mark: Ah, <FF0F>あ. It's nothing, no big deal.",
        "Mark: My old hag probably went home before anything happened.",
        "Mark: She's probably watching the afternoon shows and making a big fuss by now." + pm + " Now let's hurry!"
    ],
    18: ["There doesn't seem to be anyone here..."],
}

E41 = {
    0: [
        "Clerk: Oh, Mayuzumi-san, you're early. It isn't time for your shift yet. Do you need something?"
    ],
    1: [
        "Yukino: Something came up suddenly... My shift will be a bit late, I'll work longer to make up for it."
    ],
    2: [
        "Clerk: Oh, that's fine. But you're so dedicated. Having a goal really does make the difference."
    ],
    3: ["Nanjo: I cannot imagine Mayuzumi in that uniform, smiling."],
    4: ["Nanjo: Open for business even with demons around. Admirable."],
    5: [
        "Mark: Yukino's working part-time seriously? So what's the goal?"
    ],
    6: [
        "Mark: I wonder if demons don't come into the shops. Whatever, it's a relief."
    ],
    7: [
        "Yukino: I want to study abroad and learn photography over there, so I'm saving money."
    ],
    8: [
        "Yukino: Did I say something irresponsible? Without any guarantee..."
    ],
    9: ["Clerk: Welcome! What can I get you?"],
    10: [
        "Elly: It feels strange. Standing here, I begin to wonder if everything was a dream."
    ],
    11: [
        "Clerk: M-Mayuzumi-san! A m-monster appeared! Please stay here!"
    ],
    12: [
        "Yukino: Sorry, I have to go. If you stay inside, you'll surely be fine."
    ],
    13: [
        "Clerk: ..." + pt + " If I stay in the store, I'll be fine..." + pn + " I have to keep the shop open... Open every day of the year, after all...",
        "Clerk: Welcome!"
    ],
}

E42 = {
    0: [
        "Nanjo: If I lived in Shibuya, I think it would be too noisy to bear... She is somehow lacking in reality."
    ],
    1: [
        "Mark: I wanna leave a house like that quick too... It's so embarrassing I can't even invite friends."
    ],
    2: [
        "Yukino: That girl is Yuka's friend." + pt + " They really are alike. And chatty" + pm + " ..."
    ],
    3: [
        "Girl: I wanna live alone soon, around Shibuya, in a cool apartment...",
        "Girl: That'd be nice" + pm + " Ahh, I wanna leave this boring town quick."
    ],
    4: ["Clerk: Welcome! Will you be eating here?"],
    5: [
        "Yukino: Honestly! This is no time to be leisurely eating burgers!"
    ],
}

E43 = {
    0: [
        "Nanjo: A card game? Hm, that is acceptable. It is an adult pastime.",
        "Nanjo: Inaba, at his age, still makes a fuss over computer games.",
        "Nanjo: ...Surely you do not also like computer games?"
    ],
    1: [
        "Mark: Oops, my bad. I got no money right now! Man, this is bad. Wahaha! Sorry, sorry, the all-you-can-eat's for another time!"
    ],
    2: [
        "Mark: Uesugi ain't here, right?" + pn + " ...Nope, thank goodness.",
        "Mark: Damn it, I shouldn't have said that unnecessary thing about all-you-can-eat!"
    ],
    3: [
        "Yukino: Demons..." + pm + " Hey, if something like that became real, I don't think we could laugh about it."
    ],
    4: [
        "Man: This card game I've been into lately is called \"Persona.\"",
        "Man: You can summon demons with cards called \"Spell Cards.\" It'd be fun if you could really do that."
    ],
    5: [
        "Clerk: ..." + pm + " Welcome..." + pm + " Ugh, the register isn't working! What do I do about this? I don't know!"
    ],
}

E45 = {
    0: [
        "Nanjo: Indeed, exams can be done here too, but we are going to Mikage General Hospital, are we not?"
    ],
    1: ["Nanjo: ........." + pt + " Ah, sorry, <FF0F>あ. I was thinking about something."],
    2: ["Mark: This is such a pain."],
    3: [
        "Mark: Sonomura's mom is at the shrine, right? Let's hurry over to her."
    ],
    4: [
        "Mark: It was all Kandori pulling the strings behind the scenes." + pm + " Hey, we're going, right? To the abandoned factory?"
    ],
    5: [
        "Yukino: I've never been taken care of by a doctor..." + pm + " I've put the other guy in the hospital, though."
    ],
    6: ["Yukino: <FF0F>あ... Don't overdo it. We're here too, you know."],
    7: ["Elly: The atmosphere here at the hospital is bright and reassuring."],
}

if __name__ == '__main__':
    for n, d in ((33, E33), (34, E34), (37, E37), (38, E38), (40, E40), (41, E41), (42, E42), (43, E43), (45, E45)):
        apply('E2', n, d, {})
