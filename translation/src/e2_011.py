"""E2 entries 11-33 - school clubs NPCs; SEBEC reception."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

pm = P('み'); pn = P('な'); pyu = P('ゆ')

E11 = {
    3: [
        "Student: I'm cutting weight right now, so even boxing gloves look like bean-paste candy to me."
    ],
    4: [
        "Student: Ah! Don't open lockers without permission! There's something important in there!"
    ],
}

E12 = {
    0: ["Nanjo: Archery seems interesting too, but do not forget about the hospital."],
    1: ["Mark: They say there are lots of bows in this clubroom. Maybe I'll borrow one and play around sometime."],
    2: ["Yukino: I'm not good with bows. A razor's still my weapon of choice, I guess."],
    3: [
        "Student: Archery is an intellectual, adult sport! Even if you don't have a bow, I'll lend you one, so it's fine!"
    ],
}

E13 = {
    0: [
        "Nanjo: I was taken to see ballet by Yamaoka when I was small... Perhaps he meant it as an education of sensibility."
    ],
    1: [
        "Mark: This kind of stuff throws me off. Hey, let's hurry to the hospital!"
    ],
    2: [
        "Yukino: Ballet, huh..." + pm + " \"The Nutcracker\" is fun, isn't it?",
        "Yukino: The happy dream world a girl saw on Christmas night..." + pm + " Dreamy...",
        "Yukino: What's with that face! I like ballet! Got a problem?!"
    ],
    3: [
        "Student: Toe shoes are surprisingly hard, you know. You didn't know that, did you? When I first wore them, I was surprised too."
    ],
    4: [
        "Student: Thanks to the gym's reconstruction we got a clubroom, which is a relief.",
        "Student: Because if we change in the classroom, someone might peek!",
        "Student: Ah! Could you be here to peek too?!"
    ],
}

E15 = {
    0: ["Nanjo: There was something compelling about the paintings of Sonomura that I saw."],
    1: ["Mark: Right, she's good at painting, isn't she..." + pm + " <FF0F>あ! Now, let's go to the hospital!"],
    2: [
        "Yukino: I've seen Sonomura's painting too." + pm + " It won a prize under the title \"The Door to Paradise.\""
    ],
    3: [
        "Student: We're short on members, which is a problem. Sonomura-san is in the hospital, and Kozai-san doesn't come to school."
    ],
    4: "=Student: Do you know them?<FF03>Both of them?<FF03><FF0E>い<FF01>",
    5: [
        "Student: Sonomura-san's paintings are amazing. She's won several prizes.",
        "Student: Her best friend Kozai-san was hopeless at painting, but it seems she won in the boyfriend department."
    ],
    6: [
        "Student: I see, you don't know. Ah, the art club has had one hardship after another. Maybe it's cursed or something."
    ],
}

E16 = {
    0: ["Nanjo: I have little connection with the gymnasium, but well, I suppose it is fine..."],
    1: ["Mark: If only it had a big mirror, it'd be perfect for dance practice."],
    2: ["Yukino: I'd like to get to the hospital quickly, though."],
    3: [
        "Student: With the gym being new, the sound system's perfect too!",
        "Student: Look forward to our live show at the school festival!",
        "Student: So on sports festival day, I'll ditch quickly and go straight to the studio!"
    ],
    4: [
        "Student: I heard a second-year named Naito went missing together with his girlfriend, but",
        "Student: I'm betting it's SEBEC's doing! ..." + pn + " Eh? Any evidence? Well, that's a man's intuition for you!"
    ],
}

E17 = {
    0: ["Nanjo: Curses, all of it, are mere superstitions."],
    1: ["Mark: Secret shortcut... Ah, you mean the hole in the wall."],
    2: ["Yukino: SEBEC's reputation seems to be the worst."],
    3: [
        "Student: I'd like to avoid passing near the SEBEC building at night.",
        "Student: They tore down the haunted house, so that company is cursed!"
    ],
    4: [
        "Student: I'm hungry, gonna go eat something..." + pm + " If you use the secret shortcut it's quick! Recommended!"
    ],
}

E18 = {
    0: [
        "Nanjo: I agree with his opinion. That man Kandori is quite capable of building biological weapons without a second thought."
    ],
    1: ["Mark: Why's everyone so interested in SEBEC? It's just a company."],
    2: [
        "Yukino: I didn't know you liked rumors that much. Now that's enough, let's go to the hospital."
    ],
    3: [
        "Student: SEBEC being cursed is just kids' rumor! They're definitely making biological weapons there."
    ],
}

E19 = {
    0: ["Nanjo: Code Breaker... I used to play it with Yamaoka long ago."],
    1: [
        "Mark: That guy was playing betting Daifugo in class the other day and got yelled at by the teacher."
    ],
    2: [
        "Yukino: Leave the gambling lovers alone and let's go to the hospital. Before I lose my temper."
    ],
    3: [
        "Student: Gambling, the dream of men! Casino, the bunny girls!",
        "Student: Slots, blackjack, Code Breaker... Ahh, I wish I were old enough to go to a casino already."
    ],
}

E20 = {
    0: ["Nanjo: Dreams have no meaning. A dream is merely a dream."],
    1: [
        "Mark: A blue room... Now that you mention it, I feel like I had a dream like that too."
    ],
    2: [
        "Yukino: Don't forget that there are people at the hospital waiting to be heard."
    ],
    3: ["Student: I had a weird dream... It's really bothering me."],
    4: "=Student: Want to hear my dream?<FF03><FF0E>　<FF01>",
    5: [
        "Student: It was a blue room. I could hear a piano and singing, and a strange old man was sitting in a chair...",
        "Student: Hey, what do you think it means?"
    ],
    6: [
        "Student: It was a very strange dream. Like it was foreshadowing something that's going to happen..."
    ],
}

E21 = {
    0: ["Nanjo: Exploring is fine, but <FF0F>あ, do not forget to go to the hospital."],
    1: ["Mark: The principal's out, huh. I see, he's in the courtyard again."],
    2: [
        "Yukino: Pretty flowers... So it was true that the principal likes flowers."
    ],
}

E22 = {
    0: [
        "Nanjo: Indeed, it is prettier than when I gave the new students' representative address at the entrance ceremony."
    ],
    1: ["Mark: If only this place were bigger. It's too small for my stage!"],
    2: [
        "Yukino: What are you going to do, coming all the way to the stage? We're going to our exams, right?"
    ],
    3: [
        "Student: Many things happened on the old stage.",
        "Student: In its long history, sweat, tears, and blood were shed. Even if the stage is gone, the feelings of those who stood on it won't fade so easily...",
        "Student: How's my line? It was long, I had trouble memorizing it."
    ],
    4: [
        "Student: The time has finally come. The time for the old feelings poured into the stage to be released...",
        "Student: Just kidding" + pm + " Good line, isn't it! It's a script I wrote."
    ],
}

E24 = {
    0: ["Nanjo: There is nothing of great value here."],
    1: ["Mark: This mat's comfortable to sleep on, you know."],
    2: [
        "Yukino: Dusty and sweaty... How can you want to sleep in a place like this."
    ],
}

E32 = {
    0: [
        "Takeda: What do you lot want? This isn't a place for kids! Hey, get those brats outside!"
    ],
    1: ["Man's Voice: Takeda, what's all the fuss?"],
    2: ["Nanjo: Kandori...!"],
    3: [
        "Kandori: Oh, how unusual. What business could the Nanjo family's young master have at our humble company?"
    ],
    4: [
        "Nanjo: I did not come because I have business with you. I only came as a companion."
    ],
    5: [
        "Kandori: Oh... So those over there are the young master's schoolmates. Coming all the way to such a cramped place for the sake of schoolmates..." + pn + " What a beautiful friendship."
    ],
    6: [
        "Nanjo: Stop calling me \"young master.\" I do not recall giving you permission to call me that."
    ],
    7: ["Takeda: This brat...!"],
    8: [
        "Kandori: Stand down, Takeda! ..." + pm + " It seems the Nanjo family has not disciplined him.",
        "Kandori: Well, no matter. Nanjo-kun, I shall teach you in due time how to speak to your elders."
    ],
    9: ["Mark: Nanjo's an annoying guy too, but you're way, way more annoying...!"],
    10: ["Takeda: Tch..." + pyu + " Lord Kandori, it's about time..."],
    11: [
        "Kandori: Understood. I'm coming right away. Now then, would you kindly leave?"
    ],
    12: ["Mark: Tch! Let's go, <FF0F>あ!"],
    13: [
        "Man: Sir, do you have an appointment for a meeting?",
        "Man: Excuse me, but we ask those without appointments to leave."
    ],
}

if __name__ == '__main__':
    for n, d in ((11, E11), (12, E12), (13, E13), (15, E15), (16, E16), (17, E17), (18, E18), (19, E19), (20, E20), (21, E21), (22, E22), (24, E24), (32, E32)):
        apply('E2', n, d, {})
