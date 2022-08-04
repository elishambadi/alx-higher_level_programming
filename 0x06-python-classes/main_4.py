#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print(my_square.size)
print(my_square.area())
my_square.size = 33
print(my_square.size)
print(my_square.area())
