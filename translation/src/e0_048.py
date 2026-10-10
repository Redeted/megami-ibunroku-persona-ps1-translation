"""E0 entry 48 - Police station: searching for the Holding Cell Key."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Maki: This was the police..." + P('み') + " wasn't it? That's right, it was a place like this!"],
    1: [
        "Nanjo: ..." + P('た') + " ..." + P('た') + " That is so." + P('み') + " <FF0F>あ, Inaba should be held captive in the holding cell.",
        "Nanjo: However, without the key we cannot enter the holding cell. Now, what to do..."
    ],
    2: ["Maki: Maybe it's been left somewhere. Let's try looking."],
    3: ["Nanjo: That is true. <FF0F>あ, you search together with us as well."],
    4: [
        "Found the \"Holding Cell Key\"...",
        "Obtained the \"Holding Cell Key\"."
    ],
    5: ["There don't seem to be any more useful keys inside..."],
    6: ["Nanjo: Good. With this, we should be able to open the door of the holding cell!"],
    7: [
        "Nanjo: Inaba should be in the holding cell.",
        "Nanjo: It is not that I particularly want to save him, but that guy has the \"security card\"."
    ],
    8: ["Maki: Hold-ing cell..." + P('み') + " Ohh, the holding cell. Yeah, yeah, there was a place like that too, wasn't there?"],
    9: ["Maki: Hey, <FF07>あ-kun, Nanjo-kun says I'm strange, but what do you think?"],
    10: [
        "Brown: <FF08>あ, you thought the great me was in trouble and came to help, right?",
        "Brown: Tsk, tsk, that's not how it is!",
        "Brown: I'd even thought up a super cool way to escape. Aww, what a waste!"
    ],
    11: ["Nanjo: If we only took the card, it might have been fine to leave Inaba and Uesugi as they are."],
    12: [
        "Mark: That octopus geezer! Don't hand the police over to Demons that easily, man!",
        "Mark: Octopus geezer..." + P('み') + " No, the Inspector hauled me in for guidance a lot and it ticked me off at times, but...",
        "Mark: He was a guy who really worried about me. Could it be that that Demon...",
        "Mark: ..." + P('み') + " No way. There's no way that ogre Inspector gets taken out that easily, right?"
    ],
    13: [
        "Maki: You can't open the door of the holding cell without the key, right?",
        "Maki: Let's look for the key first."
    ],
    14: [
        "Nanjo: No matter what, it is unthinkable that the key would be lying outside. Search the inside a little more.",
    ],
}
REVIEW = {
    1: "FF0F name used as a vocative; 'そうだな' answers Maki's odd remark in box 0",
    8: "Maki stumbles over katakana リュウチジョウ (does not recognise the word); rendered as 'Hold-ing cell...'",
    9: "<FF07>あ + 君: FF07 name insert (probably the player name) followed by -kun; kept as '<FF07>あ-kun'",
    10: "<FF08>あ at the start is a name insert; rendered as vocative. Brown's チッチッ違うんだなこれが - what is 'wrong' is vague",
    12: "警部にはよ補導 - probably 'よく' with a dropped glyph; read as 'often'. オニ警部 = 'ogre Inspector'",
    13: "リュウチジョウ in katakana here too; rendered plainly as 'holding cell'",
}

if __name__ == '__main__':
    apply('E0', 48, BOXES, REVIEW)
