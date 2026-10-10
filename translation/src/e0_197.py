"""E0 entries 197-208 - the Sea of Consciousness: the other self, the real Maki, the return."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

E197 = {
    0: [
        "Maki: Who's there!? <FF07>あ-kun, someone's there!" + P('キ') + " No way!? That's...",
        "Maki: <FF07>あ-kun!?"
    ],
    1: [
        "Maki: There are two <FF07>あ-kuns!? What's going on!? Why are you playing a game in a place like this!?"
    ],
    2: ["<FF08>あ: ...Shut up. It's none of your business what I do."],
    3: ["Maki: Are you... really <FF07>あ-kun?"],
    4: [
        "<FF08>あ: That's right. I'm <FF0F>あ <FF07>あ. Nickname: <FF08>あ.",
        "Enrolled in Class 4 of Year 2 at St. Hermelin...",
        "If you doubt me, I'll tell you everything from my height, weight and shoe size to my taste in girls."
    ],
    5: ["Maki: Huh?"],
    6: [
        "<FF08>あ: I'm you. I know everything you've done up to now,",
        "and what kind of person you are..."
    ],
}

E199 = {
    0: [
        "<FF08>あ: ...Get it now? I'm your reflection. I'm you, and you're me.",
        "We're two sides of the same coin... No, it's not only me.",
        "Inside your heart are thousands, tens of thousands of you."
    ],
    2: [
        "<FF08>あ: ...Now, don't bother me anymore. You of all people should understand how I feel.",
        "I'm content as long as I'm playing games. I don't want any part of troublesome stuff.",
        "Just get going. See ya."
    ],
    3: ["Maki: Who do you think you are, acting so big! <FF07>あ-kun is a good person! Let's go! <FF07>あ-kun!"],
    4: [
        "<FF08>あ: ...You made it this far, so you're not totally hopeless.",
        "Well, do your best, me."
    ],
    5: [
        "<FF08>あ: ...Some of them are aiming to take your place, but it looks like they can't.",
        "Your ego is firmly rooted in that body. That's proof you're steady."
    ],
    6: [
        "<FF08>あ: Here, take this. You can make use of it.",
        "It's the key that awakens the strongest Persona sealed deep in your heart. Go ask that old geezer Igor.",
        "Just... don't forget that the me you saw here is also you.",
        "If you can realize that much, you'll be fine. You're strong enough."
    ],
    7: [
        "<FF08>あ: Here, take this.",
        "You and that girl can make use of it.",
        "It's the key that awakens the strongest Persona sealed deep in your heart. Go ask that old geezer Igor.",
        "Just... don't forget that the me you saw here is also you.",
        "If you can realize that much, you'll be fine. You're strong enough."
    ],
    8: [
        "<FF08>あ: Here, take this.",
        "You and your friends can make use of it.",
        "It's the key that awakens the strongest Persona sealed deep in your heart. Go ask that old geezer Igor.",
        "Just... don't forget that the me you saw here is also you.",
        "If you can realize that much, you'll be fine. You're strong enough."
    ],
    9: ["<FF08>あ: What's wrong? Hurry up and go. Your friends are waiting. See ya, me."],
    10: ["Maki: It isn't only me... Everyone has all kinds of selves, don't they."],
    11: ["Maki: Let's hurry. I don't like that <FF07>あ-kun."],
    12: ["Received the \"Rosetta Stone\"!"],
    13: ["Received the \"Rosetta Stone\" and \"Passe\"!"],
    14: [
        "Received the \"Rosetta Stone,\" \"Passe,\" and \"Holy Water\"",
        "\"Tortoiseshell Glasses,\" and \"Coffin of Babylon\"!"
    ],
    15: [
        "Received the \"Rosetta Stone,\" \"Passe,\" and \"Holy Water\"",
        "\"Tortoiseshell Glasses,\" and \"Judgment Contract\"!"
    ],
    16: [
        "Received the \"Rosetta Stone,\" \"Passe,\" and \"Holy Water\"",
        "\"Tortoiseshell Glasses,\" and \"Victoria Rune\"!"
    ],
    17: [
        "Received the \"Rosetta Stone,\" \"Passe,\" and \"Holy Water\"",
        "\"Tortoiseshell Glasses,\" and \"Deer Mount\"!"
    ],
    18: ["<FF08>あ: ...You're noisy. Hurry up and get lost."],
    19: [
        "It's Atlus's fighting game \"Groove On Fight.\" It looks super fun!!"
    ],
}

E201 = {
    0: ["Maki: Found you at last! The real me!"],
    2: [
        "Maki: Wait! Where else do you think you can run? There's nowhere left to run!"
    ],
    3: [
        "Maki: ........." + P('キ') + " Those countless bubbles are the many consciousnesses of many people...",
        "Maki: A person's consciousness is nothing but a fragile bubble born from this sea...",
        "Maki: I was a consciousness that shouldn't have been born... If you had been born from the start, it would have been a different life..."
    ],
    4: [
        "Maki: Stop it!! I don't want to hear such lines from my own mouth!!",
        "Maki: Did you ever try to change yourself? What have you done? All you do is cry in bed, right!?",
        "Maki: I want to change with you!" + P('キ') + " Inaba-kun, Nanjo-kun, Kido-kun... and <FF07>あ-kun...",
        "Maki: Looking at everyone, don't you think there's nothing you can't do?",
        "Maki: What ruins everything is your heart!"
    ],
    5: [
        "Maki: Stop it!! I don't want to hear such lines from my own mouth!!",
        "Maki: Did you ever try to change yourself? What have you done? All you do is cry in bed, right!?",
        "Maki: I want to change with you!" + P('キ') + " Inaba-kun, Nanjo-kun, Elly... and <FF07>あ-kun...",
        "Maki: Looking at everyone, don't you think there's nothing you can't do?",
        "Maki: What ruins everything is your heart!"
    ],
    6: [
        "Maki: Stop it!! I don't want to hear such lines from my own mouth!!",
        "Maki: Did you ever try to change yourself? What have you done? All you do is cry in bed, right!?",
        "Maki: I want to change with you!" + P('キ') + " Inaba-kun, Nanjo-kun, Uesugi-kun... and <FF07>あ-kun...",
        "Maki: Looking at everyone, don't you think there's nothing you can't do?",
        "Maki: What ruins everything is your heart!"
    ],
    7: [
        "Maki: Stop it!! I don't want to hear such lines from my own mouth!!",
        "Maki: Did you ever try to change yourself? What have you done? All you do is cry in bed, right!?",
        "Maki: I want to change with you!" + P('キ') + " Inaba-kun, Nanjo-kun, Yuka... and <FF07>あ-kun...",
        "Maki: Looking at everyone, don't you think there's nothing you can't do?",
        "Maki: What ruins everything is your heart!"
    ],
    9: ["Maki: I won't run anymore... I'll settle my own accounts myself!"],
    10: [
        "Maki: ........." + P('キ') + " Take this with you... With it you can enter Avidya's realm, where Pandora is.",
        "Maki: I..." + P('キ') + " didn't want <FF07>あ-kun of all people to see me like this."
    ],
    11: [
        "Maki: I wonder if I said it well... But now all I can do is believe in myself... Let's go back to everyone!"
    ],
    12: ["Obtained the \"Blue Compact\""],
}

E202 = {
    0: ["Maki: Sorry to keep you waiting, everyone!"],
    1: ["Mark: I'm sick of waiting!"],
    2: [
        "Nanjo: It seems it went well. Then let us go to the school to meet this Pandora."
    ],
    3: ["Maki: Everyone looks like they got bored."],
    4: ["Mark: Hey, <FF0F>あ, you didn't do anything bad, did you?"],
    5: ["Nanjo: What is it? Did something happen in there?"],
    6: [
        "Reiji: Looks like you're alive. When this is over, we'll settle which of us is stronger. You won't say no, will you?"
    ],
    7: ["Elly: <FF07>あ! Thank goodness~ Are you hurt?"],
    8: ["Elly: <FF07>あ! Thank goodness... Are you not hurt?"],
    9: [
        "Brown: Tch, so stubborn. I thought the script was <FF08>あ gets beaten",
        "and I make a dashing entrance!"
    ],
    10: ["Ayase: <FF0F>あ, you took so long, Ayase thought you'd died."],
    11: ["Ayase: <FF08>あ, you took so long, Ayase thought you'd died."],
    12: [
        "Butterfly: Until this world vanishes, there is not much time left. Hurry."
    ],
}

E208 = {
    0: ["Maki: Chisato! Yosuke-kun! Thank goodness, you're safe!"],
    1: ["Chisato: Maki! You're safe!"],
    2: [
        "Mark: Hey, Naito. What happened to the school? There's nobody but you two."
    ],
    3: [
        "Yosuke: We don't know. When we came back, nobody was there.",
        "Yosuke: The east half of the town has vanished too. We're the ones who want to know what's going on."
    ],
    4: ["Nanjo: It is Pandora's doing..."],
    5: ["Chisato: Pandora?"],
    6: [
        "Maki: I'm sorry... Chisato, Yosuke-kun. It's all my fault... Everything is like this...",
    ],
    7: ["Chisato: ..."],
    8: ["Yosuke: ...I see."],
    9: [
        "Maki: I promise I'll send everyone back to their original world.",
        "Maki: No matter how much I apologize, it can't be forgiven... but I'm truly sorry.",
        "Maki: Hit me as much as you like, Chisato."
    ],
    10: [
        "Chisato: Stupid Maki! You're so clumsy. You've been like that since long ago..."
    ],
    11: ["Yosuke: Hey, Chisato..."],
}

if __name__ == '__main__':
    for n, d in ((197, E197), (199, E199), (201, E201), (202, E202), (208, E208)):
        apply('E0', n, d, {})
