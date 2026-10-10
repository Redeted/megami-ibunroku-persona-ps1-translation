"""E2 entries 54 and 112 - Tadashi's uncle's store in Mikage Sun Mall (two story states of the same scene)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

NANJO_PRIDE = ["Nanjo: The only thing one can believe in<FF03>is one's own strength...<FF03>That is the correct way of thinking."]
MARK_KIDS = ["Mark: Kids these days<FF03>sure have their heads on straight."]
PRIVATE = ["Shopkeeper: That's my private room~<FF03>so you can't go in there~"]
NO_FEAR = ["Shopkeeper: Uncle isn't the least bit<FF03>scared of demons!",
           "Shopkeeper: That stuff is just a misunderstanding<FF03>or some kind of trick,<FF03>I'm sure of it!"]
CUSTOMER_TV = ["Customer: The TV and radio don't work, and my<FF03>parents are shaking under the futon.",
               "Customer: In the end, I've got to do something<FF03>about it myself."]

BOXES_54 = {
    0: ["Nanjo: ...Let's cure that sickness...<FF03>Dis-sick...", "Nanjo: What is this song!<FF03>It'll brainwash us!"],
    1: NANJO_PRIDE,
    2: ["Mark: So this is Tadashi's uncle's<FF03>store.", "Mark: He said his family's place is the<FF03>store in Mikage Sun Mall, right?"],
    3: MARK_KIDS,
    4: ["Yukino: A tree nobody has ever seen...<FF03>that makes you curious, huh."],
    5: ["Yukino: Sonomura's mother did well to make<FF03>it all the way to the shrine.",
        "Yukino: If she'd collapsed on the way, she'd<FF03>have become demon bait for sure..." + P('み') + "<FF03>probably."],
    6: ["Elly: I want to solve this mystery<FF03>by myself, too.", "Elly: It's a chance to put to use<FF03>everything I have learned so far."],
    7: ["Shopkeeper: Are you kids friends of my nephew<FF03>Tadashi? Then I'll give you a deal!"],
    8: NO_FEAR,
    9: ["Customer: I went to the park and there's a tree<FF03>growing there I've never seen before.<FF03>It's interesting, why not go take a look?"],
    10: PRIVATE,
    11: CUSTOMER_TV,
}

BOXES_112 = {
    0: ["Maki: I don't think we really need TV<FF03>or radio, but...<FF03>is that such a big deal?"],
    1: NANJO_PRIDE,
    2: MARK_KIDS,
    3: ["Elly: I want to solve this mystery<FF03>by myself.", "Elly: It's a chance to put to use<FF03>everything I have learned so far."],
    4: ["Brown: We go from the abandoned factory<FF03>to SEBEC, right?<FF03>Then we take down Kandori, right?",
        "Brown: And then everything is solved,<FF03>and the great me is the hero!" + P('な') + "<FF03>That's how it goes, right?"],
    5: ["Brown: Kandori...<FF03>We really should go after him,<FF03>shouldn't we..."],
    6: ["Ayase: No TV, no radio...<FF03>does that mean<FF03>radio wave interference?",
        "Ayase: Why would something like that<FF03>happen?"],
    7: CUSTOMER_TV,
    8: PRIVATE,
    9: NO_FEAR,
}

REVIEW = {}

if __name__ == '__main__':
    apply('E2', 54, BOXES_54, REVIEW)
    apply('E2', 112, BOXES_112, REVIEW)
