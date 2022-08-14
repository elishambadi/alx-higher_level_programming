#!/usr/bin/python3
'''
   Handling text files and JSON
'''

import json


def from_json_string(my_str):
    '''
       from_json_string(my_str)
       Return Object from json
    '''

    return json.loads(my_str)
