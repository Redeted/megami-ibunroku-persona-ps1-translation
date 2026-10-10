"""E0 entry 65 - Yosuke's explanation."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Yosuke: Is it really you, <FF0F>あ-kun? I never thought I would be able to see people from my original world again!"],
    1: ["Mark: What did you say? Could you be... Naito, who went missing?"],
    2: [
        "Yosuke: Yeah, that's right! About two months ago, Chisato... Kozai-san and I wandered into this world.",
        "Yosuke: We are humans from the same world as you!"
    ],
    3: ["Nanjo: You said \"world\"." + P('で') + " That means this place is not the past, but another dimension... another world?"],
    4: [
        "Yosuke: Yeah. At first, I thought it was the past too. It was exactly like the town from a year ago.",
        "Yosuke: But some places are strange. The police station has turned into a forest, and the general hospital has become a castle.",
        "Yosuke: And Maki-kun is exactly as you see her now. Yes, it was a town like a paradise..." + P('キ') + " Up until a month ago."
    ],
    5: ["Nanjo: A parallel world... You mean the theory that several similar worlds exist in parallel universes..."],
    6: [
        "Mark: Are you serious, man... I was wondering where you ran off to with Kozai, but you went to another world?",
        "Mark: I'd say that's crazy..." + P('で') + " But I guess it ain't someone else's problem now."
    ],
    7: ["Elly: Fantastic! How wonderful! It is just like a novel or a movie!"],
    8: ["Ayase: Wait, seriously? Ayase has a ton of plans coming up! What're we gonna do, <FF0F>あ-!"],
    9: ["Brown: No way! How are we gonna get back? *Sigh*~"],
    10: ["Nanjo: It is difficult to believe so suddenly, but given the existence of the Deva System, it is appropriate to accept it as fact..."],
    11: ["Yosuke: Well, I don't blame you..." + P('サ') + " Still, to think this world's Maki-kun would bring you all back with her."],
    12: ["Mark: Hold on! Does that mean... Sonomura is Sonomura, but she ain't the Sonomura from our world?"],
    13: [
        "Maki: I'm sorry! I didn't mean to deceive you, but I wasn't completely sure until we came back.",
        "Maki: I never thought another world actually existed, or that I would go there myself."
    ],
    14: ["Nanjo: I see. That explains why your behavior was so strange."],
    15: ["Maki: I was dozing off in the classroom, and when I woke up, I was already in another world. I didn't realize it until much later, though."],
    16: [
        "Mark: What the hell... Then that means the real Sonomura is still somewhere in the hospital...",
        "Mark: You could've said something, right? Err..." + P('ヒ') + " Sonomura, I mean."
    ],
    17: [
        "Maki: I'm really sorry. But even if I told you, you wouldn't have believed me, right?",
        "Maki: Besides, I thought that if we defeated Kandori, both worlds would return to normal... So I was going to tell you after it was over."
    ],
    18: ["Mark: I see... Huh? Kozai isn't here, where is she?"],
    19: ["Yosuke: Chisato... Kozai-san was taken away by the Girl in Black..." + P('キ') + " Dammit!"],
    20: ["Brown: Uwaah!? W-What the!?"],
    21: ["Elly: What's!? What is it!?"],
    22: ["Ayase: Kyaa!? I've had enough! What is it!?"],
    23: ["Maki: Could it be? Her again!?"],
    24: [
        "Girl's Voice: Kyahahahaha! This time for sure, I'm going to break this school!",
        "Girl's Voice: I erased the exits, so nobody can escape! Kyahahahahahahahaha..."
    ],
    25: ["Yosuke: No doubt about it! It's her! She erased the exits!? If demons appear in this situation..."],
    26: ["We'll all be killed! Dammit, I have to go!"],
    27: [
        "Maki: No! Yosuke-kun! Please, don't push yourself!",
        "Maki: Everyone, lend a hand! We have to do something!"
    ],
    28: ["Mark: I don't really get it, but we can't go outside like this. Let's go, <FF0F>あ!"],
    29: [
        "Yosuke: Dammit! If only my body would listen to me, I'd get Chisato back this time for sure!",
        "Yosuke: Eh? This injury?" + P('キ') + " The last time that girl came, I was beaten to a pulp...",
        "Yosuke: Really, how pathetic of me!"
    ],
    30: [
        "Maki: That girl must definitely be somewhere in the school!",
        "Maki: Don't let your guard down just because she's a kid. She has a mysterious power."
    ],
    31: ["Nanjo: What exactly is the relationship between Kandori and that little girl? We have too few materials to judge from..."],
    32: ["Mark: Ain't no point in worrying about it! To find a way to get back, we gotta do somethin' about this situation first."],
    33: ["Brown: *Sigh* I wonder if there's really a way to get back~"],
    34: ["Ayase: <FF0F>あ~, make sure you properly look for a way back, okay~?"],
    35: [
        "Elly: A girl who commands demons...",
        "Elly: I suppose you could call her a Devil Summoner?"
    ],
    36: [F6('い') + "Naito Yosuke<FF03>A ladies' man who went missing<FF03>two months ago with Kozai Chisato." + F6('　')],
    37: ["Mark: I see... And Kozai is still with that brat in black?"],
    38: ["Yosuke: Yeah... Even though I was with her..." + P('キ') + " Dammit!"],
    39: ["Reiji: ...Kandori's kid? That bastard shouldn't have any kids."]
}

REVIEW = {
    26: "Unlabeled box. Likely Yosuke continuing his line, so left unlabeled to match."
}

if __name__ == '__main__':
    apply('E0', 65, BOXES, REVIEW)
