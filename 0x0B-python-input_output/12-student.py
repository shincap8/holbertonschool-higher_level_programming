#!/usr/bin/python3
"""Student Class"""


class Student():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        attributes = self.__dict__
        attribute = {}
        if attrs is not None:
            for i in attrs:
                if i in attributes:
                    attribute[i] = attributes[i]
            return attribute
        return attributes
