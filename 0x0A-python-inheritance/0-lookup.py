#!/usr/bin/python3
'''
   Module that has dir method
'''
def lookup(obj):
    '''
       lookup(object).  Shows methods in an object 
    '''
    methods = []
    for dirs in dir(obj):
        methods.append(dirs)
    return (methods)
