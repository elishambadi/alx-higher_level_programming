#!/usr/bin/python3
'''
   Handling text files and JSON
'''

import json


def load_from_json_file(filename):
    '''
       load_from_json_file(my_obj, filename)
       Load JSON obj from text file
    '''

    with open(filename, 'r', encoding='utf-8') as fw:
        return json.load(fw)
