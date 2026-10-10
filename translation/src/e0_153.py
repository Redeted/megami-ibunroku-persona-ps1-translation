"""E0 entry 153 - the mirror stops working; trying Kandori's mirror."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: [
        "Mark: H-Hey... It's gone!!",
        "Mark: What do we do!? We can't go back like this!!"
    ],
    1: [
        "Nanjo: ........." + P('キ') + " Something must have happened in the town in Sonomura's heart.",
        "Nanjo: With Kandori gone, she is the only one who could do this."
    ],
    2: ["Reiji: ..." + P('キ') + " What about Kandori's mirror? We could just order it to send us back."],
    3: [
        "Elly: Mark! If we make a wish to Kandori's mirror, couldn't we go to that town!?"
    ],
    4: [
        "Brown: That's it!! We still have Kandori's mirror!! Just wish on it!",
        "Brown: Tell it to send us to that town!!"
    ],
    5: [
        "Ayase: Hey, what about Kandori's mirror!? Just wish on it!",
        "Ayase: Tell it to take us to that town!"
    ],
    6: ["Mark: Why didn't I think of that!!"],
    7: ["Mark: Whoa!? W-What the...!?"],
    8: [
        "Nanjo: ..." + P('で') + " Is Sonomura refusing it!?",
        "Nanjo: I cannot think of anything else."
    ],
    9: ["Mark: Damn it!! What do I do... what do..." + P('ヌ') + " Huh?"],
    10: [
        "Mark: This... Did Sonomura drop it..." + P('キ') + " Leaving only this behind is no use..."
    ],
    11: ["Nanjo: What is it, Inaba?"],
    12: ["Mark: It's Sonomura's compact..."],
    13: ["Nanjo: The mirror is not set in it..."],
    14: ["Reiji: Hey. This world's Sonomura has a compact on her, too."],
    15: ["Elly: Hey! The Original Maki has a Compact too!"],
    16: ["Brown: Hey! The real Maki-chan has a compact too!?"],
    17: ["Ayase: Ah!! The real Sonomura has a compact too!!"],
    18: [
        "Nanjo: Let me see..." + P('キ') + " The real Sonomura's compact and the ideal Sonomura's compact...",
        "Nanjo: The real one has the mirror set in it..."
    ],
    19: ["Mark: Nanjo, lend it here!"],
    20: "=Mark: Please!!<FF03>Send us back into<FF03>Sonomura's heart!<FF02><FF03>..." + "".join(P('ほ') + " ..." for _ in range(13)) + P('ほ') + "<FF02><FF01>",
    21: [
        "Nanjo: A real compact surely cannot have such power... If at least the ideal Sonomura's compact were complete, there might have been a chance..."
    ],
    22: [
        "Mark: Maki... Everyone's waiting, you know? You don't have to suffer alone.",
        "Mark: Please, call us... I'll go anywhere..."
    ],
    23: [
        "Nanjo: The ideal Sonomura's existence is the expression of a desire to change herself. But that ideal heart itself denied her own existence...",
        "Nanjo: Sonomura... have you truly lost hope?",
        "Nanjo: If even a fragment remains, call us..."
    ],
    24: [
        "Reiji: Sonomura!! Don't run away! Running away is easy...",
        "Reiji: My mother was Kandori's old man's woman... She was thrown away like a rag.",
        "Reiji: Mother gave birth to me, prepared to be abandoned. Know why?",
        "Reiji: Mother said, you can't treat your own child's life carelessly.",
        "Reiji: You have a mother too. No parent doesn't love their child. Go home to your mother.",
        "Reiji: Hurry up and wake up!"
    ],
    25: [
        "Elly: Maki! Please wake up! Please...",
        "Elly: You are not the only one suffering from having many selves...",
        "Elly: Everyone says I am refined or beautiful, but that is not true...",
        "Elly: I have been putting on an act all along. When boys talk about other girls, I cannot stand it.",
        "Elly: So I always smiled falsely... It was very stifling. I am a nasty girl, am I not?",
        "Elly: But I understood. What matters is friends you can open your heart to. Everyone here, too...",
        "Elly: I have someone I like now. Probably the same person as Maki... Please, wake up...",
        "Elly: Let us chat about that person and many other things, all right? Please..."
    ],
    26: [
        "Brown: Wake up, Maki-chan! I'll tell you my best funny story!",
        "Brown: You know me as Brown, right? It's a nickname I got in middle school...",
        "Brown: Everyone thinks it's because of my brown hair, but..." + P('ソ') + " actually, it's because I crapped my pants.",
        "Brown: Funny, right? Seriously. Pathetic, huh? In middle school! I became the laughingstock of the whole school...",
        "Brown: I was so frustrated and miserable... I came to Hermelin because I couldn't stay in my hometown.",
        "Brown: So once I got in high school, I made up a self and did my best to look cool... I was fooling myself the whole time.",
        "Brown: But I'm done with that. Watching Maki-chan made me feel like an idiot.",
        "Brown: Come on, laugh. Please..."
    ],
    27: [
        "Ayase: Wake up, Sonomura! I've still got your handkerchief! Ayase will listen to you...",
        "Ayase: Ayase gets how Sonomura feels. Ayase has thought it too: I wish the future would just disappear...",
        "Ayase: I think I was acting like an idiot because I was scared about the future. Thinking about it brings you down, right?",
        "Ayase: So I think I was running away, saying as long as now is good, it's fine. But that's not it, is it...",
        "Ayase: It's my own future, so I have to decide it myself. Ayase decided.",
        "Ayase: I'll catch a good guy and live an easy life! Sonomura... tell me your dreams too... Please..."
    ],
    28: ["There is a shard of the Mirror of Chaos!"],
    29: "=Pick it up?<FF03><FF0E>　<FF01>",
    30: [
        "Nanjo: What is it, <FF0F>あ?" + P('キ') + " A shard of Kandori's mirror!?",
        "Nanjo: This size, this shape... It looks like it would fit Sonomura's compact!"
    ],
    31: [
        "Mark: Really!? Maybe we can go back with that! Lend it here, <FF0F>あ!"
    ],
    32: ["Mark: It fits perfectly!!" + P('キ') + " Whoa!?"],
    33: ["Obtained a \"Mirror Shard\"!"],
    34: ["The real Maki won't wake up... It's as if she's dead..."],
    35: [
        "Nanjo: Where are you going? Are you going to leave Sonomura like this?"
    ],
    36: ["Obtained the \"Green Compact\""],
    37: ["Obtained the \"Broken Compact\""],
    38: [
        "The \"Mirror of Chaos\" is cracked...",
        "What on earth happened in the town in Maki's heart..."
    ],
    39: [
        "It is Maki's painting, \"The Door to Paradise.\" With what feelings did Maki paint this picture?"
    ],
    40: [
        "It is a hologram of the Deva System. It seems Maki is directly connected to the system."
    ],
}
REVIEW = {}

if __name__ == '__main__':
    apply('E0', 153, BOXES, REVIEW)
