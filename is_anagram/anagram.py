#Python Morsels

'''
I want you to write a function that accepts two strings and returns True if the two strings are anagrams of each other.
'''

import unicodedata
import re

def transform(string):

    letters_list = []
    original_word = unicodedata.normalize('NFKD', string)
    original_word = original_word.encode('ascii', 'ignore')
    original_word = original_word.decode("utf-8")
    original_word_list = re.split("\W", original_word)
    for word in original_word_list:
        for letter in word.lower():
            letters_list.append(letter)
    letters_list.sort()
    return letters_list
    

def is_anagram(original_word1, original_word2):
    letters_list1 = transform(original_word1)
    letters_list2 = transform(original_word2)
    if len(letters_list1) != len(letters_list2):
        return print(False)
    for i in range(len(letters_list1)):
        if letters_list1[i] != letters_list2[i]:
            return print(False)
    return print(True)

is_anagram("tea", "eat")
is_anagram("tea", "treat")
is_anagram("sink", "skin")
is_anagram("Listen", "silent")
is_anagram("William Shakespeare", "I am a weakish speller")
is_anagram("A diet", "I'd eat")
is_anagram("Siobhán Donaghy", "Shanghai Nobody")