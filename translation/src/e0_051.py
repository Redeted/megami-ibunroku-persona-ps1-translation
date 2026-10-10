"""E0 entry 51 - Subway entrance / Elly."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Maki: Ah, Elly! Wow, I'm so glad. How have you been?"],
    1: [
        "Elly: ..." + P('み') + " Maki? When were you discharged from the hospital?",
        "Elly: Oh, now is not the time to be saying such things. Above all else, I am glad you are safe."
    ],
    2: ["Mark: So this place is no good either..."],
    3: [
        "Elly: Yes..." + P('な') + " I tried looking around just in case, but every path underground is blocked.",
        "Elly: It does not seem like we can go outside at all."
    ],
    4: [
        "Brown: It's dangerous if you stay in a place like this, right?",
        "Brown: The great me'll solve this in a jiffy.",
        "Brown: So until then, wait in a safe place somewhere!"
    ],
    5: [
        "Ayase: Hey, it's dangerous by yourself!",
        "Ayase: Wouldn't it be better if you went somewhere safe?"
    ],
    6: [
        "Elly: I know... But since I am here, I will try exploring the town a little more.",
        "Elly: Then, please be careful."
    ],
    7: ["Elly: Thank you. But I will be fine by myself." + P('な') + " Well then."],
    8: ["Elly: And everyone? Are there any new developments?"],
    9: ["Mark: Oh, yeah. It's a long story, but actually since then..."],
    10: [
        "Elly: I see..." + P('な') + " What!? So that is what happened! It is a shame I could not see it...",
        "Elly: But, we are only just beginning. There should still be chances for me as well!",
        "Elly: Say, <FF07>あ, won't you bring me along as well? There are various things I wish to investigate."
    ],
    11: "=Please, bring me along!<FF03><FF0E>き<FF01>",
    12: ["Elly: Oh, I am so glad! I will do my best!"],
    13: [
        "Nanjo: Then, Kirishima. I will hand a gun over to you as well.",
        "Nanjo: ...I am reluctant to give a gun to a woman, but it cannot be helped in this state of emergency."
    ],
    14: ["Maki: What business did they have in the subway?"],
    15: [
        "Brown: Ma~rk, it'd have been better if you went somewhere else.",
        "Brown: The great me prefers Elly over you."
    ],
    16: [
        "Nanjo: The subway is no good as well... In the end, it means we cannot escape from this town."
    ],
    17: ["Mark: Elly's got some guts too, huh..."],
    18: ["Elly: To think I would be able to experience such a thing..." + P('な') + " I am so glad."],
    19: ["Ayase: Ahh, what's gonna happen to us?"]
}
REVIEW = {
    6: "I know... kept as Elly's English text since it's I know in the Japanese.",
    8: "Missing speaker label in Japanese, but the speech style is clearly Elly's."
}

if __name__ == '__main__':
    apply('E0', 51, BOXES, REVIEW)
