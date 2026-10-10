"""E1 entries 73-83 - Hypnos defeated; Michiko of the Tower of Nemesis; torture room."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

p = P('ほ')


def S(*parts):
    """join text parts with the Japanese's pause code between them"""
    return p.join(parts)


E73 = {
    19: [
        "Yukino: Hah!... If the opponent is a Persona user, no need to hold back!",
        "Yukino: Everyone! Here we go!!"
    ],
}

E74 = {
    0: [
        "Yukino: You lose. Your precious prince... no, the \"Lord Persona\" born of your heart is gone.",
        "Yukino: Want to keep going? I don't mind at all..."
    ],
    1: [
        "Kumi: ...In the end... in the end, I have no place anywhere, do I...",
        "Kumi: Neither in reality... nor in dreams.",
        "Kumi: Heh... I'd have to run away from dreams too... Hehe..."
    ],
    2: [
        "Nanjo: A person without dreams is generally shallow and dull. A person who only chases dreams generally has no substance.",
        "Nanjo: Live without losing your dreams, and without being swept away by them.",
        "Nanjo: A dream is not something to chase... and a dream is not a place to flee to...",
        "Nanjo: A dream is... food for the heart. But a dream does not become yours by merely waiting for it.",
        "Nanjo: A dream is not given. It is something you grasp with your own hands......!",
        "Nanjo: Yamaoka used to say that."
    ],
    3: [
        "Brown: Great me's strength brought a big victory, but...",
        "Brown: somehow it leaves a bad taste... This kind of thing..."
    ],
    4: [
        "Ayase: Yay! We won!",
        "Ayase: Did you see" + p + " did you see! Ayase and the others' power! How's that" + p + " how's that!",
        "Ayase: Had enough?!"
    ],
    5: [
        "Kumi: You are all truly strong people... If I had even a little of such strength...",
        "Kumi: I might have lived without falling for the temptation of the \"Snow Queen's mask.\"",
        "Kumi: I only blamed others, put myself in a safe zone, and just complained...",
        "Kumi: I was just the same as the other people who blamed me."
    ],
    6: [
        "Nanjo: Hmph... Understanding even that much is good enough. Reflect deeply.",
        "Nanjo: Dreams are indeed food for the heart... but fleeing into dreams cannot change reality."
    ],
    7: [
        "Elly: Kumi-san, now that you have realized that, you are no longer a weak person.",
        "Elly: Dreams are like an Oasis in our hearts. They quench the thirst of travelers weary from walking the desert of life.",
        "Elly: But however comfortable the Oasis, the traveler must eventually start walking into the desert again.",
        "Elly: For no matter how hard it is, as long as we live we are travelers crossing the desert called \"reality.\""
    ],
    8: [
        "Kumi: Thank you... everyone... If I had had even one friend like you by my side... that would have been nice...",
        "Kumi: I won't forget you.",
        "Kumi: Thank you" + p + " ...Goodbye."
    ],
    10: ["Obtained 1 \"Ambrosia\""],
    11: [
        "Yukino: \"Hirose Kumi\"... She wasn't such a bad person.",
        "Yukino: She was also a victim whose life the \"mask\" drove astray.",
        "Yukino: Now, let's go back! We have to save Saeko-sensei quickly!!"
    ],
    12: ["The Tower of Hypnos has been conquered!"],
}

