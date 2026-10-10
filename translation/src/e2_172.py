"""E2 entries 172-181 - other-world school chatter, Yukino does not remember, the forest rumor."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

pm = P('み'); pn = P('な'); pg = P('ぎ'); pt = P('た'); pyu = P('ゆ')

E172 = {
    13: ["Principal Oishi: No, Vice Principal, it's thanks to your guidance!"],
    14: ["Nanjo: ..." + pg + " I cannot put up with this. <FF0F>あ, let us go!"],
    16: [F6('い') + "Hanya Vice Principal<FF03>Known as Vice Principal Hannya. Supposed to be strict and disliked by students, but..."],
}

E173 = {
    0: ["Maki: This town is quite different from your town, too, huh!"],
    1: ["Nanjo: The school's problem has been settled for the time being, but..."],
    2: [
        "Mark: It feels weird. The faces are familiar but something's different about them."
    ],
    3: [
        "Elly: Dawdling in a place like this will get us nowhere! Now, let us go outside!"
    ],
    4: [
        "Brown: The inside of the school alone is too small for my stage! Wahahahaha!"
    ],
    5: ["Ayase: Why did they try to lock Ayase and the others in?"],
    6: [
        "Reiji: I've got no business with this school. I just want to beat that guy quickly."
    ],
    7: ["Mark: Hey, Yukino! Long time no see!"],
    8: ["Yukino: ...I don't think it's been a long time."],
    9: [
        "Nanjo: Indeed, you are right. Playing Persona-sama, visiting the hospital, and that incident happening..."
    ],
    10: ["Yukino: ......?"],
    11: ["Nanjo: Surely you were watching with us?"],
    12: [
        "Yukino: Persona-sama play?" + pm + " ...Visiting? Whose? What are you talking about?"
    ],
    13: [
        "Nanjo: ..." + pm + " You do not remember? Or are you not the Mayuzumi we know?",
        "Nanjo: ..." + pm + " In any case, it seems best to withdraw for now."
    ],
    14: [
        "Mark: Hey, <FF0F>あ, Naito said to come to the library, didn't he? Let's hear him out before we go outside."
    ],
}

E174 = {
    0: [
        "Maki: It seems we really are the only ones with this kind of power."
    ],
    1: [
        "Nanjo: I cannot believe Kandori will stay quiet like this. What will he do next..."
    ],
    2: [
        "Nanjo: That girl seems to hold considerable power... It would be a problem if someone were abusing it."
    ],
    3: ["Mark: No hole here either, I guess."],
    4: [
        "Mark: It's clear she's no ordinary girl, though."
    ],
    5: [
        "Elly: Whatever Demon appears, we will be fine! We only have to solve it ourselves."
    ],
    6: [
        "Elly: Even if her appearance is as cute as an angel, her inside is not necessarily so."
    ],
    7: [
        "Brown: Everywhere I go it's demons, demons. Isn't there a more fun story?"
    ],
    8: [
        "Brown: A kid who's too naughty gets a spanking from big brother!"
    ],
    9: [
        "Ayase: This school's kinda weird. It smells somehow oddly fake."
    ],
    10: [
        "Ayase: This place really is different from Ayase's school, huh. No wonder it seemed fake!"
    ],
    11: [
        "Reiji: Happy fools. They lounge around without even knowing what's happening."
    ],
    12: [
        "Student: Why is the girl in black targeting this school? Does she hold a grudge or something?"
    ],
    13: [
        "Student: I'm not surprised by anything anymore! Even if I heard that you can control demons too!",
        "Student: ..." + "Eh?" + pm + " You really can?" + pg + " ...Come on! No way, right?"
    ],
    14: ["Student: Doesn't the girl in black look like somebody?"],
    15: [
        "Student: I just remembered. I've met a girl in white. A girl in white clothes..." + pm + " But that's unrelated, right?"
    ],
}

E175 = {
    0: [
        "Maki: Your school's gym is new, right? Does it have clubrooms, too?"
    ],
    1: [
        "Nanjo: How old-fashioned. It would not be strange if it collapsed at any time."
    ],
    2: [
        "Mark: The curtains are full of holes, so it'd be easy to peek" + pg + " ...Just kidding! I don't peek, me!"
    ],
    3: [
        "Elly: The more I see of this town, the more mysterious it is. It truly seems like the past."
    ],
    4: [
        "Brown: Tch, filthy. They should just tear it down already, this place too!"
    ],
    5: ["Ayase: Ayase has never been to a place like this."],
    6: ["Reiji: I can't keep up with your strolling."],
    7: [
        "Student: Ah! You didn't come to peek, did you!"
    ],
    8: ["Mark: W-What the hell! Who'd peek at you lot..."],
    9: [
        "Student: President~!" + pn + " We want a clubroom for the ballet club~!",
        "Student: If we had a clubroom, we wouldn't get peeked on while changing!"
    ],
    10: [
        "Mark: " + pm + "I said" + pn + " I'm not a peeper, I told you!!"
    ],
    11: ["Elly: ...It is useless, Mark. Now, let us go."],
    12: ["Brown: It's useless for you to say it, Mark. Now let's go!"],
    13: [
        "Ayase: Inabaaa" + pm + " Isn't your usual behavior too bad? Come on, let's go already!"
    ],
    14: ["Nanjo: Do not fixate on trivial things, Inaba! Now, let us go."],
}

E176 = {
    0: [
        "Student: Th-That's the girl! The one who took Kozai-san away! She seemed to be bringing demons too!",
        "Student: Do we have to just wait here to be attacked by demons?"
    ],
    1: ["Maki: It's okay! Don't worry, leave it to us!"],
    2: ["Maki: <FF07>あ-kun, let's hurry!"],
}

E177 = {
    0: ["Student: I've met a girl who looks like that girl in black."],
    1: ["Nanjo: You mean there is another girl?"],
    2: [
        "Student: Probably. ...There's a place that's a forest now, but until a little while ago was a flower garden, right?",
        "Student: I saw her playing there."
    ],
    3: [
        "Mark: Let's see, a former flower garden that's now a forest" + pm + " ...I don't get this town."
    ],
    4: [
        "Elly: A forest..." + pm + " Is it about what Naito-kun said, that the police station's location has become a forest?"
    ],
    5: [
        "Ayase: Forest, like what Naito said? That the police turned into a forest?"
    ],
    6: [
        "Brown: Forest, huh. Naito said something like that, didn't he. That the police became a forest."
    ],
    7: [
        "Nanjo: A forest..." + pm + " Speaking of which, Naito said the police station's site had become a forest."
    ],
    8: [
        "Maki: The police, that's where we went to save Inaba-kun and Uesugi-kun, right?",
        "Maki: Now that you say so, that's indeed around there. It used to be a beautiful flower garden, but suddenly became a big forest, and I was surprised too."
    ],
    9: [
        "Student: What are you all mumbling about? ..." + pt + " You guys are suspicious. Hey, are you really <FF0F>あ?"
    ],
    10: [
        "Maki: Hey, everyone, we have to hurry! Then we're going now, see you!"
    ],
}

E178 = {
    0: [
        "Maki: Let's hurry and find that girl! She must be somewhere in the school!"
    ],
    1: [
        "Nanjo: Why does the girl in black target the school? What good would attacking a school do?"
    ],
    2: ["Mark: When can we save the real Sonomura..."],
    3: [
        "Elly: Does the girl in black really bring Demons with her? If so, we must steel ourselves."
    ],
    4: [
        "Brown: Hey, <FF0F>あ, don't you worry about leaving two women behind? If you want, I'll stay here and protect the teachers!"
    ],
    5: [
        "Ayase: Finding the nurse's office in a place like this somehow makes me feel relieved."
    ],
    6: ["Reiji: What's with that gloomy teacher?"],
    10: [
        "Natsumi-sensei: Ah, <FF0F>あ-kun. What's going on right now? I don't know what to do either, I'm so troubled" + pyu + " Right, Saeko-sensei?"
    ],
    12: [
        "Natsumi-sensei: At a time like this I thought she'd say something" + pg + " but she's still gloomy..."
    ],
    13: [
        "Natsumi-sensei: If you get hurt, come to the nurse's office! * Now, let me take a look."
    ],
}

E181 = {
    0: [
        "Himeno: Oh, everyone, what do you want? Did you come to see our treasured heirlooms?",
        "Himeno: But I'm sorry, to prevent theft they're not open to the public."
    ],
    1: [
        "Mark: I don't even wanna see your house's treasures! Does \"to prevent theft\" mean you suspect us?"
    ],
    2: [
        "Himeno: Oh, did it sound like that? How resentful you are. I didn't mean it that way."
    ],
    3: [
        "Elly: <FF07>あ... I feel a little unwell. May I go outside first?"
    ],
    4: [
        "Brown: Gaah! This is so annoying! Who does she think she is, just because she's a bit rich!"
    ],
    5: ["Ayase: Himeno, you were way cuter before."],
}

if __name__ == '__main__':
    for n, d in ((172, E172), (173, E173), (174, E174), (175, E175), (176, E176), (177, E177), (178, E178), (181, E181)):
        apply('E2', n, d, {})
