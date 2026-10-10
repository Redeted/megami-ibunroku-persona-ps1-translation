"""E0 entry 29 - Returning from the shrine."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Yukino: What was that just now... A dream...?"],
    1: ["Nanjo: Truth is stranger than fiction... Well said."],
    2: ["Elly: I have had yet another precious experience..."],
    3: ["Maki's Mother: Ugh... Ooh..."],
    4: [F6('う') + "Maki's Mother<FF03>Maki's mother, who works at SEBEC. An elite engineer." + F6(0)],
    5: ["Mark: H-hey! You're forgetting Sonomura's mom."],
    6: ["Yukino: Ma'am! Are you okay?"],
    7: ["Nanjo: This wound is a gunshot. Just who did this to you?"],
    8: ["Maki's Mother: Kandori's... underlings..."],
    9: ["Nanjo: Kandori!? That Kandori from SEBEC?"],
    10: [
        "Maki's Mother: The strange incidents in town... they are all Kandori's doing...",
        "Maki's Mother: I... was involved in the development of a certain machine as an engineer."
    ],
    11: ["Nanjo: A machine... And that machine is the cause of these strange incidents?"],
    12: [
        "Maki's Mother: The Deva System... It's something that brings about artificial effects on space...",
        "Maki's Mother: To think it would produce such a result... Kandori... He said he didn't care what happened to the town...",
        "Maki's Mother: I have to hurry and tell the police..."
    ],
    13: [
        "Elly: We have a problem... The Police station is already a den of Demons.",
        "Elly: I saw it just a while ago."
    ],
    14: ["Maki's Mother: Oh no... Someone has to stop Kandori..."],
    15: ["Mark: ...Ma'am, how did you get away?"],
    16: ["Maki's Mother: The abandoned factory... it serves as a secret loading entrance. With this \"security card\"..."],
    17: [
        "Yukino: Ma'am! ...Thank goodness, she just fainted. We need to hurry and take her to the school!"
    ],
    18: ["Mark: ...<FF0F>あ, I'll leave the rest to you. I'm gonna go rough 'em up a bit."],
    19: [
        "Nanjo: Wait, Inaba. One cannot catch a tiger cub without entering the tiger's den. I will go too.",
        "Nanjo: Besides, we will not be able to get close to Kandori without this card."
    ],
    20: [
        "Yukino: H-hey! ..." + P('キ') + " Geez! It can't be helped. It'll just be us heading back to the school!",
        "Yukino: Honestly, boys! They never think about the feelings of the ones left behind."
    ],
    21: [
        "Elly: Their recklessness is quite similar, isn't it? Well, they will likely give up and come back after checking things out for a bit."
    ],
    22: ["Butterfly: If you are hurt before returning to the school, come back. I shall grant you strength..."],
    23: [
        "Yukino: Anyway... What in the world is this butterfly?",
        "Yukino: I guess there's no point in thinking about it... Anyway, let's hurry back to the school."
    ],
    24: ["Elly: What a mysterious butterfly. Don't you get the feeling it's looking deep into your heart?"],
    25: ["Butterfly: Wounded young ones... Close your eyes..."],
    26: ["She seems to be unconscious."]
}

if __name__ == '__main__':
    apply('E0', 29, BOXES)
