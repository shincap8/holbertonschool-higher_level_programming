#!/usr/bin/python3
"""Base Class"""
import json


class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    def to_json_string(list_dictionaries):
        if len(list_dictionaries) <= 0 or list_dictionaries == None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        text = cls.to_json_string(cls.to_dictionary(list_objs))
        filename = "" + cls.__name__ + ".json"
        with open(filename, mode="w", encoding="UTF-8") as f:
            f.write(text)