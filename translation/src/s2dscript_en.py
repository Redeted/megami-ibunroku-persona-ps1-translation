"""English for the overworld dialogue boxes (translation/strings/S2DSCRIPT.tsv, tools/s2dscript.py).

Syntax = event boxes (<FF03> newline, <FF02> wait, <FF04> new page; <FF05> = pause, its two parameter bytes are copied from the
Japanese; <FF07>あ / <FF0F>あ = names, keep the あ); no trailing <FF01>.
Run: python translation/src/s2dscript_en.py (fills the `en` column), then python tools/s2dscript.py build.
"""
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import s2dscript  # noqa: E402

NANJO_POLICE = "Nanjo: <FF0F>あ<FF03>This is the police station?<FF03>Keep your jokes to your face!<FF02>"
NANJO_DUMP = "Nanjo: <FF0F>あ<FF03>You have no business in a filthy<FF03>place like this, do you?<FF02>"
MARK_JERK = "Mark: Nanjo, you jerk...<FF02>"
BLACK = "Man in Black: Beyond this point is<FF03>SEBEC's jurisdiction!<FF03>Passage is forbidden!<FF02>"
MAKI_MAD = "Maki: Who does he think he is?!<FF03>Seriously, that makes me so mad!<FF03>Let's go, everyone! Bleeeh!<FF02>"
MARK_AMNESIA = "Mark: What are you talking about,<FF03>Sonomura? This is the hospital you<FF03>were in! Seriously, amnesia?<FF02>"
MAKI_ALRIGHT = "Maki: ...<FF05>Ah ha! Yeah,<FF03>I'm starting to feel that way too!<FF03>Come on, let's hurry!<FF02>"
NANJO_DOTS = "Nanjo: ...<FF02>"
MARK_DUMP = "Mark: Nothing left for us in this<FF03>gloomy dump, right? Let's go<FF03>pound Kandori already!<FF02>"

