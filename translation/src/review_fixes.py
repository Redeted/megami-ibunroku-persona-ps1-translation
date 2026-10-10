"""2026-10-09: corrections found while closing translation/review.tsv. Same Japanese -> same English everywhere,
so the replacements run on all event TSVs (like width_fixes.py).
"""
import glob
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
NL = '<FF03>'

REPLACE = [
    # E0/101/19: かとうが　まけようが = 勝とうが負けようが ("whether you win or lose"), not a person named Kato
    ("Aki: He said to leave you alone" + NL + "even if Kato loses!",
     "Aki: He said to just leave you be" + NL + "whether you win or lose!"),
]


def replace_all():
    n = 0
    for f in sorted(glob.glob(os.path.join(ROOT, 'translation', 'events', 'E?.tsv'))):
        s = open(f, encoding='utf-8').read()
        t = s
        for old, new in REPLACE:
            n += t.count(old)
            t = t.replace(old, new)
        if t != s:
            open(f, 'w', encoding='utf-8', newline=chr(10)).write(t)
    print('replaced', n, 'occurrences')


if __name__ == '__main__':
    replace_all()
