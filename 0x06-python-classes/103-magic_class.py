#!/usr/bin/python3
import math


class MagicClass:
    def __init__(self, radius=0):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
            return self.__radius = None
        else:
            self.__radius = radius

    def area(self):
        return ((self ** 2) * math.pi)

        def circumference:
            return ((math.pi * 2) * self__radius)
