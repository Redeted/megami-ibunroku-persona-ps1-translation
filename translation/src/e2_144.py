"""E2 entries 144-165 - SEBEC building NPCs and party chatter."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

p = P('ほ'); pm = P('み'); pn = P('な'); pg = P('ぎ')

E144 = {
    1: ["Student: Ah, that's locked."],
}

E154 = {
    0: [
        "SEBEC Employee: I figured this company had something behind it, but to think they were even making biological weapons..."
    ],
    1: [
        "SEBEC Employee: The other day in the office I saw the ghost of a girl in black clothes... It must be the haunted house's curse! It must be! It has to be!!"
    ],
    2: ["Maki: The haunted house, huh. I often went to play there alone when I was little."],
    3: ["Mark: Biological weapons!?"],
    4: [
        "Nanjo: That Kandori! He has completely made the company his own. What on earth does he intend to do?"
    ],
    5: ["Ayase: Such a pretty building, but what they do is the worst."],
    6: [
        "Brown: Ghosts or biological weapons, they're a piece of cake with me around."
    ],
    7: ["Elly: Is there a house where Ghosts appear?"],
    8: ["Reiji: How long are you going to dawdle! Let's go."],
}

E155 = {
    0: [
        "Receptionist: Huh? The branch manager's room? It's on the top floor, but" + p + " what for?"
    ],
    1: [
        "Receptionist: Huh? You came from the basement?",
        "Receptionist: I heard there's a department in the basement that's secret even within the company. Could you be from there?"
    ],
    2: ["It's broken and won't open."],
    3: [
        "Maki: To think there's a secret even the company's employees don't know. What's going on with this company?"
    ],
    4: ["Mark: Look at him, drooling. Honestly."],
    5: [
        "Nanjo: They say that fools and smoke like high places. Let us go to the top floor!!"
    ],
    6: ["Ayase: SEBEC's suits" + p + " are so lame."],
    7: [
        "Brown: Even the company's own people don't know? Can't be helped" + p + " ...just kidding.",
        "Brown: Dehyahyahya."
    ],
    8: ["Elly: We have no time to play with the receptionist!"],
    9: ["Reiji: No time to waste. Let's go."],
}

E156 = {
    0: [
        "SEBEC Employee: A high school student in the same uniform as you passed through earlier too.",
        "SEBEC Employee: To have this happen on a field trip day, you've got it rough too."
    ],
    1: [
        "SEBEC Employee: Who did it! Who changed the room layout without telling me and made a storeroom!!",
        "SEBEC Employee: Even put weird toys in it! I won't forgive you!!"
    ],
    2: ["Maki: These people are victims too."],
    3: ["Mark: Let's hurry and find Kandori."],
    4: ["Nanjo: The ordinary employees seem to know nothing."],
    5: ["Ayase: One of our students is here? Who could it be?"],
    6: ["Brown: What's one of our students doing here? Not that I can talk."],
    7: [
        "Elly: Besides us, another student of ours? Who on earth could it be?"
    ],
}

E157 = {
    0: ["Maki: We have to restore the town."],
    1: ["Maki: To think Kandori can use a Persona too..."],
    2: ["Mark: If we just deal with Kandori, the town should return to normal."],
    3: ["Mark: Let's hurry and chase Kandori!"],
    4: ["Nanjo: We have no time to waste in a place like this."],
    6: ["Ayase: Let's go give Kandori what for! Hey, hurry~!!"],
    7: ["Ayase: Did that Kandori guy dream of the butterfly too?"],
    8: [
        "Brown: As long as I'm here, Kandori has no future. Dehyahyahyahya"
    ],
    9: ["Brown: So Kandori dreamed of the butterfly too."],
    10: ["Elly: Let us hurry."],
    11: ["Elly: Did Kandori also dream of the butterfly?"],
}

E160 = {
    0: ["Maki: My heart's pounding!"],
    1: ["Nanjo: It seems we are about to be able to enter the SEBEC building."],
    2: [
        "Nanjo: <FF0F>あ, if you have become afraid, you may go home. I will defeat him even alone!"
    ],
    3: ["Mark: Sonomura, I feel like your personality has changed..."],
    4: ["Elly: Kandori is in SEBEC, correct?"],
    5: [
        "Elly: We have stuck our necks into something huge." + pm + " ...It is becoming interesting!"
    ],
    6: ["Brown: My arms are itching! Let me rampage soon!"],
    7: [
        "Ayase: Hey, hey, we're just high school students, right? They wouldn't, like, blast us with guns..." + pm + " Even if it's SEBEC."
    ],
    8: ["Ayase: <FF0F>あ's a liar! Kandori was totally serious, wasn't he!"],
}

E161 = {
    4: "=It'll cost 2000 yen, okay?<FF03><FF0E>　<FF01>",
}

E163 = {
    0: [
        "Maki: That scientist said he knows my mother... But I truly have no mother, you know!"
    ],
    1: ["Nanjo: Those people..." + pg + " what research are they doing?"],
    2: [
        "Mark: A suspicious room." + pm + " So the rumors about SEBEC weren't hoaxes after all!"
    ],
    3: [
        "Elly: Whatever research they were doing, it was probably not something to be done openly."
    ],
    4: [
        "Brown: What a gloomy room! Isn't there anything useful lying around?"
    ],
    5: ["Ayase: Hmm, there's an obviously suspicious box."],
    6: [
        "Scientist: Isn't this the basement? Why is this room above ground!"
    ],
    7: [
        "Scientist: Did you meet a woman on the way here?" + pn + " Short hair, glasses...",
        "Scientist: " + pm + "Ah, Sonomura-kun! Please be safe!"
    ],
    8: ["Scientist: So Kandori used that machine..."],
    9: [
        "Scientist: What a thing! To change even the building's structure... This is beyond my calculations!"
    ],
    10: ["This door doesn't look like it will open..."],
}

E164 = {
    0: [
        "Maki: It seems a St. Hermelin student got in here before us!"
    ],
    1: ["Nanjo: Kandori... I will not forgive him!"],
    2: [
        "Mark: Do these guys feel guilty about what they did?"
    ],
    3: [
        "Elly: Did Kandori have them build a machine that creates Demons?"
    ],
    4: [
        "Brown: The story's getting complicated, and I don't like it. Even I understand some things and not others, you know!"
    ],
    5: ["Ayase: I wonder who Dr. Nicolai is."],
    6: [
        "Scientist: Are you friends of that high school student from before?",
        "Scientist: It's unfortunate" + pm + " but he..."
    ],
    7: [
        "Scientist: Dr. Nicolai intended to stop Kandori, but..." + pm + " what could we possibly do?"
    ],
    8: [
        "Scientist: We never expected demons to appear in town. But isn't it an interesting situation?" + pm + " Don't you think?"
    ],
}

E165 = {
    0: ["Maki: I feel like I've seen this scenery before."],
    1: ["Nanjo: <FF0F>あ... are your weapons ready?"],
    2: [
        "Nanjo: <FF0F>あ... are your weapons ready? This time I will not let him escape!"
    ],
    3: [
        "Mark: Almost there..." + pm + " Soon we can beat Kandori and restore the town..."
    ],
    4: ["Mark: This time I'll beat Kandori and put the town back to normal!"],
    5: ["Elly: Do you not hear the sound of some large machine?"],
    6: [
        "Brown: ..." + pm + " I wish I had a personal researcher too."
    ],
    7: [
        "Ayase: Those guys are the worst! All they think about is their own research!"
    ],
    8: [
        "Scientist: That Kandori! Staying in a safe place himself, he intends to make us demon food!"
    ],
    9: [
        "Scientist: I can't find Dr. Nicolai..." + pm + " I thought he was sneaking around by himself, but he got in good with Kandori!"
    ],
}

if __name__ == '__main__':
    for n, d in ((144, E144), (154, E154), (155, E155), (156, E156), (157, E157), (160, E160), (161, E161), (163, E163), (164, E164), (165, E165)):
        apply('E2', n, d, {})
