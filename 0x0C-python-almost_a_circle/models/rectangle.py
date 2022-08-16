#!/usr/bin/python3

'''
   Rectangle class
'''

from models.base import Base


class Rectangle(Base):
    '''
       Rectangle()
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    def area(self):
        '''
           area() calculate area of a rectangle
        '''
        return self.__width * self.__height

    def display(self):
        '''
           display() - Displays the rectangle
        '''
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        '''Return the object as a string'''

        return "[{}] ({}) {}/{} - {}/{}"
        .format(__class__.__name__, self.id, self.__x, self.__y,
                self.__width, self.__height)
