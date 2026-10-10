"""E1 entries 147-149 - the story of Saeko and Tomomi; the Queen of the Night appears."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

p = P('ほ')
ps = P('そ')
pk = P('か')

E147 = {
    8: [
        "Elly: So that is why the Queen called Sensei" + p + " \"Saeko-san\"" + p + " But why would her best friend possess her?"
    ],
    9: [
        "Nanjo: I see. That explains why she called her \"-san.\" But why would a best friend try to sacrifice her?"
    ],
    10: [
        "Saeko-sensei: That she thought of me like that... Sometimes we hurt people without noticing" + p + "..." + p + " ..." + p
    ],
}

E148 = {
    0: [
        "Saeko: Congratulations on getting the Snow Queen role. At the very end of our school life, you finally beat me, Tomomi."
    ],
    1: [
        "Tomomi: Thanks. I'll do my best for Saeko-san's share too. But I'm uneasy" + p + " that mask...",
        "Tomomi: Is it true everyone who has played the Queen has been cursed?"
    ],
    2: [
        "Saeko: What are you saying! Of course that's a superstition!",
        "Saeko: If you always keep a cheerful heart, even a curse will find it uncomfortable and run away!",
        "Saeko: You get swept away by rumors right away. That's your bad point, Tomomi!"
    ],
    3: ["Tomomi: Saeko-san is great... So strong."],
    4: [
        "Saeko: Get a grip! You won the big role by competing with me, so you'd better look happier or I'll have no standing!!"
    ],
    5: ["Tomomi: Y-" + p + " You're right."],
    6: ["Drama Club Member: Whaaat~!! Senpai, Saeko-san is tricking you!"],
    7: ["Tomomi: Huh!? Tricking me?"],
    8: [
        "Drama Club Member: You don't know!? Saeko-san withdrew her candidacy for the Snow Queen role herself.",
        "Drama Club Member: Everyone's saying it. Because she feared the mask's curse, she pushed the Snow Queen role onto Tomomi-senpai" + p + ", they say."
    ],
    9: [
        "Tomomi: Withdrew..." + p + " Because she feared the curse...? No way!?",
        "Tomomi: Even if she really withdrew, she surely just thought of me!",
        "Tomomi: Even though I'm in the same year as Saeko-san..." + p + " I've never been given a better role than Saeko-san."
    ],
    10: [
        "Drama Club Member: So she wanted to let you have the spotlight at least at the end? Tomomi-senpai is so naive.",
        "Drama Club Member: The Snow Queen is the most eye-catching role. There's no way she'd give it up to someone else for no reason."
    ],
    11: ["Tomomi: ......"],
    12: [
        "Saeko: What's wrong, Tomomi? Calling me out like this. What are you hiding for?",
        "Saeko: Tomorrow's performance, do your best for my share too. I'm counting on you."
    ],
    13: ["Tomomi: ......Y-" + p + " ou" + p + " ......" + p + " ...are..."],
    14: ["Saeko: What? I can't hear you!"],
    15: [
        "Tomomi: Y-" + p + " ou-" + p + " ...it's" + p + " your" + p + " fault......!!",
        "Tomomi: Your" + ps + " your" + ps + " your" + ps + "<FF03>fault, it iiis...!!"
    ],
    16: ["Saeko: Huh!? What's wrong, Tomomi! Calm down!!"],
    17: ["Tomomi: Beca-" + p + " use you" + p + " forced the mask on me"],
    18: ["Saeko: Tomomi..." + p + " Are you okay? What's wrong with the mask?"],
    19: [
        "Tomomi: The mask, the mask" + p + "<FF03>suddenly won't come off, won't" + p + " come off" + p + "<FF03>it suddenly" + p + " got hot," + p + " hot," + p + " hot",
        "My face, my face goes sizzle," + p + " sizzle" + p + " sizzling sound",
        "Your" + p + " your" + p + " your fault!"
    ],
    20: ["Tomomi: It's your fault!!"],
    21: ["Saeko: Kyaaaaa" + pk + "aa" + pk + "aa" + pk + "aa" + pk + "aa" + pk + " !" + pk + " !"],
}

E149 = {
    0: [
        "Ayase: That's not Sensei's fault at all. You didn't force it on her, right? It's just that Tomomi girl's misunderstanding."
    ],
    1: [
        "Saeko-sensei: Maybe so. But" + p + " I can't say for sure it was.",
        "Saeko-sensei: Perhaps somewhere in my heart I was basking in superiority. Playing the best friend" + p + " and being kind only on the surface.",
        "Saeko-sensei: Maybe I didn't truly care about Tomomi's feelings. I was just drunk on myself for being so devoted to others...",
        "Saeko-sensei: and maybe I was hurting her in return."
    ],
    2: ["Yukino: Sensei..."],
    3: ["Saeko-sensei: It's not the mask's curse! What made her like that was..."],
    4: ["Yukino: Stop it!!"],
    5: ["Saeko-sensei: ..." + p + " ..."],
    6: ["Ayase: Whoa" + p + " ..." + p + " It's cold......"],
    7: ["Nanjo: !! What is this..."],
    8: ["Elly: Oh! How can this be..."],
    9: ["Yukino: What is it?"],
    10: [
        "Nanjo: We defeated the Snow Queen and saved Saeko-sensei... yet the school has not returned to normal!!"
    ],
    11: [
        "Elly: We defeated the Snow Queen and saved Saeko-sensei, but the school is still frozen!!"
    ],
    12: ["Ayase: Now that you mention it" + p + " ..." + p + " ...the color of the sky is still weird too."],
    13: ["Voice: Kukukuku... It must be so cold... Ahahahaha..."],
    14: ["Saeko-sensei: W-" + p + " What is it!?"],
    15: [
        "Brown: Aaaaaaahhh. No way, that's not allowed~ We just beat her!!"
    ],
    16: ["Elly: What!?"],
    17: [
        "Queen: The Tomomi within me" + p + ", the Tomomi who held human weakness, is dead. I thank you.",
        "Queen: I have left my host Tomomi and left the mask, my vessel, and am now free.",
        "Queen: With this, I become complete. As the complete Queen of the Night, I shall cover this world with white and black, nothingness and despair."
    ],
    18: ["Yukino: What did you say!?"],
}

if __name__ == '__main__':
    for n, d in ((147, E147), (148, E148), (149, E149)):
        apply('E1', n, d, {})
