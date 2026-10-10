"""E0 entry 149 - the three Makis; Nanjo and Mark clash."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Maki: No way..." + P('で') + " That can't be..."],
    1: [
        "Maki: Idiot!! Why did you kill Papa!? Do you know what you've done!?",
        "Maki: Waaaaaaaaaaah!!"
    ],
    2: [
        "Maki: It's a lie..." + P('キ') + " That this is me...",
        "Maki: That I'm the one who made everyone suffer..."
    ],
    3: [
        "Maki: You killed the person the real me depended on, yourselves!?",
        "Maki: No one will save us anymore! It's over!!"
    ],
    4: ["Reiji: Three Sonomuras..." + P('キ') + " They're all her?"],
    5: [
        "Elly: Three Makis... Jesus... How can this be... They are all Maki..."
    ],
    6: ["Brown: Three Maki-chans... Seriously...? No way..."],
    7: ["Ayase: They're all the same Sonomura? Seriously...? That's so..."],
    9: ["Maki: No..." + P('キ') + " Don't come! Don't look at me!"],
    10: ["Mark: Calm down, Sonomura! It's gotta be some mistake, right?"],
    11: [
        "Maki: No no no! It's a lie! This is me! I know it!",
        "Maki: Making the town strange, making everyone suffer, it was all me! It was me!"
    ],
    12: ["Reiji: Don't let it get to you. You were just being used!"],
    13: [
        "Elly: Calm down, Maki! You were only being used. There is nothing to worry about, all right?"
    ],
    14: [
        "Brown: Calm down! You were just used, that's all, right? Come on over here."
    ],
    15: [
        "Ayase: Sonomura! Don't worry about it! It's Kandori's fault!"
    ],
    16: ["Maki: No, no..."],
    17: [
        "Maki: Please, don't be kind to me..." + P('キ') + " I understand everything now. I envied everyone...",
        "Maki: Wearing cute clothes and walking around town, getting excited talking about boys, laughing out loud...",
        "Maki: I envied everyone who went to school happily. I wished the school and the town would just disappear...",
        "Maki: I thought that."
    ],
    18: ["Mark: Sonomura..."],
    19: [
        "Maki: I wanted to do something about it, but couldn't... I cried, and cried...",
        "Maki: Envying and resenting people... I created an ideal town and an ideal self to comfort myself...",
        "Maki: Now you understand?" + P('キ') + " I'm... a hopeless girl.",
        "Maki: I have no right to live!!"
    ],
    20: ["Maki: *Sniff*... Y-You!"],
    21: [
        "Maki: You're finished too. Kandori is gone."
    ],
    22: ["Maki: Nomoraka tanomamaa~"],
    23: ["Maki: N-No! I don't wanna!!"],
    24: [
        "Maki: Now we can go back to the quiet town again... Thank you, big brother."
    ],
    25: ["Maki: Are you... still planning to continue living in that town!?"],
    26: [
        "Maki: Yes... Because if I don't, poor me...",
        "Maki: You must go back too. I want you to keep being the ideal me."
    ],
    27: ["Maki: No! I never want to go back to a town like that!"],
    29: ["Maki: Noooo!! <FF07>あ...!!"],
    30: [
        "Maki: Now you've come to like big brother, haven't you... That's fine. I'll make as many as you want.",
        "Maki: It's easy..." + P('キ') + " Bye-bye," + P('で') + " big brother..."
    ],
    31: ["Mark: Sonomura!!" + P('キ') + " Sonomuraaaaaaa!!"],
    32: [
        "Maki: That's right, it's all over! Everyone, just disappear! Disappear, all of you!!"
    ],
    33: ["Mark: Sonomura! Come over here. Okay?"],
    34: ["Maki: I... can't be by your side anymore..."],
    35: ["Maki: Please, send me... back into my heart!"],
    37: [
        "Mark: ..." + P('キ') + " Y-You... " + P('キ') + " Idiot!!",
        "Mark: Why... why does it have to be like this!"
    ],
    38: ["Mark: <FF0F>あ! Let's go back into Sonomura's heart!"],
    39: [
        "Nanjo: ...Wait, Inaba." + P('キ') + " Do you know the foolish woman called Pandora?"
    ],
    40: ["Mark: What did you say?"],
    41: [
        "Nanjo: A woman of legend who opened the box of the gods and scattered every calamity upon the earth.",
        "Nanjo: Sonomura is, so to speak, Pandora. The town's ruin is what she wished for.",
        "Nanjo: Rather than save such a woman, destroying the Deva System comes first."
    ],
    42: [
        "Mark: Y-You bastard... And you call yourself a friend!!",
        "Mark: What happens to Sonomura if we smash that thing!?"
    ],
    43: [
        "Nanjo: By all appearances, Sonomura's life is sustained by that system.",
        "Nanjo: If we destroy it, Sonomura will die as well. But as long as that system exists, there is no fundamental solution.",
        "Nanjo: Do not put personal feelings first. Sacrificing the small to save the large is the natural choice."
    ],
    44: ["Mark: Grit your teeth!!"],
    45: [
        "Mark: I'm disappointed in you... Honestly, I didn't think you were that cold.",
        "Mark: Maybe what you say is right. It's an adult's logic. But...",
        "Mark: If Sonomura's the one who made us suffer, she's also the one who tried to save us and the town, ain't she?",
        "Mark: I believe in Sonomura's heart. I believe she'll cut her ties with that machine for sure."
    ],
    46: [
        "Elly: Yes... We must tell Maki she is not alone."
    ],
    47: [
        "Brown: Good thing to say... If it helps Maki overcome herself, I'm going."
    ],
    48: ["Ayase: Ayase will go too... I'm borrowing her handkerchief, after all."],
    49: [
        "Reiji: I'm going... If that white brat is Sonomura too, I owe her for picking me up."
    ],
    50: [
        "Nanjo: Heh... Believe in her heart, hm... Yamaoka also said he believed in my heart.",
        "Nanjo: After all, humans are creatures of emotion. No matter how much one reasons, in the end it is the heart that speaks.",
        "Nanjo: I will go as well."
    ],
    51: [
        "Mark: Geez, splitting hairs. You could've just said so honestly.",
        "Mark: Don't smart adults stay behind?"
    ],
    52: [
        "Nanjo: Unfortunately, I am seventeen. By law I am not yet recognized as an adult."
    ],
    53: ["Mark: Heh heh... You always have an answer."],
    54: [
        "Nanjo: <FF0F>あ, no time to lose. Let us return into Sonomura's heart using the Deva System."
    ],
    55: ["Elly: What's that!? Something in the mirror!?"],
    56: ["Brown: H-Hey!? Something's reflected in the mirror!"],
    57: ["Ayase: Hey!? Something's reflected in the mirror!!"],
    58: ["Reiji: Look at the mirror! Something's reflected in it."],
}
REVIEW = {}

if __name__ == '__main__':
    apply('E0', 149, BOXES, REVIEW)
