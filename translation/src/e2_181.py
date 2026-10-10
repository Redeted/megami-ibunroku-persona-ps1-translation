"""E2 entries 181-186 - other-world Himeno, Kaneda, shops, townspeople."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

pm = P('み'); pn = P('な'); pg = P('ぎ'); pyu = P('ゆ')

E181 = {
    6: ["Reiji: <FF0F>あ... I'm going out first."],
    7: ["Maki: Yuko, that's rude to everyone. Apologize."],
    8: [
        "Himeno: But, Maki..." + pm + " Maki is my friend, but the others aren't!"
    ],
    9: ["Maki: Honestly, Yuko, what am I going to do with you..."],
    10: ["Maki: Well then, everyone, let's go."],
    12: [
        "Himeno: Maki, won't you stop by for tea? My family's pastry chef made sweets and there's exactly one portion left.",
        "Himeno: If you did, my little brothers would surely be happy!"
    ],
    13: [
        "Maki: Yuko..." + pm + " Then next time I'll stop by with everyone."
    ],
    14: ["Himeno: ..." + pm + " How boring!"],
    15: [
        "Himeno: Oh, it's you? " + pm + "...Fine, today I'll invite all of you as a special treat."
    ],
    16: [
        "Mark: Why are you suddenly" + pm + " ...I get it. You're scared because the town's acting weird, right?"
    ],
    17: [
        "Himeno: N-No, I'm not! We have our Doberman John, and our butler Sebastian, too!",
        "Himeno: I'm not scared!"
    ],
    18: [
        "Nanjo: Heh. Then after everything is resolved, we shall all stop by."
    ],
}

E182 = {
    0: [
        "Kaneda: What do you want with my house? Don't tell me you're debt collectors!? " + pm + "As you can see, we've got no money here!",
        "Kaneda: The ruins I was counting on had no treasure, so my business is finished!"
    ],
    1: [F6('う') + "Kaneda Katsue<FF03>Recently came into sudden wealth and should be living in a fine house, but..." + F6('　')],
    2: ["Nanjo: Business? Do you do business at ruins?"],
    3: [
        "Maki: Nanjo-kun! Isn't Kaneda-san's job grave robbing at ruins!"
    ],
    4: [
        "Elly: Grave robbing is not called a job. Besides, such a thing cannot be done in today's Japan, can it?",
        "Elly: Maki says strange things."
    ],
    5: [
        "Brown: Grave robbing? How could you do that in Japan? Maki-chan says weird stuff."
    ],
    6: [
        "Ayase: Grave robbiiing~? There's no way anyone does that as a job. Get it together, Sonomura."
    ],
    7: [
        "Reiji: Grave robbing...?" + pm + " There's no way that can be done. We're not kids, so don't say stupid things."
    ],
    8: ["Maki: But..." + pm + " everyone says so, don't they?"],
    9: [
        "Mark: Come to think of it, there was a rumor about a year ago that the old lady suddenly got rich by plundering ruins.",
        "Mark: Sonomura, did you take that seriously?" + pg + " ...Well, you're a different Sonomura."
    ],
    10: ["Kaneda: Quit your noise! If you've got no business, go home!"],
    11: ["Kaneda: You're still here! If you've got no business, get out already!"],
    12: [
        "Nanjo: <FF0F>あ, Sonomura said the old woman Kaneda makes her living grave robbing.",
        "Nanjo: In our town that was merely a rumor. But in this town it seems to be reality.",
        "Nanjo: Why did the rumor become reality?"
    ],
    13: [
        "Maki: The rumor became reality...?" + pm + " ...Oh" + pn + " no, my head hurts... Hey, everyone, let's go!"
    ],
    14: [
        "Kaneda: What's happened to this town! Suddenly everywhere's gone to ruin!",
        "Kaneda: You lot are strong, aren't you? Seeing this state, don't you think of doing something about it!?"
    ],
    15: [
        "Mark: ..." + pm + " Sorry, old lady. We're running around trying to do something about it too."
    ],
    16: [
        "Elly: Mark, calm down... Maki will surely be all right. Now let us hurry and go find her!"
    ],
    17: [
        "Elly: Mark, calm yourself...",
        "Elly: Maki will surely be all right. Now, let us hurry and go find her."
    ],
    18: [
        "Elly: Mark, calm down... It will be all right! Everything will be resolved soon."
    ],
    19: [
        "Elly: Mark, calm yourself... It will be all right. Everything should be resolved soon."
    ],
    20: [
        "Brown: Now now, Mark, don't get so worked up! I'll put everything back to normal soon!"
    ],
    21: [
        "Ayase: Don't be mad, Inaba..." + pm + " Everything will be back to normal soon!"
    ],
    22: [
        "Reiji: Calm down, Inaba. Just a little more patience. Then I'll put everything back to normal."
    ],
}

E183 = {
    0: ["Maki: The girl in white clothes must be Mai-chan."],
    1: [
        "Nanjo: In this town, weapons are entirely for use against demons. That is why there is no need for police, I suppose."
    ],
    2: [
        "Mark: No matter how many times I come, I can't get used to it. Being told with a big smile, \"Are you looking for weapons?\""
    ],
    3: [
        "Elly: The magazines placed here are all old. They are all from about a year ago."
    ],
    4: [
        "Elly: The magazines placed here are all old. They are all from about a year ago."
    ],
    5: [
        "Brown: Huh? This girl retired, so why is she on the cover?"
    ],
    6: [
        "Ayase: Eww! Look at this model! Nobody wears clothes like that anymore... Huh? This magazine's old! It's from a year ago!"
    ],
    7: ["Reiji: What is this shop? It only has awfully old magazines."],
    8: [
        "Youth: The place that used to be a pretty flower field suddenly turned into a forest. Are they doing a greening campaign now?"
    ],
    9: [
        "Townsperson: A girl used to play often in the flower field. But it turned into a forest, I wonder how she's doing.",
        "Townsperson: ?" + pm + " Was she wearing black, you ask?" + pg + " No, that girl was a cute child in white clothes."
    ],
    10: ["Clerk: Welcome! Are you looking for weapons?"],
    11: [
        "Clerk: Kya!" + pm + " That doesn't open!" + pm + " If you're shopping, please come around to the counter!"
    ],
}

E184 = {
    0: [
        "Maki: That lady said something odd. That when you're too happy, you get anxious. Having fun every day is the best, isn't it? Don't you think so?"
    ],
    1: [
        "Nanjo: I am not one for luxury, but if there were armor marked \"Number One\"..." + pm + " Of course there is not. Sorry."
    ],
    2: [
        "Mark: My mom has the worst taste in clothes! Once she bought me a T-shirt with \"Sukeroku\" on the chest!",
        "Mark: Where does she even find that stuff!",
        "Mark: " + pyu + "A-" + pn + " Not that I'm worried about my mom" + pn + " or anything. Don't get the wrong idea."
    ],
    3: ["Elly: I do not care much for armor."],
    4: [
        "Brown: <FF08>あ! Pick me something cool, even if its defense is low."
    ],
    5: [
        "Ayase: Ayase likes minis. If it's too long, doesn't it look frumpy?"
    ],
    6: ["Reiji: Whatever, just hurry up, would you?"],
    7: [
        "Townsperson: I'm happy to live in such a nice town.",
        "Townsperson: But when people are too happy, they actually get anxious.",
        "Townsperson: I start to think that if I wake up tomorrow, it'll all turn out to have been a dream."
    ],
    8: [
        "Mannequin Girl: Welcome! What kind of thing are you looking for, handsome? If you like, I'll fit the size for you!"
    ],
}

E185 = {
    0: [
        "Maki: I've heard of Shibuya, but what is Daikanyama? Is that a place name? So your world has towns like that, hmm..."
    ],
    1: [
        "Nanjo: <FF0F>あ, do you also think having fun every day is good?",
        "Nanjo: Even if something is happening behind the scenes, is it better to play around without knowing?"
    ],
    2: [
        "Mark: Daikanyama is a smaller town compared to Shibuya, but they feature it in magazines a lot lately. I thought these girls would know it."
    ],
    3: [
        "Elly: One cannot always be doing only fun things. Sometimes there are things you must endure, are there not?"
    ],
    4: [
        "Brown: I'd like it to be fun too. Like, for example, surrounded by cute girls squealing over me" + pm + " ...hehehehe."
    ],
    5: [
        "Ayase: Ayase wants to do only fun things too. I want to beat Kandori quick and go back to being a normal girl!"
    ],
    6: ["Reiji: Are these people idiots? There's no way it's all fun!"],
    7: [
        "Schoolgirl: We used to be able to go play past the subway, but they built a weird wall on the surface and a big monster at the ticket gate, so we can't pass.",
        "Schoolgirl: Nobody uses the subway anyway, so it's fine, but I'm lonely that places to play have decreased."
    ],
    8: [
        "Schoolgirl: The subway monster is gone, right? So I thought of going over to the other side to play, but...",
        "Schoolgirl: ..." + pn + " It's kind of weird, the town on the other side... It was scary, so I turned back before the market."
    ],
    9: [
        "Schoolgirl: I went to play on the other side of the subway. Then all they talked about was how \"the Queen is gone\"" + pn + " I wonder what happened?"
    ],
    10: [
        "Schoolgirl: I want to leave home and live alone soon. Near the plasma wall would be nice, because the night view is pretty."
    ],
    11: ["Mark: Don't you wanna live in Shibuya or Daikanyama or something?"],
    12: [
        "Schoolgirl: Daikanyama...?" + pm + " What's that, I don't know. Well, whatever, I like this town, so I'm staying here."
    ],
    13: [
        "Man: It's super fun here every day, it's the best, if only demons didn't show up. They've suddenly increased lately."
    ],
    14: "=            OUT OF ORDER            <FF02><FF01>",
}

E186 = {
    0: [
        "Maki: The demons in town suddenly increased only recently. But though they increased, there aren't many stories of people being attacked."
    ],
    1: [
        "Nanjo: Demons that do not attack people... But we are in fact being attacked.",
        "Nanjo: Are you saying demons choose their targets?" + pm + " ...Surely not."
    ],
    2: [
        "Mark: Yahoo! I'm Froggy-kun, hoppyyyy!" + pg + " Just kidding!"
    ],
    3: ["Mark: You too, stop making such serious faces and lighten up! That's what I'm saying!"],
    4: [
        "Elly: My skin has been rough lately. Fighting Demons is quite Hard, after all."
    ],
    5: [
        "Brown: Lately I can't shake off the fatigue. Even I can't beat age, I guess."
    ],
    6: [
        "Ayase: N-No way! There was viper in Gara-Gara Drink!? Ayase drank it!"
    ],
    7: ["Reiji: No, I'm not tired. Let's get going."],
}

if __name__ == '__main__':
    for n, d in ((181, E181), (182, E182), (183, E183), (184, E184), (185, E185), (186, E186)):
        apply('E2', n, d, {})
