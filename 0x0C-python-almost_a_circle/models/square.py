#!/usr/bin/python3

'''
   Defines a square
'''


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
       Square(size, x, y, id). Creates a square
    '''

    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    def __str__(self):
        '''
           Returns a square as a string
        '''
        return "{} - ({}) {}/{} - {}".format(__class__.__name__,
                                             self.id,
                                             self.x,
                                             self.y,
                                             self.size)
