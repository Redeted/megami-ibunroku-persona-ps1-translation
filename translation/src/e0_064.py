"""E0 entry 64 - Arriving in the other world."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Mark: ...Oww..."],
    1: ["Mark: S-Sonomura! Are you okay!?"],
    2: ["Maki: ...N-Ngh..."],
    3: ["Maki: ...Inaba" + P('で') + "-kun?"],
    4: ["Nanjo: Guh..."],
    5: ["Nanjo: ...Where are we?" + P('で') + " Ah, <FF0F>あ, you were safe."],
    6: ["Brown: Owwowow... M-My back..."],
    7: ["Brown: A-Alright! I'm alive, <FF08>あ! As expected of the great me, I'm so lucky!"],
    8: ["Elly: ...Ah."],
    9: ["Elly: ...Where are we? Ah, <FF07>あ... You aren't injured, are you?"],
    10: ["Ayase: ...Ugh~."],
    11: ["Ayase: ...It huuurts! I've had enough! Ayase's going home! Why do I have to go through this!?"],
    12: ["Nanjo: It seems everyone is safe. You people truly have strong, devilish luck."],
    13: ["Elly: ...This place is our school's gymnasium. And from half a year ago..."],
    14: ["Brown: ...Hey, hey, is this our school's gym!? And the one from half a year ago..."],
    15: ["Ayase: ...Hey, hey, isn't this Ayase's school's gym? Was it half a year ago? When we broke it..."],
    16: ["Maki: I see... We came back..."],
    17: ["Mark: Came back? To half a year ago!? Get a grip, Sonomura."],
    18: ["Nanjo: ...A time slip? That is quite different from what your mother said."],
    19: [
        "Maki: ...I've said it so many times, but I really don't have a mom.",
        "Maki: To think that what Yosuke-kun said... was actually true..."
    ],
    20: [
        "Student: Ah! There you are! It's terrible, Maki! Naito-kun was badly injured!",
        "Student: That Girl in Black came again, and..."
    ],
    21: ["Maki: No way! T-That can't be! Yosuke-kun!"],
    22: ["Mark: H-Hey, Sonomura!"],
    23: [
        "Elly: By Yosuke-kun, I wonder if she means that Naito Yosuke-kun?",
        "Elly: If I recall, he went missing with Chisato Kozai-san about two months ago."
    ],
    24: [
        "Brown: Does she mean that Naito Yosuke by Yosuke?",
        "Brown: If I remember right, he eloped with his girlfriend Kozai two months ago."
    ],
    25: [
        "Ayase: Yosuke as in that Naito Yosuke?",
        "Ayase: Like, didn't he elope with his girlfriend Kozai two months ago?"
    ],
    26: [
        "Nanjo: ...To think that idiot would act on her own in this situation.",
        "Nanjo: <FF0F>あ, let us chase Sonomura."
    ],
    27: [
        "Nanjo: ...<FF0F>あ. Do you not think Sonomura's behavior is strange for amnesia?",
        "Nanjo: Is this really half a year ago...? That girl certainly came to call for Sonomura, but...",
        "Nanjo: Even half a year ago, Sonomura was hospitalized."
    ],
    28: ["Mark: ...Naito" + P('ほ') + ", huh... ...I see. ...O-Oh, what is it, <FF0F>あ?"],
    29: [
        "Elly: Time slip... <FF07>あ, do you believe it is true?",
        "Elly: I feel like it is something else."
    ],
    30: [
        "Brown: Still, is this really the school? Isn't it somewhere different?",
        "Brown: I know! It's a dream, a dream! Wahaha."
    ],
    31: [
        "Ayase: A time strip, is that like a new custom or something~? Is it popular?",
        "Ayase: If so, that's super bad! Is Ayase falling behind the trend?"
    ],
    32: ["Student: I think Maki likes Naito-kun. So nice, they make a fitting couple."],
    33: ["Nanjo: Hey, you woman over there. How many days are left until the sports festival?"],
    34: ["Student: Still as rude as always. It's one month until the sports festival, isn't it. Do you have amnesia, Nanjo-kun?"],
    35: ["Nanjo: ...The date is the same. Hey, what year am I?"],
    36: ["Student: ...You really have amnesia!? Everyone's a 2nd-year, aren't they. I have to report this to everyone!"],
    37: ["Nanjo: ...The academic year is the same as well. This is becoming increasingly inexplicable."],
    38: [
        "Student: Aha, ahahaha... Somehow, it looked like you guys suddenly appeared.",
        "Student: But it must be my imagination, right! Ahahahaha!"
    ],
    39: ["Mark: ...Hey, isn't this the school gym? The one we wrecked half a year ago..."],
    40: ["Mark: H-Hey, Sonomura!... By Naito, do you mean that guy who went missing two months ago?"]
}

REVIEW = {
    31: "Ayase mishears 'Time slip' as 'Time strip' (タイムストリップ)"
}

if __name__ == '__main__':
    apply('E0', 64, BOXES, REVIEW)
