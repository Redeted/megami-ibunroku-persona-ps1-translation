"""E2 entries 207-217 - other-world shops, hospital, subway-side NPCs."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

pk = P('キ')
H = F6('う') + "*" + F6('　')

E207 = {
    6: [
        "Nanjo: The weapons placed here are also products of Sonomura's imagination, then... How strange."
    ],
    7: ["Ayase: Don't they have guns with cute flower patterns?"],
    8: [
        "Brown: If real convenience stores started selling weapons, Japan would be finished."
    ],
    9: ["Elly: No matter how many times I come, I cannot get used to the shop's atmosphere."],
    10: ["Elly: No matter how many times I come, I cannot get used to the shop's atmosphere."],
    11: ["Reiji: If you're buying, hurry up."],
}

E208 = {
    2: [
        "Townsperson: This was such a livable town. What on earth happened? Maybe I'm having a bad dream."
    ],
    3: ["Maki: A livable town, huh... I have to apologize to the townspeople too."],
    4: ["Mark: Same old suspicious shop."],
    5: [
        "Nanjo: A commoners' shop has many unusual things. Well, this town is in a class of its own."
    ],
    6: [
        "Ayase: I'm hungry~ But Ayase will hold out. Sonomura's in trouble, after all."
    ],
    7: ["Brown: I'm tired from walking~ but this is no time to say that!"],
    8: ["Elly: Have you finished shopping?"],
    9: ["Elly: Have you finished shopping?"],
    10: ["Reiji: How long are you going to shop?"],
}

E209 = {
    0: [
        "Shopkeeper: Boy~ It's a terrible situation, isn't it~ But business goes on~"
    ],
    1: [
        "Townsperson: It feels like someone is going around destroying this town..."
    ],
    2: ["Maki: Tadashi-kun's dad... I'm sorry."],
    3: ["Mark: It's always this song whenever I come~ It's gonna drive me crazy."],
    4: ["Nanjo: Heh. I am used to it now! Trying to brainwash me is pointless."],
    5: ["Ayase: Kyaaah! These diapers have frogs on them! So pretty~~~~ " + H],
    6: ["Brown: Hey hey, don't they have love potions or something!"],
    7: ["Elly: Is there not any decent medicine that fits daily life?"],
    8: ["Elly: Is there not any decent medicine that fits daily life?"],
    9: ["Reiji: What? Is it wrong for me to look at baby goods?"],
}

E210 = {
    0: ["Mannequin Girl: Welcome~"],
    1: ["Townsperson: If only we could have stayed as before, we'd have been happy..."],
    2: [
        "Maki: Just as before... But this town is a fake, right? No matter how good a town it is."
    ],
    3: [
        "Mark: The clerk girl in the real world would faint if she saw this."
    ],
    4: [
        "Nanjo: There is no end if one looks upward, but we should at least prepare minimum equipment."
    ],
    5: ["Ayase: Isn't there protective gear with animal prints?"],
    6: ["Brown: Let's see, armor with a cool design..."],
    7: [
        "Elly: It is to avoid being defeated, so I do not intend to be picky, but the Sense just does not suit me."
    ],
    8: [
        "Elly: It is to avoid being defeated, so I do not intend to be picky, but the Sense just does not suit me."
    ],
}

E211 = {
    0: [
        "Clerk: The customer is a god, they say. You're a customer, it seems. In other words, you're a god, it seems.",
        "Clerk: Please! Put the town back to normal! I can't restock and I'm in trouble!"
    ],
    1: [
        "Townsperson: I always felt something was different about this town. Maybe the disturbance happening was for the best."
    ],
    2: [
        "Maki: The disturbance was for the best... Indeed. Otherwise I... wouldn't have known anything."
    ],
    3: ["Mark: Let's hurry to the forest!"],
    4: ["Mark: Let's hurry to the shrine!"],
    5: ["Mark: Let's hurry to the school!"],
    6: [
        "Nanjo: Restocking? Come to think of it, where do this town's goods come from? Well, there is no use thinking about it."
    ],
    7: ["Ayase: I'm hungry~ But hold out, hold out!"],
    8: [
        "Brown: It's a food shop, so pray to the gods? Dehyahyahyahyahya"
    ],
    9: ["Elly: <FF07>あ, we cannot be leisurely."],
    10: ["Elly: <FF07>あ, we cannot be leisurely."],
    11: [
        "Reiji: You've got no business in a place like this... Honestly, are you gutsy or just an idiot? I can't tell, but you're certainly an interesting guy."
    ],
}

E212 = {
    11: [
        "Nurse: Don't let Maki-chan get hurt, okay? She's the idol of the town!"
    ],
    12: [
        "Nurse: Oh, you're from the same high school as Sonomura Maki-chan.",
        "Nurse: Eh? You're friends with her!? Friends with the town idol, how envious!!",
        "Nurse: Get her autograph for me next time!!"
    ],
    13: [
        "Maki: Idol? That's not true... Everyone's just made to think so."
    ],
    14: [
        "Mark: Sonomura an idol, huh... Sounds good! Don't you think so too?"
    ],
    15: [
        "Nanjo: ..." + pk + " That must be a painful line for Sonomura, who knows everything now."
    ],
    16: ["Ayase: Doctors seem kinda arrogant."],
    17: [
        "Brown: Forget the injuries, give me medicine for my clever head."
    ],
    18: [
        "Elly: Being an Idol is hard in many ways. You have to deceive yourself too."
    ],
    19: [
        "Elly: Being an Idol is hard in many ways. You have to deceive yourself too."
    ],
    20: ["Reiji: What's wrong? If something this much gets to you, you've got a long way to go."],
}

E214 = {
    4: "=It'll cost 3000 yen, okay?<FF03><FF0E>　<FF01>",
}

E215 = {
    0: ["Maki: Are you done? Let's hurry and get out of here!"],
    1: [
        "Nanjo: Wounds of the heart are apparently hard to heal because they cannot be seen.",
        "Nanjo: No, there is no special meaning. It just came to mind."
    ],
    2: ["Mark: What are you being so leisurely for? Once you heal your injuries, we're setting out!"],
    3: [
        "Elly: I want to exterminate the Demons and return the town to peace, but I also feel a little sad."
    ],
    4: [
        "Brown: When will the day come that I become the idol of the whole town, no, all of Japan!"
    ],
    5: ["Ayase: Ayase wants to go back to being an ordinary schoolgirl soon!"],
    6: [
        "Reiji: I'd like to settle everything quickly. You have people waiting for you to come back, too, don't you?"
    ],
    7: ["Nurse: It's dangerous, so don't wander around too much!"],
    8: [
        "Doctor: I hope the demons disappear soon. Though then our business would dry up, ha ha ha."
    ],
}

E216 = {
    3: [
        "Elly: I want to exterminate the Demons quickly and return the town to peace..."
    ],
    6: [
        "Reiji: I hope everything is resolved quickly. You have people waiting for you to come back, too, don't you?"
    ],
    7: [
        "Doctor: This place too used to be a peaceful, wonderful town, but it suddenly fell into ruin. Now, how are you feeling?"
    ],
    8: [
        "Nurse: At this rate, this town will perish. I can't hold any hope either.",
        "Nurse: Sometimes I even think it'd be fine if everything just disappeared."
    ],
}

E217 = {
    0: ["Maki: Oh, <FF07>あ-kun, aren't you going to the shrine?"],
    1: [
        "Maki: The monster in the subway... I feel like I've seen it in a book. Was it a Cthulhu book?"
    ],
    2: ["Maki: The \"Hama Mirror\" is here, isn't it?"],
    3: [
        "Nanjo: Do you not trust Kurouri? Unlike the one in our town, he seems quite capable."
    ],
    4: ["Nanjo: Still, that was a terrible smell!"],
    5: [
        "Nanjo: Right, the \"Hama Mirror\" should have been on display here."
    ],
    6: [
        "Mark: It's like a field trip! Is there anything different from our town?"
    ],
    7: [
        "Mark: It said \"Yog-soto,\" right, that monster? What was that about?"
    ],
    8: ["Mark: We ran into that shady old guy again."],
}

if __name__ == '__main__':
    for n, d in ((207, E207), (208, E208), (209, E209), (210, E210), (211, E211), (212, E212), (214, E214), (215, E215), (216, E216), (217, E217)):
        apply('E2', n, d, {})