E80 = {
    0: [
        "Yukino: This room gives off an unpleasant presence. As if we're being stared at with malicious eyes..."
    ],
    1: [
        "???: Ohohohohoho. Good day, everyone. Thank you for coming to this tower.",
        "???: I welcome you from my heart. Ohohohohohohohohoho!"
    ],
    2: [
        "Nanjo: Who is it!? Show yourself! You are no doubt a mere guard of this tower!!",
        "Nanjo: However much you put on airs, you are nothing but a small fry, a \"fox borrowing the tiger's might\" from the Snow Queen!"
    ],
    3: [
        "Elly: Who? Show yourself! You are most likely this tower's Guardian, are you not?",
        "Elly: Can you not come out before us? Heh... I suppose it cannot be helped.",
        "Elly: A tower's Guardian is a small fry who can do nothing without the Snow Queen's power, after all!"
    ],
    4: [
        "Ayase: That's right! That's right! You can't come out because you're scared of Ayase and the others!",
        "Ayase: Neener! Neener! Everyone! This tower's boss looks weak!",
        "Ayase: Super lucky, right!? Kyahahaha!"
    ],
    5: [
        "???: Ohohohohoho! What foolish yet noisy little puppies you are!",
        "???: How very... bully-able. Heh heh... I won't be bored at all!",
        "???: Because, you see, if I bully a weak opponent too much, they break right away!",
        "???: Hee hee... I'm late with introductions. My apologies.",
        "???: I have been ordered by the \"Snow Queen\" to guard this \"Tower of Nemesis.\" I am \"Matsudaira Michiko.\"",
        "???: Please consider it an honor to die by my hand.",
        "???: By the way..." + p + " ......" + p + " ........." + p + " ...Oh? You? " + p + " Yes" + p + " you! My, my! What a thing!",
        "???: What a han" + p + "d" + p + "some man! *",
        "???: How about it? Rather than being killed by me together with those people, would you become my pet?"
    ],
    6: [
        "Nanjo: W-" + p + " W-" + p + " Wha-" + p + " What did you say?! Me?" + p + " You mean me!?",
        "Nanjo: A-" + p + " And a woman as markedly bad in personality, " + p + " attitude, " + p + " and looks as you?!",
        "Nanjo: I should become a pet?! Do not underestimate Nanjo Kei!",
        "Nanjo: I shall make you regret speaking to me like that, in hell!"
    ],
    7: [
        "Brown: Hnh?! Me?" + p + " Is it me?? Wait a minute!",
        "Brown: What the heck, this ugly woman! She suddenly appears and says some nonsense!",
        "Brown: Don't screw with me! Making \"Brown\" your p-" + p + " pet?",
        "Brown: Don't mess with me! Don't make a fool of me!! I'll beat you up!",
        "Brown: I'll give that ugly face plastic surgery to make it even uglier!"
    ],
    8: [
        "Michiko: Kyaaah! I, " + p + " I, Michiko, even " + p + " even went to the trouble " + p + " of showing mercy...",
        "Michiko: H-" + p + " Hmph! It was an unreasonable request to ask the lowly to understand my greatness.",
        "Michiko: ...Very well, puppies. I will break every last one of you with my own hands...",
        "Michiko: I have just lifted this tower's time limit! You may take as many hours as you like!",
        "Michiko: By all means, come to me! Understand? Take as many hours as you like!",
        "Michiko: Then I shall be waiting! Good day!!"
    ],
    9: ["Yukino: Matsudaira Michiko... Looks like she's not easy to deal with."],
    10: [
        "Yukino: No time limit? Considering that woman's character, there's a catch.",
        "Yukino: Don't you think so?"
    ],
    11: [
        "Ayase: Say, that Michiko woman looks like somebody.",
        "Ayase: Like, how super arrogant she is."
    ],
    12: [
        "Nanjo: What is that woman!? Looking down on people with such an arrogant attitude!",
        "Nanjo: Who does she think she is!? Does she think she is the greatest in the world?",
        "Nanjo: How unpleasant! Truly unpleasant!!"
    ],
    13: [
        "Brown: That arrogant attitude that looks innate... that shameless attitude like she thinks nobody in the world is above her!",
        "Brown: Between us, she's just like somebody whose last name has \"na\" in it!"
    ],
    14: [
        "Elly: No Time limit? What does that mean?",
        "Elly: Is it the woman's confidence that she can easily defeat us even without it?",
        "Elly: Or is there another reason? In any case, there is surely a catch.",
        "Elly: It might be better to be rather mindful of the Time limit."
    ],
}

if __name__ == '__main__':
    for n, d in ((73, E73), (74, E74), (80, E80)):
        apply('E1', n, d, {})
