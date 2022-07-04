#!/usr/bin/python3
def no_c(my_string):
    list_string = []
    list_string[:0] = my_string
    str1 = ""

    for i in range(len(list_string)):
        if list_string[i] == 'c' or list_string[i] == 'C':
            list_string[i] = ""

    for i in range(len(list_string)):
        str1 += list_string[i]
    return str1
