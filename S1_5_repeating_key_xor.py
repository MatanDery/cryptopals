import binascii


def repeting_key_xor(s1, key):
    # s1=binascii.hexlify(bytes(s1.encode()))
    # s1 = binascii.a2b_hex(s1)
    if type(s1) == type('str'):
        s1 = bytes(s1.encode())
    if type(key) == type('str'):
        key = bytes(key.encode())
    key_pos = 0
    s2 = ''
    for char in s1:
        s2 += chr(ord(chr(char)) ^ ord(chr(key[key_pos])))
        key_pos += 1
        key_pos %= len(key)
    #print(s2)
    s2 = binascii.hexlify(bytes(s2.encode()))
    #print(s2)
    return s2


# s1="Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
# s1=repeting_key_xor(s1,'ICE')
# print(s1)
