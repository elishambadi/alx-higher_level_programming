#!/usr/bin/python3
import json
'''
   Handling text files and JSON
'''


def to_json_string(my_obj):
    '''
       to_json_string(object)
       Return JSON representation of object
    '''

    return json.dumps(my_obj)
