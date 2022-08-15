#!/usr/bin/python3

'''
   Base Class for models
'''


class Base:
    '''
       Base class model
    '''

    __nb_objects = 0
    id = 1

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.id = Base.id
            Base.id += 1
        Base.__nb_objects += 1

    @property
    def nb_obj(self):
        return self.__nb_objects
