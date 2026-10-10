"""E0 entry 7 - Student Council."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Nanjo: To be unable to handle even the meager power of a Student Council President... He is a man of small caliber."],
    1: ["Mark: I just don't like the Student Council President, man... Aaah, I wanna hurry up and go to Sono..." + P('ぶ') + " No, no, I wanna go to the hospital!"],
    2: ["Yukino: It might be way better to make one of the council members president instead of the current one."],
    3: ["Student Council President: Sorting old records isn't the job of the Student Council President! If it were Kandori-senpai, he would have proudly refused a job like this... That's right. To get closer to his level, I will firmly refuse as well!"],
    4: [F6('い') + "Student Council President<FF03>President of St. Hermelin High's student council. It seems he isn't very dedicated to his work."],
    5: ["Council Member: Our president just gives orders and doesn't do anything. Who made him president anyway? If I were president, I'd work a guy like him to the bone!"],
    6: ["Council Member: He's actually like that, but somehow he's good at cutting corners and the teachers like him... He's never even been scolded! The world is so unfair!"],
    7: ["Council Member: The president says he's aiming to be like the 18th president, Kandori-senpai. Huh? You don't know the branch manager of SEBEC? He's an alumnus of our school. He's an amazing person who became a branch manager of a huge company while still young!"]
}

if __name__ == '__main__':
    apply('E0', 7, BOXES)
