#!/usr/bin/python3
"""Write a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """function to find the peak"""
    length = len(list_of_integers)
    if length > 1:
        middle = int(length / 2)
        for i in range(middle):
            if i == 0 and list_of_integers[i] >= list_of_integers[i + 1]:
                return list_of_integers[i]
            if list_of_integers[i] >= list_of_integers[i + 1] and\
            list_of_integers[i] >= list_of_integers[i - 1]:
                return list_of_integers[i]
        for i in range(middle, length):
            if i == (length - 1) and list_of_integers[i] >\
            list_of_integers[i - 1]:
                return list_of_integers[i]
            if list_of_integers[i] >= list_of_integers[i + 1] and\
            list_of_integers[i] >= list_of_integers[i - 1]:
                return list_of_integers[i]
    if length == 1:
        return list_of_integers[0]
    else:
        return None
