#!/usr/bin/python3
"""Class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """ """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ """
        return self.__width

    @width.setter
    def width(self, value):
        """ """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """ """
        return self.__height

    @height.setter
    def height(self, value):
        """ """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """ """
        return self.__x

    @x.setter
    def x(self, value):
        """ """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """ """
        return self.__y

    @y.setter
    def y(self, value):
        """ """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ """
        return (self.width * self.height)

    def display(self):
        """ """
        string = ""
        for i in range(self.y):
            print()
        for i in range(self.__height):
            string = string + (" " * self.x) + ("#" * self.__width) + "\n"
        print(string[:-1])

    def __str__(self):
        """ """
        string = "[Rectangle] (" + str(self.id) + ") "
        string = string + str(self.x) + "/" + str(self.y)
        string = string + " - " + str(self.width) + "/" + str(self.height)
        return string

    def update(self, *args, **kwargs):
        """ """
        attributes = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dictionary(self):
        """ """
        dictionary = {}
        dictionary['x'] = self.x
        dictionary['y'] = self.y
        dictionary['id'] = self.id
        dictionary['height'] = self.height
        dictionary['width'] = self.width
        return dictionary
