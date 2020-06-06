import base64 as b64
import binascii

def hex_to_base64(s1):
    xstr = binascii.a2b_hex(s1) # converts string to hex
    print (xstr)
    return b64.b64encode(xstr)   # encodes the hex string

def fixed_xor_same_len (s1,s2):
    '''
                xors 2 strings together
    :param s1: first string
    :param s2: second string
    :return: xored string
    '''
    s1 = binascii.a2b_hex(s1) # converts string to hex
    s2 = binascii.a2b_hex(s2) # converts string to hex
    xored=''
    for i in range(len (s1)):
        xored += chr(ord( chr(s1[i]) ) ^ ord( chr(s2[i]) )) # xors each char in the string
    xored = binascii.hexlify(xored.encode()) # converts result to bytestring and to hex
    return xored

def create_word_list():
    '''
    :return: creates wordlist
    '''
    word_file = open('wiki-100k.txt', 'r+')    # 1000 most used english words
    word_list = []
    try:
        for i in word_file:
            word_list.append(i)
        word_file.close()
    except:
        pass
    for i in range(len(word_list)):
        word_list[i] = word_list[i].replace('\n', '')   # remove newline symbol from words
    return word_list

#WORDLIST1 = create_word_list()

def score_frequently_used_words(s1):
    '''
                                scores strings by used words
    :param s1: string to score
    :return: score by frequent words
    '''
    #s1 = s1.lower()                         # for equality
    score = 0
    for word in WORDLIST1:
        if word in s1:
            score += 1          # if the word fits in the text/part of it the score rises
            #print(word)
    return score

def score_ENGLISH_frequancy_analasys(s1):
    '''
                    scores strings by common letters frequancy
    :param s1: string to score
    :return: float of the score
    '''
    s1.lower()
    #  http://www.macfreek.nl/memory/Letter_Distribution
    letters_freq={ 'a' : 6.53216702 ,     'k' : 0.56096272    ,    'u' : 2.27579536 ,
                    'b' : 1.25888074 ,     'l' : 3.31754796     ,    'v' : 0.79611644,
                    'c' : 2.23367596 ,     'm' :  2.02656783    ,    'w' : 1.70389377 ,
                    'd' : 3.28292310 ,     'n' : 5.71201113    ,    'x' : 0.14092016 ,
                    'e' :  10.26665037,     'o' : 6.15957725   ,    'y' : 1.42766662 ,
                    'f' : 1.98306716 ,     'p' : 1.50432428     ,    'z' : 0.05128469 ,
                    'g' : 1.62490441 ,     'q' : 0.08367550     ,   ' ' : 18.28846265 ,
                    'h' : 4.97856396 ,     'r' : 4.98790855     ,
                    'i' : 5.66844326 ,     's' : 5.31700534     ,
                    'j' : 0.09752181,     't' : 7.51699827
                    }
    score = 0
    for char in s1:
        char = letters_freq.get(char)
        if char is not None:
            score += char
    return score

def xor_singele_byte_brute_find_STRING(s1):
    '''
            finds with bruteforce 1 xored bytes and returns plaintext decrypted
    :param s1: string to xor bruteforce
    :return: string that got the highest score
    '''
    s1 = binascii.a2b_hex(s1) # converts to hex
    xoredArr = []
    for i in range(256):      # 8 bit xor all possibility
        s2=''
        for j in s1:
            s2 += chr( ord(chr(j))^i )
        xoredArr.append(s2)

    scores=[]
    for xored in xoredArr:
        scores.append(score_ENGLISH_frequancy_analasys(xored)) # lists of scores from my score function
    xordic = zip (scores ,xoredArr)                      # only allows 1 per score-key
    xordic = dict(xordic)                                 # creates dict from zip
    key1 = max(xordic.keys())              # only max. (can be modified with sorted to view more options)

    #print(key1, ":", xordic[key1])          # testings
    ### Might return switched cases
    solved = xordic[key1]
    return solved  # !!!!!!!!!!!!!!!!!!!!!!!! THIS !!!!!!!!!!!!!
    # if not solved[0].isupper() and not solved.islower():
    #     print(solved.swapcase())
    #     return binascii.hexlify(solved.encode())
    # print(solved)
    # return binascii.hexlify(solved.encode())

def xor_singele_byte_brute_find_KEY(s1):
    '''
            findes with bruteforce 1 xored bytes and returns plaintext decrypted
    :param s1: string to xor bruteforce
    :return: string that got the highest score
    '''
    s1 = binascii.a2b_hex(s1) # converts to hex
    xoredArr = []
    for i in range(256):      # 8 bit xor all possibility
        s2=''
        for j in s1:
            s2 += chr( ord(chr(j))^i )
        xoredArr.append(s2)

    scores=[]
    for xored in xoredArr:
        scores.append(score_ENGLISH_frequancy_analasys(xored)) # lists of scores from my score function
    xordic = zip (scores, xoredArr)                      # only allows 1 per score-key
    xordic = dict(xordic)                                 # creates dict from zip
    key1 = max(xordic.keys())              # only max. (can be modified with sorted to view more options)
    return scores.index(key1)      # to return key of SOLUTION




#1.4 test
# def test_1_4():
#     t_f = open('1-4.txt', 'r+')
#     lis=[]
#     for line in t_f:
#         line = line.replace('\n', '')
#         lis.append(xor_singele_byte_brute(line))
#     scorlis=[]
#     for i in range(len(lis)):
#         scorlis.append(int(score_frequently_used_words(lis[i])))
#     print(lis[scorlis.index(max(scorlis))])
# test_1_4()

# 1.3
#print(xor_singele_byte_brute_find_KEY('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'))

# 1.2
# s1 = '1c0111001f010100061a024b53535009181c'
# s2 = '686974207468652062756c6c277320657965'
# print (fixed_xor_same_len(s1,s2))

# 1.1 str='49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
# print(hex_to_base64(str))