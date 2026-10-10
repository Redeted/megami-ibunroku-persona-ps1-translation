"""E1/210 end; E2 entries 0-4 - school gate and corridor chatter (hospital quest)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

p = P('ほ')
pk = P('け')
pm = P('み')
pg = P('ぎ')

E1_210 = {
    5: ["Yukino: Ah..." + p + " Outside the hole too... the town is frozen..."],
    6: ["Elly: If even the town is frozen, who is left alive..."],
    7: ["Brown: If even the town's frozen, who's left alive..."],
    8: [
        "Ayase: It's not just Ayase and the others!! No way...",
        "Ayase: Ayase did her best, right? Everyone did their best, right!? And yet such a cruel thing...",
        "Ayase: No..." + p + " I don't want that" + pk + " ..." + pk + " ..." + pk + " ..." + pk + " ..." + pk + " !!" + pk
    ],
    9: ["Yukino: What's going to happen to us" + P('で') + " from here" + P('で') + " on..."],
}

E2_0 = {
    0: [
        "Nanjo: What is it? Is the school gate blockaded or something?",
        "Nanjo: If we do not hurry, the hospital reception may close."
    ],
    1: [
        "Mark: Ugh, Vice Principal Hannya's there! I hate that guy! Let's get over there quick!"
    ],
    2: [
        "Yukino: Actually, aside from Saeko-sensei and the principal, this school doesn't have any decent teachers, does it?"
    ],
    3: [
        "Vice Principal Hanya: You lot, who said you may pass through here?",
        "Vice Principal Hanya: If you want to go out, use the school gate properly! Principal's education is too lenient, so this school is full of brats like you!",
        "Vice Principal Hanya: Now, hurry over there! I'll call a contractor right away and have this filled in!"
    ],
    5: ["Vice Principal Hanya: You! I told you not to use this!"],
}

E2_1 = {
    0: ["Himeno: U-Um... <FF0F>あ-kun, you're going to Mikage General Hospital, right...?"],
    1: [F6('う') + "Himeno Yuko<FF03>Maki's friend. A dutiful girl working part-time for her family's finances."],
    2: "=Himeno: Sorry, but" + pm + "<FF03>Sonomura-san lent me a book.<FF03>I'll return it when I visit.<FF02><FF03>Could you tell her?<FF03><FF0E>あ<FF01>",
    3: ["Himeno: U-Um... Thank you. Sorry for asking such a bother..."],
    4: ["Himeno: U-Um... Well... I asked a weird thing, sorry. Please don't mind it...!"],
    5: ["Yukino: <FF0F>あ! Don't say such stingy things!"],
    6: ["Himeno: U-Um, that book was so interesting I'm reading it again..."],
    7: ["Mark: What book is it?"],
    8: ["Himeno: U-Um... It's called \"The Door to Paradise\"..."],
    9: ["Mark: Whoa, how philosophical! Sonomura reads books like that..."],
    10: ["Nanjo: If you like it that much, why not buy the same book?"],
    11: [
        "Himeno: U-Um... It's a bit expensive, I can't buy it..." + pg + " and I want to buy new clothes for my little brother too..."
    ],
    12: ["Yukino: Nanjo, you idiot! She works part-time to help her family's finances!"],
    13: ["Mark: Well, we're in a hurry! We'll be sure to tell her!"],
    14: ["Himeno: U-Um... Did you tell Sonomura-san..."],
    15: [
        "Yukino: Sorry, not yet. But we'll go right away.",
        "Yukino: ...Hey, <FF0F>あ! Let's hurry to the hospital!"
    ],
}

E2_2 = {
    0: [
        "Nanjo: Kido... Kido Reiji, is it? At a glance he does not stand out, but it seems he does so on purpose."
    ],
    1: [
        "Mark: That girl seems to be a Reiji fan... Not that I'm jealous or anything!"
    ],
    2: [
        "Yukino: We don't have time for pointless chatter! Let's get to the hospital quick."
    ],
    3: [
        "Student: Senpai, \"Kido-san\" is in your class, isn't he?",
        "Student: Even if I go to the classroom during breaks and after school, I can't meet him, and I want to talk, but I have no chance!",
        "Student: His mysterious profile is so cool! *" + pg + " but..."
    ],
}

E2_3 = {
    0: [
        "Nanjo: Indeed, I do not think Kozai has much of a personality.",
        "Nanjo: She went out of her way to show off that she was dating Naito."
    ],
    1: [
        "Mark: Naito's good-looking and a nice guy. It pisses me off, but he's a nice guy!"
    ],
    2: [
        "Yukino: True, it was a surprise when Naito and Kozai started dating. Kozai gave no sign of it at all.",
        "Yukino: If anything, she liked Na..." + pg + " Hey, what about the hospital?"
    ],
    3: [
        "Student: Hey, why not give up on Naito-kun already? I bet they eloped! It's been two months!"
    ],
    4: [
        "Student: Naito-kun was popular with the girls, but he stopped coming to school two months ago."
    ],
    5: [
        "Student: That's a lie! Naito-kun is being fooled by Kozai-san! That girl actually has a terrible personality!"
    ],
    6: [
        "Student: Kozai-san is Sonomura-san's best friend, right? If you're visiting her, ask about that for me!"
    ],
}

E2_4 = {
    0: [
        "Nanjo: <FF0F>あ, I may have said this before, but what about the hospital? Are you not going?"
    ],
    1: [
        "Mark: Toro's got guts, huh! To say that to Ayase..." + pm + " No no, not me, thanks!"
    ],
}

if __name__ == '__main__':
    apply('E1', 210, E1_210, {})
    for n, d in ((0, E2_0), (1, E2_1), (2, E2_2), (3, E2_3), (4, E2_4)):
        apply('E2', n, d, {})
