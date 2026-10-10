"""E1 entries 83-96 - the chest letter, Michiko's boss fight, Thanatos tower entry."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

p = P('ほ')


def S(*parts):
    return p.join(parts)


E83 = {
    12: [
        "Obtained a \"Mirror Fragment\"",
        "..." + p + " ..." + p + " ..." + p + " ..." + p + " ..." + p + " ..." + p + " ..." + p + " ..." + p + " ..." + p + " ..." + p + " ..." + p + " ..." + p + " ...<FF03>There is something like paper<FF03>in the corner of the chest.",
        "...It seems to be a letter from Michiko?",
        "You opened the letter."
    ],
    13: [
        "\"Ohohohohohohoho! To think you made it all the way to this chest! What greedy people you are!",
        "It must have been so hard! Hohohohohohohohoho! How about it? Did you find what you were after?",
        "I, unlike you humans, never tell lies! So as promised, I shall tell you Michiko's weakness too!",
        "Th" + p + "at" + p + " is" + p + " it! * " + p + "Don't take too much time, now!",
        "Ohohohohohoho! Hurry to me! I shall be waiting! *",
        "How was it? Was it helpful? Now then, good day.\"",
        "        From Michiko<FF02><FF03>        For You"
    ],
    14: ["The treasure chest is empty now."],
}

E86 = {
    0: [
        "Yukino: Alright! As you wished, we came! Matsudaira Michiko!!",
        "Yukino: Hand over the \"Key to the Chains\" binding Toro and Kurouri! We can take it by force if need be!",
        "Yukino: Well, I was planning that from the start, but with your personality you won't hand it over quietly, will you?"
    ],
    1: [
        "Michiko: No way!? You all? You came here this fast?",
        "Michiko: Wh-" + p + " What about the \"mirror fragment\"? Surely you did not go get it? Oh!" + p + " Oh!? What a thing!?",
        "Michiko: This will not do!" + p + " This will not do!! The \"negative\" power of human emotion, the source of my power! The power of \"hatred\" and \"anger\"! Is lacking!" + p + " Far too lacking!!",
        "Michiko: No," + p + " worse than that... What is it?? This unpleasant sensation entering me?",
        "Michiko: W-" + p + " What? " + p + "\"Gratitude\"? " + p + "\"Friendship\"? Su-" + p + " Surely they, while under that torture, are feeling such emotions?",
        "Michiko: I-" + p + " Impossible!? Was this tower's mechanism found out? By you??",
        "Michiko: No, that cannot be! My plan was perfect!",
        "Michiko: The feeling every human has, \"I don't care what happens to others as long as I'm fine\"...",
        "Michiko: No!" + p + " It is not so lofty as to be called a feeling! Instinct!" + p + " Yes, the plan used you humans' instinct!!",
        "Michiko: Why?" + p + " Why?? How can you try to help others without any return?",
        "Michiko: Michiko cannot understand! Like this!" + p + " Like this, I will!! Lack the power!!",
        "Michiko: What should I do?"
    ],
    2: [
        "Nanjo: Well, the usual me would have ignored those two and gone for the \"mirror fragment.\"",
        "Nanjo: Hmph! I do not know what you schemed with your meager wits, but you made one mistake.",
        "Nanjo: That is that you truly angered me, Nanjo Kei.",
        "Nanjo: Surely you did not think you would get away unscathed after making a fool of me to that extent?",
        "Nanjo: The sin of calling the great Nanjo Kei a pet! You will atone for it with your death! Prepare yourself!!"
    ],
    3: [
        "Brown: If I abandon my friends, it'd stain my glorious record!!",
        "Brown: A guy like you is the one thing I can't forgive! For hurting Toro and Akuma-kun! For calling everyone dogs!",
        "Brown: And above all! I'll pay you back in full for calling Great me a pet!",
        "Brown: Get ready!!"
    ],
    4: [
        "Ayase: Heh! Besides, we don't even need all twelve \"mirror fragments,\" about eight is totally fine!",
        "Ayase: Ayase doesn't care what happens to Toro and Kurouri, but a nasty woman like you acting all high and mighty is, like, MMC, you know? Get it?"
    ],
    5: [
        "Michiko: Kyaaaah! Be quiet! Be quiet!! Be quiet, I say! Silence!!",
        "Michiko: So what, you mean to say I am inferior to those two ugly ones?? Me, the beautiful? What a thing?? Oh!! Ohhh!!",
        "Michiko: As I thought, my wonderful plan was too highbrow for puppies like you!",
        "Michiko: Ohhh! Ooh! I should have slaughtered you all the moment you entered this tower!",
        "Michiko: Ohhhh!!"
    ],
    6: [
        "Nanjo: You are noisy with your \"oh, oh.\" Hmph! You are not a sea lion.",
        "Nanjo: Well, Ayase is right. Missing a mirror fragment or two here will not shake our victory!",
        "Nanjo: We cannot forgive a villain like you in any case! First, we beat you! No mercy!!"
    ],
    7: [
        "Elly: Michiko... You are making a poor showing. The more you rant, the more your ugliness stands out.",
        "Elly: You should look at your face in a mirror now. Heh... It is not something fit to show people.",
        "Elly: Indeed, as Ayase says, we would not mind missing a \"mirror fragment\" or two in this tower.",
        "Elly: Let us end the idle talk. And the reason we came straight here...",
        "Elly: no matter how much I tell you, you will never understand. Now, prepare yourself!"
    ],
    8: [
        "Michiko: Kyaaah! I will never admit it! The \"kindness,\" the \"friendship,\" the \"trust\" of the human heart!",
        "Michiko: Such things!" + p + " Such things!! Do not exist in this world, absolutely! I shall prove it with your defeat!!",
        "Michiko: \"Lord Nemesis\"... Become the armor that protects me! \"Lord Nemesis\"... Become the sword that destroys them!",
        "Michiko: Come!" + p + " \"Nemesis\"!! To my side! \"Nemesis Power" + p + " Build up!\""
    ],
    9: [
        "Yukino: So you're gonna call a Persona, huh? Everyone, here we go! Time to pay back for Toro and Kurouri!"
    ],
    10: [
        "Yukino: This seems to be Michiko's room. What a tasteless room. What are all these faces lined up on the walls??"
    ],
    11: [
        "Michiko: Ohohohohoho! Those faces are what became of the humans who did not heed me... And they are your future selves as well.",
        "Michiko: Heh heh... To think I'll get five new faces! What a wonderful day today! Ohohohohohoho!",
        "Michiko: How about it? My collection? Is it to your liking?",
        "Michiko: You filthy thieves who abandoned your suffering friends in the grip of greed?",
        "Michiko: It seems you did receive my gift, the \"mirror fragment.\" Ohohohohohoho! You fell so easily for the trap I set!",
        "Michiko: Lured by bait, a single \"mirror fragment,\" you threw away the chance to defeat me with your own hands!",
        "Michiko: Ohohohohoho!"
    ],
    12: [
        "Nanjo: What? You say we fell into a trap? What do you mean? You! What did you do!!"
    ],
    13: [
        "Brown: Hnh? We fell in a trap?? What's that supposed to mean?",
        "Brown: Hey! You! Explain!!"
    ],
    14: [
        "Ayase: Ugh! What! This ugly hag! You're just bluffing because Ayase and everyone took your \"mirror fragment\" and you're in trouble, right?",
        "Ayase: You liar!! Quietly just get beaten by Ayase and the others!"
    ],
    15: [
        "Michiko: Hohohohoho! This \"Tower of Nemesis\" is a, so to speak, \"living tower\" that grows while absorbing negative emotions such as human \"anger,\" \"hatred,\" and \"despair\" as energy.",
        "Michiko: And I take the energy the tower draws up into my body, so I grow infinitely strong. That is the mechanism.",
        "Michiko: Understand? Kukuku... The \"sadness\" and \"anger\" born of the pain of those two ugly men being tortured...",
        "Michiko: the \"hatred\" and \"despair\" born of feeling abandoned by the friends they believed would save them...",
        "Michiko: Fahahahaha! All of it gave my body wonderful power!",
        "Michiko: Ohohoho! If you must resent someone, resent your own base nature! You rabble!"
    ],
    16: [
        "Nanjo: Truly tremendous power! And she is merely standing there!",
        "Nanjo: What murderous \"aura\" this is, crashing into us! Did that guy really power up from Yokouchi's and Kurouri's \"anger\" and \"hatred\"...",
        "Nanjo: A blunder! To needlessly give her strength..."
    ],
    17: [
        "Elly: What? This vicious pulse? Michiko is only standing there...!",
        "Elly: The \"anger\" and \"hatred\" of the two being tortured are making Michiko's Power unmanageably Big...",
        "Elly: We were thoroughly outmaneuvered!"
    ],
    18: [
        "Michiko: Now then, I shall add the faces of five insolent puppies who defied the \"Snow Queen\" and made a fool of me",
        "Michiko: among the faces of the humans who once betrayed me!",
        "Michiko: \"Anger\"!" + p + " \"Regret\"! \"Despair\"!" + p + " \"Hatred\"! More!" + p + " More!!",
        "Michiko: Bare your human instincts and come at me! Even that is an irresistible feast for me!",
        "Michiko: Kukuku! Hahahahahaha! Fahahahaha!",
        "Michiko: \"Lord Nemesis\"... Become the armor that protects me! \"Lord Nemesis\"... Become the sword that destroys them!",
        "Michiko: Come!" + p + " \"Nemesis\"!! To my side! \"Nemesis Power" + p + " Build up!\""
    ],
    19: [
        "Yukino: Tch!" + p + " A Persona? Everyone! No use whining over spilled milk! Let's deal with this one in front of us!!"
    ],
    21: [
        "Michiko: Ohohohohoho! Those faces are what became of the humans who did not heed me... And they are your future selves as well.",
        "Michiko: Heh heh... To think I'll get five new faces! What a wonderful day today! Ohohohohohoho!",
        "Michiko: How about it? My collection? Is it to your liking?",
        "Michiko: Even so, what a leisurely arrival! I got tired of waiting!",
        "Michiko: Ohohohohohoho! But to think you would fall so easily for the trap I set!",
        "Michiko: Lifting the tower's time limit was the right call!",
        "Michiko: You threw away the chance to defeat me with your own hands! Michiko cannot stop laughing! Ohohohohoho"
    ],
    24: [
        "Ayase: Ugh! What! This ugly hag! You're just bluffing because you're about to lose to Ayase and the others, right?",
        "Ayase: You liar!! Quietly just get beaten by Ayase and the others!"
    ],
    25: [
        "Michiko: Hohohohoho! This \"Tower of Nemesis\" is a, so to speak, \"living tower\" that grows while absorbing negative emotions such as human \"anger,\" \"hatred,\" and \"despair\" as energy.",
        "Michiko: And I take the energy the tower draws up into my body, so I grow infinitely strong. That is the mechanism.",
        "Michiko: Understand? Kukuku... The \"sadness\" and \"anger\" born of the pain of those two ugly men being tortured...",
        "Michiko: the \"doubt\" and \"despair\" born of the anxiety that the friends they believed would save them have not come...",
        "Michiko: Fahahahaha! All of it gave my body wonderful power! And plentifully so!",
        "Michiko: And it is thanks to you taking your time to get here! I am grateful!"
    ],
    27: [
        "Elly: What? This vicious pulse? Michiko is only standing there...!",
        "Elly: The \"anger\" and \"hatred\" of the two being tortured are making Michiko's Power unmanageably Big...",
        "Elly: We were thoroughly outmaneuvered! If only I had paid more attention to the absence of a Time limit...!"
    ],
}

if __name__ == '__main__':
    for n, d in ((83, E83), (86, E86)):
        apply('E1', n, d, {})
