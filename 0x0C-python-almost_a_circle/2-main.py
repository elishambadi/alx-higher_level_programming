#!/usr/bin/python3
""" 2-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    try:
        base1 = Rectangle(10, "2")
        print("Rectangle made: {}".format(base1.height))
    except Exception as e:
        print("1. [{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print("2. [{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("3. [{}] {}".format(e.__class__.__name__, e))

    try:
        base2 = Rectangle(10, 2, 3, -1)
        print(base2.y)
    except Exception as e:
        print("4. [{}] {}".format(e.__class__.__name__, e))
