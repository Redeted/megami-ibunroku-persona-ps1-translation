"""E2/217 rest; E3 entries 0-4 - Snow Queen school corridors (principal's office, library, drama club, shop)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

p = P('ほ'); pm = P('み'); pn = P('な'); pt = P('た')
H = F6('う') + "*" + F6('　')

E2_217 = {
    9: [
        "Elly: I wish this place displayed a bit more about Demons."
    ],
    10: ["Elly: That Demon from before was wonderful! I was moved."],
    11: [
        "Elly: As long as we have the \"Hama Mirror,\" we can fight the Demon in the subway, correct?"
    ],
    12: ["Brown: I'm not really interested in this kind of stuff."],
    13: [
        "Brown: Me fight that guy from before?" + pt + " ..." + pn + " Seriously?"
    ],
    14: [
        "Brown: As long as we have the \"Hama Mirror\"!" + pm + " we can fight demons, huh..."
    ],
    15: [
        "Ayase: What? <FF0F>あ is surprisingly studious, huh!"
    ],
    16: ["Ayase: Urp. I can't get that monster's smell off."],
    17: [
        "Ayase: Someday I'm definitely going to find out who that shady old man really is!"
    ],
    18: ["Reiji: <FF0F>あ, you seem to have some leeway, don't you?"],
    19: ["Reiji: I've never seen a monster like that."],
    20: [
        "Reiji: Can't be helped. Let's hurry and go get that \"Hama Mirror\" thing."
    ],
}

E3_0 = {
    0: [
        "Principal Oishi: Honestly, the vice principal... Even in picking a fight, he must have his own reasons.",
        "Principal Oishi: We should hear that first before judging..."
    ],
    1: ["Principal Oishi: I had a bad dream. Ahh, my head hurts..."],
    2: ["Principal Oishi: Education is not only about handing out punishments, surely."],
    3: [
        "Vice Principal Hanya: Outrageous! Taking a rebellious attitude! I won't hear this guy's excuses!",
        "Vice Principal Hanya: It's surely a lie anyway! As punishment, window washing, kanji copying, and then polishing my shoes!!"
    ],
    4: [
        "Vice Principal Hanya: Ah, if only that were reality... Hm, no, it's nothing. Don't disturb the copying."
    ],
    5: [
        "Vice Principal Hanya: Hey now, don't disturb the copying. Or do you want to do it too?"
    ],
    6: [
        "Kiichi-kun: You gotta be kidding me! Why am I the only one getting lectured? The student council president's just as guilty!",
        "Kiichi-kun: Is yelling without hearing reasons what educators do!"
    ],
    7: [
        "Kiichi-kun: Shut up! Why am I the only one copying!",
        "Love" + p + " love" + p + " love" + p + " strange" + p + " love" + p + " ......"
    ],
    8: [
        "Kiichi-kun: Shut up! I'm busy right now!",
        "Dog" + p + " dog" + p + " dog" + p + " fat" + p + " dog" + p + " ......"
    ],
    9: [
        "Yukino: Unbearable, that bald old man. One-sided lecturing again."
    ],
    10: ["Yukino: Is Kiichi still copying?"],
    11: [
        "Ayase: Kiichi did nothing wrong... I saw it before the school froze. He only \"warned a little\" because he couldn't stand the student council president skipping."
    ],
    12: [
        "Ayase: Hey, hey, don't you want to hit that bald head when you look at it?"
    ],
    13: ["Nanjo: Both parties in a fight are to blame. The copying should be given to both."],
    14: ["Nanjo: Nothing will start by staying here."],
    15: [
        "Brown: Being argued with logic is annoying, but I wish he'd stop getting angry on emotion."
    ],
    16: ["Brown: Let's hurry and go elsewhere."],
    17: [
        "Elly: Grown adults behaving like this is not a pretty sight."
    ],
    18: ["Elly: Where did the Queen of the Night go?"],
}

E3_1 = {
    0: [
        "Student: <FF0F>あ! Across from the library is a casino now!! I'm having a blast! You go check it out too!"
    ],
    1: [
        "Student: While you were gone, I sank all the club budget into poker...",
        "Student: Whoever plays next is lucky. The prize bonus must be way up by now..."
    ],
    2: [
        "Underclassman: Hee hee hee. It's over. We'll die someday anyway... It just comes a bit sooner. Yes," + p + " that's all.",
        "Underclassman: We get to end our lives beautiful, so we should thank the Snow Queen."
    ],
    3: [
        "Underclassman: Hee hee hee. A pitch-blue room. A pitch-blue piano.",
        "Underclassman: Pitch-blue curtains, a pitch-blue carpet. I wonder what that room is for.",
        "Underclassman: Leave here, the room right on the left. Hee hee hee hee."
    ],
    4: [
        "Underclassman: Hee hee hee. In a pitch-dark room, a light floats. The light takes me to another world. It's very lovely.",
        "Underclassman: At the crossroads right outside here, turn left and keep going straight and you'll find it.",
        "Underclassman: Hee hee hee hee."
    ],
    5: ["Yukino: A casino? Tempting."],
    6: [
        "Yukino: Huh, so the prize can go up while you're away fighting for a while."
    ],
    7: [
        "Ayase: I'm hungry~ Come to think of it, where did the home economics room go?",
        "Ayase: There're lots of leftover ingredients for the sweets I made this morning, just sitting there."
    ],
    8: ["Ayase: I'm hungry~"],
    9: [
        "Nanjo: A casino? Getting involved with such things will ruin you."
    ],
    10: ["Nanjo: Foolish fellow. It is his own doing."],
    11: [
        "Brown: Huh~ Sounds fun! Let's go check it out! The casino!!"
    ],
    12: ["Brown: I wanna go blow off steam at a casino once in a while."],
    13: [
        "Elly: That girl by the window... she has been muttering something for a while."
    ],
    14: ["Elly: That girl by the window... she is still muttering something."],
}

E3_2 = {
    0: [
        "Student Council President: Phew... That was close, that was close. Man, I got into a fight and almost got caught by the vice principal. Nearly got a lecture.",
        "Student Council President: Well, he won't find me here."
    ],
    1: [
        "Student Council President: Ow ow ow... M-My legs are numb. I'm sick of lectures."
    ],
    2: [
        "Student Council President: You guys work hard, too. Leave this to me, the president, and do your best."
    ],
    3: [
        "Drama Club Member: This is from when Saeko-sensei was in the drama club. I heard she competed for the Snow Queen role with her best friend.",
        "Drama Club Member: I forgot the surname, but I think it was someone named Tomomi. Sensei was crying when she told that story."
    ],
    4: [
        "Drama Club Member: The Snow Queen mask had a lot of sad history. When the town returns to normal, maybe we'll turn that story into a play."
    ],
    5: ["Yukino: Our drama club's so good it wins contests, huh."],
    6: [
        "Yukino: For the three who guarded the towers, too, let's hurry and go beat the Queen of the Night."
    ],
    7: [
        "Ayase: Cramped room~ It's like being inside a super huge fridge~"
    ],
    8: [
        "Ayase: That student council president! Thinking someone like him runs the school makes me mad!"
    ],
    9: ["Nanjo: Where did the other clubrooms go?"],
    10: ["Nanjo: There does not appear to be anything useful."],
    11: [
        "Brown: Is this full of the sweat-and-tears aroma of maidens who devoted their youth to drama? What do I do, hey!!"
    ],
    12: [
        "Brown: I wonder if TV station dressing rooms are like this. I wanna go see~"
    ],
    13: [
        "Elly: Ice everywhere. Only cold, I cannot find it beautiful."
    ],
    14: ["Elly: Where are the other club members?"],
}

E3_3 = {
    0: [
        "Boy Student: Oh, you came too, <FF0F>あ! Look! With this, we can fight back whenever demons come!!"
    ],
    1: [
        "Boy Student: Huh? The lineup's different from last time. It's gotten even more dangerous..."
    ],
    2: [
        "Teacher: What's with that child! This is a school!! Don't open a shop without permission!!"
    ],
    3: [
        "Shopkeeper: Welcome. I come from Demon Mountain. I bring very good things.",
        "Shopkeeper: Oni-san need this. I study, so buy, okay!"
    ],
    4: [
        "Shopkeeper: Waiting for you! Oni-san lucky. Shop closing soon. Last sale, loss if you don't buy!"
    ],
    5: [
        "Yukino: From Demon Mountain? Then is that kid a demon too?"
    ],
    6: [
        "Yukino: Making humans and demons fight and doing business off it. What a terrible kid, honestly!"
    ],
    7: ["Ayase: Hey~ Is this the real thing?"],
    8: ["Ayase: What country was that kid born in?"],
    9: ["Nanjo: Amazing!! All of it looks usable."],
    10: [
        "Nanjo: How many times has that child saved our lives? Even if we are overcharged a bit, we must be grateful."
    ],
    11: [
        "Brown: Dehya~ What is this kid, selling dangerous things at school. Well, whatever, such a petty matter."
    ],
    12: ["Brown: Dehyaaa! Isn't it even more amazing now?"],
    13: [
        "Elly: That child seems to be a merchant of death from the Demon world."
    ],
    14: [
        "Elly: Whichever of us or the Queen wins, does it not matter to that child?"
    ],
}

E3_4 = {
    0: ["Girl Student: Kyaa, look look! This dress is so cute! " + H],
    1: ["Girl Student: Kyaa, look look! This skirt is so cheap! " + H],
    2: ["Himeno: Ah... cute clothes... Ah... still expensive..."],
}

if __name__ == '__main__':
    apply('E2', 217, E2_217, {})
    for n, d in ((0, E3_0), (1, E3_1), (2, E3_2), (3, E3_3), (4, E3_4)):
        apply('E3', n, d, {})
