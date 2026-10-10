"""E2 entries 192-199 - Black Market and Kama Palace approach NPCs."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

pm = P('み'); pn = P('な'); pg = P('ぎ'); pru = P('る')

E192 = {
    8: [
        "Nurse: My happiness wasn't thanks to the Queen after all! Then what am I happy thanks to?"
    ],
    9: ["Doctor: What, a cold? If it's a cold, sleep it off!"],
    12: "=Doctor: It will cost 1500 yen.<FF03>Is that all right?<FF02><FF03><FF0E>　<FF01>",
}

E193 = {
    0: ["Maki: Is the Senrinmando here really that strange?"],
    1: ["Nanjo: There seem to be no decent shops in this market."],
    2: [
        "Mark: So we can't eat Senrinmando sweets in this town."
    ],
    3: ["Elly: How exotic! What a lovely shop!"],
    4: [
        "Brown: I like this pot. Hey, <FF08>あ, wanna give it to me as a present?"
    ],
    5: [
        "Ayase: Did you talk to the person at this shop? Super weird makeup!"
    ],
    6: ["Reiji: ...Is this a haunted house?"],
    9: [
        "Customer: Me too, if I were a pretty boy like a puppy caught in the rain, the Queen would've liked me!",
        "Customer: Then I could be living leisurely in the palace instead of a dirty place like this."
    ],
    10: [
        "Customer: The men at the Harem Palace were submitting to the Queen, right? That's pathetic. I'm gonna live without submitting to anyone."
    ],
}

E194 = {
    0: [
        "Maki: This shop is run by the uncle of my friend Tadashi-kun.",
        "Maki: Tadashi-kun gets along terribly with a transfer student girl named Tamaki-chan, and they won't even talk to each other anymore..."
    ],
    1: [
        "Nanjo: ...If you recover hit points..., enough! <FF0F>あ, you sing too!"
    ],
    2: [
        "Mark: Tadashi's uncle, huh. Doesn't seem much different from our town."
    ],
    3: [
        "Elly: Excuse me, but does the medicine here really work?"
    ],
    4: [
        "Brown: That old guy's hair" + pg + " surely that's not a wig, is it?"
    ],
    5: [
        "Ayase: Everything for babies is cute. It's fun just to look."
    ],
    6: ["Reiji: What a crazy old guy."],
    7: [
        "Shopkeeper: Welcome to Satomi Tadashi! Call me Sato-chan~ *",
        "Shopkeeper: Alright, let's do some business!"
    ],
    8: [
        "Customer: I'm feeling blue today. At times like this, all there is to do is go to the bar and talk about the Queen's paintings."
    ],
    9: [
        "Customer: The Queen's finally gone! I've got to raise a toast at the bar!"
    ],
    10: [
        "Shopkeeper: You can't go in there~ Even if you say just a little, it's no good~!"
    ],
}

E195 = {
    0: ["Maki: You know, <FF07>あ-kun, actually, I..."],
    1: ["Nanjo: Well, now and then a splash of fun is necessary."],
    2: ["Mark: Alright! I'll show you my poker skills!"],
    3: [
        "Elly: I do not care for places like this! The air is bad!"
    ],
    4: [
        "Brown: Heh heh! A casino is the way to go! Hey, <FF08>あ, by the way, what do you think of that thing at the counter...?"
    ],
    5: [
        "Ayase: Hey, <FF0F>あ! Save up coins and get Ayase a piercing! Eh, there's only Paralyma Stones and such? Ugh, disappointing!"
    ],
    6: ["Reiji: Hmph, how stupid."],
    9: [
        "Customer: You don't have a mole. Did you just arrive here? Now the trend is to wear a mole like the Queen."
    ],
    10: [
        "Customer: Oh no, I forgot to take off my mole! Ugh, how lame!!"
    ],
    11: [
        "Customer: I sometimes see a girl in black clothes in this market. I wonder if even a little kid like that got trapped here?"
    ],
    12: [
        "Customer: They say the girl in black clothes grants any wish."
    ],
}

E198 = {
    0: ["Maki: <FF07>あ-kun, I'm very anxious."],
    1: ["Maki: ..." + pru + " Chisato, I wonder what happened to her."],
    2: [
        "Maki: Everyone seems to be being considerate of me. I'm totally fine, though."
    ],
    3: [
        "Nanjo: Yamaoka always told me to hold my pride and never to fawn on the strong."
    ],
    4: [
        "Nanjo: Vanished from our town, kidnapped by Aki in this one too" + pm + " and a Harem Queen no less."
    ],
    5: ["Nanjo: A woman's heart is difficult, is it not, <FF0F>あ?"],
    6: ["Mark: If I meet the Queen, she's in for it!"],
    7: [
        "Mark: Acting like a ruler in a place like this... What am I supposed to tell Naito?"
    ],
    8: [
        "Mark: Did Sonomura give up on Naito? Maybe she's got someone else she likes" + pm + " ...Heh, no way."
    ],
    9: ["Elly: The one called the Queen must be quite a lover of pretty faces."],
    10: [
        "Elly: Turning people into ornaments is like a detective novel I once read." + pm + " ...Dreamy... Oh, excuse me."
    ],
    11: ["Elly: What is difficult is the human heart."],
    12: [
        "Brown: Hey, hey" + pm + " Who's cooler, that guy standing there or me? It's me, right? Right, right?"
    ],
    13: ["Brown: Hmm. That was one huge mole..."],
    14: [
        "Brown: Even that Kozai had a complex, huh. Me? I'm perfect, so there's no way I'd have one!"
    ],
    15: [
        "Ayase: I wonder if the Queen has an afro too... I'm curious."
    ],
    16: [
        "Ayase: What happened with those moles? Don't underestimate UV rays, I guess!"
    ],
    17: [
        "Ayase: After having such a good time, she makes up with Naito at the end, the sly one."
    ],
    18: ["Reiji: You need something from me?"],
    19: [
        "Reiji: It's better to find out early than to pass time thinking someone's a friend without noticing."
    ],
    20: ["Reiji: Pointless. I can't keep up with kids' games."],
    21: [
        "Young Man: This is a painting by the Queen! Amazing, right?",
        "Young Man: The Queen has talent at painting, and above all she's beautiful! She's gotten more moles lately..." + pm + " but still, she's beautiful!"
    ],
    22: [
        "Young Man: This painting's no good! No talent at all! Calling yourself Queen, you should be ashamed!"
    ],
}

E199 = {
    0: ["Maki: Chisato..." + pm + " There's no way, right!"],
    1: ["Maki: It feels like I'm having a bad dream."],
    2: [
        "Maki: I hope Chisato gets along well with Naito-kun. I'm not just being a sore loser" + pm + " because" + pm + " I..."
    ],
    3: [
        "Nanjo: Is he locking us in to tease us? Or is it stalling for time? I cannot grasp his intent."
    ],
    4: [
        "Nanjo: This time we will surely be allowed a proper discussion, will we not?"
    ],
    5: [
        "Nanjo: The more one tries to suppress emotions, the bigger the explosion that eventually comes.",
        "Nanjo: You, however, have no such worry!"
    ],
    6: ["Mark: And we don't have time!"],
    7: ["Mark: Damn it, what palace! Don't make me laugh!"],
    8: ["Mark: What is Aki plotting, using even Kozai?"],
    9: ["Elly: Is she so confident about her own paintings?"],
    10: [
        "Elly: Doesn't a road you have passed before feel shorter?" + pg + " ...No, it does not, does it."
    ],
    11: ["Elly: I am glad we can go outside now!"],
    12: [
        "Brown: Lady Queeeen! I've been looking forward to meeting you! *",
        "Brown: Is that a good greeting?"
    ],
    13: [
        "Brown: Kozai made one heck of a room, too... Imagine yourself becoming one of those... Hmm, that's rough!"
    ],
    14: [
        "Brown: Well, it means don't worry about trivial things! Eh? Worry more, you say? Okay, okay! Leave it to me!"
    ],
    15: [
        "Ayase: Is the Queen planning to open an idol training school or something?"
    ],
    16: ["Ayase: Geez, my ankles hurt!!"],
    17: ["Ayase: Ayase might be a little jealous."],
    18: [
        "Reiji: No matter how much you think, what you don't know, you don't know! Anyway, find where this Queen is.",
    ],
    19: [
        "Reiji: If you're hurt by every little thing like this, you can't get by in the world. There are plenty of people having it way worse."
    ],
    20: ["Reiji: What? Do you expect me to say \"I'm moved\"?"],
    21: [
        "Young Man: This is the painting the Queen drew, and it's kind of nice...",
        "Young Man: The Queen is good at painting and beautiful too" + pm + " but I'm cool too, right?"
    ],
}

if __name__ == '__main__':
    for n, d in ((192, E192), (193, E193), (194, E194), (195, E195), (198, E198), (199, E199)):
        apply('E2', n, d, {})
