import math

def wordfre(words):
    wordfrequency = {}
    for word in words:
        wordfrequency[word] = wordfrequency.get(word, 0) +1
    return wordfrequency.items()

def count():


