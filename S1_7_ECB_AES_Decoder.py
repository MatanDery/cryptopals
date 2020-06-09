import binascii
from Crypto.Cipher import AES
import base64

def r_cipher(path):
    with open(path, 'r') as cipher_doc:
        cipher = cipher_doc.read()
        try:
            cipher = base64.b64decode(cipher)  #base64 input
        except:
            pass
        return cipher


def decrypt_AES_ECB(cipher, key):
    if(type(key)!= type(b'bytes')):
        print('enter key in bytes!!!')
        return None
    if type(cipher) == type('str'):
        cipher = cipher.encode()
    decoded = AES.new(key, AES.MODE_ECB)
    #return(decoded.decrypt(cipher).decode())
    return(decoded.decrypt(cipher))


def encrypt_AES_ECB(cipher, key):
    if(type(key) != type(b'bytes')):
        print('enter key in bytes!!!')
        return None
    if type(cipher) == type('str'):
        cipher = cipher.encode()
    enc = AES.new(key, AES.MODE_ECB)
    #return binascii.hexlify(enc.encrypt(cipher))
    return enc.encrypt(cipher)

# cipher = r_cipher('1_7_cipher_text.txt')
#
# print(decrypt_AES_ECB(cipher, b'YELLOW SUBMARINE'))
#
# print((encrypt_AES_ECB(b'YELLOW SUBMARINE',b'YELLOW SUBMARINE')))
#
# print(decrypt_AES_ECB(binascii.unhexlify('d1aa4f6578926542fbb6dd876cd20508'), b'YELLOW SUBMARINE'))