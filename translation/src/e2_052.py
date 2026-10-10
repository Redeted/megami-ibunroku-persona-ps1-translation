"""E2 entries 52-103 - hospital NPCs and party chatter, police station ghost."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

pm = P('み'); pn = P('な'); pg = P('ぎ')

E52 = {
    3: ["Mark: Is it really okay to keep the shop open? Don't blame me if demons get you!"],
    4: ["Elly: Come to think of it, someone at school said something similar."],
    5: ["Yukino: A strange shop... I wonder what kind of shop it is."],
    6: ["Yukino: That's enough exploring, don't you think? Shall we go to Araya Shrine next?"],
    7: ["Shopkeeper: Oh, welcome. Well, take your time."],
    8: ["Shopkeeper: Oh, welcome. My, you folks have it rough, too."],
    9: [
        "Customer: There's just one odd shop on this shopping street. It's always closed whenever I look, and no one's ever seen people going in or out.",
        "Customer: But apparently music can be heard from it now and then..." + pg + " Strange things do happen."
    ],
    10: [
        "Customer: About that odd shop on this shopping street, I heard a rumor it's opening soon.",
        "Customer: When, I don't know, though."
    ],
}

E56 = {
    0: [
        "Nanjo: Is nobody here?" + pm + " ...My, what a cozy little house."
    ],
    1: [
        "Mark: Compared to your house, anywhere's cozy! Geez, that's why rich boys...",
    ],
    2: [
        "Yukino: This is Himeno Yuko's house. Sonomura's friend... I work part-time for my future, but she does it for her family."
    ],
    3: ["Mark: Ugh... that's heartbreaking!"],
    4: ["Mark: Nanjo, you work part-time too and pay Yamaoka's salary yourself!"],
    5: ["Yukino: Himeno doesn't seem to be back yet."],
}

E64 = {
    0: [
        "Nurse: Oh my, you all! You really must wait your turn properly! Now please leave!"
    ],
}

E65 = {
    0: ["Nanjo: Is that old man serious, or is he joking..."],
    1: ["Mark: Tch, who's Hiroshi?"],
    2: ["Yukino: The nurses have it tough, too."],
    3: ["Old Man: Oh, Akiko-san. Hiroshi has come to see me."],
    4: ["Nurse: That's right, Grandpa. It's Hiroshi-san."],
    5: ["Old Man: Thank you for coming, Hiroshi."],
    6: "=Listen to the old man?<FF03><FF0E>さ<FF01>",
    7: [
        "Old Man: Listen, Hiroshi. A person's heart is complicated.",
        "Old Man: What shows on the surface isn't always their true feelings. Find the truth hidden behind it..."
    ],
    8: ["Old Man: I see, school is fun?"],
    9: [
        "Nurse: Hiroshi seems to be his grandson's name. I'm being mistaken for his daughter, too..."
    ],
}

E66 = {
    0: ["Nurse: Oh? Aren't you a friend of Sonomura Maki-chan?"],
    1: ["Mark: Well, no..."],
    2: [
        "Nurse: You came to visit last week too, didn't you? And the week before, I think..."
    ],
    3: ["Nanjo: Oh~... How very kind of you."],
    4: ["Yukino: Nanjo, stop it."],
}

E67 = {
    0: [
        "Nanjo: As expected, there are few people in this hospital who could talk with Sonomura.",
        "Nanjo: No wonder she feels no urge to leave her room..."
    ],
    1: ["Mark: Sonomura's room is the second one straight ahead from here."],
    2: ["Yukino: Visiting was the right call. Sonomura will surely be glad."],
    3: [
        "Patient: Oh, a high school girl? Hmm, but I've never seen her.",
        "Patient: She must stay in her room all the time... She should come out once in a while."
    ],
    4: [
        "Patient: There's a girl about high school age on the same floor as me, you know.",
        "Patient: Sometimes I hear a little girl's voice.",
        "Patient: It's supposed to be a single room, so maybe a little sister came to visit?"
    ],
}

E68 = {
    0: ["Nanjo: Sonomura's mother is, of all places, at a company like that!"],
    1: ["Mark: Ah! Dang! Maybe I should've brought flowers. Oh well, can't be helped!"],
    2: ["Yukino: Now, Sonomura is waiting for you."],
    3: [
        "Nurse: You're Maki-chan's friends, aren't you? That's good. She's been in and out of the hospital since she was a child, you know?",
        "Nurse: I've always worried whether she gets along with her friends..."
    ],
    4: [
        "Nurse: I just can't believe it! Their precious only daughter is in the hospital and her mother doesn't even visit!",
        "Nurse: I don't know how busy the work at SEBEC is, but she's an unfit mother!",
        "Nurse: ...Poor Maki-chan..."
    ],
}

E80 = {
    0: [
        "Nanjo: If I..." + pg + " if I had properly made him go home then" + pm + " ..." + pm + " "
    ],
    1: [
        "Mark: If we use this power, we should be able to find the cause of this happening!"
    ],
    2: [
        "Elly: Exciting..." + pm + " I'm getting thrilled somehow! Oh my, how silly of me" + pn + " ...Excuse me."
    ],
    3: [
        "Yukino: Making a fool of us" + pg + " I won't let it slide! I'll definitely put things back!"
    ],
    4: [
        "Doctor: Damn it, why can't we get to the intensive care unit! There are patients!" + pn + " I must treat Sonomura-kun...!"
    ],
    5: [
        "Nurse: The TV doesn't work, and the phone doesn't connect! What on earth happened!"
    ],
    6: [
        "Nurse: If it were the examination room, I could treat your injuries... But I don't know where the examination room is!",
        "Nurse: The positions of the rooms have been completely scrambled!"
    ],
}

E81 = {
    0: [
        "Nanjo: <FF0F>あ..." + pg + " Sorry, but my head is not working as usual" + pm + " ."
    ],
    1: ["Mark: Damn, if only we had some clue!"],
    2: [
        "Elly: I want to help Maki's mother quickly..." + pm + " Come with me to Araya Shrine!"
    ],
    3: [
        "Yukino: I feel like the air in this town has changed. It's kind of suffocating."
    ],
    4: [
        "Nurse: There's something like mist hanging outside the window. It looks like it's surrounding the town.",
        "Nurse: Surely it can't be like some weird novel, where you can't leave this town. That can't be, right?"
    ],
    5: [
        "Old Man: Hiroshi, it's been a while. Did you come to hear my stories? Then I'll tell you a useful one.",
        "Old Man: Think calmly and act. Then you will surely reach" + pg + " the truth.",
        "Old Man: By the way, Akiko-san, isn't lunch ready yet?"
    ],
}

E82 = {
    0: [
        "Nanjo: I will definitely find the cause" + pg + " There should be nothing I cannot do!"
    ],
    1: ["Mark: Hey, do the others have this power too?"],
    2: ["Elly: It is Araya Shrine, please do not forget!"],
    3: [
        "Yukino: That power's creepy, but it looks useful."
    ],
    4: [
        "Patient: Ughhh, my cavity's started hurting. Can't get treated unless I make it there!"
    ],
    5: [
        "Patient: I'm prepared for whatever happens, but I worry about my little grandchild.",
        "Patient: They should be at school, so I hope nothing's happened at school."
    ],
}

E83 = {
    0: ["Nanjo: ........." + pg + " Hm? Ah, what is it?"],
    1: ["Mark: I wonder if there are others suffering besides Sonomura."],
    2: [
        "Elly: I am worried about Maki's mother's condition..." + pm + " Let us hurry to the shrine!"
    ],
    3: [
        "Yukino: <FF0F>あ, I thought you'd be more of a weakling, but you're surprisingly calm."
    ],
    4: [
        "Nurse: We can't get in touch with the patients... What on earth should I do? Could you do something?",
        "Nurse: ..." + pm + " Of course not, sorry. I'm confused..."
    ],
    5: ["Doctor: Are you all right? Let me see."],
    6: [
        "Doctor: I want to help as many people as I can. Please do not overdo it yourself."
    ],
}

E96 = {
    3: [
        "Nanjo: Money without class... Good grief, what a nuisance."
    ],
    4: [
        "Kaneda: Oh, young master Nanjo!",
        "Kaneda: Say, tell the police that Kaneda Katsue is in trouble, even if through your father! Please, I beg you!"
    ],
}

E97 = {
    0: [
        "Yukino: Excuse me! Demons are out in town! Lots of people are hurt! Please patrol..." + pm + " Um" + pg + " officer?"
    ],
    1: ["Demon" + pm + " you say...?"],
    2: ["Elly: Yukino, wait! Something's wrong with that person...!"],
    3: ["Plenty of demons came. Thanks to them, I'm in this state..."],
    4: [
        "Police Officer's Ghost: Damn it..." + pm + " Inspector..." + pm + " help me..." + pm + " help..."
    ],
    5: ["Elly: As I thought! Everyone, let us run!"],
    6: ["Yukino: Tch! So we can't count on the police either!"],
}

E103 = {
    0: ["Maki: What? Are you buying ice cream or something?"],
    1: [
        "Brown: Don't they sell super strong guns or armor or something? Are we okay with such flimsy equipment?"
    ],
    5: ["Ayase: Hey, what are we doing about SEBEC? Is it fine now?"],
    6: ["Ayase: Hey, let's hurry and chase Kandori!"],
}

if __name__ == '__main__':
    for n, d in ((52, E52), (56, E56), (64, E64), (65, E65), (66, E66), (67, E67), (68, E68), (80, E80), (81, E81), (82, E82), (83, E83), (96, E96), (97, E97), (103, E103)):
        apply('E2', n, d, {})
