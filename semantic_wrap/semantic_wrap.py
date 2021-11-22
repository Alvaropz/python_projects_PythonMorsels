#Python Morsels

import re
import sys

def semantic_wrap(sentence):
    replacements = [
    ('\n+', '\n\n'),
    ('\.\".', '."\n'),
    (' [. ]+', '\n'),
    ('[.]\s', '.\n')
    ]
    for old, new in replacements:
        sentence = re.sub(old, new, sentence.rstrip())
    sentence = sentence + "\n"
    return sentence