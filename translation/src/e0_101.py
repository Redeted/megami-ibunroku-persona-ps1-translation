"""E0 entry 101 - aftermath; Aki abandons Chisato."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Maki: Chisato was troubled too. I feel kind of refreshed."],
    1: ["Nanjo: To be petrified at a crucial moment is the shame of a lifetime!"],
    2: ["Nanjo: They are back together, then. Well, if they are happy with it, that is fine."],
    3: ["Mark: Maybe they were talking about something really important? Dammit, I'm curious!"],
    4: [
        "Mark: Don't think I'm happy about this!",
        "Mark: Even if she ain't the Sonomura from our world, I ain't so pathetic as to be glad to see her get her heart broken."
    ],
    5: ["Elly: Didn't Maki like Naito-kun?"],
    6: ["Elly: So there are people who love you as you are, without pretending..."],
    7: [
        "Brown: Hasn't Kozai's vibe changed? Like, she got softer?"
    ],
    8: ["Brown: I jotted down Naito's lines! Now, who should I use them on~?"],
    9: ["Ayase: Hey, hey, what happened while Ayase was inside the stone?!"],
    10: ["Ayase: W-What's with you! Ayase isn't crying or anything!"],
    11: ["Reiji: ...Nothing to say."],
    12: ["Young Men: Um... we'd like you to hurry up and turn us back..."],
    13: [
        "Naito: Sorry to trouble you all. It happened because I wasn't being reliable.",
        "Naito: I'm sorry."
    ],
    14: [
        "Kozai: Maki is actually shut in the hospital...",
        "Kozai: While Maki is suffering, is it okay for only me to be happy?"
    ],
    15: ["There is a painting Maki drew..."],
    16: ["The mirror has lost its power..."],
    17: [
        "Aki: Hey~! Losing to these guys, you're too weak!",
        "Aki: Since you couldn't win, Aki won't fix your face! " + P('ぎ'),
        "Aki: Not that Aki ever planned to fix it from the start!"
    ],
    18: ["Kozai: Wh-What? Wait..." + P('な') + " What do you mean?!"],
    19: [
        "Aki: Papa said you're just an \"experiment subject\" and a \"disposable pawn\"!",
        "Aki: He said to leave you alone even if Kato loses!",
        "Aki: So stay like that forever, okay?" + P('み') + " Bye-bye!"
    ],
    20: ["Aki: Nomoraka tanomamaa~!"],
    21: ["Kozai: W-Wait...! Am I going to stay like this forever?!" + P('み') + " ...No way...!!"],
    22: [
        "Maki: Chisato...!" + P('ぎ') + " Wait for us. We'll catch that girl right away.",
        "Maki: Then we'll make her restore Chisato's face!"
    ],
    23: ["Kozai: Maki..." + P('ぎ') + " Liar! Don't talk nonsense!" + P('た') + " You think it serves me right, don't you?"],
    24: ["Maki: It's not a lie. I like Chisato, after all."],
    25: ["Kozai: You" + P('ぎ') + " like me?"],
    26: [
        "Maki: Yeah!" + P('み') + " You're lively, pretty, stylish, and you have a firm sense of self.",
        "Maki: I understand why Naito-kun likes you."
    ],
    27: [
        "Kozai: That's a lie! Yosuke surely still" + P('ぎ') + " likes Maki." + P('ぷ') + " ...Maki, I'm sorry.",
        "Kozai: I envied Maki. Having a firm sense of self, I only made it look that way.",
        "Kozai: The real me can't do anything. If I don't always look pretty and put on a show, no one will turn to look at me.",
        "Kozai: So I envied Maki so much, who is loved by everyone just as she is."
    ],
    28: ["Maki: Chisato..."],
    29: [
        "Kozai: Now Yosuke will surely lose patience with me.",
        "Kozai: Then, Maki, this time you and Yosuke...",
        "Kozai: ..." + P('ぎ') + " Yosuke..."
    ],
    30: [
        "Maki: Chisato, you stubborn girl! You really like Yosuke, don't you?",
        "Maki: But you don't have to worry about me" + P('ぎ') + " because..."
    ],
    31: ["Kozai: Eek, what...?"],
    32: [
        "Naito: Chisato...!!" + P('ぎ') + " I finally found you! I've been looking for you all this time!",
        "Naito: ..." + P('ぎ') + " What's with that face! Are you hurt?!"
    ],
    33: ["Kozai: No! Don't look, Yosuke!"],
    34: ["Maki: Um, actually, Aki put a curse on her..."],
    35: [
        "Kozai: Maki! You're covering for me?" + P('ょ') + " No," + P('ぎ') + " that's enough!"
    ],
    36: [
        "Kozai: Yosuke, look at this! This is my face now!",
        "Kozai: I did so many bad things and said awful things to Maki too." + P('ぎ') + " This is my punishment!"
    ],
    37: ["Naito: Chisato...!"],
    38: [
        "Kozai: I don't deserve to be liked by Yosuke!",
        "Kozai: My personality is bad, and even the face I was proud of has changed.",
        "Kozai: If they saw you with someone like me, even Yosuke would be laughed at!",
        "Kozai: So it's fine now. Go to Maki! You've liked her for a long time, haven't you?"
    ],
    39: [
        "Naito: Hey, don't get the wrong idea!" + P('み'),
        "Naito: It's true I once liked Sonomura, but that's in the past. Now it's only Chisato I love!",
        "Naito: ..." + P('ぎ') + " Geez, what are you making me say! It's embarrassing! Now, let's go home together!"
    ],
    40: [
        "Kozai: But..." + P('ょ') + " these moles of mine will never come off, you know...?",
        "Kozai: Is that okay? Even if your friends laugh at you..."
    ],
    41: [
        "Naito: That's fine! I don't care if someone laughs!",
        "Naito: You said your personality is bad, but I have ugly sides too, and you don't need to act composed all the time.",
        "Naito: Like now, just tell me honestly what you think. I'm Chisato's boyfriend, after all.",
        "Naito: I don't care what you look like. Just be yourself. I love Chisato!!"
    ],
    42: ["Maki: Ah, the mirror...!"],
    43: ["Naito: Chisato!" + P('ぎ') + " Your face" + P('ぎ') + " is back to normal!"],
    44: [
        "Kozai: It's true!" + P('ぶ') + " I'm happy..." + P('ょ') + " No, it's not about my face.",
        "Kozai: I always thought Yosuke actually liked Maki.",
        "Kozai: ...Thank you..."
    ],
    45: ["Mark: Aah, that was cramped!" + P('ぎ') + " Gah, Naito!" + P('ぎ') + " ...Kozai, did your moles come off?"],
    46: ["Nanjo: Hmm..." + P('ぎ') + " It seems the story took a sudden turn while I was not looking."],
    47: ["Elly: What's happening? Why is Naito-kun here?"],
    48: ["Brown: Huh, Naito! Why are you here?" + P('ぎ') + " Oh, Kozai's moles are gone too!"],
    49: ["Ayase: Why is Naito here?" + P('ぎ') + " Oh, Kozai's back to normal too! Geez, I don't get it!"],
    50: ["Reiji: Naito...?" + P('ぎ') + " Kozai's back to normal, too."],
    51: [
        "Kozai: I'm sorry, Maki." + P('ぶ') + " I lied.",
        "Kozai: Just as you said, I really do like Yosuke.",
        "Kozai: I wanted you to forgive me... " + P('ぎ') + " but you can't forgive me anymore, can you? I wanted us to be best friends again..."
    ],
    52: [
        "Maki: Idiot! There's nothing to forgive or not forgive!",
        "Maki: Chisato is still my best friend." + P('ぎ') + " I'm glad for you, Chisato...!"
    ],
    53: [
        "Nanjo: Aki has fled, then. Kozai, do you know anything about a man called Kandori?",
        "Nanjo: He should be acting together with Aki."
    ],
    54: [
        "Kozai: I don't know a man called Kandori.",
        "Kozai: ...Come to think of it, that girl said she lives in a castle."
    ],
    55: ["Mark: A castle? What the hell's that!"],
    56: ["Nanjo: There is no need to be surprised. Child though she is, Aki's power is immense. Building a castle must be easy for her."],
    57: ["Maki: Alright, let's go! Let's find the castle!"],
    58: ["Naito: Chisato, I forgot to tell you. That Sonomura is not the Sonomura we know."],
    59: ["Kozai: Huh?"],
}
REVIEW = {19: "かとう = Kato (guessed Kandori subordinate; check glossary)"}

if __name__ == '__main__':
    apply('E0', 101, BOXES, REVIEW)
