#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit_l = abs(number)%10;

if digit_l > 5:
	print(f"Last digit of {number} is {digit_l} and is greater than 5")
elif digit_l < 6 and digit_l != 0:
	print(f"Last digit of {number} is {digit_l} and is less than 6 and not 0")
else:
	print(f"Last digit of {number} is {digit_l} and is 0")
