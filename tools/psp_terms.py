"""Terminology of the PSP-script variant (build.py --psp): our own text (overworld strings, movie subtitles) is aligned with
the official PSP release. Active only when PERSONA_TEXT is set (build.py sets it for --psp); otherwise fix() is the identity."""
import os

ACTIVE = bool(os.environ.get('PERSONA_TEXT'))

# in-game strings that are ours (S2D location names / overworld dialogue); events and talk already carry the PSP text
GAME = [('Hama Mirror', 'Expel Mirror'), ('Araya', 'Alaya')]
# movie subtitles follow the English voice acting of the PSP release
FMV = GAME + [('The Rock Gate of Araya', 'The Alaya Cavern'), ('The Rock Gate of Alaya', 'The Alaya Cavern'),
              ('may enter the Rock Gate.', 'may enter the cavern.'), ("shattered the Devil's Mirror", 'broke the Demon Mirror'), ("Devil's Mirror", 'Demon Mirror'),
              ('state\nwho you are?', 'state\nyour name?')]

# opening movie (MV1C) quote cards, one list of English lines per card (the last line of card 4 is the attribution)
OPENING = [
    ['Once, I dreamt I was a butterfly.'],
    ['I forgot myself and knew only', 'my happiness as a butterfly.', 'Soon, I awoke,', 'and I was myself again.'],
    ['Did I dream that I was a butterfly?', 'Or do I now dream that I am a man?'],
    ['Yet there is a distinction between', 'myself and the butterfly.', 'This is the transformation of the physical.', '-Zhuangzi'],
]


def fix(text, table=GAME):
    if not ACTIVE:
        return text
    for a, b in table:
        text = text.replace(a, b)
    return text


def fix_fmv(text):
    return fix(text, FMV)
