#Python Morsels

import re

def count_words(sentence):
    list_of_words = re.split("[^\w']|\s+", sentence)
    dict_words = {}
    for word in list_of_words:
        if word != "":
            if not word in dict_words:
                word = word.lower()
                dict_words[word] = 1
            else:
                dict_words[word] += 1
    return dict_words