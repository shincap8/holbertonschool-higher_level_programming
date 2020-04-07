#!/usr/bin/python3
"""Write a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """function to find the peak"""
    if len(list_of_integers) > 0:
        peak = list_of_integers[0]
        for i in list_of_integers:
            if i > peak:
                peak = i
    else:
        peak = None
    return peak
