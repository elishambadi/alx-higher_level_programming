#!/usr/bin/python3
'''
   Math module. Has add()
'''


def add_integer(a, b=98):
    '''
       Add 2 integers. add_integer(a, b=98)
    '''

    if a is None or b is None:
        raise SyntaxError("Please enter both numbers")

    if type(a) == int or type(a) == float:
        pass
    else:
        raise TypeError("a must be an integer")
    if type(b) == int or type(b) == float:
        return int(a) + int(b)
    else:
        raise TypeError("b must be an integer")
