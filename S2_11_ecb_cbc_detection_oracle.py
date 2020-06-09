from random import choice, randint , Random
from S2_10_implement_CBC_mode import *
from S1_7_ECB_AES_Decoder import *
from S2_9_PKCS_padding import PCKS_padding


def gen_rand(size):
    key=''
    for i in range(size):
        key += chr(randint(0, 127))
    return key.encode()

def aes_type_detect(txt):
    arr_of_blocks = []
    for i in range(0, len(txt), 16):
        arr_of_blocks.append(txt[i:i + 16])
    for block in arr_of_blocks:
        if arr_of_blocks.count(block) > 1:
            return 'EBC'
    return 'CBC'


def encryption_oracle(txt):
    aa = randint(5, 10)
    aa = gen_rand(aa)
    ab = randint(5, 10)
    ab = gen_rand(ab)
    txt = aa + txt + ab
    enc_type = choice(('CBC', 'EBC'))
    if enc_type == 'CBC':
        txt = encrypt_CBC_mode(txt, gen_rand(16), gen_rand(16))
    elif enc_type == 'EBC':
        txt = PCKS_padding(txt, 16)
        txt = encrypt_AES_ECB(txt, gen_rand(16))

    res = aes_type_detect(txt)
    #return (res == enc_type)

# for i in range(10000):
#     if(encryption_oracle(b'X'*64) != True):
#         print('error')
# else:
#     print('detection works')

