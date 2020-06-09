
FILE_PATH = '1_8_task.txt'

def AES_Detector(txt):

    count_reps_in_arr = 0
    maxreps = 0
    suspect_block=''
    for cipher in txt:
        arr_of_arr_blocks = []
        for i in range(0, len(cipher), 16):
            arr_of_arr_blocks.append(cipher[i:i+16])
        for block in arr_of_arr_blocks:
            if arr_of_arr_blocks.count(block) > maxreps:
                maxreps = arr_of_arr_blocks.count(block)
                suspect_block = cipher

    return('suspected ECB is ', suspect_block,' reapeted:', maxreps)


# with open(FILE_PATH,'r') as f:
#     arr = []
#     for line in f:
#         arr.append(bytes.fromhex(line.strip()))
#
# print(AES_Detector(arr))