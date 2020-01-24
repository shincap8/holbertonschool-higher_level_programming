#!/usr/bin/python3
"""Class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        string = "[Square] (" + str(self.id) + ") "
        string = string + str(self.x) + "/" + str(self.y)
        string = string + " - " + str(self.width)
        return string

    def update(self, *args, **kwargs):
        if args and len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "size" in kwargs:
            self.width = kwargs["size"]
        if "x" in kwargs:
            self.x = kwargs["x"]
        if "y" in kwargs:
            self.y = kwargs["y"]

    def to_dictionary(self):
        dictionary = {}
        dictionary['id'] = self.id
        dictionary['x'] = self.x
        dictionary['size'] = self.size
        dictionary['y'] = self.y
        return dictionary
