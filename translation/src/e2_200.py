"""E2 entries 199-207 - the haunted house (SEBEC scientists), brainwashing radio waves, casino lobby."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

pm = P('み'); p = P('ほ')

E199 = {
    22: [
        "Young Man: I think, what's so good about a painting like this? She acted all grand calling herself the Queen, but I'm way more attractive!"
    ],
}

E200 = {
    0: ["Maki: We have to hurry! <FF07>あ-kun and the others won't be able to go home!"],
    1: ["Nanjo: Kandori... What is he plotting...!"],
    2: [
        "Mark: Thinking about it now, only the old man who invented the machine tried to take responsibility himself."
    ],
    3: ["Elly: This mansion... has a most wonderful atmosphere."],
    4: ["Brown: Whatever, this is a creepy place!"],
    5: ["Ayase: A woman's crying... I've been hearing it all along."],
    6: [
        "Reiji: Are all these people reflecting on what they did?"
    ],
    7: [
        "Scientist: The dimensional passage on the third floor was in a rather unstable state. If we don't hurry, it might become unusable!"
    ],
    8: [
        "Scientist: Dr. Nicolai" + pm + " he alone noticed Kandori's true nature. It's no use regretting now, but we should have stopped Kandori even if it cost us our bodies.",
    ],
    9: [
        "Scientist: Are you chasing Kandori? But it's too late. By now he must be putting a terrible scheme into action."
    ],
}

E201 = {
    0: ["Maki: Those people are in the same situation as <FF07>あ-kun and the others."],
    1: ["Nanjo: They say the ghost of a woman appears here."],
    2: ["Mark: A haunted house that actually has ghosts!"],
    3: [
        "Elly: Wonderful! To see even a ghost... Let us go look quickly!"
    ],
    4: [
        "Brown: If it's a drop-dead beauty ghost, that might be nice" + pm + " ...nah, I'll pass!"
    ],
    5: [
        "Ayase: Ayase should've brought a camera! I'd take loads of spirit photos and sell them everywhere!"
    ],
    6: [
        "Reiji: Scientists frightened of ghosts" + pm + " ...Kandori's blessed with fine personnel."
    ],
    7: [
        "Scientist: Actually, we're not from this world, and we're stuck because we can't enter the room with the machine to get back to our own world...",
        "Scientist: Would you please go check on it?"
    ],
    8: [
        "Scientist: Damn it! That Kandori, he used our research to the fullest and then abandoned us!"
    ],
    9: [
        "Scientist: We can hear a woman ghost crying from inside that room! We say ghosts can't exist, but",
        "Scientist: we're too scared and nobody goes near it..."
    ],
}

E203 = {
    0: [
        "Scientist: Uhyahyahyahyahya! The hammer of judgment will fall on foolish humanity!",
        "Scientist: Uhyahyahyahyahya!"
    ],
    1: [
        "Scientist: I feel like I was thinking something absurdly stupid..."
    ],
    2: ["Scientist: Humanity needs no future!!"],
    3: [
        "Scientist: We must not crush humanity's future! Right, gentlemen!!"
    ],
    4: ["Scientist: What on earth was humanity born for?"],
    5: [
        "Scientist: What was humanity born for? I haven't thought about that since I was a child.",
        "Scientist: I couldn't afford to, after all..."
    ],
    6: ["Maki: Is everyone brainwashed?"],
    7: ["Maki: Good thing that weird signal stopped."],
    8: ["Mark: These guys are nuts."],
    9: ["Mark: You finally woke up."],
    10: ["Nanjo: We must stop Kandori as soon as possible!"],
    11: ["Nanjo: What were we born for" + p + " ..." + p + " is it?"],
    12: ["Ayase: Hey! Your eyes are gone~!!"],
    13: ["Ayase: Phew~ Everyone's eyes look normal again."],
    14: ["Brown: Aaaaah."],
    15: ["Brown: Radio waves are scary."],
    16: [
        "Elly: There is nothing we can do by staying here. Let us hurry on."
    ],
}

E204 = {
    0: [
        "SP: Humans who sometimes hate and kill each other, who even pollute the planet they live on to satisfy their desires...",
        "SP: As living creatures, they were a failure after all!!"
    ],
    1: [
        "SP: I wonder if my family back home is doing okay. I'm quitting this job."
    ],
    2: [
        "SP: Humans only think about themselves in the end! They'd be better off vanishing from the Earth!!"
    ],
    3: ["SP: What was I born for..."],
    4: ["Maki: What's wrong with these people?"],
    6: ["Mark: Every one of them talks like Kandori!!"],
    10: ["Ayase: I'm scared. Let's get out quick."],
    12: ["Brown: Aaaaaaah."],
    13: ["Brown: Radio waves are scary. Seriously."],
    16: ["Reiji: They keep saying the same things."],
}

E205 = {
    0: [
        "SP: A" + p + " my head... hurts..." + p,
        "SP: Judgment upon humanity!!"
    ],
    1: ["SP: My head's heavy... like a hangover morning."],
    2: ["SP: Humanity needs no future!! Don't you think so, gentlemen?"],
    3: ["SP: A future... Suddenly I feel anxious."],
    4: [
        "Scientist: What is this? Everyone has started saying the same nonsense.",
    ],
    5: [
        "Scientist: What is this? Why has everyone suddenly come to their senses?"
    ],
    6: ["Maki: That person seems sane."],
    8: ["Mark: This is bad. Let's hurry on!"],
    10: ["Nanjo: It seems there are other sane people besides us."],
    12: ["Ayase: Doesn't the back of your head kind of hurt?"],
    14: ["Brown: Dehya~ Are these guys serious?"],
    18: ["Reiji: I won't forgive this."],
}

E206 = {
    0: [
        "Kogal: Everyday was so fun, and now what's gonna happen?",
        "Kogal: So I decided! Until the town vanishes, I'm gonna have fun playing here!"
    ],
    1: [
        "Ayase: Are you stupid!? This is no time to be playing!",
        "Ayase: Why don't you think about doing something so the town doesn't vanish?"
    ],
    2: [
        "Kogal: What's wrong, Ayase...? That's not like you. Do you have a fever or something?"
    ],
    3: [
        "Schoolgirl: The town is vanishing little by little! What do we do!?"
    ],
    4: [
        "Maki: Everyone is imagined by the real me, right... I wish she'd make it easier to win."
    ],
    5: ["Mark: Hey hey! Is this the time to play!"],
    6: [
        "Nanjo: You intend to play even in this situation? I cannot tell whether you are great or just thoughtless..."
    ],
    7: ["Ayase: Playing is fine, but do it in moderation!!"],
    8: [
        "Brown: That clerk's also imagined by Maki-chan, right? Make her a bunny girl!"
    ],
    9: ["Elly: Is the break over? Then let us hurry!"],
    10: ["Elly: Have you finished your break? Then let us hurry!"],
    11: ["Reiji: Pointless."],
    12: "= <FF03>       OUT OF ORDER<FF03> <FF02><FF01>",
}

E207 = {
    0: ["Shopkeeper: Ohoho, welcome~"],
    1: [
        "Clerk: Hey~! You little brat~!! There's a safe over there! It's no place for you!",
        "Clerk: I'll kill you, damn it!!"
    ],
    2: [
        "Youth: The place that was a wasteland disappeared completely. What on earth is happening!?"
    ],
    3: ["Townsperson: I wonder what happened to the girl who played in the flower field?"],
    4: ["Maki: Did you find a good weapon?"],
    5: [
        "Mark: The demons are getting stronger too. If we don't arm ourselves properly, we're done for."
    ],
}

if __name__ == '__main__':
    for n, d in ((199, E199), (200, E200), (201, E201), (203, E203), (204, E204), (205, E205), (206, E206), (207, E207)):
        apply('E2', n, d, {})
