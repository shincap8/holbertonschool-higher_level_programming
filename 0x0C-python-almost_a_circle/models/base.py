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
        obj = []
        if list_objs is not None:
            for i in list_objs: 
                obj.append(i.to_dictionary())
        filename = "" + cls.__name__ + ".json"
        with open(filename, mode="w", encoding="UTF-8") as f:
            f.write(cls.to_json_string(obj))

    @staticmethod
    def from_json_string(json_string):
        if len(json_string) <= 0 or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        cls()