#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        try:
            if not isinstance(size, int):
                raise TypeError
            if size < 0:
                raise ValueError
            self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
                raise ValueError("size must be >= 0")

        try:
            if isinstance(position, tuple):
                for i in range(len(position)):
                    if i < 0:
                        raise ValueError
                if i > 1:
                    raise IndexError
                self.__position = position
            else:
                raise TypeError
        except (ValueError, IndexError, TypeError):
            raise ValueError("position must be a tuple of 2 positive integers")
            raise IndexError("position must be a tuple of 2 positive integers")
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    @property
    def position(self):
        return self.__position

    @size.setter
    def position(self, value):
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                        print("-", end="")
                for j in range(self.__size):
                    print ("#", end="")
                print()
