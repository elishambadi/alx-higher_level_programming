#!/usr/bin/python3
"""The base class module"""

import json
import turtle


class Base:
    """The base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialized method
        Args:
            id (int): id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries:list of dictionaries
        Return:
            If list_dictionaries is None || empty return  "[]"
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file
        Args:
            cls:
            list_objs:a list of instances who inherits of Base
        """
        if list_objs is None:
            fc = "[]"
        else:
            fc = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(cls.__name__ + '.json', 'w') as f:
            f.write(fc)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation
        Args:
            json_string:string representing a list of dictionaries
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        Args:
            dictionary:double pointer to a dictionary
        """
        """Creating dummy instance that is square and rectangle"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances
        Args:
            none
        """
        try:
            with open(cls.__name__ + '.json', 'r') as f:
                json_list = cls.from_json_string(f.read())
                obj_list = []
                for i in json_list:
                    obj_list.append(cls.create(**i))
                return obj_list
        except FileNotFoundError:
            return []

    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares
        Args:
            list_rectangles: rectangles with various dimensions
            list_squares: squares with various dimensions
        """
        '''Creating a turtle with Turtle() and the screen'''
        t = turtle.Turtle()
        wn = turtle.Screen()
        wn.bgcolor("blue")
        t.pensize(3)
        t.speed(1)

        t.color("yellow")
        for i in list_rectangles:
            t.up()
            t.setpos(i.x, i.y)
            t.down()
            for j in range(2):
                t.forward(i.width)
                t.left(90)
                t.forward(i.height)
                t.left(90)

        t.color("brown")
        for i in list_squares:
            t.up()
            t.setpos(i.x, i.y)
            t.down()
            for j in range(2):
                t.forward(i.width)
                t.left(90)
                t.forward(i.height)
                t.left(90)

    turtle.exitonclick()
