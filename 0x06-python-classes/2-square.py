#!/usr/bin/python3
'''Define size of square
'''


class Square:
    '''square(size)
       Defines a square with it's size
    '''
    __size = 0

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
