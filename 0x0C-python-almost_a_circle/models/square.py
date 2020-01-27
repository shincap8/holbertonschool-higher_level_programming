#!/usr/bin/python3
"""Class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """comment"""
    def __init__(self, size, x=0, y=0, id=None):
        """init"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """comment"""
        return self.width

    @size.setter
    def size(self, value):
        """comment"""
        self.width = value
        self.height = value

    def __str__(self):
        """comment"""
        string = "[Square] (" + str(self.id) + ") "
        string = string + str(self.x) + "/" + str(self.y)
        string = string + " - " + str(self.width)
        return string

    def update(self, *args, **kwargs):
        """comment"""
        attributes = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dictionary(self):
        """comment"""
        dictionary = {}
        dictionary['id'] = self.id
        dictionary['x'] = self.x
        dictionary['size'] = self.size
        dictionary['y'] = self.y
        return dictionary
