"""E1 entries 205-210 - farewell to Saeko-sensei; Mark arrives; the Queen of the Night freezes the school."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

p = P('ほ')
ps = P('そ')

E205 = {
    1: [
        "Nanjo: Yes. I am worried about Inaba and Sonomura. And there is something else on my mind.",
        "Nanjo: That student in the white mask looked a lot like Sonomura..."
    ],
    2: [
        "Elly: Yes! I am worried about Mark and Maki. And there is something else on my mind.",
        "Elly: That person in the white mask looked just like Maki."
    ],
    3: ["Yukino: Yeah. We've still got things we have to do."],
    4: "=Right, <FF0F>あ?<FF03><FF0E>　<FF01>",
    5: ["Yukino: We have to find Sonomura. She seemed to be suffering."],
    6: ["Yukino: Can't be helped. Well, we'll find out sooner or later."],
    7: [
        "Saeko-sensei: ...I see. Then do your best so you have no regrets!",
        "Saeko-sensei: You're adults now. I won't stop a departure that adults decided on.",
        "Saeko-sensei: But in return" + p + " ..." + p + " ..."
    ],
    8: ["Ayase: In return?"],
    9: [
        "Saeko-sensei: Come back before you become old men! And report to me in person that everyone is safe!"
    ],
    10: [
        "Yukino: Yeah, don't worry! We're Saeko-sensei's excellent students, after all!"
    ],
    11: [
        "Saeko-sensei: Excellent indeed. Every one of you in outfits that break school rules!",
        "Saeko-sensei: I wish you'd put yourselves in your homeroom teacher's shoes once in a while!!",
        "Saeko-sensei: Day after day being yelled at by the vice principal..."
    ],
    12: [
        "Saeko-sensei: Heh... Well, it seems the vice principal changed his mind because of this. He told me to tell everyone \"thank you.\"",
        "Saeko-sensei: It looks like he'll turn a blind eye to rule violations for a while."
    ],
    13: ["Ayase: Huh? That bald old man?"],
    14: [
        "Saeko-sensei: He has his good points. Now! This is no time to stand around chatting!!",
        "Saeko-sensei: You'd better get going or the sun will set!!"
    ],
    15: ["Yukino: Yeah, we're going!"],
    16: [
        "Brown: Well, you don't need to worry with me around." + ps + " ..." + ps + " Oh! Tears don't suit a pretty face" + p + ", honey. " + F6('う') + "*" + F6('　'),
        "Brown: Dehyahyahyahyahyahya"
    ],
    17: [
        "Elly: So the school has returned to normal... But this is only the beginning.",
        "Elly: Taking back the town and our peaceful days, the real battle is after that.",
        "Elly: To fight through a long, long life" + p + " Do my best! I will try hard so I have no regrets."
    ],
    18: [
        "Nanjo: \"Where there is a will, there is a way\"" + p + ", is it? With this crowd, I truly begin to believe it.",
        "Nanjo: Saeko-sensei! We will surely find Inaba and Sonomura! <FF0F>あ! Let us go!!"
    ],
    19: [
        "Ayase: Up till now Ayase has lived kinda vaguely, but seeing <FF0F>あ and Mayuzumi and the others working so hard, Ayase has to try too.",
        "Ayase: What to try at, I'll decide after we restore the town. See ya, Sensei!"
    ],
    20: [
        "Yukino: Once the town is back to normal, I'll study seriously.",
        "Yukino: I'll study" + p + " and someday become a great teacher like Saeko-sensei!",
        "Yukino: Heh..." + p + " I won't say goodbye" + p + " Sensei!"
    ],
    21: [
        "Saeko-sensei: <FF0F>あ! Thank you for everything.",
        "Saeko-sensei: Everyone seems to have found something to think about for their future. What about you?"
    ],
    22: "=Do you have any dreams?<FF03><FF0E>　<FF01>",
    23: [
        "Saeko-sensei: I see! Don't forget how you feel now, having accomplished something big, and do your best!!"
    ],
    24: [
        "Saeko-sensei: I see. Well, you're young, so there's no need to rush. Anyway, I'm counting on you to look after everyone!"
    ],
    25: ["Saeko-sensei: Now" + p + " then."],
    26: [
        "Saeko-sensei: Oh, where did you wander in from? Heh... You celebrate those kids' departure too."
    ],
}

E207 = {
    0: ["Nanjo: Inaba!!"],
    1: ["Brown: M-" + p + " Mark!?"],
    2: ["Ayase: Huh? Where's Sonomura?"],
    3: ["Mark: We're in trouble! Lend us a hand!!"],
    4: ["Yukino: Did something happen to Sonomura?"],
    5: [
        "Mark: Sorry! Even though I was with her... We went to SEBEC, but the demons inside caught us...",
        "Mark: They're armed. I can't take them on by myself."
    ],
    6: ["Yukino: What did you say!?"],
    7: ["Elly: We must rescue her quickly!!"],
    8: ["Brown: Already time for me and the rest to make our entrance!"],
    9: ["Yukino: Alright!"],
    10: ["Everyone: Let's go!!"],
}

E209 = {
    0: ["Ayase: We did" + p + " it?"],
    1: ["Yukino: Where's Saeko-sensei!?"],
    2: ["Voice: Kukukuku... Ahahahaha..."],
    3: ["Ayase: Wh-" + p + " Who's there!?"],
    4: [
        "Queen: Saeko, the symbol of your hope, has become the sacrifice" + p + " along with Tomomi.",
        "Queen: I am the Persona that dwelled in Tomomi" + p + " the Queen of the Night. As you see, I thank you.",
        "Queen: I have left my host Tomomi and left the mask, my vessel, and have been freed at last.",
        "Queen: The \"Eternal Night\" arrives, and now I am complete. I shall cover this world with white and black, nothingness and despair.",
        "Queen: Ahahahahahahahaha"
    ],
    6: [
        "Queen of the Night: You fools! Witness with your own eyes the arrival of the \"Eternal Night.\"",
        "Queen of the Night: From this castle of ice, from the peak of the castle, I shall make snow of despair fall.",
        "Queen of the Night: Kukuku..." + p + " Ahahaha..."
    ],
    7: ["Yukino: W-" + p + " Wait!!"],
}

E210 = {
    0: ["Ayase: N-" + p + " No..." + p + " way......"],
    1: ["Ayase: They're frozen!!"],
    2: ["Brown: It's... over..."],
    3: ["Nanjo: What a thing..."],
    4: [
        "Ayase: Hey, Natsumi-sensei!" + p + " Stop this bad joke!! You too, Kurouri! Hey! Come on!!",
        "Ayase: Hey" + p + " ..." + p + " ..." + p + " ...say something..."
    ],
}

if __name__ == '__main__':
    for n, d in ((205, E205), (207, E207), (209, E209), (210, E210)):
        apply('E1', n, d, {})
