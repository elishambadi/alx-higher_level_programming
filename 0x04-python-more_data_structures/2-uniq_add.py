#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = my_list.copy()
    uniq = []
    sum = 0
    for i in range(len(new_list)):
        if i == 0:
            sum += new_list[i]
            uniq.append(new_list[i])
        if my_list[i] not in uniq:
            sum += new_list[i]
            uniq.append(new_list[i])
    return sum
