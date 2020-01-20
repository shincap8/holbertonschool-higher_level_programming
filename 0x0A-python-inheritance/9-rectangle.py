#!/usr/bin/python3
"""Class Rectangle"""


class BaseGeometry():
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError('' + name + ' must be an integer')
        if value <= 0:
            raise ValueError('' + name + ' must be greater than 0')


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        BaseGeometry().integer_validator("width", width)
        BaseGeometry().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
