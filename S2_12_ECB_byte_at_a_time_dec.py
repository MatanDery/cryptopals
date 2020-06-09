from S2_11_ecb_cbc_detection_oracle import *
from base64 import b64decode
from string import printable
from binascii import hexlify


def encryption_oracle2(txt):

    txt = PCKS_padding(txt, AES.block_size)
    txt = encrypt_AES_ECB(txt, b'abcdefg3bcDefghh')
    return txt


def detect_blocksize():
    init_len = len(encryption_oracle2(b'A' * 1))
    changed = 0
    for i in range(2, 50):
        x = len(encryption_oracle2(b'A'*i))
        if(x != init_len):
            init_len = x
            if changed != 0:
                return (i-changed)
            else:
                changed = i


aes_type = aes_type_detect(encryption_oracle2(b'A'*64))


def attack_ecb_byte_at_a_time(ciphertext):
    blocksize = detect_blocksize()
    brute_payload = ''
    try:
        aa = b64decode(ciphertext)
    except:
        aa = ciphertext
    while len(brute_payload) != len(aa):

        hidden_data = hexlify(encryption_oracle2(b'A' * 15 + aa[len(brute_payload):])).decode()
        hidden_data = split_to_blocksize(hidden_data, blocksize)
        payload = (blocksize - 1) * b'A'
        for i in printable:
            p = payload + i.encode()
            res_enc_padded = hexlify(encryption_oracle2(payload+i.encode())).decode()
            res_enc_padded = split_to_blocksize(res_enc_padded, blocksize)
            if res_enc_padded[0] in hidden_data:
                brute_payload += i
                #print(brute_payload)
                break
    return brute_payload



#print(aes_type)
# ciphertext = '''Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
#                 aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
#                 dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
#                 YnkK'''
#
# print(attack_ecb_byte_at_a_time(ciphertext))
#print(hexlify(encryption_oracle2(b'')).decode())