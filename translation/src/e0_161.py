"""E0 entry 161 - Child Maki explains Pandora and the three compacts."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Maki's Mother: Maki-chan... Maki-chan, is that you!?"],
    1: ["Maki: Waaaaaaaah!! Mama!!"],
    2: ["Maki's Mother: I'm sorry, Maki-chan. I'm so sorry..."],
    3: ["Maki: Mama!! Mama!! Waaaaaaaaaah!!"],
    4: ["Mark: Feeling calmer?"],
    5: ["Maki: ...Yes."],
    6: [
        "Mark: Hey, Maki-chan. We wanna save Sonomura. Can you do anything, Maki-chan?",
        "Mark: It's kind of a strange thing to ask, though."
    ],
    7: ["Maki: No... I can't do anything about it."],
    8: ["Nanjo: Why? You are the same Sonomura, are you not?"],
    9: [
        "Maki: Aki is trying to erase this world...",
        "Maki: Aki went to the worst me."
    ],
    10: ["Mark: There's still another Sonomura!?"],
    11: [
        "Maki: The worst me is called Pandora...",
        "Maki: Aki undid Pandora's seal.",
        "Maki: Aki, swallowed by Pandora, is trying to erase this world. Even the real me will die..."
    ],
    12: ["Reiji: ..." + P('で') + " Where is that Pandora?"],
    13: ["Elly: What's that!? Where is that Pandora!?"],
    14: ["Elly: What is that!? Where is that Pandora?!"],
    15: ["Brown: What!? Where is that Pandora thing!?"],
    16: ["Ayase: Seriously!? Where is that thing!?"],
    17: [
        "Nanjo: The school! Behind that door in the library. Right?"
    ],
    18: [
        "Maki: Yes. But to go in there you need three compacts...",
        "Maki: and the strength of the lively me."
    ],
    19: [
        "Nanjo: The lively... You mean the ideal Sonomura?",
        "Nanjo: And the three compacts are the ones we have, I take it?"
    ],
    20: [
        "Reiji: <FF0F>あ, you had two, right? Red and green... One's missing."
    ],
    21: [
        "Elly: <FF07>あ-kun, you had two, correct? Red & Green...",
        "Elly: One more is missing."
    ],
    22: [
        "Elly: <FF07>あ, you had two, didn't you? Red & Green...",
        "Elly: One more is missing."
    ],
    23: ["Brown: <FF08>あ, didn't you have two? Red and green... One's missing."],
    24: ["Ayase: <FF08>あ, didn't you have some? Red and green? One's missing."],
    25: ["Ayase: <FF0F>あ, didn't you have some? Red and green? One's missing."],
    26: ["Nanjo: Where are the last compact and the ideal Sonomura?"],
    27: [
        "Maki: First, please help the lively me... The bad one is me, after all...",
        "Maki: The lively me is crying deep in this forest..."
    ],
    28: ["Maki's Mother: Is Maki beyond this door too?... I'm going as well!"],
    29: [
        "Mark: We've come this far. Okay, everyone? Let's go, <FF0F>あ."
    ],
    30: ["Maki: I'm sorry, me."],
    31: [
        "Maki: No, it's okay. I'm the one who should apologize... I'm sorry, me.",
        "Maki: I'm the ideal Sonomura Maki. I can't keep being gloomy.",
        "Maki: Now, tell me where the last compact is."
    ],
    32: ["Maki: Yes. The third compact is held by the real me."],
    33: [
        "Mark: The real Sonomura? The real Sonomura's is the green one, right?",
        "Mark: <FF0F>あ has it, right?"
    ],
    34: [
        "Maki: That's the one from the real world. Right now the real me's consciousness has come to Araya's Rock Cave.",
        "Maki: The last one is held by the real me's consciousness."
    ],
    35: ["Maki: Araya's Rock Cave?"],
    36: ["Maki: It's behind the shrine."],
    37: ["Maki's Mother: I'll go too..."],
    38: ["Maki: Mama, wait here, please."],
    39: ["Maki's Mother: Why? Why not, Maki-chan!?"],
    40: [
        "Maki: From here on I want to do it myself... I have friends who will help me.",
        "Maki: I'll be okay."
    ],
    41: ["Maki's Mother: Maki-chan... I understand. Make sure you come back."],
    42: ["Maki: Take care of Mama, me."],
    43: [
        "Maki: Yes... Be careful, me.",
        "Maki: When you have all three compacts, say the spell in front of Pandora's door.",
        "Maki: Then the door will open."
    ],
    44: ["Nanjo: Then shall we go? To Araya Shrine."],
    45: [
        "Maki: Mai-chan is me too, isn't she..." + P('キ') + " I was cute even when I was little, huh.",
        "Maki: Don't say that myself, you say? Hee hee."
    ],
    46: [
        "Mark: Man, my head's getting all tangled.",
        "Mark: How many Sonomuras are there, anyway?"
    ],
    47: [
        "Mark: Heh heh... Sonomura was cute even when she was little, huh."
    ],
    48: ["Nanjo: Deeper beyond this, then... Hurry, <FF0F>あ."],
    49: [
        "Nanjo: Hm. Truly a dialogue with oneself. A strange sight."
    ],
    50: [
        "Reiji: ...What?" + P('キ') + " I have a \"kind face\"?",
        "Reiji: Save the jokes for your own face."
    ],
    51: [
        "Reiji: ...What? \"The corners of my mouth are smiling\"!?",
        "Reiji: Don't get the wrong idea! My cavity hurts."
    ],
    52: [
        "Elly: Hee hee. Children calm down the most when they cry on Mama's chest.",
        "Elly: <FF07>あ, do you like homely women too?"
    ],
    53: [
        "Elly: Hee hee. Children calm down the most when they cry on Mama's chest, do they not?",
        "Elly: <FF07>あ, do you like homely women too?"
    ],
    54: [
        "Elly: I was very cute when I was little, too. Want to see a photo sometime?"
    ],
    55: [
        "Elly: I was very cute when I was little, too. Would you like to see a photo sometime?"
    ],
    56: [
        "Brown: Little Maki-chan's cute too, huh. But say it was Nanjo or Mark instead?",
        "Brown: They'd be not cute at all. I'd probably punch them!"
    ],
    57: [
        "Brown: I was super cute as a kid too! The big sisters in the neighborhood adored me!",
        "Brown: No lie! When I walked around, they'd wipe my nose for me."
    ],
    58: [
        "Ayase: Hey, hey, <FF0F>あ, what kind of kid were you? Ayase was super cute.",
        "Ayase: But if you imagine Nanjo or Uesugi, don't they seem kinda hateful?"
    ],
    59: [
        "Ayase: Hey, <FF08>あ, what kind of kid were you? Ayase was super cute.",
        "Ayase: But if you imagine Nanjo or Uesugi, don't they seem kinda hateful?"
    ],
    60: [
        "Ayase: Um, so, Little Sonomura and the ideal Sonomura, right?",
        "Ayase: And the real Sonomura...",
        "Ayase: <FF0F>あ~, my head's starting to hurt."
    ],
    61: [
        "Ayase: Um, so, Little Sonomura and the ideal Sonomura, right?",
        "Ayase: And the real Sonomura...",
        "Ayase: <FF08>あ~, my head's starting to hurt."
    ],
    62: ["Maki: The ideal me is crying deep in here..."],
    63: ["Maki: The real me can only be saved by the ideal me..."],
    64: ["Maki's Mother: To think that girl was the ideal Maki... Maki..."],
    65: [
        "Maki's Mother: Huh? Nomoraka tanomama?",
        "Maki's Mother: Ah..." + P('キ') + " That's a charm I taught Maki when she was little.",
        "Maki's Mother: Her father died early and I was busy with work, so Maki was always alone...",
        "Maki's Mother: So I told her, when you're lonely alone in the hospital, say this spell.",
        "Maki's Mother: Then Mama will feel Maki-chan no matter where she is, I said.",
        "Maki's Mother: She remembered it..." + P('キ') + " Please try saying it backwards. This child is my treasure."
    ],
}
REVIEW = {65: "ノモラカ・タノママ reversed = ママのたからもの (Mama's treasure); hint left as 'say it backwards'"}

if __name__ == '__main__':
    apply('E0', 161, BOXES, REVIEW)
