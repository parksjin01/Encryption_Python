import string

def word_frequency(file):
    word = {}
    ascii = string.ascii_letters
    with open(file, 'r') as f:
        text = f.read()
        for char in text:
            char = char.lower()
            if char in ascii:
                try:
                    word[char] += 1
                except:
                    word[char] = 1
    return word
