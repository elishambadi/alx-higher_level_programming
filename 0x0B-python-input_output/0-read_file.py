#!/usr/bin/python3
'''
   Handling text files
'''


def read_file(filename=""):
    '''
       read_file(filename)
    '''

    with open(filename, encoding='utf-8') as f:
        print("{}".format(f.read()), end='')
