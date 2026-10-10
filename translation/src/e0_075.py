"""E0 entry 75 - Trish, the fountain of recovery."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: [
        "Trish: Hi! I'm Trish! This is the Fountain of Recovery!",
        "Trish: In this world, it's give and take! Anything gets recovered, depending on the money!"
    ],
    1: "=What can I do for you?<FF03><FF0E>ち<FF01>",
    2: ["Trish: OK!"],
    3: ["Trish: Let's see, the recent recovery rate comes to this much, so for everyone..."],
    4: "=It'll cost 2500 yen, okay?<FF03><FF0E>　<FF01>",
    5: ["Trish: Thanks! Then I'll heal you! Pain, pain, fly away!"],
    6: ["Trish: Phew... That's all! You're all better now!"],
    7: "=Anything else?<FF03><FF0E>　<FF01>",
    8: [
        "Trish: Boo~! You don't have any money?! Trish hates people with no money!",
        "Trish: Save up some money and come back! Bye-bye!"
    ],
    9: ["Trish: Boo~! Cheapskate, cheapskate, tightwad! Don't blame me if you die!"],
    10: "=Then come again.<FF03>I'll be waiting.<FF03>Bye-bye!<FF02><FF01>",
    11: ["Trish: Boo~! You called me with nothing to do?! Get out!"],
}
REVIEW = {}

if __name__ == '__main__':
    apply('E0', 75, BOXES, REVIEW)
