"""E0 entry 96 - the gloomy bar ruled by the Harem Queen."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Nanjo: Ugh..." + P('ぎ') + " What is this atmosphere?"],
    1: ["Elly: It does not feel very bright."],
    2: ["Ayase: It's so dark here. Ayase can't stand this!"],
    3: ["Brown: Hey hey, what's with this gloom! Let's liven it up a little!"],
    4: ["Reiji: The air's bad. It smells like a place with the windows shut for a month."],
    5: ["Customer: Tch, newcomers show up! You probably don't know a thing!"],
    6: ["...Alright, a straight!"],
    7: [
        "Customer: You think we're gloomy, don't you?",
        "Customer: Right, our only salvation is Lady Harem Queen!"
    ],
    8: ["...Heh, a full house!"],
    9: [
        "Customer: Heh heh... We are your future selves.",
        "Customer: You'll understand soon enough!"
    ],
    10: [
        "Customer: Aaah..." + P('ぎ') + " You're from outside, huh...? Somethin' about you pisses me off..." + P('ぎ') + " I remembered...",
        "Customer: About the outside..." + P('ぎ') + " Uwaaah, ugh..." + P('み') + " I wanna get out..."
    ],
    11: [
        "Master: Everyone! Come, let us drink together in peace.",
        "Master: Our fates are the same anyway. There is no point in quarreling!",
        "Master: We are all loyal servants of Lady Harem Queen!"
    ],
    12: [
        "Customer: You came back with dumb looks on your faces. I get it, you met the Queen, didn't you?",
        "Customer: A handsome guy like you could've lived in the palace if only the Queen had taken a liking to you."
    ],
    13: [
        "Customer: ...I understand how you feel, but if you don't grow up a little more, you won't get by, you know?"
    ],
    14: ["Maki: What kind of person is the Harem Queen?"],
    15: ["Maki: ............ I... I didn't know anything, did I..."],
    16: [
        "Maki: Do you think I was shocked?",
        "Maki: But I feel like Chisato and I can become true best friends from now on."
    ],
    17: ["Nanjo: This is what that brat was talking about. We have been shut in again."],
    18: ["Nanjo: I was a little surprised, but one should say that was Kozai's true nature."],
    19: ["Nanjo: Even after seeing such a form, his love does not waver? Hmph. Well, let him do as he pleases."],
    20: ["Mark: Man, this is irritating! We've gotta hurry and beat that Kandori bastard!"],
    21: ["Mark: Sonomura..." + P('ぎ') + " She must be shocked..."],
    22: ["Mark: Naito really is a nice guy, after all."],
    23: ["Elly: I think I understand the cause of this atmosphere."],
    24: [
        "Elly: <FF07>あ, do you dislike people like the Queen?",
        "Elly: Yet outwardly they only pretend to obey, and stick their tongues out behind her back...",
        "Elly: The townspeople are the same."
    ],
    25: [
        "Elly: Why does Naito-kun not come to hate Kozai-san?",
        "Elly: Seeing the other person's ugly side, it is natural to be disillusioned and come to hate them, is it not?",
        "Elly: I cannot believe someone would still care for you even after you bare everything about yourself.",
        "Elly: Is there such a person..." + P('ぎ') + " for me too..."
    ],
    26: ["Brown: A \"Queen\" must be a drop-dead beauty, don't ya think? Right? Right? I'm gettin' my hopes up! *"],
    27: ["Brown: So Kozai was..." + P('み') + " that kind of person..." + P('み') + " I'm kinda disappointed..."],
    28: ["Brown: The relationship between men and women..." + P('み') + " runs deep, huh! *"],
    29: ["Ayase: Ayase hates it here. It feels like Ayase's power is being sucked away."],
    30: ["Ayase: Kozai... that was bold of her!"],
    31: [
        "Ayase: Ayase wants... " + P('み') + " that mirror too~!",
        "Ayase: Ayase's gonna make a harem too~!"
    ],
    32: ["Reiji: Harem Queen? Heh, don't make me laugh."],
    33: ["Reiji: Being true to your desires... I don't think that's bad."],
    34: ["Reiji: A stupid ending," + P('ぎ') + " but maybe now and then it's fine."],
    35: [
        "Customer: Hic~ Lady Queen~ Lady Queen's paintings are the best~",
        "Customer: So let me out of here~"
    ],
    36: [
        "Customer: The Queen's paintings are no better than a kid's scribbles!",
        "Customer: Serves her right!"
    ],
    37: [
        "Customer: A labyrinth of sorrow, forgotten in the gap of time...",
        "Customer: Only sake can soothe my suffering...",
        "Customer: ..." + P('ぎ') + " Damn it alllll! That little brat!!",
        "Customer: She takes all the good guys to her place!",
        "Customer: ...I wanna go to the harem toooo!!"
    ],
    38: [
        "Customer: Even if the stopped clock starts moving again..." + P('み') + " my suffering stays the same as back then...",
        "Customer: ..." + P('ぎ') + " Damn it alllll! That little brat!!",
        "Customer: She built a harem and she had a boyfriend all along, the sly thing!!"
    ],
    39: [
        "Master: No one is allowed to leave this market.",
        "Master: Because Lady Queen, the ruler of this market, has decided so.",
        "Master: You had best behave so as to be liked by Lady Queen."
    ],
    40: [
        "Mark: ...Let's go to the palace! We don't have time.",
        "Mark: We ain't got time to play along with this Queen's ruler games, right?"
    ],
    41: [
        "Maki: Inaba-kun's right. Let's go see the Queen!",
        "Maki: And then have her let us out of here, okay?"
    ],
    42: [
        "Master: If you think you can leave at any time, life here is not so bad."
    ],
    43: [
        "Customer: You want to meet Lady Harem Queen? She's in the Kama Palace underground.",
        "Customer: The entrance is next to the casino. One piece of advice: don't make the Queen angry."
    ],
    44: [
        "Customer: There's an old, filthy mansion farther east.",
        "Customer: They say it leads to another world."
    ],
    45: [
        "Customer: Let me tell you one thing.",
        "Customer: Always praise the Queen's paintings. If you don't, you'll make the Queen angry."
    ],
    46: ["Customer: The Queen probably had no confidence in herself in the end. Come to think of it, it's pitiful."],
    47: ["Customer: You're not wearing a mole?" + P('み') + " Copying the Queen and wearing a mole is the latest fashion, you know."],
    48: ["Customer: Ahh, finally I don't have to wear this mole anymore! Moles don't suit me."],
}
REVIEW = {10: "slurred drunk speech", 26: "★ and ♥ replaced with *"}

if __name__ == '__main__':
    apply('E0', 96, BOXES, REVIEW)
