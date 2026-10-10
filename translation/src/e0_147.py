"""E0 entry 147 - confrontation with Kandori: why do you live?"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: [
        "Mark: Kandori! I won't let you get away again! Prepare yourself!!"
    ],
    1: ["Reiji: ..." + P('で') + " Finally found you... You're not getting away anymore!"],
    2: ["Aki: So persistent!! Aki won't let you get in Papa's way!!"],
    3: ["Kandori: ..." + P('で') + " Stop, Aki. Step back."],
    4: ["Aki: But, Papa..."],
    5: ["Kandori: Wait in that room. I will join you soon."],
    6: ["Aki: ..." + P('で') + " Okay."],
    7: ["Maki: Stop making people suffer! Put everyone back the way they were!"],
    8: [
        "Kandori: ..." + P('で') + " Do not worry. I will do nothing further. Now...<FF05><B4><00> nothing matters anymore."
    ],
    10: [
        "Brown: What do you mean!? Don't you suddenly seem to have lost your drive?",
        "Brown: We came all fired up, so that's not fair."
    ],
    11: ["Elly: Why!? He is acting strange."],
    12: [
        "Ayase: Hey! Did you chicken out? Apologizing now won't help, you know!",
        "Ayase: Ayase is super pissed off!"
    ],
    13: [
        "Reiji: ..." + P('で') + " What are you up to? Are you begging for your life now?"
    ],
    14: ["Kandori: ..." + P('で') + " What do you live for?"],
    15: ["Mark: What did you say!?"],
    16: [
        "Kandori: ...People are not strong enough to live without goals.",
        "Kandori: Everyone is surely seeking something, no matter how trivial. That is exactly why they can live desperately.",
        "Kandori: But..." + P('で') + " once everything is fulfilled, what should one seek next?",
        "Kandori: Continuing to fulfill one's own wishes and climbing to the heights, what lies beyond is... only endless emptiness and solitude.",
        "Kandori: Then would it not be better not to climb the stairs one set for oneself? If so...",
        "Kandori: one could go on dreaming forever."
    ],
    17: [
        "Kandori: I kept climbing the stairs in order to destroy this worthless world...",
        "Kandori: But now it no longer matters. For me now... nothing is impossible.",
        "Kandori: Heh..." + P('で') + " A wind of solitude and emptiness rages. Is this what they call the realm of gods?"
    ],
    18: ["Maki: ..."],
    19: [
        "Kandori: Boy." + P('キ') + " That is also why I let you come this far, to ask that.",
        "Kandori: What do you all live for?"
    ],
    20: "=For what reason do you live?<FF03><FF0E>そ<FF01>",
    21: [
        "Maki: That's right! What we live for...",
        "Maki: We may never know." + P('キ') + " But! I believe in myself!",
        "Maki: I'll live without regrets!"
    ],
    22: [
        "Maki: No, no! What we live for...",
        "Maki: We may never know." + P('キ') + " But! I believe in myself!",
        "Maki: I'll live without regrets!"
    ],
    23: [
        "Mark: Idiot. At your age, you don't know something like that?",
        "Mark: To shine brightly in each and every moment, obviously!",
        "Mark: Your vibe is gloomy. So bad! Be more positive!"
    ],
    24: [
        "Reiji: ..." + P('で') + " Obviously, it's to kill you!",
        "Reiji: That settles things with this filthy blood. Without that, I can't make my mother happy!"
    ],
    25: [
        "Elly: To protect those dear to me! The ones here are my true friends...",
        "Elly: I cannot lose what I have finally obtained!"
    ],
    26: [
        "Brown: To surpass myself! I'm sick and tired of lying and tucking my tail!",
        "Brown: I've decided! I'll beat the old man and say goodbye to my fake self!"
    ],
    27: [
        "Ayase: For my future husband! Ayase's the one who'll struggle in the future.",
        "Ayase: Even a small cute house is fine, and the kids would be a boy and a girl.",
        "Ayase: I'll name them Takuya and Yuki, and then..."
    ],
    28: [
        "Nanjo: Kandori..." + P('で') + " Stop it. It is painful to watch such excessive bluster."
    ],
    29: ["Kandori: What...?"],
    30: [
        "Nanjo: You must have noticed. The place you reached by using people is not the seat of a god.",
        "Nanjo: You have done nothing by yourself..."
    ],
    31: ["Kandori: You..."],
    32: [
        "Nanjo: You are suffering. You despair of yourself, who could only live that way."
    ],
    33: ["Kandori: Silence..."],
    34: [
        "Nanjo: Wishing for humanity's erasure is the same as with her..." + P('キ') + " it comes from anxiety about your own future."
    ],
    35: ["Kandori: Silence!"],
    36: [
        "Nanjo: You want to change" + P('で') + " but cannot. " + P('で') + " You want to disappear...",
        "Nanjo: Did you think that the fear of being alone would grow lighter if all of humanity carried it?"
    ],
    37: ["Kandori: ..."],
    38: [
        "Nanjo: Why not stop justifying your complex with grand pretenses?",
        "Nanjo: You are the one who is most aware of your own absurdity."
    ],
    39: [
        "Kandori: ..." + P('で') + " Your many insults to a god cannot be tolerated.",
        "Kandori: I shall deliver your final rites with my own hands."
    ],
    40: ["Mark: Heh, finally in the mood, huh!"],
    41: ["Kandori: Can you defeat me? Can you protect what you call precious?"],
    42: ["Reiji: ..." + P('で') + " I'll protect my mother and these guys. By killing you."],
    43: ["Elly: Yes! We can do it!"],
    44: ["Brown: Damn right!"],
    45: ["Ayase: Damn right!"],
    46: [
        "Kandori: Then show me! Before the throne of God!"
    ],
    47: ["Kandori: Boy... I have not heard your answer."],
}
REVIEW = {}

if __name__ == '__main__':
    apply('E0', 147, BOXES, REVIEW)
