#!/usr/bin/python3
'''
   Handling text files
'''


def write_file(filename="", text=""):
    '''
       write_file(filename, text)
    '''

    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)	
