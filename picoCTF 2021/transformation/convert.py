#!/usr/bin/env python3

encoded_flag = open("enc").read()
flag = ""


decoded_flag = encoded_flag.encode('utf-16be')
# for i in range(0, len(encoded_flag)):
#     character1 = chr((ord(encoded_flag[i]) >> 8))
#     character2 = chr(encoded_flag[i].encode('utf-16be')[-1])
#     flag += character1
#     flag += character2

print("Flag:", decoded_flag)