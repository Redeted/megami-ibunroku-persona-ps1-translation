"""English for the ADV system messages (translation/strings/SYSMSG.tsv, tools/sysmsg.py).

Syntax = event boxes (<FF03> newline, <FF02> wait, <FF04> new page, <FF0E><param> choice); no trailing <FF01>.
Run: python translation/src/sysmsg_en.py (fills the `en` column), then python tools/sysmsg.py build.
"""
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import sysmsg  # noqa: E402

PERSONA_ERASE = "You wish to erase this<FF03>Persona, correct?"

EN = {
    0: "Not enough money.",
    1: "No more coins fit.",
    2: "Specify the quantity.",
    # 3: unreferenced duplicate of 7 (kept Japanese)
    4: "Will this Persona do?",
    5: "Persona already owned.",
    6: "Your level is too low.",
    7: "Erase this Persona?",
    8: "The game will end.<FF03>Is that OK?",
    9: "Turn off the power.<FF03>(Any button returns to<FF03>the game)",
    10: "No memory card is<FF03>inserted. Cannot save.<FF02>",
    11: "Select the memory card<FF03>slot to use.",
    12: "The memory card is<FF03>damaged. Cannot save<FF03>to it.<FF02>",
    13: "The memory card is<FF03>full. Cannot save.<FF02>",
    14: "Save complete.<FF02>",
    15: "The memory card is not<FF03>formatted.<FF02><FF04>Format it?<FF03><FF0E>　",
    16: "Formatting the<FF03>memory card.<FF03>Please wait.",
    17: "Memory card format<FF03>complete.<FF02>",
    18: "Memory card format<FF03>failed.<FF02>",
    19: "Writing data. Do not<FF03>remove the memory card.",
    20: ("Suspend data saved.<FF03>The game will end.<FF02><FF04>Choose CONTINUE to resume<FF03>from this data."
         "<FF02><FF04>Turn off the power.<FF03>(Any button: title<FF03>screen)<FF02>"),
    21: "Old data will be erased.<FF02><FF03>Overwrite?<FF03><FF0E>　",
    22: "Save Data (S) cannot<FF03>overwrite the Suspend<FF03>Data (C) area.<FF02>",
    23: "Suspend Data (C) cannot<FF03>overwrite the Save<FF03>Data (S) area.<FF02>",
    24: "Will you add an item as well?",
}

if __name__ == '__main__':
    rows = open(sysmsg.TSV, encoding='utf-8').read().split(sysmsg.NL)
    out = [rows[0]]
    for line in rows[1:]:
        c = line.split('\t')
        if len(c) >= 5 and c[0].isdigit():
            c = c[:5] + [EN.get(int(c[0]), '')]
            line = '\t'.join(c)
        out.append(line)
    open(sysmsg.TSV, 'w', encoding='utf-8', newline=sysmsg.NL).write(sysmsg.NL.join(out))
    print('filled', len(EN), 'messages')
