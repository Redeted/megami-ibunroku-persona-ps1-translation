"""E2 entries 45-52 - hospital, candy store, pharmacy, casino lobby, clothes shop NPCs."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

pm = P('み'); pn = P('な'); pt = P('た'); pyu = P('ゆ')

E45 = {
    8: ["Nurse: Our hospital was just rebuilt, you know! Pretty, isn't it?"],
    9: [
        "Nurse: I hear things are a mess outside? If I weren't on duty, I'd go see!"
    ],
    10: [
        "Doctor: You're students of St. Hermelin, aren't you? I hear the gym construction is finished. It must be easier to use now that it's new."
    ],
    11: ["Doctor: The nurses here are so starstruck. It won't do."],
    12: "=Doctor: Now, what shall we do?<FF03><FF0E>ち<FF01>",
    13: ["Doctor: Alright, then, everyone..."],
    14: "=Doctor: It will cost 800 yen.<FF03>Is that all right?<FF02><FF03><FF0E>　<FF01>",
    15: ["Doctor: Hm. Then let us treat you."],
    16: ["Doctor: Yes, that should do."],
    17: "=Doctor: Anything else?<FF03><FF0E>　<FF01>",
    18: [
        "Doctor: I'm afraid we cannot treat you without money... Come back with the fee."
    ],
    19: [
        "Doctor: I hope skimping on the treatment fee doesn't cause you trouble later."
    ],
    20: ["Doctor: Alright, then come right away if anything happens again."],
    21: ["Doctor: I'm not idle either. If you have no business, please be on your way."],
}

E46 = {
    0: [
        "Nanjo: I have never eaten penny candy. Yamaoka would not allow it."
    ],
    1: [
        "Nanjo: That shopkeeper seems to suspect us. But we who possess such strange power, are we still truly human?",
        "Nanjo: What do you think?"
    ],
    2: [
        "Mark: Do kids these days still eat penny candy? I went there every day! Drew lots and stuff!"
    ],
    3: ["Mark: <FF0F>あ, you're so carefree, huh."],
    4: [
        "Yukino: A shop like this now and then is fine, but have you forgotten we have to go to the hospital?"
    ],
    5: ["Yukino: I'm worried about the school too. I feel uneasy somehow."],
    6: [
        "Elly: There are surprisingly calm people around. I am impressed."
    ],
    7: [
        "Shopkeeper: One bite, a thousand years. Two bites, ten thousand years.",
        "Shopkeeper: The taste of Senrinmando, which prolongs life. Now, how about one?"
    ],
    8: [
        "Shopkeeper: ..." + pt + " Are you real humans?" + pm + " Well, if you're customers, you're welcome."
    ],
}

E47 = {
    0: [
        "Nanjo: ...the sun" + " was... disparises... ...Damn! That song will not leave my head!"
    ],
    1: [
        "Nanjo: \"Be prepared and you have nothing to fear!\"" + pyu + " ...Yamaoka used to say that."
    ],
    2: [
        "Mark: Don't tell me you're gonna settle this with medicine? Hey, let's go to the hospital properly!"
    ],
    3: [
        "Mark: When I left home this morning, I never imagined something like this would happen."
    ],
    4: ["Yukino: That lady is the nosy type, for sure."],
    5: [
        "Yukino: I wonder how badly Sonomura's mom is hurt. I hope it's not bad."
    ],
    6: [
        "Elly: The shrine is south, through the shopping street and then straight south. You enter a narrow street, so it may be hard to find."
    ],
    7: [
        "Shopkeeper: Are you St. Hermelin students? Do you know my son? His name's Tadashi!",
        "Shopkeeper: He's hopeless and lazy, but he fell for a super cute girl!",
        "Shopkeeper: If a girl like that married into the family, I'd be so happy!" + pyu + " ...Eh? Oh, medicine. Yes, yes."
    ],
    8: [
        "Shopkeeper: Welcome! Hey, you, have you met Tamaki-chan? I'm so worried whether Tamaki-chan is safe...",
        "Shopkeeper: Not that I care about my son at all! ...Eh? Oh, medicine. Yes, yes."
    ],
    9: [
        "Customer: Hey, you think it's weird too, right? Kaneda-san! To become that rich in just half a year! It's suspicious. Definitely weird!"
    ],
    10: [
        "Shopkeeper: Oh my? Do you need my Tadashi? That good-for-nothing should be at his club by now.",
        "Shopkeeper: Ahh, I'd like to have a verbal spat with Tamaki-chan at least once. *"
    ],
    11: ["Shopkeeper: Oh my? Medicine is over here!"],
}

E48 = {
    0: [
        "Nanjo: To think you were a gambler. One really cannot judge people by appearances."
    ],
    1: [
        "Nanjo: What a blissful fellow. To have such leeway at a time like this is almost enviable."
    ],
    2: [
        "Mark: Elly's quite a celebrity, huh! With looks that cool, it might be natural."
    ],
    3: [
        "Mark: I don't dislike casinos either, but right now I want to go to the shrine first."
    ],
    4: [
        "Yukino: I don't care what you do, but could you do it after we go to the hospital?"
    ],
    5: [
        "Yukino: Eriko's fearlessness is amazing. Well, with her looks, I guess so."
    ],
    6: ["Elly: I do not care for this kind of person..."],
    9: [
        "Customer: Hey, you guys are St. Hermelin students? Then you know that girl, right?",
        "Customer: Long hair, nice figure, called Sally or Merry or something... That girl's beautiful, isn't she? Hey, introduce me sometime!"
    ],
    10: [
        "Customer: Oh, there you are, I was looking for you! You shouldn't wander around!",
        "Customer: With demons showing up, it's scary, right? I was thinking of protecting you!"
    ],
    11: [
        "Elly: Thank you very much for that. But I have more knowledge about Demons than you,",
        "Elly: and can protect myself, so no" + pn + " thank" + pn + " you!"
    ],
    12: ["Customer: O-" + pn + " Oh, I see..."],
    13: [
        "Customer: No Elly girl here? I was going to show off my manly side..."
    ],
    14: [
        "Customer: Tch, my plan fell through. But sooner or later she'll say she's scared of demons! Until then, I'll keep attacking!"
    ],
    15: [
        "Customer: Dang, lost again!",
        "Customer: I sank so much in, the next guy might hit the jackpot and profit instead.",
        "Customer: Ah! Maybe you're going to play next? Ugh, that's unfair!"
    ],
}

E49 = {
    0: [
        "Nanjo: It is surprising that the townspeople know so much about St. Hermelin."
    ],
    1: [
        "Nanjo: A place I would prefer to avoid visiting, a doctor's..."
    ],
    2: [
        "Mark: Don't you find this a pain now? Are you giving up on going to the hospital?"
    ],
    3: ["Mark: Damn, this is irritating. We gotta get to the shrine quick..."],
    4: [
        "Yukino: Saeko-sensei is our senior, right? I've heard that."
    ],
    5: [
        "Yukino: Maybe the one that nurse saw was Sonomura's mom?"
    ],
    6: [
        "Elly: After healing the wound, let us hurry to Araya Shrine. It is very close now."
    ],
    7: [
        "Elly: After healing the wound, let us hurry to the abandoned factory.",
        "Elly: But can we truly enter SEBEC from such a place?"
    ],
    8: [
        "Nurse: Oh my, that uniform! How nostalgic, I'm an alumna! My classmate's a teacher now, too.",
        "Nurse: Do you know Takami Saeko? Even so, I can't believe Saeko is a teacher! Hee hee..."
    ],
    9: [
        "Nurse: They say an injured woman walked around here a while ago. I wonder if she was attacked by a demon..."
    ],
    10: [
        "Doctor: Oh, hello. As always, your friends are quite individualistic."
    ],
}

E50 = {
    0: [
        "Nanjo: I cannot join a conversation about haunted houses. I have never been to one, after all."
    ],
    1: [
        "Nanjo: I would like to become able to heal wounds with guts alone."
    ],
    2: [
        "Mark: The haunted house is basically just an abandoned house, right? We played there without permission."
    ],
    3: [
        "Mark: It's quiet here. It feels as if nothing ever happened."
    ],
    4: ["Yukino: Actually, I played in the haunted house too."],
    5: [
        "Yukino: Those things out in town... " + pt + " they're not bears, are they?"
    ],
    6: [
        "Elly: But why did Demons suddenly begin to appear in town?"
    ],
    7: [
        "Nurse: Did you go to the haunted house as a kid too? It was the kids' playground."
    ],
    8: [
        "Nurse: A bear showed up, they say? A brown one? A polar bear? Or maybe a raccoon?"
    ],
    9: ["Doctor: Nice weather again today."],
    10: ["Doctor: Do bears appear even in a city like this...?"],
    13: "=Doctor: It will cost 1000 yen.<FF03>Is that all right?<FF02><FF03><FF0E>　<FF01>",
}

E51 = {
    0: [
        "Nanjo: A uniform suffices for my clothing. And this muffler, that is all."
    ],
    1: [
        "Mark: Speaking of clothes, what do you think of Nanjo's muffler? He's always wearing it."
    ],
    2: [
        "Yukino: Did Yuka ask you to get clothes for her? We're going to the hospital once you're done!"
    ],
    3: [
        "Clerk: The people in this town all have bad taste! The only slightly better one is the brown-haired boy I see sometimes. He wears goggles, and he's cute!"
    ],
}

E52 = {
    0: [
        "Nanjo: Now then, where to next? I do not mind anywhere, as long as we end at the hospital."
    ],
    1: [
        "Nanjo: Business cannot stop even with demons around, it seems. Humans are unexpectedly tough."
    ],
    2: [
        "Mark: Music... Isn't that piano and singing?",
        "Mark: Huh? I heard something just like that somewhere."
    ],
}

if __name__ == '__main__':
    for n, d in ((45, E45), (46, E46), (47, E47), (48, E48), (49, E49), (50, E50), (51, E51), (52, E52)):
        apply('E2', n, d, {})
