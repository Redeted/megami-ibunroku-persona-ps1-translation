"""E0 entry 6 - Hiremon Stone."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Nanjo: A megalithic structure... A precious cultural heritage. Who built it, and for what purpose? My interest is boundless."],
    1: ["Mark: I think our principal's a good person and all... but she's kinda girly, man."],
    2: ["Yukino: I have my part-time job today, you know... Let's hurry to the hospital and get this over with."],
    3: ["Principal Oishi: My, <FF0F>あ-kun. Are you all on a walk as well? Praying to this guardian deity for everyone to become fine adults... that has been my daily routine since I was young."],
    4: [F6('う') + "Principal Oishi<FF03>St. Hermelin High's principal. A woman who loves children and flowers."],
    5: ["Student: The Principal is a very kind teacher. She also loves flowers very much. She cares for them as if they were her own children."],
    6: ["Student: It's in such an uproar outside, yet it's so quiet here... I wonder why demons don't appear here? Is it divine protection?"],
    7: ["Hiremon Stone<FF03>A huge rock unearthed in 1963 during the school's construction. The rock is made of Samatite, but magnetic anomalies have been detected. Legend says a celestial being named Hiremon threw it down from the heavens to be the guardian stone of Mikage-cho."]
}

REVIEW = {
    7: "Samatite is a literal translation of サマタイト, possibly a fictional mineral or a typo of something else."
}

if __name__ == '__main__':
    apply('E0', 6, BOXES, REVIEW)
