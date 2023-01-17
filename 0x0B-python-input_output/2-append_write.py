#!/usr/bin/python3
'''
   Handling text files
'''


def append_write(filename="", text=""):
    '''
       append_write(filename, text)
       Adds text to a textfile
    '''

    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
