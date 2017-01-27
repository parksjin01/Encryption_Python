import random
import string
import os

def encryption(file_name, key_len=10, key=[]):
    alphabet = string.ascii_letters
    try:
        with open(file_name, 'r') as f:
            data = f.read()
    except:
        data = file_name
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
                if alpha > ord('z'):
                    alpha = alpha - ord('z') + ord('a')
                f.write(chr(alpha))
            else:
                f.write(alpha)
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
                if alpha < ord('a'):
                    alpha = alpha + ord('z') - ord('a')
                f.write(chr(alpha))
            else:
                f.write(alpha)

def ECB_Mode_Encryption(file_name, key = [], key_len=10, block_size=1, algorithm="Vigenere"):
    res = ''
    with open(file_name, 'r') as f:
        data = f.read()
    if len(data)%block_size != 0:
        data += 'z'*(block_size-len(data)%block_size)
    if key == []:
        key = []
        for _ in range(key_len):
            key.append(random.randrange(1, 25))
    else:
        key_len = len(key)
    key_idx = 0
    for idx in range(len(data)/block_size-1):
        with open('tmp', 'w') as f:
            f.write(data[idx*block_size:(idx+1)*block_size])
        encryption('tmp', 1, [key[key_idx%key_len]])
        with open('_cipher.txt', 'r') as f:
            res += f.read()
        key_idx += 1
    os.remove('tmp')
    os.remove('_cipher.txt')
    with open(file_name[:-4]+'_cipher.txt', 'w') as f:
        f.write(res)
    return key

def ECB_Mode_Decryption(file_name, key = [], key_len=10, block_size=1, algorithm="Vigenere"):
    res = ''
    with open(file_name, 'r') as f:
        data = f.read()
    key_len = len(key)
    key_idx = 0
    for idx in range(len(data)/block_size-1):
        with open('tmp_cipher.txt', 'w') as f:
            f.write(data[idx*block_size:(idx+1)*block_size])
        decryption('tmp_cipher.txt', [key[key_idx%key_len]])
        with open('tmp_plain.txt', 'r') as f:
            res += f.read().rstrip('z')
        key_idx += 1
        os.remove('tmp_cipher.txt')
        os.remove('tmp_plain.txt')
    with open(file_name[:file_name.index('_cipher.txt')]+"_plain.txt", 'w') as f:
        f.write(res)
