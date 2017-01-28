import random
import string
import os
import Convert

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

def ECB_Mode_Encryption(file_name, key = [], key_len=10, block_size=1):
    res = ''
    with open(file_name, 'r') as f:
        data = f.read()
    if len(data)%block_size != 0:
        data += '='*(block_size-len(data)%block_size)
    if key == []:
        key = []
        for _ in range(key_len):
            key.append(random.randrange(1, 25))
    else:
        key_len = len(key)
    key_idx = 0
    for idx in range(len(data)/block_size):
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

def ECB_Mode_Decryption(file_name, key = [], key_len=10, block_size=1):
    res = ''
    with open(file_name, 'r') as f:
        data = f.read()
    key_len = len(key)
    key_idx = 0
    for idx in range(len(data)/block_size):
        with open('tmp_cipher.txt', 'w') as f:
            f.write(data[idx*block_size:(idx+1)*block_size])
        decryption('tmp_cipher.txt', [key[key_idx%key_len]])
        with open('tmp_plain.txt', 'r') as f:
            res += f.read().rstrip('=')
        key_idx += 1
        os.remove('tmp_cipher.txt')
        os.remove('tmp_plain.txt')
    with open(file_name[:file_name.index('_cipher.txt')]+"_plain.txt", 'w') as f:
        f.write(res)

def CBC_Mode_Encryption(file_name, key = [], key_len = 10, block_size=1):
    res = ''
    init_vec = random.randrange(1, 2**(block_size*8))
    print init_vec
    cur_vec = init_vec
    with open(file_name, 'r') as f:
        data = f.read()
    if len(data)%block_size != 0:
        data += '='*(block_size-len(data)%block_size)
    if key == []:
        key = []
        for _ in range(key_len):
            key.append(random.randrange(1, 25))
    else:
        key_len = len(key)
    key_idx = 0
    for idx in range(len(data)/block_size):
        tmp = int(Convert.to_bin(data[idx*block_size:(idx+1)*block_size]), 2)
        tmp ^= cur_vec
        tmp = bin(tmp)[2:]
        tmp = '0'*(8*block_size-len(tmp))+tmp
        tmp = Convert.to_str(tmp)
        temp = ''
        for char in tmp:
            char = ord(char)+key[key_idx%key_len]
            temp += chr(char%256)
        key_idx+=1
        cur_vec = int(Convert.to_bin(temp), 2)
        res += temp
    with open(file_name[:-4]+"_cipher.txt", 'wb') as f:
        f.write(res)

    return (init_vec, key)

def CBC_Mode_Decryption(file_name, key, init_vec, block_size=1):
    res = ''
    cur_vec = init_vec
    with open(file_name, 'rb') as f:
        data = f.read()
    key_len = len(key)
    key_idx = 0
    for idx in range(len(data)/block_size):
        temp = data[idx*block_size:(idx+1)*block_size]
        temp = Convert.to_bin(temp)
        temp = int(temp, 2)
        tmp = ''
        for char in data[idx*block_size:(idx+1)*block_size]:
            char = ord(char)-key[key_idx%key_len]
            if char < 0:
                char += 256
            tmp += chr(char)
        tmp = int(Convert.to_bin(tmp), 2)
        tmp ^= cur_vec
        tmp = bin(tmp)[2:]
        tmp = '0'*(block_size*8-len(tmp))+tmp
        tmp = Convert.to_str(tmp)
        key_idx+=1
        res += tmp
        cur_vec = temp
    with open(file_name[:file_name.index('_cipher.txt')]+'_plain.txt', 'w') as f:
        f.write(res)
