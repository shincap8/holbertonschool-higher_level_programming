#!/usr/bin/python3
"""Base Class"""


import json


class Base:
    """comment"""
    __nb_objects = 0

    def __init__(self, id=None):
        """comment"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    def to_json_string(list_dictionaries):
        """comment"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """comment"""
        obj = []
        if list_objs is not None:
            for i in list_objs:
                obj.append(i.to_dictionary())
        filename = "" + cls.__name__ + ".json"
        with open(filename, mode="w", encoding="UTF-8") as f:
            f.write(cls.to_json_string(obj))

    @staticmethod
    def from_json_string(json_string):
        """comment"""
        if json_string is None or len(json_string) == 0:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """comment"""
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """comment"""
        filename = cls.__name__ + ".json"
        text = ""
        instlist = []
        try:
            with open(filename, "r", encoding="UTF-8") as f:
                text = f.read()
                obj = cls.from_json_string(text)
                for i in obj:
                    instlist.append(cls.create(**i))
                return instlist
        except:
            return instlist
