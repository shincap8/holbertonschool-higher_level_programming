#!/usr/bin/python3
import math
"""Import math"""


class MagicClass:
    """Magic Class"""
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Area method"""
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """Circumference method"""
        return ((math.pi * 2) * self.__radius)
