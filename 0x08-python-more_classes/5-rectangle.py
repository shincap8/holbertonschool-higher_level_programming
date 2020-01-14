#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """Function for Rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        string = ""
        if self.__height == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            string = string + ("#" * self.__width) + "\n"
        return string[:-1]

    def __repr__(self):
        str1 = str(self.__width)
        str2 = str(self.__height)
        return "Rectangle(" + str1 + ", " + str2 + ")"

    def __del__(self):
        print ("Bye rectangle...")
