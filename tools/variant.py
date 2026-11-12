"""Build variant for the data tools: PERSONA_VARIANT = base / qol / easy, set by tools/build.py only.

The base build is the translation only. The QoL items and skills (Clean Salt = item 110, Emergency Exit = item 111,
Estoma = skill record 111, the real Traesto description) live in the translation TSVs; for the base build the
rows below are replaced by the plain translation of the original data (unused "Last Abble / Mabble Pie", the
unused Trafuri, the placeholder descriptions). Run outside build.py (dump, qa, ...) nothing is replaced, so the
TSVs are never rewritten with these values.
"""
import os

VARIANT = os.environ.get('PERSONA_VARIANT')

# table -> {row index: {column: base value}}; columns as in the TSV (3 = en, 4 = full for ITEMS)
BASE_ROWS = {
    'ITEMS': {110: {3: 'LAST ABBLE', 4: 'Last Abble Pie'},
              111: {3: 'LAST MABBL', 4: 'Last Mabble Pie'}},
    'SKILLS': {111: {3: 'Trafuri'}},
    'DESCS': {110: {3: 'No Trafuri'},
              111: {3: 'No Traesto'},
              267: {3: 'This is the last abble pie'},
              268: {3: 'This is the last mabble pie'}},
}


def cell(table, idx, col, value):
    """The value of TSV cell (idx, col) for this build: the base value in the base build, else value."""
    if VARIANT == 'base':
        return BASE_ROWS.get(table, {}).get(idx, {}).get(col, value)
    return value
