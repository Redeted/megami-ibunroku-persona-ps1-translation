"""E0 entry 67 - the party meets Reiji; he joins them."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Mark: I'm really surprised. You can use Personas too?"],
    1: ["Reiji: ...What did you say? You guys are the same as me...?"],
    2: ["Nanjo: Well, that is the case." + P('ぶ') + " By the way, you seem to be the real Kido."],
    3: ["Reiji: ...What do you mean?"],
    4: [
        "Elly: This place looks very similar, but it is not our world.",
        "Elly: Do you understand?"
    ],
    5: [
        "Brown: Heh heh! Clean out your ears and listen up!",
        "Brown: This is the school we know, and yet it isn't!",
        "Brown: It's a school from another world! Bet that surprised ya! Dammit!" + P('で') + " Boo-hoo..."
    ],
    6: [
        "Ayase: We're the ones who wanna ask! Can you believe this is another world?",
        "Ayase: Geez, I don't get any of this!"
    ],
    7: [
        "Nanjo: We were sent to a very similar world by Kandori. You are the same, are you not?",
        "Nanjo: The boy Kandori and that scientist spoke of, sent to the gap between dimensions, is you." + P('キ') + " Am I wrong?",
        "Nanjo: Why are you here safely after being sent to the gap between dimensions? And why are you chasing Kandori?"
    ],
    8: [
        "Reiji: ..." + P('ス') + " I was drifting in a place with nothing, and a kid in white clothes appeared...",
        "Reiji: Then when I noticed, I was here. That's all... I've got no reason to tell you the rest."
    ],
    9: ["Maki: A child in white clothes...?"],
    10: [
        "Mark: Don't be so edgy. We're gonna beat the crap out of Kandori and look for a way home.",
        "Mark: Come with us. Your mom's probably worried about you, too."
    ],
    11: ["Reiji: Shut up! I've got no intention of flocking with you guys! I'll do things my own way."],
    12: [
        "Mark: What the hell?! I worry about the guy and he gets all cocky!",
        "Mark: Fine, do what you want! Don't blame me if you die in a ditch! You jerk!" + P('で') + " What's with that guy...",
        "Mark: I only said 'mom' and his eyes changed..."
    ],
    13: [
        "Maki: Stop it, Inaba-kun. Nothing you say will get through to him. He has those kind of eyes...",
        "Maki: I'm sure Kandori hurt something important to him, just like he did to us..."
    ],
    14: ["Elly: " + P('で') + "Something important..."],
    15: ["Brown: Quit prying! Everybody's got things they don't want touched, right?"],
    16: [
        "Nanjo: Do you have a fever, Uesugi? That was a surprisingly sensible remark from you.",
        "Nanjo: You understand how he feels, is that the look?"
    ],
    17: [
        "Brown: W-What's that? Guys as honest as me are rare, y'know?",
        "Brown: Any day now I'll be designated a national treasure!"
    ],
    18: ["Nanjo: Same old fool... Well, <FF0F>あ, shall we get going?"],
    19: ["Brown: What the hell, Nanjo! Even if I'm designated a national treasure, I won't talk to you!"],
    20: ["Ayase: Huh~? Does that guy even have anything like that? Isn't he just unfriendly~?"],
    21: [
        "Maki: He... Kido-kun, was it? I'm sure even Kido-kun has something important.",
        "Maki: Like friends... or dreams for the future."
    ],
    22: ["Ayase: ...Dreams for the future?" + P('ょ') + " Who cares, as long as the present's good. You're such an idiot..."],
    23: ["Maki: See, this place is not your world. How should I explain it..."],
    24: [
        "Reiji: What? So that bastard's come here too?" + P('ヒ') + " Fine...",
        "Reiji: I'll go with you."
    ],
    25: ["Maki: It's settled! I'm Sonomura Maki! Nice to meet you, Kido-kun!"],
    26: ["Reiji: ..." + P('ほ') + " ..." + P('ほ') + " ..."],
    27: [
        "Maki: What? Do I have something on my face?" + P('ヒ') + " Ah!",
        "Maki: You were so taken with how cute I am, weren't you? Yeah, I get it, I get it."
    ],
    28: ["Mark: C'mon, we can't be dawdling forever. Let's get going!"],
    29: [
        "Maki: Kido-kun... you said you were saved by a \"child in white clothes,\" right? Could it be...",
        "Maki: Maybe it's Mai-chan... I've seen her a few times, and she's a very mysterious girl..."
    ],
    30: ["Mark: That damn idiot..."],
    31: ["Mark: Come on, hurry up and move! Huh? \"What are you so angry about?\" Shut up!"],
    32: [
        "Nanjo: Leave him alone. He is chasing the same man. We will likely meet again.",
        "Nanjo: As long as he does not get in our way, that is enough."
    ],
    33: ["Nanjo: Kido's reason for chasing Kandori? Well, we will find out eventually. For now, it is enough that he is useful to us."],
    34: ["Elly: Something important... someone dear... <FF07>あ, you..."],
    35: "=Do you have someone dear to you?<FF03><FF0E>ふ<FF01>",
    36: ["Elly: I see..." + P('で') + " As for me..." + P('で') + " I am sorry for asking such a strange thing..."],
    37: ["Elly: I see..." + P('で') + " Then you are the same as me..."],
    38: ["Brown: Man, it ain't good to go pryin' into stuff people are hiding."],
    39: "=You've got secrets too, right?<FF03><FF0E>へ<FF01>",
    40: ["Brown: See? See? Told ya, right? That's just how people are!"],
    41: ["Brown: Liar~! Is that all there is to you and me? Just this surface-level stuff?"],
    42: ["Ayase: No point worrying about the future, right? <FF0F>あ thinks so too, right?"],
    43: "=Present's all that matters, right?<FF03><FF0E>ひ<FF01>",
    44: ["Ayase: ..." + P('で') + " I knew it! We totally click, <FF0F>あ!"],
    45: ["Ayase: ..." + P('で') + " What the heck! Idiot idiot idiot idiot idiot idiot idiot!"],
    46: ["Reiji: That Sonomura girl... I don't feel like I'm meeting her for the first time... Who is she...?"],
    47: ["Student: Is his name Kido-kun? He's cool..."],
}
REVIEW = {}

if __name__ == '__main__':
    apply('E0', 67, BOXES, REVIEW)
