#Python Morsels

def count_words(sentence):
    list_of_words = sentence.split()
    print(list_of_words)
    dict_words = {}
    for word in list_of_words:
        if not word in dict_words:
            word = word.lower()
            dict_words[word] = 1
        else:
            dict_words[word] += 1
    return dict_words

sentence = input("Write a sentence: ")
count_words(sentence)