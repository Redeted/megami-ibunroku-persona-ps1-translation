"""E1 entries 195-205 - masked boy (Kandori), girl in black, Queen of the Night."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

p = P('ほ')

E195 = {
    5: ["Yukino: She said she'd destroy the school. Something like that."],
    6: [
        "Masked Boy: I see. That sounds like her.",
        "Masked Boy: In the end, the ice school is a byproduct of her heart. However it turns out, my plan is unharmed."
    ],
    7: ["Ayase: Huh?"],
    8: [
        "Masked Boy: I too have always thought schools unnecessary. Education should be given only to the chosen.",
        "Masked Boy: If she wishes destruction, it would not hurt to humor her."
    ],
    9: ["Nanjo: Hey! You are Kandori, are you not!?"],
    10: ["Masked Boy: Now then. Think hard with your insufficient head."],
    11: ["Yukino: Who is that, with that weird mask..."],
    12: ["Yukino: Nothing here. Let's move on."],
    13: ["Ayase: Is this the old student council room?"],
    14: ["Ayase: What does \"Aijin to Nari\" mean?"],
    15: ["Nanjo: ..."],
    16: ["Nanjo: Was there anything of note?"],
    17: ["Brown: He looks like someone I've seen somewhere."],
    18: [
        "Brown: It gets colder and colder as we go up. How many more floors are there... Boo-hoo..."
    ],
    19: ["Elly: That person, not being frozen..."],
    20: ["Elly: Is Ayase really a high school student?"],
}

E196 = {
    0: [
        "Girl in Black: This is no time for this! Hey, have you seen Papa?"
    ],
    1: [
        "Ayase: Papa~? Is this girl lost? Hey, little girl, why are you in a place like this? It's dangerous, go home."
    ],
    2: [
        "Nanjo: Hey, do you think a lost child would be in a place like this!? Be careful! We do not know what she will do!!"
    ],
    3: [
        "Elly: Miss Ayase! Could you be a little more careful? Because of You and your carelessness, how much Trouble have we been dragged into!!",
        "Elly: Could you learn at least a little?"
    ],
    4: [
        "Ayase: S-Shut up! Geez, every little thing! What if she's really lost? Are you going to leave her to die!?"
    ],
    5: [
        "Girl in Black: Hey~! Can't you understand words? I'm asking if you've seen Papa!!",
        "Girl in Black: He's wearing the same clothes as you big brothers and a black mask."
    ],
    6: ["Yukino: Sorry, but I don't know any man wearing a mask."],
    7: ["Girl in Black: Oh, really."],
    8: ["Yukino: I saw him."],
    9: ["Girl in Black: Eh!? Where was he? Tell me!!"],
    10: ["Yukino: One floor down. He was in the student council room."],
    12: ["Yukino: One floor up. He's in a place like a stage."],
    14: ["Ayase: Why is there a girl here?"],
    16: ["Brown: I'm weak against tough-looking girls like that."],
    17: ["Elly: She must be a Monster!"],
}

E200 = {
    0: [
        "Queen of the Night: Kukukuku... To think you chased me this far.",
        "Queen of the Night: You should have quietly awaited the \"Eternal Night.\" Then I shall give you the despair you wish for.",
        "Queen of the Night: I am not like Tomomi, you know" + p + " Kukukuku..."
    ],
    1: [
        "Masked Girl: Why do you try to protect the school? School..." + p + " I wish schools would just disappear!"
    ],
    2: [
        "Masked Boy: Queen of the Night, we shall lend you our strength.",
        "Masked Boy: That said, it is a bit cramped here to combine our three powers. I invite you all to the top floor" + p + " Follow us at your leisure."
    ],
    3: ["Masked Boy: Gentlemen, are you ready?"],
    4: "=Ready to go to the upper floor?<FF03><FF0E>　<FF01>",
    5: ["Masked Boy: Very well."],
    6: [
        "Masked Boy: Then continue your training. Whoever wins, it matters little to me."
    ],
    7: ["Yukino: Let's hurry upstairs!"],
    8: ["Ayase: My heart is ready."],
    10: [
        "Brown: The happy ending is right around the corner. When the school returns to normal...",
        "Brown: the exploits of me and the rest will be talked about for generations!",
        "Brown: Dehyahyahyahyahya" + p + " Can't wait! Let's go quickly!"
    ],
    11: ["Elly: We will soon be saying goodbye to this cold."],
}

E202 = {
    0: ["Queen of the Night: I've been waiting."],
    1: ["Masked Girl: I wish the school would just disappear!"],
    2: ["Masked Boy: Let us see your true strength, gentlemen."],
}

E203 = {
    0: [
        "Queen of the Night's Voice: Ugh..." + p + " To be defeated by such brats" + p + " how vexing...",
        "Queen of the Night's Voice: But remember this.",
        "Queen of the Night's Voice: As long as there is a heart within people that turns hope into despair, the \"Eternal Night\" will come again and again..."
    ],
    1: [
        "Masked Girl: No..." + p + " Why?" + p + " This is my world..."
    ],
    2: [
        "Masked Boy: As expected. In the end, a stopgap is no good. We shall have to do something ourselves.",
        "Masked Boy: <FF0F>あ-kun" + p + " was it? It seems we will meet again."
    ],
}

E205 = {
    0: ["Saeko-sensei: You're really going, aren't you."],
}

if __name__ == '__main__':
    for n, d in ((195, E195), (196, E196), (200, E200), (202, E202), (203, E203), (205, E205)):
        apply('E1', n, d, {})
