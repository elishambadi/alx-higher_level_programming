#!/usr/bin/python3
'''Define a rectangle
'''


class Rectangle:
    '''Rectangle(width, height)
       Defining a rectangle
    '''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__height != 0 and self.__width != 0:
            return (2 * self.__height + 2 * self.__width)
        else:
            return 0

    def __print__(self):
        if (self.__width != 0) and (self.__height != 0):
            i = 0
            while i < self.__height:
                # print("i = {}, height = {}".format(i, self.__height))
                print("#" * self.__width)
                i += 1
            return ''
        else:
            return ""

    def __str__(self):
        if (self.__width != 0) and (self.__height != 0):
            i = 0
            while i < self.__height:
                # print("i = {}, height = {}".format(i, self.__height))
                print("#" * self.__width)
                i += 1
            return ''
        else:
            return ""

    def __repr__(self):
        return 'Rectangle({},{})'.format(self.__width, self.__height)
