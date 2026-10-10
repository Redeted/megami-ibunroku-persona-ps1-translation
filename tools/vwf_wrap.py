"""Word-wrap English for VWF dialogue boxes (ADV/DNG/S2D).

Measures text with the same rules as vwf/vwf_dialog.asm:
  ASCII 0x20-0x7E -> font/vwf_width.bin advance
  any other char  -> 16 px (original FONT.BIN glyph)
  <...> tokens    -> 0 px (control codes such as <FF03>, <FF02>)
and inserts <FF03> line breaks so no line exceeds the box width.
Existing <FF03> breaks are kept; <FF02>/<FF04> (wait/next page) reset nothing
width-wise but are passed through.

Usage:
  python tools/vwf_wrap.py "text"            -> wrapped text on stdout
  python tools/vwf_wrap.py --check "text"    -> report line widths, exit 1 if any overflow
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# The box is 240 px, but vwf_dialog.asm wraps as soon as the pen reaches 240 after a glyph; an explicit
# <FF03> after such a line would then skip a second line (found 2026-10-04: Nanjo card). Max 239.
BOX_WIDTH = 239
NEWLINE = "<FF03>"
TOKEN = re.compile(r"(<[^>]+>)")

_widths = open(os.path.join(ROOT, "font", "vwf_width.bin"), "rb").read()


def char_width(c):
    o = ord(c)
    return _widths[o - 0x20] if 0x20 <= o <= 0x7E else 16


# Name insertion codes + parameter byte (written あ): <FF07> family name, <FF0F> given name (5 typed characters each,
# name entry limit), <FF08> nickname (up to 8). Counted at the widest Latin glyph (9 px) so a line never overflows with
# a long name (found 2026-10-05: "Jho/n", "sa/ys" + an empty line after the engine's own wrap).
NAME_TOKENS = {'<FF07>あ': 5 * 9, '<FF0F>あ': 5 * 9, '<FF08>あ': 8 * 9}
NAME_TOKEN = '<FF0F>あ'
NAME_WIDTH = 5 * 9


def text_width(s):
    w = 0
    for tok, tw in NAME_TOKENS.items():
        w += s.count(tok) * tw
        s = s.replace(tok, '')
    return w + sum(char_width(c) for part in TOKEN.split(s) if not TOKEN.fullmatch(part) for c in part)


def wrap_line(line, width=BOX_WIDTH):
    """Wrap one logical line (no NEWLINE inside) into a list of lines."""
    words = line.split(" ")
    out, cur = [], ""
    for w in words:
        trial = w if not cur else cur + " " + w
        if text_width(trial) <= width or not cur:
            cur = trial
        else:
            out.append(cur)
            cur = w
    out.append(cur)
    return out


def wrap(text, width=BOX_WIDTH):
    # split on explicit newlines but keep page/wait tokens attached to their line
    result = []
    for logical in text.split(NEWLINE):
        result.extend(wrap_line(logical, width))
    return NEWLINE.join(result)


def check(text, width=BOX_WIDTH):
    ok = True
    for line in text.split(NEWLINE):
        w = text_width(line)
        flag = "" if w <= width else "  <-- overflow"
        ok &= w <= width
        print(f"{w:4} px  {line}{flag}")
    return ok


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    args = sys.argv[1:]
    if args and args[0] == "--check":
        sys.exit(0 if check(args[1]) else 1)
    print(wrap(args[0]))
