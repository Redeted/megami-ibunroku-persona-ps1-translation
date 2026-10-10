"""E1 entries 112-129 - Tartarus: Personas returned, Mariko, Yuriko's room."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

p = P('ほ')

E112 = {
    11: "=Return the Persona to Yukino?<FF03><FF0E>　<FF01>",
    12: ["The lost power of the Persona is revived in Yukino..."],
    14: ["Ayase's Persona is here."],
    15: "=Return the Persona to Ayase?<FF03><FF0E>　<FF01>",
    16: ["The lost power of the Persona is revived in Ayase..."],
    18: ["Nanjo's Persona is here."],
    19: "=Return the Persona to Nanjo?<FF03><FF0E>　<FF01>",
    20: ["The lost power of the Persona is revived in Nanjo..."],
    22: ["Brown's Persona is here."],
    23: "=Return the Persona to Brown?<FF03><FF0E>　<FF01>",
    24: ["The lost power of the Persona is revived in Brown..."],
    26: ["Elly's Persona is here."],
    27: "=Return the Persona to Elly?<FF03><FF0E>　<FF01>",
    28: ["The lost power of the Persona is revived in Elly..."],
    30: ["You stopped returning the Persona."],
    31: [
        "???: Oh, hello. Nice to meet you. I'm Yabe Mariko of the \"Yamakumo Private High School Paranormal Phenomena Club\"! Pleased to meet you!",
        "???: Well, though it's an illegal club where I'm both president and the only member!",
        "???: My homeroom teacher won't approve setting up the club just because he says it's \"lame\"!",
        "???: Anyway, today I came to meet my comrade Kurouri-kun, but I never" + p + " thought" + p + " I'd get caught up in such an amazing paranormal phenomenon!",
        "???: I'm so lucky! I've been snapping photos like crazy! And I'm going to submit these demon photos to a magazine!",
        "???: Then maybe the teacher will approve the club too! Alright! I'll do my best!"
    ],
}

E119 = {
    0: ["Yukino: Who is she? That girl with a camera hanging around her neck."],
    1: [
        "Yukino: What a weirdo, that Mariko. Kurouri too, I don't get people who like the occult."
    ],
    2: ["Ayase: That girl's super suspicious."],
    3: ["Ayase: That pink uniform is cute, isn't it."],
    4: ["Nanjo: Who is that woman? She does not seem to be a student of our school."],
    5: ["Nanjo: That Mariko truly seems to be enjoying this situation."],
    6: [
        "Brown: That's the uniform of \"Yamakumo Private High School,\" famous for its free school spirit.",
        "Brown: She's quite a cutie! Who is she?"
    ],
    7: ["Brown: Maybe I'll adventure through the tower with Mariko-chan..."],
    8: ["Elly: What is she doing in a place like this?"],
    9: ["Elly: She may be more of a Danger than Kurouri-kun."],
    10: [
        "Mariko: Eh? Whether there was anything in that chest? Yeah, there was this \"mirror fragment\" in it!",
        "Mariko: This mirror, I sense a strong spiritual power from it.",
        "Mariko: It must be a psychic item hiding great power. Eh? You want this? Hmm...",
        "Mariko: 5000 yen! How about it? I found it first, so isn't it not expensive?"
    ],
    11: "=Buy the \"Mirror Fragment\"?<FF03><FF0E>　<FF01>",
    12: [
        "Mariko: Thanks for your business! Since entering this tower I've been snapping photos like crazy, so the film costs are rough.",
        "Mariko: Alright! Now I can buy film!"
    ],
    14: [
        "Mariko: Hmm. Oh, I see. You don't want it.",
        "Mariko: Then I'll send it to \"Lemuria\" to be appraised!"
    ],
    15: [
        "Mariko: Hey! You don't even have 5000 yen? Haah, how pathetic!",
        "Mariko: Then you could come with me and work off the 5000 yen, if you like.",
        "Mariko: Eh? No way? Then pay 5000 yen right now, in full!"
    ],
    16: [
        "Mariko: I'm so lucky! Photos of the afterlife are something you couldn't get in a whole lifetime!",
        "Mariko: When I get back, I've got to submit these photos to \"Fontian World\"!"
    ],
    17: ["The chest is already empty."],
}

E128 = {
    0: [
        "Yukino: This seems to be Yuriko's room. With that act of hers, you'd never imagine a room in such bad taste.",
        "Yukino: You already know we've come, don't you? Then come out! Or are you plotting something again?"
    ],
    1: [
        "Yuriko: Geez! This is Yuriko's room, so you don't have to shout, I can hear you fine!!",
        "Yuriko: More importantly, you? You have such a pretty face! To make that beauty eternal, why not die here!?",
        "Yuriko: If you keep living and age, you'll only become a dirty old lady or hag!!",
        "Yuriko: So, like Yuriko, die at the cutest time of your life! And live in this tower, staying pretty!!",
        "Yuriko: Hey, let's do that? Okay? It'll be fun! Surely!!",
        "Yuriko: Yuriko is really glad she came to this tower as the \"Snow Queen's mask\" said!",
        "Yuriko: Because I can stay cute and pretty forever! But it was a bit boring all alone, and Yuriko doesn't want to fight everyone.",
        "Yuriko: Hey? Hey??"
    ],
    2: [
        "Nanjo: You... Do you understand what you are saying?",
        "Nanjo: What you obtained through \"death\" by borrowing the \"Snow Queen's mask\" power is",
        "Nanjo: \"the end of your own existence\" and \"a real world without you,\" and \"absolute solitude\" in this tower.",
        "Nanjo: It is by no means \"eternal beauty\"!"
    ],
    3: [
        "Brown: Hnh? What are you saying, Yuriko-chan? That means you were killed by the \"Snow Queen's mask\" and became this tower's guardian, right?",
        "Brown: Well, since you're already dead... maybe you won't age.",
        "Brown: But even throwing away \"life\" and \"future\" in reality, we don't want \"eternal beauty.\"",
        "Brown: Sorry, but pass 1! That's it!!"
    ],
    4: [
        "Yuriko: S-Shut up! How could a man understand a maiden's heart!",
        "Yuriko: Hey, y-you? Judging by looks, you're the cutest one here!",
        "Yuriko: Hey? You get what Yuriko-chan is saying, right? Let's get \"eternal beauty\" here together!",
        "Yuriko: And stay pretty..."
    ],
    5: [
        "Ayase: Pass 1! Don't make fun of me! Don't lump Ayase together with a dorky woman like you!! Totally MMC!!",
        "Ayase: Ayase doesn't wanna stay pretty even after \"dying\"! You know what! In the end you've",
        "Ayase: given up on \"dying\"! On \"getting old\"!! On \"living\"!!! Everything everything everything! Every-thiiiiing!!",
        "Ayase: Given up! Run away! Thrown it all away!!! You're the worst woman!!"
    ],
    6: [
        "Nanjo: Heh. Well said, Ayase! Truly \"even a worm an inch long has its half-inch soul.\"",
        "Nanjo: Give up, Yuriko. With Ayase, the one you'd get along with best here, in this state,",
        "Nanjo: there is no one left here who will lend an ear to your nonsense."
    ],
    7: [
        "Elly: Yeah!! Ayase, so Cool! Well said! I have a new respect for you!",
        "Elly: Now, Yuriko-san. With Ayase, the one you'd get along with best, in this state, there is no one left here who will lend an ear to your words!",
        "Elly: So what will you do!!"
    ],
    8: [
        "Yuriko: Ugh............ Yuriko-chan tried so hard to help everyone, everyone! I tried to have fun with everyone, everyone!",
        "Yuriko: Why, why don't you understand me?? You blockheads!!",
        "Yuriko: Fine!! Fine!!! I won't forgive you anymore!!",
        "Yuriko: Yuriko-chan is strooong, you know!! Even if you cry and apologize later, I won't forgive you!",
        "Yuriko: I'll beat you so hard even your souls after death will vanish!"
    ],
    9: [
        "Yukino: Heh...! In Nanjo's words, you're a case of \"fools don't get cured unless they die\"!",
        "Yukino: No, in your case, it looks like you didn't get cured even after dying once!",
        "Yukino: Come on, bring it! Die again and get that stupidity cured! Here we go!"
    ],
}

E129 = {
    0: [
        "Yukino: Yuriko... You... lose! Resign yourself.",
        "Yukino: Or will you cry and cling to the kind \"Snow Queen\" who gave you \"eternal beauty\"?",
        "Yukino: What'll it be!! Huh?"
    ],
}

if __name__ == '__main__':
    for n, d in ((112, E112), (119, E119), (128, E128), (129, E129)):
        apply('E1', n, d, {})
