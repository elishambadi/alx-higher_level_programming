#!/usr/bin/python3
'''
   Handling text files and JSON
'''

import json


def save_to_json_file(my_obj, filename):
    '''
       save_to_json_file(my_obj, filename)
       Save JSON obj to text file
    '''

    with open(filename, 'w', encoding='utf-8') as fw:
        json.dump(my_obj, fw)
