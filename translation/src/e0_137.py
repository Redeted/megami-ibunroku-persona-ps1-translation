"""E0 entry 137 - Hariti; Maki's mother from the other world."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Mark: Tch! So it was a trap after all! <FF0F>あ, let's go!"],
    1: ["Hariti: Maki...?" + P('み') + " Maki, I finally found you. You're safe..."],
    2: ["Nanjo: As I thought, that voice..." + P('み') + " Sonomura's mother...!"],
    3: [
        "Hariti: Mother has been looking for you all this time..." + P('ぎ') + " Come," + P('な') + " Maki," + P('な') + " to Mother..."
    ],
    4: [
        "Elly: Maki!" + P('た') + " ...No, she seems to be controlled by that Demon...",
        "Elly: The voice does sound like Maki's mother," + P('み') + " but we cannot trust it!",
        "Elly: <FF07>あ, let us fight!"
    ],
    5: [
        "Brown: Hey, is this okay?! <FF08>あ!",
        "Brown: Maki-chan's gonna get killed by that thing! We gotta beat it fast!"
    ],
    6: [
        "Ayase: Hey, is this okay, <FF0F>あ!?",
        "Ayase: Sonomura might get killed by that monster! Let's hurry and take it out!"
    ],
    7: [
        "Reiji: You're going to leave Sonomura alone, <FF0F>あ?",
        "Reiji: We have to defeat that demon!"
    ],
    8: [
        "Mark: But, man, that voice is definitely Sonomura's mom's voice. Right?",
        "Mark: I don't know why she's dressed like that, but what if she's really her mom...?",
        "Mark: <FF0F>あ, don't fight her!"
    ],
    9: ["Nanjo: ..." + P('た') + " ..." + P('た') + " ..." + P('た') + " ..." + P('た') + " ..."],
    10: "=What will you do?<FF03><FF0E>つ<FF01>",
    11: [
        "Hariti: Why are you getting in my way...?",
        "Hariti: Give me back my daughter!"
    ],
    12: [
        "Maki's Mother: Ah..." + P('み') + " Where is this..." + P('み') + " Isn't this the infirmary...?",
        "Maki's Mother: Oh my, isn't this the haunted house? I was just dreaming about it."
    ],
    13: [
        "Mark: There's no Sonomura's mom in this world, so...",
        "Mark: ...She's the real one! But why are you in a place like this..." + P('み') + " Ma'am, are you okay?"
    ],
    14: [
        "Maki's Mother: Yes, I'm fine... When Maki was little, she often got lost in the haunted house and I'd come looking for her. That was the dream.",
        "Maki's Mother: While searching alone in this big mansion, I heard Maki calling... I don't remember anything after that."
    ],
    15: [
        "Maki: Um, ma'am... I'm really not your child."
    ],
    16: ["Maki's Mother: What...?"],
    17: ["Nanjo: Allow me to explain in order."],
    18: [
        "Maki's Mother: I see..." + P('み') + " You're this world's Maki.",
        "Maki's Mother: But why is there no me in this world...?"
    ],
    19: ["Maki: Ah! The dimensional passage is disappearing...!"],
    20: [
        "Mark: Ma'am, we have to chase after Kandori."
    ],
    21: ["Maki's Mother: I understand. Please wait a moment!"],
    22: [
        "Maki's Mother: This dimensional passage is in a very unstable state.",
        "Maki's Mother: Someone has to stay here and operate the machine."
    ],
    23: [
        "Maki: Does someone have to stay?",
        "Maki: No, we can't leave anyone behind!"
    ],
    24: [
        "Maki's Mother: I'll do it! I'll keep the passage stable, so don't worry. Go on.",
        "Maki's Mother: Though, once everything is over, I'd be glad if you came to pick me up."
    ],
    25: ["Maki: Ma'am..."],
    26: ["Maki's Mother: What is it? We have no time, hurry."],
    27: [
        "Maki: I don't have a mother, but...",
        "Maki: If I had a kind mother like you," + P('み') + " that would have been nice..."
    ],
    28: [
        "Maki: Once we defeat Kandori, we'll surely find your \"Maki-chan\" for you!"
    ],
    29: [
        "Maki's Mother: ..." + P('た') + " ..." + P('た') + " ..." + P('た') + " ..." + P('た') + " ..." + P('た') + " Yes, I'm sure you will." + P('ぶ') + " Thank you..."
    ],
    30: ["Nanjo: ..............."],
    31: [
        "Maki's Mother: Everyone, off you go! Be careful!"
    ],
}
REVIEW = {}

if __name__ == '__main__':
    apply('E0', 137, BOXES, REVIEW)
