"""E0 entry 77 - Igor in the Velvet Room (menu lines and tutorials)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: [
        "Igor: Welcome to the Velvet Room...",
        "Igor: This is a room that awakens the ancient forms of the human heart.",
        "Igor: Would you show me your Persona?"
    ],
    1: ["Igor: Welcome to the Velvet Room..."],
    2: "=Igor: What do you wish?<FF03><FF0E>し<FF01>",
    3: "=Igor: Now then,<FF03>what shall we discuss?<FF02><FF03><FF0E>ぬ<FF01>",
    4: ["Igor: You lack Spell Cards."],
    5: ["Igor: I cannot take any more Personas in my keeping."],
    6: "=Igor: What shall you do?<FF03><FF0E>な<FF01>",
    7: ["Igor: Then, farewell..."],
    8: [
        "Igor: Should you desire a new Persona, I can fuse one for you.",
        "Igor: To create a Persona, I must fuse demons summoned from the Demon World.",
        "Igor: However, summoning a demon requires a certain card.",
        "Igor: On that card is written the spell that calls the demon.",
        "Igor: It is called a Summoning Spell Card, and each demon holds exactly one.",
        "Igor: Therefore... to fuse, you must first collect Spell Cards.",
        "Igor: Negotiate with demons and obtain Spell Cards yourselves.",
        "Igor: Even when you meet a demon, fighting is not all there is.",
        "Igor: Do you understand?",
        "Igor: They do not always wish for battle, after all..."
    ],
    9: [
        "Igor: To make use of a newly fused Persona as your own power...",
        "Igor: Fusing alone is not enough.",
        "Igor: Only by summoning the Persona into your own body can you master its power.",
        "Igor: Each person can have up to three Personas summoned.",
        "Igor: I keep newly fused Personas safe with me.",
        "Igor: When needed, ask me to summon one.",
        "Igor: I can keep up to 16 Personas, so swap them as needed.",
        "Igor: Personas vary as much as people's characters, as the saying goes, \"ten people, ten colors.\" Their forms differ, and so do their contents.",
        "Igor: Judging that and using them as the situation demands will also be necessary.",
        "Igor: If you master them so, you will become a fine Persona user."
    ],
    10: [
        "Igor: Each person can have up to three Personas summoned.",
        "Igor: One of them is active, and can be invoked in battle.",
        "Igor: Invoking means calling out the Persona during battle.",
        "Igor: The other two are charged, and during battle you can make them active with a Persona Change.",
        "Igor: The active Persona supplements your various abilities.",
        "Igor: Without the power of a Persona, you are no different from ordinary humans, and would not withstand magic cast by demons.",
        "Igor: If you took it head-on, you would most likely not survive.",
        "Igor: Yet once a Persona is summoned, your defense against magic, which you lacked until now, rises remarkably.",
        "Igor: Some will gain strength, and some will gain luck.",
        "Igor: This too is the power of a Persona. Persona though it may be, it is all a hidden side of yourself.",
        "Igor: After summoning, take a good look at your status.",
        "Igor: You will see how you have changed.",
        "Igor: Also, at first no one can bring out a Persona's full power.",
        "Igor: But the more you invoke it, the more of its ability you can draw out.",
        "Igor: As your mastery of invoking a Persona rises, the attacks you can use in battle increase.",
        "Igor: However, even if you choose stronger attacks as they increase, the SP needed to invoke does not change.",
        "Igor: You grow through battle, but do not forget that your Personas grow as well..."
    ],
    11: [
        "Igor: This is merely my meddling, but...",
        "Igor: A Persona grows through eight stages, so I recommend raising one fully once in a while.",
        "Igor: I believe something good will come of it...",
        "Igor: Also, fusion involves many factors, from subtle ones to great ones.",
        "Igor: For example, even when making the same Persona,",
        "Igor: which Spell Cards were originally combined...",
        "Igor: the order the demons were summoned...",
        "Igor: the compatibility of the demons' attributes...",
        "Igor: the positions of Terra and Luna during fusion...",
        "Igor: whether some other essence was added...",
        "Igor: I forgot to mention...",
        "Igor: During fusion, you can also add an item to cause a change.",
        "Igor: With some items the result can be predicted beforehand, but at times even I cannot predict it. Please forgive me then.",
        "Igor: But I think it is worth trying...",
        "Igor: Incidentally, jewels have the effect of changing the class within the same race of the fusion result.",
        "Igor: As for other items, I recommend trying them yourself."
    ],
}
REVIEW = {2: "prompt label 'Igor:' kept", 10: "SP/active/charged terms", 11: "Terra/Luna kept as in fusion menu"}

if __name__ == '__main__':
    apply('E0', 77, BOXES, REVIEW)
