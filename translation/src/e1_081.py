"""E1 entries 81-83 - Michiko's torture room (Toro and Kurouri), the treasure chest."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

p = P('ほ')


def S(*parts):
    """join text parts with the Japanese's pause code between them"""
    return p.join(parts)


E81 = {
    0: [
        "Demon Teacher: Hey! Who said you could spill it? Milk is good for your body, you know!",
        "Demon Teacher: A greedy little piglet like you should be overjoyed to drink as much as you like, right?",
        "Demon Teacher: " + S("Here", "here", "here", "here", "here!") + " " + S("Drink", "drink", "drink it all!") + " Ohohohohohoho!",
        "Demon Teacher: And you there, four-eyes! What's with that weak back? A push-up only counts once your chin touches the ground!",
        "Demon Teacher: If you don't do them properly, I'll raise your quota again! Ohohohohohoho!"
    ],
    1: [
        "Toro: " + S("Guh", "guh", "guh", "guh"),
        S("Gulp", "gulp", "gulp", "gulp", "gulp"),
        S("Gh!?", "Ghghghghgh!!", "Gh!"),
        "Bleh!" + p + "<FF03>Bluuurgh!!" + p + "<FF03>Bleaaargh!!!" + p,
        S("S-", "stop it! H-", "help me!!<FF03>F-", "forgive me!!<FF03>I", "I..."),
        S("Milk", "is the one thing!<FF03>Dairy", "products are the one thing!!<FF03>I can't do ithhh!!!")
    ],
    2: [
        "Kurouri: " + S("Zeh", "zeh zeh", "zeh"),
        S("Ii", "iiiiiiiiiiiiih!"),
        S("Uu", "uuuuuuuuuuuuuh!"),
        S("Y-", "Yeah, I knew it,<FF03>I c-", "can't do iiit~"),
        S("M-", "My arms,<FF03>a g-", "genius whose brain works, a-", "arms like mine,<FF03>a", "ren't", "made for push-ups!<FF03>Fsh-"),
        S("C-", "can't be done!<FF03>Fsh-", "Fshhhhh")
    ],
    3: [
        "Yukino: " + S("T-", "Toro!?<FF03>And Kurouri!! What are you doing?!"),
        "Weren't you two at school!?"
    ],
    4: [
        "Toro: " + S("S-", "Stop it!<FF03>No m-", "more! S-", "Stop it~!!"),
        "Bleaargh!!" + p + "<FF03>Bleeech!!!" + p,
        S("I'm g-", "gonna die... d-", "dying~~")
    ],
    5: [
        "Demon Teacher: Hey! Little piglet! Why are you rolling your eyes!?<FF03>" + S("Drink more,", "more!"),
        S("A machine! Yes!", "Become a machine born to drink milk!!")
    ],
    6: [
        "Kurouri: " + S("Fsh", "fshhhh... I can't do any more~~"),
        S("Ah", "ah", "ahhaaa..."),
        S("E", "hehe", "hehehe", "he", "heeheh...")
    ],
    7: [
        "Demon Teacher: Hey! You four-eyed monkey!! Don't break on your own!",
        "Demon Teacher: Breaking you last is Lady Michiko's job! If I break you before then, I'll be broken by Lady Michiko!!"
    ],
    8: [
        "Nanjo: Just as I thought" + p + " or rather, I suspected" + p + " Michiko is pulling the strings.",
        "Nanjo: Even so, this is a thoroughly calculated and truly effective torture.",
        "Nanjo: It attacks the two's weak points, with no waste in method. And the torture itself seems to have no meaning.",
        "Nanjo: Torture for the sake of torture. Truly frightening..."
    ],
    9: [
        "Elly: Oh!! Those two! Their eyes are already vacant!",
        "Elly: We must do something quickly, or it will become irreversible!"
    ],
    10: [
        "Kurouri: A-Ahahaha. Huh??? It's a fairy!",
        "Kurouri: Hee hee hee. I really saw it. Mooommy!! Hehehe"
    ],
    11: [
        "Toro: Bleaargh!! " + S("Kehh", "hh", "Hhhh!"),
        S("H-", "Huh?<FF03>A-", "Ayase-san! Everyone!!"),
        S("H-", "H-", "Help me!<FF03>Heeelp meeeee!")
    ],
    12: [
        "Ayase: Hmm... With these two, it's like... a pass?",
        "Ayase: But why would that Michiko do this? Does it mean something?"
    ],
    13: [
        "Michiko: Ohohohohoho! Because they are ugly! Ugliness alone is a sin! A sin!",
        "Michiko: So I, the Beautiful, am now judging the sin called \"ugliness\"!",
        "Michiko: Understood? Little puppies? Ohohohohohohohoho!"
    ],
    14: [
        "Nanjo: ................." + p + " You are one to say so" + p + "?",
        "Nanjo: Never mind. Ugly as they may be, they are our schoolmates. I cannot leave them to d" + p + "ie...",
        "Nanjo: Now, hand over the key to the chains."
    ],
    15: [
        "Brown: " + S("Y-", "You've got a n", "nerve to s", "say that!!") + " You ugly woman!!",
        "Brown: I won't forgive you! Ugly as you are, torturing Toro and Akuma-kun!",
        "Brown: Open the chain key and stop the torture right now!"
    ],
    16: [
        "Michiko: My! What friend-loving people. Beautiful friendship? Ohohohohohoho. Splendid, wonderful!! Hmph!! Friendship!!!",
        "Michiko: Then, in honor of that lovely friendship... I shall tell you where the key to the chains binding these ugly men is!",
        "Michiko: The key to the chains is on the top floor... yes! I'm holding it myself!! Ohohoho!",
        "Michiko: If you want to save these ugly men, hurry to me! Ohohoho!",
        "Michiko: Yes... go straight left and my room is right there... Ohohohohohohoho!",
        "Michiko: But the \"mirror fragment\" you want so badly you'd reach out of your throat for it...",
        "Michiko: is \"beyond the door behind me\"!",
        "Michiko: The \"mirror fragment\" is stored in a big treasure chest together with a \"hint for defeating me.\"",
        "Michiko: Ohohohohohoho! This tower has no time limit, so you can take your time to fetch it!",
        "Michiko: Your friends will just have to put up with it a while" + p + " right? Ohohohohohoho!",
        "Michiko: What to do is up to you! Now, good day!",
        "Michiko: Ohohoho! Ohohohohohoho!!"
    ],
    17: [
        "Toro: Please help me! The key! The key right now! " + p + " Gebuh!!",
        "Toro: K-" + p + " The keyyyyy"
    ],
    18: [
        "Kurouri: Bub" + p + " bu... bushuuuu... " + "M-" + p + " My h-" + p + " heart's key... where is it?",
        "Kurouri: Zeh" + p + " zeh..."
    ],
    19: [
        "Demon Teacher: Come on, come on! Do it properly! Hyahyahyahyahyahyahya!",
        "Demon Teacher: Drink! Do it!"
    ],
    20: [
        "Yukino: We can't leave them, but the \"mirror fragment\" matters too. What should we do?"
    ],
    21: ["Yukino: Michiko... I can't forgive her..."],
    22: [
        "Ayase: Wouldn't it be good medicine for Toro and Kurouri? Ayase isn't good with those two..."
    ],
    23: [
        "Nanjo: More than the \"mirror fragment,\" more than saving these two, I want to go beat Michiko up right now...!!"
    ],
    24: [
        "Brown: They're annoying guys, but they're not bad guys. I wanna save them quick!"
    ],
    25: ["Elly: What a truly awful person! That Michiko...!"],
    26: [
        "Demon Teacher: I'm only doing this on Lady Michiko's orders. Take your complaints to Lady Michiko."
    ],
    27: [
        "Toro: " + S("No", "more...") + "<FF03>Bleaargh!!" + p + "<FF03>Bleeech!!!" + p,
        S("I'm g-", "gonna die... d-", "dying~~")
    ],
    28: [
        "Kurouri: " + S("Haah...", "haah..."),
        S("Hee...", "hee...")
    ],
}

