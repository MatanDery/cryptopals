from S2_9_PKCS_padding import PCKS_padding
from S1_7_ECB_AES_Decoder import *
from Crypto.Cipher import AES
import binascii
import base64

def split_to_blocksize(txt, block_size):
    arr =[]
    for i in range(0, len(txt), block_size):
        arr.append(txt[i:i+block_size]) ### is rstrip neseccery???
    return arr

def xor_same_len (s1, s2):
    # try:
    #     s1 = (s1).encode()
    # except:
    #     pass
    # s2 = (s2).encode()
    xored=[]
    for i, j in zip(s1, s2) :
        xored.append(i ^ j)
    return bytes(xored)



def encrypt_CBC_mode(txt,key,iv):
    block_size = AES.block_size
    txt = split_to_blocksize(txt, block_size)
    priv_block = iv
    final_txt=b''
    for i in txt:
        if len(i) != block_size:
            i = PCKS_padding(i, block_size)
        next_block = xor_same_len(priv_block, i)
        next_block = encrypt_AES_ECB(next_block, key)
        final_txt += next_block
        priv_block = next_block
    return final_txt


def decrypt_CBC_mode(txt,key,iv):
    block_size = AES.block_size
    txt = split_to_blocksize(txt, block_size)
    priv_block = iv
    final_txt=b''
    for i in (txt):
        next_block = decrypt_AES_ECB(i, key)
        xored_data = xor_same_len(next_block, priv_block)
        final_txt += xored_data
        priv_block = i
    return final_txt




# iv = chr(0) * AES.block_size
# iv=iv.encode()
# key = b"YELLOW SUBMARINE"
# with open ('10.txt', 'r') as f :
#     txt=base64.b64decode(f.read())
# print(decrypt_CBC_mode(txt, key, iv).decode().rstrip())
# tt= (encrypt_CBC_mode(b'k',key,iv))
# print(decrypt_CBC_mode(tt, key, iv).decode())