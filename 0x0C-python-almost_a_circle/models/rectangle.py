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
        for i in range(self.__y):
            print('')

        for i in range(self.__height):
            print(' ' * self.__x + "#" * self.__width)

    def __str__(self):
        '''
           str() print object as string
        '''
        return "[{}] ({}) {}/{} - {}/{}".format(__class__.__name__,
                                                self.id,
                                                self.__x,
                                                self.__y,
                                                self.__width,
                                                self.__height)

    def update(self, *args, **kwargs):
        '''
           update(id, width, height, x, y)
        '''
        if len(args) > 1 and args[0] != '':
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except BaseException:
                pass
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
