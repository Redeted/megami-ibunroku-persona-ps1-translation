"""E0 entry 23 - Yamaoka's death and awakening to Persona."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: [
        "Nanjo: Yamaoka... You can't die...<FF03>You wouldn't leave me behind, would you?",
        "Nanjo: Right? Yamaoka..."
    ],
    1: [
        "Yamaoka: M-My, young master...<FF03>To make such a face...",
        "Yamaoka: It ruins your handsome features...",
        "Yamaoka: Young master, you are a fine Japanese man...",
        "Yamaoka: As a man, you must one day learn to stand on your own...",
        "Yamaoka: The time that this Yamaoka can be of use to you...",
        "Yamaoka: is at an end..."
    ],
    2: [
        "Nanjo: No, no, no!<FF03>I will not permit you to leave me!",
        "Nanjo: Pull yourself together, Yamaoka!"
    ],
    3: [
        "Yamaoka: It is time to say goodbye." + P('キ') + " Young master... Just one last thing...",
        "Yamaoka: Make a promise to your Yamaoka...",
        "Yamaoka: You must become the greatest Japanese man, and carry this nation on your shoulders!" + P('テ') + " *cough* *cough* *cough*!"
    ],
    4: [
        "Nanjo: ...Yes." + P('で') + " Yes.<FF03>I will.",
        "Nanjo: I will show you that very sight.",
        "Nanjo: So until then..."
    ],
    5: [
        "Yamaoka: I expect no less, young master...<FF03>" + P('キ') + " Yamaoka will forever...",
        "Yamaoka: live on in your heart..."
    ],
    6: [
        "Nanjo: Yamaoka?" + P('で') + " ...Hey!<FF03>Please, answer me...",
        "Nanjo: Yamaokaaaaaaaaaa!"
    ],
    7: ["Yukino: Nanjo..."],
    8: ["Mark: Let's leave him alone..."],
    9: [
        "Mark: Hey, <FF0F>あ...<FF03>Did you hear those voices just now?",
        "Mark: They were saying they're me, man."
    ],
    10: [
        "Yukino: I heard it too...<FF03>Could that have been Persona-sama?"
    ],
    11: [
        "Mark: Well, they said they'd lend us their power, so it seems they're not enemies, at least.",
        "Mark: If things go well, they might even listen to what we say...",
        "Mark: Let's just call 'em \"Persona\" for now."
    ],
    12: [
        "Yukino: It certainly did feel that way, but...<FF03>I have a bad feeling about this...",
        "Yukino: Let's head outside."
    ],
    13: [
        "Yukino: I wonder if the school is okay...<FF03><FF0F>あ, let's hurry and get outside."
    ],
    14: [
        "Yukino: ...Nanjo was like a child in front of that old man...",
        "Yukino: The pain of not being able to protect someone important to you... There's nothing more painful than that."
    ],
    15: [
        "Nanjo: Yamaoka...<FF03>What should I do?...",
        "Nanjo: Without you, I'm all alone...<FF03>There will be no one left to praise me...",
        "Nanjo: No one..." + P('キ') + " No one left by my side..."
    ],
    16: [
        "Mark: To think that guy would cry...<FF03>That old man must've been really important to him..."
    ],
    17: [
        "Mark: I feel bad for Nanjo, but...<FF03>we gotta worry about the living...",
        "Mark: Let's hurry up and go save Sonomura's mom."
    ],
    18: [
        "Elly: I see, so that happened...<FF03>To lose someone important to you...",
        "Elly: Can it change a person so drastically?"
    ],
    19: ["He has already passed away..."]
}

if __name__ == '__main__':
    apply('E0', 23, BOXES)
