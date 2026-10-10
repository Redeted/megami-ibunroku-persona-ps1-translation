"""E0 entry 58 - The Deva System."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Kandori: Are the adjustments complete, Dr. Nicolai?"],
    1: [
        "Dr. Nicolai: ...Reconsider this! Mr. Kandori!",
        "Dr. Nicolai: Stop the system and atone for the crimes you have committed!"
    ],
    2: [
        "Kandori: Do not be foolish. The ones who must atone are all of foolish humanity.",
        "Kandori: I am merely their pilot."
    ],
    3: [
        "Dr. Nicolai: There was no need to send that boy earlier into the dimensional rift!",
        "Dr. Nicolai: Just what are you trying to accomplish, going so far as to lay your hands on children!?"
    ],
    4: [
        "Kandori: I will not let anyone interfere. Even if it is..." + P('ス') + " children.",
        "Kandori: " + P('で') + "The hammer of judgment will soon fall. It is merely a difference of sooner or later."
    ],
    5: ["Mark: We ain't lettin' you get away, old man!"],
    6: ["Nanjo: It is time to pay your dues, Kandori!"],
    7: [
        "Kandori: I thought you would come, boy. Was Takeda defeated?",
        "Kandori: He was unexpectedly pathetic as well."
    ],
    8: [
        "Brown: Against the great me, a guy like that was a piece of cake. You better prepare yourself and get caught!",
        "Brown: If you do it now, we might just let you off with life in prison."
    ],
    9: [
        "Elly: A man who does not know when to give up is simply an eyesore.",
        "Elly: Would you please give up already?"
    ],
    10: [
        "Ayase: Ayase is busy, so she can't be dealing with some old man forever!",
        "Ayase: Could you just quietly get caught?"
    ],
    11: [
        "Kandori: Hmph. You truly do bark a lot. Unfortunately, I have no free time to deal with you all.",
        "Kandori: There is something I must do... Come, Dr. Nicolai."
    ],
    12: ["Mark: Wait up!"],
    13: ["Nanjo: Is this the Deva System! What does Kandori plan to do!?"],
    14: ["Maki: ...This machine! I... Why...? Why have I seen it before...?"],
    15: ["Brown: Uwaaaaaah! W-What the!"],
    16: ["Elly: W-What's!? What is it?"],
    17: ["Ayase: Kyaa!? W-What is it~?"],
    18: ["Maki: Kya!? What?"],
    19: [
        "Kandori's Voice: Guh!? What is this!?" + P('ス') + " Guooooooooh! M-My body!? My body!!",
        "Kandori's Voice: My body is disappearing! What is the meaning of this!"
    ],
    20: [
        "Doctor's Voice: Branch Manager! This is the end for you! You will die with me!",
        "Doctor's Voice: You must atone for the crime of deceiving me by saying it was for humanity, and causing this incident!!"
    ],
    21: ["Kandori's Voice: Nicolai, you bastard!! Y-You set me uuuuuuup!!"],
    22: [
        "Doctor's Voice: Boys! If we are disassembled into atoms, the system will stop!",
        "Doctor's Voice: When that happens, the barrier around the town will be dispelled. Now, go!"
    ],
    23: ["Kandori: Y-You brats!! Stop the system!!"],
    24: ["Mark: Old man! Doing something so reckless..."],
    25: [
        "Mark: Let's save him! There's no reason for the old man to die for someone like Kandori!",
        "Mark: We're gonna beat that bastard to a pulp with our own hands! That's what we came here for, right!?"
    ],
    26: [
        "Nanjo: Wait! That old man may be the inventor of the system, but he wishes to take responsibility...",
        "Nanjo: We should respect his will. Besides, we do not know how to stop it."
    ],
    27: [
        "Brown: Y-Yeah, exactly! We've gotta listen to what the elderly say.",
        "Brown: If we don't hurry and leave, we're in danger!"
    ],
    28: ["Elly: <FF07>あ, we have no time to argue. Let us hurry and save him."],
    29: ["Ayase: This is seriously bad! <FF0F>あ, do something!"],
    30: [
        "Maki: <FF07>あ-kun! This! We can stop it with this machine!",
        "Maki: The red button is the emergency stop! The blue button increases the output! We can save them with the red button!"
    ],
    31: ["Nanjo: Sonomura? Why do you know such a thing!?"],
    32: ["Maki: I don't know! I just know it! <FF07>あ-kun! Hurry!"],
    33: [
        "Nanjo: <FF0F>あ, act like an adult.",
        "Nanjo: There are times when one must take responsibility in this manner."
    ],
    34: [
        "Mark: Hurry up! If he dies, it's all over.",
        "Mark: Good things might still happen to him, you know."
    ],
    35: [
        "Brown: Let's hurry and run... I mean, retreat!",
        "Brown: The leader's asking you to, come on."
    ],
    36: [
        "Elly: That elderly gentleman might also have someone precious to him...",
        "Elly: There is no need to hesitate."
    ],
    37: [
        "Maki: I don't want this anymore! For anyone else to die... Nobody wants to die, right?",
        "Maki: We just have to catch Kandori. Let's save them!"
    ],
    38: ["Kandori's Voice: Uooooooh! H-Hurry and stop it!"],
    39: ["Maki: N-No way! It won't stop!?"],
    40: ["Brown: S-Somehow, it feels like it's getting even more dangerous..."],
    41: ["Ayase: W-Wait a minute~! What exactly did you do!?"],
    42: ["Elly: Kya!? W-What is it?"],
    43: ["Kandori's Voice: Ooh!? This is! My body is returning! I see..." + P('ス') + " So it is you who calls me!"],
    44: ["Doctor's Voice: I-Impossible!? My sabotage should have been perfect! D-Don't tell me!? It's him!?"],
    45: ["Maki: !! You're!"],
    46: ["Girl in Black:" + P('ほ') + "..." + P('ほ') + "..." + P('ほ') + "..." + P('ほ') + " I won't let you kill Papa! Let's go, Papa!"],
    47: ["Kandori's Voice: Fufufu... Hahaha! I will not die! Now, invite me... into your world!!"],
    48: ["Mark: Uoah!? W-What the!?"],
    49: ["Nanjo: Tch!? K-Kandori!!"],
    50: ["Brown: Uwaaaaah!"],
    51: ["Ayase: I've had enouuuugh!!"],
    52: ["Elly: No!"],
    53: [F6('い') + "Dr. Nicolai<FF03>The genius scientist who developed<FF03>the D.V.A SYSTEM." + F6('　')],
    54: ["Ayase: Geez, <FF0F>あ! Hurry up and do something!"],
    55: ["Maki: We can save them with the red button."],
    56: "=Red or blue, which will you press!?<FF03><FF0E>た<FF01>",
    57: ["Maki: <FF07>あ-kun! Where are you going!? We have to do something!"],
    58: [
        "A hologram of the \"Dimension Variable Accelerator System\"...",
        "Commonly known as the Deva System."
    ],
    59: [
        "COMP: Emergency. Emergency situation occurring. Emergency situation occurring.",
        "COMP: An unknown virus has been detected in the hyper-dimensional shaft startup program.",
        "COMP: System shutdown impossible. System shutdown impossible.",
        "COMP: Please perform a manual emergency stop. Please perform a manual emergency stop."
    ]
}

REVIEW = {
    1: "Dr. Nicolai speaks in katakana in Japanese to represent a robotic or foreign accent. Used standard English, could capitalize to emulate.",
    56: "Choice prompt spaces"
}

if __name__ == '__main__':
    apply('E0', 58, BOXES, REVIEW)
