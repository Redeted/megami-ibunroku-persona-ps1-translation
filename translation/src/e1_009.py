"""E1 entries 9-13 - Brown joins; tower entrances (Hypnos, Nemesis, Thanatos); school chatter."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

H = F6('う') + "*" + F6('　')
HH = F6('う') + "**" + F6('　')

E9 = {
    16: [
        "Brown: Character, huh~ No problem on that front.",
        "Brown: I get it!! The butterfly must be thinking this: make Great Brown a hero of justice and have him save the school and the town!",
        "Brown: If you all insist and bow your heads, well, can't be helped.",
        "Brown: I'll lend you my strength! Everyone, follow me!!"
    ],
    17: ["Nanjo: What a happy fellow."],
    18: ["Yukino: Well, if he wants to come along, let him do as he likes."],
    19: "=Right, <FF0F>あ?<FF03><FF0E>　<FF01>",
    20: [
        "Brown: Oho? Geez~ *",
        "Brown: You want me to come along, don't you~ *",
        "Brown: Everyone, let's be more honest!"
    ],
    21: [
        "Brown: Hey hey hey hey.",
        "Brown: Miss Yukino said \"by all means\"! There's no way I can refuse!",
        "Brown: Besides, from what I heard, this school got like this because of you, didn't it?",
        "Brown: You can't go wrong putting me in charge as leader!",
        "Brown: Trust me and follow along!! Dehyahyahyahya"
    ],
    22: [
        "Yukino: Where are you looking when you make that peace sign?",
        "Yukino: Come on, stop dawdling! Let's go!!"
    ],
    23: ["Brown: Y-Yes ma'am! Understood!!"],
}

E10 = {
    0: [
        "A cold wind blows in from beyond the door.",
        "The door is frozen shut and will not budge."
    ],
    1: ["A cold wind blows in from beyond the door."],
    2: "=Go to the Demon Mountain?<FF03><FF0E>　<FF01>",
    3: [
        "Hee-Ho-kun: Hee-Ho! We transferred here from the Demon Mountain beyond the door, ya know!",
        "Hiho-ko-chan: Hee-ho! It's cooler and more comfortable over here~",
        "Hee-Ho-kun: School is fun, isn't it, Hiho-ko-chan?",
        "Hiho-ko-chan: Well, so-so.",
        "Hee-Ho-kun: Can I make 100 friends?",
        "Hiho-ko-chan: Who knows about that.",
        "Hee-Ho-kun: ...Hee-ho? Human girls don't talk in such a cold way, you know.",
        "Hiho-ko-chan: Hee-hoooo?? Humans are hard~ They're tiring~"
    ],
    4: [
        "Hee-Ho-kun: Hee-Ho! Each time you conquer a tower, one door of the Demon Mountain opens! Why is that?",
        "Hiho-ko-chan: Hee-ho! It's that age, you know. Well, the mountain has its circumstances too~",
        "Hee-Ho-kun: Hee-ho? Anyway, the door opens!"
    ],
    5: [
        "Hiho-ko-chan: Hee-hooo~ Nothing fun lately, hee-ho.",
        "Hee-Ho-kun: Hee-Ho! Wanna set the school on fire! Whoooosh!",
        "Hiho-ko-chan: Don't. The mistakes of youth. It'd be hot, too."
    ],
    6: ["Yukino: That's a creepy door."],
    7: ["Yukino: Who is it? The idiot who casually built a snowman!"],
    8: [
        "Yukino: My toes are going numb. Geez, that drama club!",
        "Yukino: Why'd they pick the Snow Queen? Isn't there a Queen of Summer or something?",
        "Yukino: I can't stand the cold."
    ],
    9: ["Ayase: That door feels like a demon might come out of it..."],
    10: [
        "Ayase: Kyaaa~ " + H + " Look, look at that stuffed toy~ " + H + " So pretty~~ " + HH
    ],
    11: ["Ayase: Do you still have business here?"],
    12: ["Nanjo: A wise man does not approach danger."],
    14: [
        "Nanjo: Not that it matters, but they look pale. They should take more iron."
    ],
    15: [
        "Brown: Hey, look! There's a weird creature! It goes Hee-Ho, Hee-Ho!"
    ],
    16: [
        "Brown: When you talk to them, those guys actually have it pretty rough. And they're still young.",
        "Brown: Ooooh! I'm gonna cry."
    ],
    17: ["Elly: There is no one here. Let us try other rooms."],
    18: [
        "Elly: Oh! It is Jack Frost!!",
        "Elly: Be careful!! That cute appearance is a disguise to attract people.",
        "Elly: It is said that those who approach carelessly are frozen by its blizzard breath!!"
    ],
    19: [
        "Elly: Innocence and cruelty are two sides of the same coin. Be careful!"
    ],
    20: [
        "Yukino: How many \"mirror fragments\" have we gathered so far? Show me the \"Mirror Frame.\""
    ],
    21: "=Show the \"Mirror Frame\"?<FF03><FF0E>　<FF01>",
    22: ["Yukino: Well, fine. But let's check once in a while."],
}

E11 = {
    0: [
        "Butterfly: I have been waiting.",
        "Butterfly: It seems that saving the boy called Toro from the Persona's magic power has weakened the Snow Queen's power.",
        "Butterfly: The door that was frozen shut should now open.",
        "Butterfly: The door is the entrance to one of the three towers surrounding the school, the Tower of Hypnos.",
        "Butterfly: Of the three, this tower has the most straightforward structure. The \"mirror fragments\" should be easy to find.",
        "Butterfly: Oh yes, a word of advice about the towers.",
        "Butterfly: Once you set foot in any tower, you cannot leave unless you defeat its lord. Think carefully before entering."
    ],
    1: [
        "Butterfly: Welcome. This is the entrance to the Tower of Hypnos.",
        "Butterfly: Of the three, this tower has the most straightforward structure. The \"mirror fragments\" should be easy to find.",
        "Butterfly: Once you set foot in any tower, you cannot leave unless you defeat its lord. Think carefully before entering."
    ],
    2: [
        "Butterfly: You have come again. This is the entrance to the Tower of Hypnos.",
        "Butterfly: Even now that it has lost its lord, demons still crowd within."
    ],
    3: [
        "A sweet, sleep-inducing scent drifts from beyond the door.",
        "The door is frozen shut and will not budge."
    ],
    4: ["A sweet, sleep-inducing scent drifts from beyond the door."],
    5: "=Enter the Tower of Hypnos?<FF03><FF0E>　<FF01>",
    6: [
        "Tadashi-kun: W-What! A little bit is fine, isn't it! You stingy stingy stingy stingy stingy stingy!",
        "Tadashi-kun: Ah, no. I was talking to this nagging girl."
    ],
    7: [
        "Tadashi-kun: Two people can have the same dream at the same time, huh.",
        "Tadashi-kun: This is no coincidence! The two of us were fated to be together."
    ],
    8: [
        "Tadashi-kun: I can see myself in your eyes...",
        "Tadashi-kun: Ah, I'm in a good part right now, so don't interrupt."
    ],
    9: [F6('い') + "Tadashi-kun<FF03>A slacker on the fencing team<FF03>Fights with Tamaki-chan every day" + F6(0)],
    10: [
        "Tamaki-chan: It's awful, Tadashi-kun!",
        "Tamaki-chan: I told him not to drink the sports drink because it's for everyone, and he drank it all!!"
    ],
    11: [
        "Tamaki-chan: I had a lovely dream and noticed my honest feelings.",
        "Tamaki-chan: From now on... I'll follow Tadashi-kun. " + H
    ],
    12: ["Tamaki-chan: Just being by his side like this makes me happy. *"],
    13: [F6('う') + "Tamaki-chan<FF03>Fencing team transfer student<FF03>Fights with Tadashi-kun every day" + F6(0)],
    14: ["Yukino: They're fighting again. Don't those two ever get tired of it?"],
    15: ["Yukino: Tch! Stop flirting in broad daylight!"],
    16: ["Yukino: Still in their own world? Don't those two ever get tired of it?"],
    17: [
        "Ayase: Tamaki-chan is pretty cute. Maybe Ayase should cut her hair short too. *"
    ],
    18: [
        "Ayase: So nice, so nice~ A young couple warming each other in a cold little room, so flavonoid~"
    ],
    19: ["Nanjo: This cold makes me sleepy... No, no, I must not."],
    20: ["Nanjo: What is Ayase trying to say?"],
    21: [
        "Brown: Must be nice for Tadashi, having someone to fight with.",
        "Brown: Being single is rough... Ooh, it's cold~"
    ],
    22: [
        "Brown: I can see myself in your eyeballs." + P('ほ') + " Could it be that you...!!"
    ],
    23: [
        "Elly: \"Tower of Hypnos.\" Hypnos is the god of sleep.",
        "Elly: It does not sound very scary."
    ],
    24: [
        "Elly: Could what Ayase wants to say be Platonic love?",
        "Elly: If she is doing it on purpose, the wit is too sharp.",
        "Elly: Does she mean \"refreshing\"?"
    ],
}

E12 = {
    0: [
        "Butterfly: I have been waiting.",
        "Butterfly: It seems that saving the boy called Toro from the Persona's magic power has weakened the Snow Queen's power.",
        "Butterfly: The door that was frozen shut should now open.",
        "Butterfly: The door is the entrance to one of the three towers surrounding the school, the Tower of Nemesis.",
        "Butterfly: This tower, structure aside, has a lord who is quite the rogue. It may be hard for you as you are now.",
        "Butterfly: Well, if you insist, I will not stop you.",
        "Butterfly: Oh yes, a word of advice about the towers.",
        "Butterfly: Once you set foot in any tower, you cannot leave unless you defeat its lord. Think carefully before entering."
    ],
    1: [
        "Butterfly: Welcome. This is the entrance to the Tower of Nemesis.",
        "Butterfly: This tower, structure aside, has a lord who is quite the rogue. Steel yourselves as you go.",
        "Butterfly: Once you set foot in any tower, you cannot leave unless you defeat its lord. Think carefully before entering."
    ],
    2: [
        "Butterfly: Welcome. This is the entrance to the Tower of Nemesis.",
        "Butterfly: This tower, structure aside, has a lord who is quite the rogue. It will probably be hard for you as you are now.",
        "Butterfly: Well, if you insist, I will not stop you.",
        "Butterfly: Once you set foot in any tower, you cannot leave unless you defeat its lord. Think carefully before entering."
    ],
    3: [
        "Butterfly: You are back. Beyond here lies the Tower of Nemesis.",
        "Butterfly: It seems Michiko dealt you quite a hard time.",
        "Butterfly: Well, when one is young, one should try everything."
    ],
    4: [
        "A growl that resonates heavily in the pit of the stomach can be heard from beyond the door.",
        "The door is frozen shut and will not budge."
    ],
    5: [
        "A growl that resonates heavily in the pit of the stomach can be heard from beyond the door."
    ],
    6: "=Enter the Tower of Nemesis?<FF03><FF0E>　<FF01>",
    7: [
        "Kurouri: Come to think of it, my uncle the detective also said he saw a demon.",
        "Kurouri: I wonder if Yarai Ward is okay. Hehehe..."
    ],
    8: [
        "Kurouri: Come to think of it, there seems to be a commotion in the cafeteria. Hehehe..."
    ],
    9: ["Kurouri: Ow ow ow ow ow ow. My arm's too heavy to lift. Hehehee..."],
    10: [
        "Kurouri: There was a classroom that was frozen shut, remember? Hehehe... The one isolated by itself.",
        "Kurouri: It seems the door has become openable. Hehehe..."
    ],
    11: [
        "Kurouri: There was a classroom that was frozen shut, remember? Hehehe... The one isolated by itself.",
        "Kurouri: It seems the door has become openable. Hehehe...",
        "Kurouri: Just a moment ago, Kirishima-san dashed off saying she'd investigate that room. Hehehe..."
    ],
    12: ["Yukino: Lots of paper here. Should we make a bonfire?"],
    13: ["Yukino: Geez! All we can do is pray Michiko doesn't show up again."],
    14: [
        "Ayase: Not just the school, the hospital got all scrambled inside too, right?",
        "Ayase: I wonder if Ayase's home is okay. It'd be awful if a demon was relaxing in the living room."
    ],
    15: ["Ayase: Michiko had so much impact. She'll show up in my dreams..."],
    16: ["Nanjo: Nothing but frozen books. A creepy room."],
    17: ["Nanjo: What? My muffler is crooked? Hm, thank you."],
    18: ["Brown: Follow me and relax like you're on a big ship!"],
    19: ["Brown: Ugh, let's drop the \"Tower of Nemesis\" talk already."],
    20: ["Elly: It is cold. If this continues, everyone will freeze to death."],
    25: ["Elly: I am researching the \"Snow Queen\" play."],
    26: [
        "Elly: Looking at old materials, there was something that caught my attention. May I tell you?",
        "Elly: Besides the Queen's mask, there seems to be one more item used for generations in the \"Snow Queen\" play.",
        "Elly: The costume worn by the protagonist. It is said to be stored in the gymnasium storeroom."
    ],
    27: [
        "Elly: The \"Tower of Nemesis,\" is it? What Nemesis means is vengeance. It gives me a bad feeling."
    ],
    29: [
        "Elly: I wonder if Toro-kun is all right. It seemed he was made to drink a lot."
    ],
    30: [
        "Elly: Did you hear Kurouri-kun's story? Let us go see right away!!"
    ],
    31: ["Elly: Let us hurry to the upper floor!"],
}

E13 = {
    0: [
        "Butterfly: I have been waiting.",
        "Butterfly: It seems that saving the boy called Toro from the Persona's magic power has weakened the Snow Queen's power.",
        "Butterfly: The door that was frozen shut should now open.",
        "Butterfly: The door is the entrance to one of the three towers surrounding the school, the Tower of Thanatos.",
        "Butterfly: This tower is extremely dangerous. It overflows with demons of great power.",
        "Butterfly: Gathering the \"mirror fragments\" will also be quite a hardship.",
        "Butterfly: Oh yes, a word of advice about the towers.",
        "Butterfly: Once you set foot in any tower, you cannot leave unless you defeat its lord. Think carefully before entering."
    ],
    1: [
        "Butterfly: Welcome. This is the entrance to the Tower of Thanatos.",
        "Butterfly: Of the three bosses, Thanatos has the strongest will. Steel yourselves.",
        "Butterfly: Well, such a warning is probably unnecessary for you now.",
        "Butterfly: Once you set foot in any tower, you cannot leave unless you defeat its lord. Think carefully before entering."
    ],
    2: [
        "Butterfly: Welcome. This is the entrance to the Tower of Thanatos.",
        "Butterfly: This tower is extremely dangerous. It overflows with demons of great power.",
        "Butterfly: Your chances of winning as you are now are slim. If you insist on going, I will not stop you.",
        "Butterfly: Once you set foot in any tower, you cannot leave unless you defeat its lord. Think carefully before entering."
    ],
    3: [
        "Butterfly: You are back. This is the entrance to the Tower of Thanatos.",
        "Butterfly: Even after its lord Yuriko is gone, it overflows with demons of great power.",
        "Butterfly: If you wish to hone your skills here, that is amusing as well."
    ],
    4: [
        "Oppressive, cold air flows from beyond the door.",
        "The door is frozen shut and will not budge."
    ],
    5: ["Oppressive, cold air flows from beyond the door."],
    6: "=Enter the Tower of Thanatos?<FF03><FF0E>　<FF01>",
}

if __name__ == '__main__':
    for n, d in ((9, E9), (10, E10), (11, E11), (12, E12), (13, E13)):
        apply('E1', n, d, {})
