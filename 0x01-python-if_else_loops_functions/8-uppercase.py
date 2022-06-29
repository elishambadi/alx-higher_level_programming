#!/usr/bin/python
def uppercase(str):
    length = len(str)
    for i in range(length):
        if (ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z')):
            str1 = ord(str[i]) - 32
            print("{}".format(chr(str1)), end="")
        else:
            print("{}".format(str[i]), end="")
    print("") 
