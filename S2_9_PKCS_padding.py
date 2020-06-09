from Crypto.Cipher import AES

str1 = "YELLOW SUBMARINEdsdfd"
def PCKS_padding(str1,blocksize):
    if  isinstance(str1, bytes):
        str1=str1.decode()
    pad = blocksize - len(str1) % blocksize
    if pad == 0:
        return str1
    c = chr(pad)
    return bytes((str1+pad*c).encode())


# x=PCKS_padding(str1,20)
# print(x)

