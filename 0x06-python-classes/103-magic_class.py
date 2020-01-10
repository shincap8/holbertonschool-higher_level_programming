#!/usr/bin/python3
import math
"""Import math"""


class MagicClass:
    """Magic Class"""
    def __init__(self, radius=0):
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """Area method"""
        return ((self ** 2) * math.pi)

        def circumference(self):
            """Circumference method"""
            return ((math.pi * 2) * self__radius)
