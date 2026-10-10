"""E0 entry 9 - Encountering Reiji."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Yukino: ..." + P('み') + " Someone's here."],
    1: ["Mark: Huh?" + P('み') + " ...Kido? You're Kido Reiji! What are you doing in a place like this?"],
    2: ["Reiji: ..." + P('た') + "..." + P('た') + "..." + P('た') + "..." + P('た') + "..."],
    3: [F6('い') + "Kido Reiji<FF03>A student who transferred here half a year ago. A quiet loner."],
    4: ["Nanjo: Hmph. What a blunt man."],
    5: ["Mark: Look who's talking."],
    6: ["Nanjo: I wonder what on earth he was thinking about in a place like this..."],
    7: ["Mark: Kido is so gloomy, man! But maybe he secretly practices magic tricks at home or something!"],
    8: ["Yukino: Kido transferred here right after the SEBEC building was built, I think... Oh right, we gotta go to the hospital."]
}

if __name__ == '__main__':
    apply('E0', 9, BOXES)
