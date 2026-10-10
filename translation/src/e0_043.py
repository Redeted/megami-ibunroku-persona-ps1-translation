"""E0 entry 43 - Heading for the police with Maki; first demon encounter."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Maki: We've got to hurry!" + P('で') + " By the way, what was \"the police\" again?"],
    1: ["Nanjo: ...Is this a time to be joking?"],
    2: ["Maki: How rude! I'm not joking around!"],
    3: ["Nanjo: ...It is a public institution that maintains the order of society. Well, in this case, it refers to the building where they are stationed."],
    4: ["Maki: Ah... I think I'm starting to remember something... maybe?"],
    5: ["Maki: Ahh! What's that gym behind us! When did it become new!?"],
    6: ["Nanjo: ...It was while you were in the hospital. It was completed about half a year ago. It is no wonder you do not know."],
    7: ["Maki: Not that again! I told you, I wasn't in any hospital! Aren't you the ones who are joking around?"],
    8: ["Nanjo: ..." + P('ょ') + " Hey, <FF0F>あ. Could this girl have amnesia? Like this, she will only be a burden."],
    9: ["Maki: What are you two fussing about? If we don't hurry, Inaba-kun is in danger!"],
    10: ["Demon: Hya hya hya! The ones in danger are you! I'll eat you all up!"],
    11: ["Maki: They showed up right away! Fine, let's do it!"],
}
REVIEW = {
    0: "ケーサツ (katakana, casual) rendered as 'the police'; Maki's amnesia gag, 警察 = police station in 42/24",
    3: "Nanjo defines 警察 as the institution and, here, the building where they are stationed",
}

if __name__ == '__main__':
    apply('E0', 43, BOXES, REVIEW)
