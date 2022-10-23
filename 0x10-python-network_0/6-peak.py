#!/usr/bin/python3

"""
   Finds the peak in a list of numbers
"""


def find_peak(list_of_integers):
    """
       Finds the peak
       Arguments:
          list_of_integer: list of integers
       Returns:
          The peak in the list of integers
    """
    size = len(list_of_integers)
    list = list_of_integers
    i = 1

    if len(list) == 0:
        return None

    peak = list_of_integers[0]
    for i in range(size-1):
        if list[i-1] < list[i] and list[i] > list[i+1]:
            peak = list[i]
        else:
            pass
    return peak
