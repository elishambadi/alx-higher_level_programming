#!/usr/bin/python3
'''Define size of square
'''


class Square:
    '''square(size)
       Defines a square with it's size
    '''

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size != 0:
            for i in range(self.__size):
                print('#' * self.__size)
        else:
             print('')
