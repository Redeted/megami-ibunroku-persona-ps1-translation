"""E0 entry 5 - Drama club."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from tl_lib import apply, P, F6

BOXES = {
    0: ["Student: President, we haven't decided what to perform for the school festival yet, have we?"],
    1: ["Student: I heard there was a traditional play performed here long ago. Are we not doing that? I believe it was the Snow..."],
    2: ["President: No! That is forbidden!" + P('ょ') + " ...We will decide on a play soon, so just wait a little longer."],
    3: ["Nanjo: By \"Snow...\" do you mean... the \"Snow Queen\"?"],
    4: ["Mark: Forget about the play! Just let me dance!"],
    5: ["Yukino: I've never heard of this school having a traditional play before."],
    6: ["Student: The trophy from nine years ago is missing. We should have won the contest that year, too, but the one from that year is the only one gone. It's reeeally suspicious. Seriously."],
    7: ["Student: Didn't the President seem a little strange? Why was she so angry?"],
    8: ["President: What is it? Do you want to join the club? If not, you're in the way, so could you please leave?"]
}

if __name__ == '__main__':
    apply('E0', 5, BOXES)
