"""E2 entries 186-192 - other-world shops and the Black Market."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

pm = P('み'); pn = P('な'); pg = P('ぎ')

E186 = {
    8: [
        "Townsperson: Until recently, we only had to watch out for demons when the girl in black showed up.",
        "Townsperson: But demons have started prowling even without the girl, and I'm anxious."
    ],
    9: [
        "Townsperson: Everyone fears demons, but I don't think there's any need to worry. I feel like we won't be attacked."
    ],
    10: [
        "Shopkeeper: Do you kids know my good-for-nothing son? A cute girl transferred into his class, but they don't get along and won't even speak to each other" + pm + " Ah, medicine. Yes, yes."
    ],
    11: [
        "Shopkeeper: Oops, if you open that, my pet Froggies will come out! Ha ha, fooled you!"
    ],
}

E188 = {
    0: [
        "Maki: Coming to a place like this is a relief. It feels like I'm an ordinary high school girl again."
    ],
    1: ["Maki: We're going to the forest, right? What on earth is the key?"],
    2: ["Maki: Let's hurry back to that castle."],
    3: [
        "Nanjo: There is no use being impatient. Advancing steadily one step at a time is, in the end, the fastest way."
    ],
    4: [
        "Nanjo: Now that we have obtained the \"Hama Mirror,\" though I am reluctant, shall we go to the subway?"
    ],
    5: [
        "Mark: No burgers, no fries, no chicken, no shakes? That's no fun! They've got nothing to sell and the clerk's acting all high and mighty!"
    ],
    6: [
        "Mark: That shady old guy can't be trusted, but should we look for it anyway? That \"Hama Mirror\" thing."
    ],
    7: [
        "Elly: I rarely made detours before. It is quite fun, this kind of thing too!"
    ],
    8: [
        "Elly: Let us go to the shrine. I am very curious what kind of person is waiting there!"
    ],
    9: [
        "Brown: A food shop without food, how's that for irony? Nahaha! Damn, I'm hungry~"
    ],
    10: ["Brown: Let's go check out the shrine soon."],
    11: ["Ayase: Looks like Ayase's friends haven't come."],
    12: [
        "Ayase: Let's go to the shrine~ They might have night stalls out" + pm + " ...Ayase wants candied apples."
    ],
    13: [
        "Reiji: I don't like it. Standing here, my body starts itching all over."
    ],
    14: [
        "Reiji: Aren't we going to the shrine? That Kurouri guy probably isn't lying."
    ],
    15: [
        "Clerk: We've got no food! But if you rest here, your friend's head will clear and he'll surely remember the next objective."
    ],
    16: [
        "Townsperson: Yesterday I ran into a demon, and it peered into my face intently and then just went on its way. It was almost like" + pm + " it was looking for someone."
    ],
    17: [
        "Townsperson: You folks seem somehow different from us. I can't put it well, but..."
    ],
    18: [
        "Townsperson: You're a really nice person. I can tell. Your friends surely think so too."
    ],
    19: [
        "Townsperson: Behind the scenes you do quite bad things, don't you? Don't forget that there are people hurt because of it!"
    ],
}

E189 = {
    0: ["Maki: That mask is cute! I'd like to decorate my room with it."],
    1: ["Nanjo: <FF0F>あ, do not get fooled into buying anything suspicious."],
    2: ["Mark: I've been wondering about those two's relationship lately..."],
    3: [
        "Elly: So Pretty! This is a Japanese good-luck charm, is it not?"
    ],
    4: ["Brown: Is this a dog? A beckoning dog? Something's different..."],
    5: ["Ayase: Ayase wants this! Hey, buy it for me!"],
    6: [
        "Reiji: If the shopkeeper's suspicious, even the ornaments are suspicious."
    ],
    7: [
        "Townsperson: Demons have increased lately. But they feel different from the ones the girl in black brought before."
    ],
    8: [
        "Tsurunkamen: Hohohoho... Welcome. What kind of goods do you need?"
    ],
    9: [
        "Kamentsurun: Hohohoho... I love jewels above all. I am currently running a bargain exchange of your jewels for my hidden treasures. Care to try?"
    ],
}

E190 = {
    0: ["Maki: Frogs... I wonder if he likes them."],
    1: [
        "Nanjo: Will the day come when convenience stores in our town sell weapons too?"
    ],
    2: [
        "Mark: Tch, nothing but weapons. It's kinda lonely without a book corner."
    ],
    3: ["Elly: What happened here, I wonder?"],
    4: [
        "Brown: Look at this picture, it's got wit!" + pm + " ...Huh? It's the real deal?"
    ],
    5: ["Ayase: Is this... surely not..."],
    6: ["Reiji: It looks a lot like the Nazca lines."],
    7: [
        "Clerk: Hi, everyone, how's it going? Welcome to Yin & Yan! So, what will you buy?"
    ],
    8: [
        "Clerk: Oh no, are you maybe a robber? I don't like bad kids like that! *"
    ],
    9: [
        "Customer: Have you met Lady Harem Queen yet? The Queen is extremely sensitive!",
        "Customer: Listen, whatever you do, don't hurt the Queen's feelings!"
    ],
    10: [
        "Customer: They say the Queen's gone! I can finally relax!"
    ],
}

E191 = {
    0: [
        "Maki: We're going to meet the person called the Queen, right?" + pn + " ...I hope she's not scary."
    ],
    1: ["Maki: I think Chisato's paintings aren't bad either..."],
    2: ["Maki: Chisato and Naito-kun looked so good together."],
    3: [
        "Nanjo: The Queen, huh. Come to think of it, Aki said something about a \"cute girl.\""
    ],
    4: [
        "Nanjo: To think Kozai was the Harem Queen. Well, it does suit her."
    ],
    5: [
        "Nanjo: So we finally have Kandori's whereabouts. But a \"castle\"... how absurd."
    ],
    6: [
        "Nanjo: I never thought that at this age I would go exploring a \"haunted house.\" It was not allowed when I was a child..."
    ],
    7: [
        "Mark: Even the armor shop has an atmosphere that fits this town."
    ],
    8: ["Mark: ........." + pm + " Be considerate of Sonomura."],
    9: [
        "Mark: Hey, don't you feel like we did something unnecessary?"
    ],
    10: [
        "Elly: Afros are in fashion, it seems. Maybe I should try an afro too."
    ],
    11: ["Elly: I can somewhat understand Kozai-san's feelings."],
    12: [
        "Elly: Kozai-san and I are a little alike" + pm + " ...Is that unexpected?"
    ],
    13: [
        "Brown: They say if the Queen likes you, you can live easy! Leave it to me! Any girl will be knocked down by my charm!"
    ],
    14: [
        "Brown: Kozai's eyes were kinda blue around them..." + pm + " ...It was scary!"
    ],
    15: [
        "Brown: A cheeky brat like that living in a castle? No way! A castle suits a sophisticated person like me!"
    ],
    16: ["Ayase: A Queen, huh... Ayase wants to be one once, too. *"],
    17: [
        "Ayase: That Kozai, not even knowing the real Sonomura is suffering..."
    ],
    18: [
        "Ayase: She's so pretty, what's Kozai unhappy about? Ayase is fine as she is.",
        "Ayase: Not that I'm pretty, but freckles are cute too, and I've got that funny face thing, right?"
    ],
    19: [
        "Reiji: Anyway, unless we can get out of here, we can't move on, is that it?"
    ],
    20: ["Reiji: Honestly, both you and Sonomura are softies, hopeless."],
    21: [
        "Reiji: At times like this, whatever others say won't help... You've got to deal with it yourself."
    ],
    22: [
        "Clerk: Won't you become strong and beautiful like the Queen with our armor too?"
    ],
    23: [
        "Clerk: Essential for surviving this world! Leave armor to our shop!"
    ],
    24: [
        "Customer: We got trapped in this market anyway! We might as well humor the Queen and live happily!"
    ],
    25: [
        "Customer: We don't have to humor the Queen anymore, right? Though it's kind of lonely somehow!"
    ],
}

E192 = {
    0: ["Maki: You know, <FF07>あ-kun" + pm + " ...no, never mind."],
    1: ["Nanjo: Black Market..." + pg + " a name fitting this ruined town."],
    2: ["Mark: The doctor's the same over here too, thank goodness."],
    3: ["Elly: I am relieved the Doctor is a decent person..."],
    4: [
        "Brown: The doctor's normal... I was so worried he might be a skinhead with an eyepatch or something!"
    ],
    5: ["Ayase: W-" + pm + " We won't get shots, right..."],
    6: [
        "Reiji: What, I was expecting a doctor with more impact."
    ],
    7: [
        "Nurse: I'm so happy all thanks to Lady Harem Queen.",
        "Nurse: Let's thank the Queen together. Lady Queen, thank you so much!"
    ],
}

if __name__ == '__main__':
    for n, d in ((186, E186), (188, E188), (189, E189), (190, E190), (191, E191), (192, E192)):
        apply('E2', n, d, {})
