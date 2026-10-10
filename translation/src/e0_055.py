"""E0 entry 55 - SEBEC abandoned factory / Ayase joins."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: [
        "Nanjo: So it is here. A secret loading bay hidden from the world.",
        "Nanjo: An idea typical of a petty villain like Kandori."
    ],
    1: [
        "Maki: Hey, hey. They say Inaba-kun drew this.",
        "Maki: It's really good, he has talent, doesn't he?"
    ],
    2: ["Elly: Mark did Graffiti art? He is surprisingly an Artist, is he not."],
    3: [
        "Brown: You think so? Ain't it super lame?",
        "Brown: The great me would spray it much better."
    ],
    4: ["Mark: Heh. As expected, Sonomura and Elly have a good eye for this."],
    5: ["Mark: Whaat!? Don't you complain about my art!"],
    6: ["Nanjo: Wait a minute." + P('キ') + " You... So you came here often, did you?"],
    7: ["Mark: Oh yeah! This is the studio for me and my pals, the \"Tailors\"."],
    8: [
        "Nanjo: ...You made this your hangout, yet you did not notice at all that SEBEC was using it?"
    ],
    9: ["Elly: ...I cannot believe it. Unbelievable!"],
    10: ["Brown: No way! As expected of Mark. Yo! Idiot general!"],
    11: [
        "Mark: Shaddap!! This is what you call, uh, \"the lighthouse waves are high\"!"
    ],
    12: ["Nanjo: It is \"it is dark at the base of the lighthouse\"! You fool!"],
    13: [
        "Maki: Ahahaha! Geez, it's fine, isn't it.",
        "Maki: Let's hurry and look for the entrance."
    ],
    14: ["Elly: Quiet! Someone is here..."],
    15: [
        "Brown: H-Hey... Something's... here, ain't it?",
        "Brown: Mark... go see what's up."
    ],
    16: ["Mark: Something's here!! Who is it? Come out!"],
    17: [
        "Ayase: Could it be... <FF0F>あ and the others...?",
        "Ayase: Hey, don't scare Ayase."
    ],
    18: ["Nanjo: Ayase? What are you doing here?"],
    19: [
        "Elly: Ayase, for you to be walking around alone in this situation...",
        "Elly: Did something happen at the school?"
    ],
    20: [
        "Brown: Ayase, are you alone?",
        "Brown: Ayase being alone in this situation is super unbelievable."
    ],
    21: [
        "Ayase: What? Even though Ayase barely escaped with her life...",
        "Ayase: Don't you have any kinder words for Ayase?"
    ],
    22: ["Maki: Barely escaped with your life... Yuka, did something happen at the school!?"],
    23: [
        "Ayase: Geez, it's the worst. Who was it that told a huge lie that the school was safe?",
        "Ayase: The school is completely gone!"
    ],
    24: [
        "Maki: No way!? What happened to Yuko and everyone else?",
        "Maki: You ran away alone!? Yuka!"
    ],
    25: [
        "Ayase: There's no way Ayase would know!",
        "Ayase: Ayase's the one who wants to ask what's going on!"
    ],
    26: ["Maki: <FF07>あ-kun! We have to go save everyone quickly!"],
    27: [
        "Nanjo: Calm down, Sonomura. The school disappearing is also likely the influence of the Deva System.",
        "Nanjo: If so, making Kandori revert it would be faster."
    ],
    28: [
        "Ayase: Ayase's tagging along too!",
        "Ayase: Being alone in a place like this is seriously bad!"
    ],
    29: [
        "Elly: ...I am against it. It is safer to stay hidden somewhere, Ayase."
    ],
    30: [
        "Nanjo: Kirishima's words are likely correct.",
        "Nanjo: Without a Persona, you are only in danger. Stay hidden somewhere."
    ],
    31: [
        "Brown: Having Ayase around won't bring anything good.",
        "Brown: The great me, the leader, doesn't approve."
    ],
    32: [
        "Nanjo: Setting aside the idiot, without a Persona, you are only in danger.",
        "Nanjo: Stay hidden somewhere."
    ],
    33: [
        "Ayase: What! Stingy! Everyone making a fool of Ayase!",
        "Ayase: Fine, idio~ts, drop dead!"
    ],
    34: ["Mark: Ayase, huh."],
    35: ["Ayase: Yay! As expected of <FF0F>あ! You really get it!"],
    36: ["Nanjo: I will hand a gun over to you. Do not become a burden."],
    37: ["Maki: Then it's decided. Let's split up and look for the entrance!"],
    38: ["Mark: You're coming too? Stay hidden somewhere."],
    39: [
        "Ayase: No way, no way, no way, no way, no way! If Ayase says she's going, she's going!",
        "Ayase: No way, no way, no way, no way, no way, no waay!"
    ],
    40: ["Maki: Yuka, I get it already! Everyone, it's fine, right?"],
    41: ["Mark: Tch, can't be helped."],
    42: [
        "Nanjo: Now then. There should be a machine that uses the \"security card\" somewhere.",
        "Nanjo: Let us split up and search."
    ],
    43: [
        "Mark: Hehehe. I drew this with spray paint. It's called Graffiti art.",
        "Mark: It's the shout of my soul."
    ],
    44: [
        "Maki: Both this town and everyone, it's all kinda strange...",
        "Maki: Ah? W-What?",
        "Maki: It doesn't seem to be this way."
    ],
    45: [
        "Brown: <FF08>あ. If anything happens, let me know right away.",
        "Brown: After all, the great me is the leader!"
    ],
    46: ["Elly: I cannot see any Machine that uses a Card."],
    47: ["Maki: ...I kinda feel sorry for Yuka."],
    48: [
        "Nanjo: Kandori... Ever since I first met him at the financial world's party, I had thought him to be a scheming man, but...",
        "Nanjo: To think he would be this bold."
    ],
    49: [
        "Nanjo: Ayase? What are you doing here?",
        "Nanjo: It is rare for you to be alone."
    ],
    50: [
        "Ayase: <FF0F>あ, Ayase's tagging along with you guys.",
        "Ayase: It's super lucky, you know?"
    ],
    51: [
        "Maki: <FF07>あ-kun, where are you going?",
        "Maki: Let's hurry and look for the entrance."
    ],
    52: [
        "Maki: Yuka!? What in the world happened to the school? And Yuko and everyone else?",
        "Maki: You ran away alone!? Yuka!"
    ],
    53: [
        "Ayase: There's no way Ayase would know!",
        "Ayase: Ayase's the one who wants to ask what's going on!"
    ],
    54: [
        "Nanjo: Calm down, Sonomura. The school disappearing is also likely the influence of the Deva System.",
        "Nanjo: If so, making Kandori revert it would be faster."
    ],
    55: "=What will you do?<FF03>Will you bring her along?<FF03><FF0E>き<FF01>",
    56: ["Discovered the machine that uses the \"security card\"!"],
    57: ["Mark: <FF0F>あ. Did you find something?"],
    58: ["Mark: Ah! Damn it. It was in a place like that!"],
    59: ["Nanjo: What is it?"],
    60: [
        "Mark: <FF0F>あ found the machine to use the card.",
        "Mark: Hey, <FF0F>あ. Hurry up and try using it."
    ],
    61: ["Nanjo: Wait. Since we do not know what will happen, you should think carefully..."],
    62: ["Mark: Doesn't matter. Here, let me see."],
    63: ["Mark: Ororororororo?"],
    64: ["Nanjo: I told you to wait!"],
    65: ["Maki's Voice: W-What? The lights are acting strange?"]
}
REVIEW = {
    11: "Mark misuses the idiom toudai-moto-kurashi ('dark at the base of the lighthouse') as toudai-nami-takashi ('the lighthouse waves are high'). Translated literally.",
    63: "Ororororororo? (flustered/dizzy sound)",
    55: "Choice prompt: =What will you do? Will you bring her along?"
}

if __name__ == '__main__':
    apply('E0', 55, BOXES, REVIEW)