EN = {
    0: "Nanjo: What is it, <FF0F>あ?<FF03>Still have business with the<FF03>Archives?<FF02>",
    1: ('Yukino: "History of Araya Shrine"...<FF02>"This shrine enshrines the god<FF03>who dwells in the human heart."'
        '<FF03>So it says.<FF02>'),
    2: "Maki: Araya Shrine...<FF05><FF03>What a strange name!<FF03>What blessings does it bring?<FF02>",
    3: ("Mark: This ruin isn't open to the<FF03>public, you know.<FF02><FF03>Not like there's anything to see<FF03>"
        "in there even if it were.<FF02>"),
    4: "Maki: Huh? Couldn't we go in<FF03>here before...?<FF02>",
    5: ("Elly: What a shame, having such a<FF03>splendid ruin so close by and<FF03>not being able to go inside.<FF02>"),
    6: ("Yukino: Hey, <FF0F>あ!<FF03>You're not running away, are you?<FF02><FF03>Saeko-sensei will chew us out<FF03>"
        "again if she finds out!<FF02>"),
    7: "Nanjo: <FF0F>あ...<FF05><FF03>Are you trying to run away?<FF03>Running will solve nothing.<FF02>",
    8: "The Archives are closed...<FF02>",
    9: "Nanjo: Just as I thought.<FF03>No one can escape from this town.<FF02>",
    10: "Elly: She has gone completely<FF03>hysterical. How awful.<FF02>",
    11: ("Ayase: Ayase hates waiting to be<FF03>rescued like that, y'know? Let's<FF03>hurry to the abandoned factory.<FF02>"),
    12: "Man: Let me out of here!<FF03>Why can't I get out of town?!<FF03>Somebody help me, c'mon!<FF02>",
    13: "The Himeno residence is closed...<FF02>",
    14: "Elly: No, <FF07>あ!<FF03>We have to get Maki's mother to<FF03>the school right away!<FF02>",
    15: "St. Hermelin High School has been<FF03>turned into a castle of ice...<FF02>",
    16: ("Man: Hey, a cute girl wearing the<FF03>same uniform as you fellas went<FF03>into the subway.<FF02>"),
    17: "The school gate is shut tight...<FF02>",
    18: NANJO_POLICE,
    19: NANJO_DUMP,
    20: MARK_JERK,
    21: ("Yukino: <FF0F>あ!<FF03>You really do love wandering<FF03>around, huh?<FF02><FF04>But pick your time and place!<FF03>Geez...<FF02>"),
    22: BLACK,
    23: MAKI_MAD,
    24: "Maki: ...Wasn't this<FF05><FF03>a castle...?<FF02>",
    25: MARK_AMNESIA,
    26: MAKI_ALRIGHT,
    27: NANJO_DOTS,
    28: "Mark: Nothing left for us in this<FF03>gloomy dump, right?<FF04>Let's go pound Kandori already!",
    29: NANJO_POLICE,
    30: "Maki: Huh?<FF03>I thought this was a castle...<FF02>",
    31: NANJO_DUMP,
    32: MARK_JERK,
    33: "Maki: <FF07>あ-kun,<FF03>was the police station always a<FF03>building like this?<FF02>",
    34: BLACK,
    35: MAKI_MAD,
    36: ("Yukino: Who does he think he is...?<FF03><FF0F>あ, this is making me sick.<FF03>Let's go.<FF02>"),
    37: ("Maki: That's weird...<FF03>Wasn't this a castle...? We're not<FF03>even supposed to get in here...<FF02>"),
    38: MARK_AMNESIA,
    39: MAKI_ALRIGHT,
    40: NANJO_DOTS,
    41: MARK_DUMP,
    42: "Maki: Going somewhere else?<FF03>Then let's meet up with<FF03>everyone first, okay?<FF02>",
    43: "Nanjo: Only you and Sonomura<FF03>are supposed to be able to<FF03>enter here.<FF02>",
    44: ("Maki: This was a flower garden, but<FF03>it became a forest and now we<FF03>can't go in.<FF02>"),
    45: ("Mark: This place should've had the<FF03>haunted house torn down for<FF03>SEBEC, right?<FF04>But it's still standing, so...<FF03>did we time-slip after all?<FF02>"),
    46: "Nanjo: ......<FF02>",
    47: "Maki: Over here it's always<FF03>been like this, though...<FF02>",
    48: "Mark: Hey!<FF03>Is this any time to be here?<FF03>Don't we have better things to do?<FF02>",
    49: "Maki: That girl<FF03>is all right now.<FF03>Come on, we have to hurry!<FF02>",
    50: "Mark: Hey, hey, we're leaving town!<FF03>Aren't we going to the hospital?<FF02>",
    51: "Nanjo: What do you intend to do<FF03>outside of town? We are going<FF03>to the hospital.<FF02>",
    52: ("Yukino: <FF0F>あ...<FF03>Cut it out, or I'll snap.<FF03>What's the point of leaving town?!<FF02><FF03>Geez...<FF02>"),
    53: "Nanjo: <FF0F>あ<FF03>Why go back to school? Kandori<FF03>is in the east of town!<FF02>",
    54: ("Mark: Hey hey hey hey hey! Is this<FF03>any time to wander around?<FF03>You're way too laid-back!!<FF04>The haunted house isn't that way!<FF02>"),
    55: ("Man: Oh my God!<FF03>The east half of town is gone!<FF04>A lot of the inside here seems to<FF03>have vanished too, so going in<FF03>is dangerous!<FF02>"),
    56: "Maki: What is this?!<FF03>The school is gone!!<FF03>What about Yuko and everyone?!<FF02>",
    57: "Nanjo: Is this also an effect of the<FF03>Deva System...?<FF03>Kandori, what a ridiculous stunt!<FF02>",
    58: "Maki: It's true!<FF03>The school is gone!<FF02>",
    59: ("Nanjo: The Deva System is truly<FF03>fearsome.<FF05> But...<FF03>Is this also Kandori's intent?<FF02><FF04>"
         "Either way, this is not a problem<FF03>we can deal with directly.<FF02>"),
    60: ("Mark: Tch.<FF05><FF03>Then we'll just make that guy<FF03>put it back.<FF02><FF03>We'll teach him what happens when<FF03>"
         "you mess with Hermelin.<FF02>"),
}

if __name__ == '__main__':
    rows = open(s2dscript.TSV, encoding='utf-8').read().split(s2dscript.NL)
    out = [rows[0]]
    for line in rows[1:]:
        c = line.split('\t')
        if len(c) >= 5 and c[0].isdigit():
            c = c[:5] + [EN.get(int(c[0]), '')]
            line = '\t'.join(c)
        out.append(line)
    open(s2dscript.TSV, 'w', encoding='utf-8', newline=s2dscript.NL).write(s2dscript.NL.join(out))
    print('filled', len(EN), 'boxes')