E83 = {
    0: [
        "Yukino: What is this?! This treasure chest? Are they making fun of us?"
    ],
    1: [
        "Nanjo: It is Michiko we are talking about. She would do something this pointless and spiteful.",
        "Nanjo: Even so... the road from the torture room to this room was brutal..."
    ],
    2: [
        "Elly: Is this the treasure chest with the \"mirror fragment\" that Michiko mentioned?",
        "Elly: Still, the road from the torture room to this room was Very hard..."
    ],
    3: [
        "Ayase: Ugh, I'm dying! I don't wanna move! Who was it~?",
        "Ayase: Who said let's go get the \"mirror fragment\"~??",
        "Ayase: If there's no \"mirror fragment\" in this box, Ayase and everyone will have worn ourselves out for nothing! Boo! Boo!!"
    ],
    4: [
        "Nanjo: Still, it is an obviously suspicious chest. Who will open it? The chance of a trap is great."
    ],
    5: [
        "Brown: Don't you think this smells like a trap? From any angle?",
        "Brown: Who'll open it? I'm an introvert, not the type to stand in front of people, so I pass."
    ],
    6: ["Yukino: No point dithering! Let's open it!!"],
    7: ["Yukino: No time limit, but we've spent a bit too long."],
    8: ["Ayase: No more! I'm tired! Resting!!"],
    9: [
        "Nanjo: Even I am fed up with this tower's malice. It is exactly like Michiko's personality."
    ],
    10: [
        "Brown: Gaah! I'm beat! I get chills thinking we have to go back to that torture room again!"
    ],
    11: ["Elly: So... Hard... Shall we rest a little? I am truly tired."],
}

if __name__ == '__main__':
    for n, d in ((81, E81), (83, E83)):
        apply('E1', n, d, {})
