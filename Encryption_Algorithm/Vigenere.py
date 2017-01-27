import random
import string

def encryption(file_name, key_len=10, key=[]):
    alphabet = string.ascii_letters
    with open(file_name, 'r') as f:
        data = f.read()
    data = data.lower()
    with open(file_name[:-4]+'_cipher.txt', 'w') as f:
        key_idx = 0
        if key == []:
            key = []
            for i in range(key_len):
                key.append(random.randrange(1, 25))
        else:
            key_len = len(key)
        for alpha in data:
            if alpha in alphabet:
                alpha = ord(alpha) + key[key_idx%key_len]
                key_idx += 1
                # if alpha > ord('Z') and alpha < ord('a'):
                #     alpha = alpha - ord('Z') + ord('A')
                if alpha > ord('z'):
                    alpha = alpha - ord('z') + ord('a')
                f.write(chr(alpha))
            else:
                f.write(alpha)
        print key,'is your key. You have to keep it.'
        return key

def decryption(file_name, key):
    alphabet = string.ascii_letters
    with open(file_name, 'r') as f:
        data = f.read()
    with open(file_name[:file_name.index('_cipher.txt')]+'_plain.txt', 'w') as f:
        key_len = len(key)
        key_idx = 0
        for alpha in data:
            if alpha in alphabet:
                alpha = ord(alpha) - key[key_idx%key_len]
                key_idx += 1
                # if alpha > ord('Z') and alpha < ord('a'):
                #     alpha = alpha + ord('z') - ord('a')
                if alpha < ord('a'):
                    alpha = alpha + ord('z') - ord('a')
                f.write(chr(alpha))
            else:
                f.write(alpha)
key = encryption('plain.txt', 1, [2])
decryption('plain_cipher.txt', key)
