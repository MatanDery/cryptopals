import binascii
import base64
from Set1_Challenge1_Convert_hex_to_base64 import xor_singele_byte_brute_find_KEY
from S1_5_repeating_key_xor import repeting_key_xor
from random import randint

def r_file(loca):
    '''
    :param location:
    :return ciper from the file:
    '''
    cipher_file = open(loca, 'r+')
    cipher = cipher_file.read()
    cipher_file.close()
    return cipher


def b64d(cipher):
    '''
    :param cipher:
    :return ciper b64 decoded:
    '''
    try:
        return base64.b64decode(cipher)
    except binascii.Error:
        return cipher

def hamming_distance_calc(str1, str2):
    '''
    :param str1: string
    :param str2: string
    :return: the hamming distance - (number of different bits) between the strings
    '''
    cnt = 0
    if type(str1) == type('str'):
        str1=str1.encode()
    if type(str2) == type('str'):
        str2 = str2.encode()

    for i in range(len(str1)):
        try:
            c1 = bin(ord(chr(str1[i])))[2:]             # cuts the 0b in the start of the string
            c2 = bin(ord(chr(str2[i])))[2:]
        except:
            continue
        if len(c1) < 8:                             # ascii - 7 bits
            c1 = '0' * (8-len(c1)) + c1
        if len(c2) < 8:
            c2 = '0' * (8-len(c2)) + c2
        for j in range(len(c1)):
            if c1[j] != c2[j]:
                cnt += 1
    return cnt

def calc_keysize(cipher):
    '''
                    Calculates The Key Size by testing hamming distance
    :param cipher:
    :return: KEY SIZE
    '''
    REPETITIONS = 100
    score_dict = {}
    for KEYSIZE in range(2, 50):
        current_key_score = hamming_distance_calc(cipher[0:KEYSIZE], cipher[KEYSIZE: 2 * KEYSIZE])
        for i in range(REPETITIONS):
            x=randint(1, len(cipher)//KEYSIZE)
            y=randint(1, len(cipher)//KEYSIZE)
            current_key_score += hamming_distance_calc(cipher[KEYSIZE*x: (x+1)*KEYSIZE], cipher[y*KEYSIZE: (y+1)*KEYSIZE] )

        current_key_score = current_key_score / KEYSIZE
        score_dict[KEYSIZE] = current_key_score

    score_vals = list(score_dict.values())
    score_keys = list(score_dict.keys())
    print(score_vals)
    print(score_keys)
    min_val = min(score_vals)                     # minimum score will probably be the right key length -same xor value
    print(min_val)
    min_score = score_keys[score_vals.index(min_val)]
    print(min_score, " is the length of the key")
    return min_score

def key_size_brut(cipher, max_size):
    '''
    :param cipher:
    :param max_size:  max size of key to test
                    prints possible keys until given value
    '''
    for key_size in range(1, max_size):
        bits_by_position_array = split_cipher_to_blocks_by_key_length(cipher, key_size)
        print(real_key_calc(bits_by_position_array), '  key_size', key_size)

def split_cipher_to_blocks_by_key_length(cipher, key_size):
    '''
    :param cipher: ciphertext binery data of text (not hex)
    :param key_size: key size to try - int
    :return:  bits_by_position_array - an array split to key size number of blocks
                                       each of the blocks is xored by the same byte
    '''
    arr_original_cipher_by_key_len = []
    for i in range(0, len(cipher), key_size):
        arr_original_cipher_by_key_len.append(cipher[i:i + key_size])

    bits_by_position_array = []
    for i in range(len(arr_original_cipher_by_key_len[0])):  # the length of each block
        current_bit_string = ''
        for j in arr_original_cipher_by_key_len:  # j is each block
            try:
                current_bit_string += chr(j[i])  # Goes on each block in the location and takes it ti new string
            except IndexError:  # For number len thats not devisable by keylen
                pass
        bits_by_position_array.append(current_bit_string)  # array of chars by key to decrypt
    # print(type(bits_by_position_array))
    return bits_by_position_array

def xor_brute_singel_byte_key(s1):
    return chr(xor_singele_byte_brute_find_KEY(s1))

def real_key_calc(bits_by_position_array):
    REAL_KEY=''
    for bit_ciper in bits_by_position_array:
        bit_ciper = binascii.hexlify(bit_ciper.encode())
        REAL_KEY += xor_brute_singel_byte_key(bit_ciper)
    return REAL_KEY

def decrypt_cipher_to_clear_text(cipher, REAL_KEY):
    plain_text = repeting_key_xor(cipher, REAL_KEY)
    # print(plain_text)
    clear_text = binascii.unhexlify(plain_text)
    return clear_text.decode()




###
def crack_xor_cipher_of_file(path, brute_key=0, custume_key = None):
    '''
    :param path: path of xor encrypted file (can be base64)
    :param brute_key: if auto key detection dosen't work can brute and try by length
    :param custume_key: if you want to try a key that you found
    '''
    cipher = r_file(path)
    cipher = b64d(cipher)
    if brute_key == 0:
        key_size = calc_keysize(cipher)
        bits_by_position_array = split_cipher_to_blocks_by_key_length(cipher, key_size)
        REAL_KEY = real_key_calc(bits_by_position_array)
    else:
        key_size_brut(cipher, brute_key)
        print('Enter (path, 0, costume_key) to view cracked cipher')
        REAL_KEY = ''
    if custume_key != None:
        REAL_KEY = custume_key
    print(REAL_KEY, '\n')
    print(decrypt_cipher_to_clear_text(cipher, REAL_KEY))


crack_xor_cipher_of_file("1-6-encrydted and base64.txt")



#cipher = r_file("1-6-encrydted and base64.txt")
#cipher = r_file('ALICE.txt')
# str1 ='this is a test'
# str2 ='wokka wokka!!!'
# print(hamming_distance_calc(str1,str2))
# for char in cipher:
#     print(char)
#
# print(cipher)




# def bit_cnt(str1):   Counts ON Bits but unnecessery....
#     cnt=0
#     for char in str1:
#         char=ord(char)
#         while char != 0:
#             if char % 2 == 0:
#                 cnt+=1
#             char /= 2
#     return  cnt
