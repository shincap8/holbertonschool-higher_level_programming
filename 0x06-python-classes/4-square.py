#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        try:
            if not isinstance(value, int):
                raise TypeError
            if value < 0:
                raise ValueError
            self.__size = value
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
                raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
