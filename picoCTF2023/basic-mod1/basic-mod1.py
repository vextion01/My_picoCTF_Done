msg = "165 248 94 346 299 73 198 221 313 137 205 87 336 110 186 69 223 213 216 216 177 138 "
dict_list= {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: '0', 27: '1', 28: '2', 29: '3', 30: '4', 31: '5', 32: '6', 33: '7', 34: '8', 35: '9', 36: '_'}
afterMod = []
msgArrayText  = msg.split()
msgArrayInt = [int(x) for x in msgArrayText]

for i in msgArrayInt:
    k = i%37
    j = dict_list[k]
    afterMod.append(j)

flag = ''.join([str(s) for s in afterMod])
print("flag is : picoCTF{"+flag+"}")

