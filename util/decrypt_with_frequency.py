import string
import numpy as np
import operator

def decrypt_with_frequency(file):
    res = ''
    with open(file, 'r') as f:
        data = f.read()
    word = word_frequency(file)
    word = sorted(word.items(), key=operator.itemgetter(1), reverse=True)
    char = {}
    idx = 0
    sequence = list('etaoinshrdlcumwfgypbvkjxqz')
    for tmp in word:
        char[tmp[0]] =sequence[idx]
        idx += 1

    for c in data:
        if c in char.keys():
            res += char[c]
        else:
            res += c
    print res
