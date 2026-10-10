"""E1 entries 1-4 - the Snow Queen's school: Saeko-sensei is possessed by the mask."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

E1 = {
    1: [
        "Yukino: !" + P('そ') + " The courtyard" + P('そ') + " ..." + P('そ') + " ..." + P('そ') + " ? What's going on!?"
    ],
    2: ["Ayase: Hey! Look at that!!"],
    3: ["Yukino: Saeko-sensei!"],
    4: ["Yukino: W-What the!?"],
    5: ["Saeko-sensei: Heh heh heh heh... At last, this moment has come."],
    6: ["Yukino: Sensei" + P('ほ') + " ..." + P('ほ') + " ..." + P('ほ') + " ?"],
    7: [
        "Saeko-sensei: Sensei?" + P('ほ') + " Ah, you mean Saeko-san.",
        "Saeko-sensei: Poor Saeko-san. Heh heh heh heh..."
    ],
    8: [
        "Yukino: Huh? \"Saeko-san\"" + P('ほ') + " is you, isn't it?",
        "Yukino: Get a grip! Did you fall and hit your head or something?"
    ],
    9: [
        "Saeko-sensei: Heh heh heh heh... \"I'm fine even if I wear a mask\"? She said that? Heh heh heh heh... Ahahahaha.",
        "Saeko-sensei: Saeko-san has always been like that. Self-confident," + P('ほ') + " self-centered..." + P('ほ') + " She never gave a thought to others if it let her be the center of conversation."
    ],
    10: [
        "Yukino: Hey, what's wrong!? Stop that lame act. This is too harsh even as a joke."
    ],
    11: [
        "Saeko-sensei: A joke?",
        "Saeko-sensei: Take a good look around. Heh heh heh heh... Does this seem like a joke to you?",
        "Saeko-sensei: Beautiful, isn't it? A pure landscape, everything embraced in eternal silence.",
        "Saeko-sensei: You too will wrap yourselves in eternal ice and spend endless time, ever beautiful. Come now."
    ],
    12: [
        "Ayase: \"Come now\"... What are you saying at a time like this! Even if you're a teacher..."
    ],
    13: [
        "Saeko-sensei: Oh, what a lovely young lady.",
        "Saeko-sensei: Heh heh heh heh... Come closer. I will give you eternal beauty as well."
    ],
    14: [
        "Yukino: Yuka, don't go near her!!",
        "Yukino: The mask" + P('ほ') + " ..." + P('ほ') + " ..." + P('ほ') + " The mask has taken over Sensei!!",
        "Yukino: You monster, what are you up to! If you do anything to Saeko-sensei, I won't let it slide!!"
    ],
    15: [
        "Mask: \"Taken over\"" + P('ほ') + " you say? That is a rather unkind way to put it.",
        "Mask: Who was it that broke the seal?" + P('ほ') + " Who put on the mask on their own?",
        "Mask: And besides... is it not rude to call someone a \"monster,\" young lady?",
        "Mask: Well then, let me borrow from the mask" + P('ほ') + " and have you call me \"Snow Queen\"" + P('ほ') + " if you will.",
        "Mask: Heh heh heh heh..."
    ],
    16: ["Yukino: Don't screw with me! What are you going to do to Saeko-sensei!!"],
    17: ["Snow Queen: I will make her the sacrifice, spirited young lady."],
    18: ["Ayase: S-" + P('ほ') + " Sacrifice?"],
    19: [
        "Snow Queen: Yes, a sacrifice.",
        "Snow Queen: If I sacrifice Saeko-san, who is overflowing with hope,",
        "Snow Queen: the silence of despair" + P('ほ') + " the \"Eternal Night\" will come."
    ],
    20: [
        "Ayase: ?",
        "Ayase: Does that mean everybody gets frozen?",
        "Ayase: I hate the cold!"
    ],
    21: ["Yukino: Not a chance! I'm taking Saeko-sensei back!!"],
    22: [
        "Snow Queen: What a spirited girl. Very well, I shall return her.",
        "Snow Queen: But unless you remove this mask, Saeko-san will not return to normal. The school will stay frozen too.",
        "Snow Queen: If you walk around a bit you will understand, but you cannot leave the school. You cannot escape.",
        "Snow Queen: Either accept the \"Eternal Night\" or remove Saeko-san's mask... One or the other."
    ],
    23: ["Ayase: How do we get the mask off?"],
    24: [
        "Snow Queen: Heh heh heh heh...",
        "Snow Queen: Struggle all you like, for nothing is more beautiful than despair after struggling.",
        "Snow Queen: It seems I will obtain many beautiful despairs. I look forward to it."
    ],
    25: ["Ayase: Hey! Are you even listening to people!?"],
    26: ["Yukino: Ah! S-Sensei!!"],
    27: [
        "Snow Queen's Voice: Heh heh heh heh... Go ahead and touch carelessly.",
        "Snow Queen's Voice: Saeko-san will shatter to pieces along with the mask.",
        "Snow Queen's Voice: Several rituals are required, so there is still time before the \"Eternal Night\" arrives.",
        "Snow Queen's Voice: Until then, let us play a game."
    ],
    28: ["Yukino: A game!?"],
    29: [
        "Snow Queen's Voice: In the school, now a castle of ice, three towers stand, each with a guardian.",
        "Snow Queen's Voice: If you can defeat them before the clock in each tower strikes twelve...",
        "Snow Queen's Voice: then I shall return the frozen Saeko-san and the school to normal.",
        "Snow Queen's Voice: I must leave the mask, my vessel, and prepare to call the \"Eternal Night.\"",
        "Snow Queen's Voice: Meanwhile, enjoy yourselves. Heh heh heh heh... Now then, good day."
    ],
    30: [
        "Ayase: \"Good day,\" she says! Hey!!" + P('ほ') + " ..." + P('ほ') + " ..." + P('ほ') + " Don't leave us here...",
        "Ayase: No way... W-" + P('そ') + " w-" + P('そ') + " What do we do!"
    ],
    31: [
        "Ayase: It all started because <FF0F>あ!! You found some weird mask, and that's why this happened!!",
        "Ayase: Take responsibility! You're a guy, aren't you!! Say something!!"
    ],
    32: [
        "Yukino: Yuka! Stop it!! Saying that now won't do any good.",
        "Yukino: <FF0F>あ didn't do it on purpose, knowing this would happen."
    ],
    33: ["Ayase: ...But~"],
    34: ["Ayase: Hey! What's that!?"],
    35: ["Yukino: Again..."],
    36: ["Ayase: Huh? \"Again\"?"],
}

E3 = {
    0: ["Obtained the \"Mirror Frame\""],
    1: ["Yukino: Okay. Anyway, we just need to find the \"mirror fragments\" and fit them into the frame, right?"],
    2: [
        "Ayase: Say, Mayuzumi, the towers are guarded by demons, right?",
        "Ayase: Isn't this party kind of unreliable?"
    ],
    3: [
        "Yukino: If you don't like it, wait here. We don't know what dangers await. You don't have to come."
    ],
    4: ["Ayase: T-That's not it. It's just..."],
    5: [
        "Yukino: I want to save Saeko-sensei no matter what.",
        "Yukino: She was the only one who tried to help a delinquent dropout whom even her parents gave up on. Always.",
        "Yukino: Now it's my turn to save her. In my own way!"
    ],
    6: [
        "Ayase: Mayuzumi... I hope not, but you're not thinking of leaving Ayase alone in a place like this, right?" + P('ほ') + " Right?",
        "Ayase: Ayase's coming too!! It feels safer with Mayuzumi and <FF0F>あ around." + F6('う') + "*" + F6('　')
    ],
    7: [
        "Yukino: Heh... Fine, do as you like.",
        "Yukino: When we feel like giving up, having you around lightens the mood."
    ],
    8: ["Yukino: Hey, Yuka!! Why do you have a gun!?"],
    9: [
        "Ayase: Nanjo left it with me.",
        "Ayase: Inaba and Nanjo went to the police station to get weapons. Nanjo got hurt there and came back to school,",
        "Ayase: and told me to keep some for him while he got treated, and handed me several.",
        "Ayase: In the confusion I kept one. Hee hee" + F6('う') + "*" + F6('　') + " I wanted to shoot one at least once."
    ],
    10: ["Yukino: ..."],
    11: [
        "Ayase: Whoa, the wind's getting stronger~ It's cold~ My ears hurt~",
        "Ayase: Let's go inside the building already~!"
    ],
    12: [
        "Yukino: Yeah. You're right, nothing will start by staying here.",
        "Yukino: Even for collecting the \"mirror fragments,\" I wonder if three of us can stand up to demons...",
        "Yukino: As Yuka says, we might do better to gather a few more members."
    ],
    13: ["Ayase: Then it's settled! Let's get inside the building! We'll freeze to death!"],
    14: ["Yukino: Saeko-sensei" + P('ほ') + " wait for us."],
}

E4 = {
    0: ["Natsumi-sensei: Hey, Nanjo-kun! If you take the bandage off, your wound will open!"],
    1: ["Nanjo: No need to worry! Besides, wrapped like this, the bandage is pointless."],
    2: ["Natsumi-sensei: Ugh... Sorry for being clumsy."],
    3: ["Nanjo: Then, if you will excuse me."],
    4: [
        "Natsumi-sensei: \"Excuse me\"..." + P('み') + " Wait, you're not planning to go outside, are you?"
    ],
    5: [
        "Student: That's right, Nanjo-kun. You'll only get hurt again. Besides...",
        "Student: We all searched around, but it seems we can't get out of the school... There's no exit anywhere!!"
    ],
    6: [F6('う') + "Nashimoto Minori<FF03>Ayase's friend. Loves to chatter. Always noisy." + F6('　')],
    7: ["Nanjo: Hm? I do not follow. Talk in your sleep after you have slept."],
    8: [
        "Ayase: It's not sleep talk! It's true!! We were locked in by the Snow Queen."
    ],
    9: [
        "Nanjo: Snow Queen? Is it April 1st today? Think of a better lie.",
        "Nanjo: I have no time to play with fools. Move aside."
    ],
    10: ["Yukino: It's true, Nanjo. There's no exit."],
    11: [
        "Nanjo: Mayuzumi, even you" + P('み') + " ..." + P('み') + " ..." + P('み') + " Could it be!!",
        "Nanjo: The school is like the hospital!?"
    ],
    12: [
        "Elly: Unfortunately, that is exactly the case.",
        "Elly: If I must name a difference, it is that instead of there being Demons, this time there is no exit."
    ],
    13: [
        "Yukino: Yeah. Same as the hospital.",
        "Yukino: The difference is that instead of demons wandering around, this time there's no exit."
    ],
    14: ["Nanjo: ...I am worried about Inaba and Sonomura. I must get outside somehow."],
    15: [
        "Maki's Mother: Maki...",
        "Maki's Mother: Can we really not get out? Isn't there some way to get outside?"
    ],
    16: [
        "Yukino: There is. But to do it, we need a few more members."
    ],
    17: ["Nanjo: What do you mean?"],
}

if __name__ == '__main__':
    apply('E1', 1, E1, {})
    apply('E1', 3, E3, {})
    apply('E1', 4, E4, {})
