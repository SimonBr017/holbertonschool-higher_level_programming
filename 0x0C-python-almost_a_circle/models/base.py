#!/usr/bin/python3
""" class call Base"""
from os import path
import json


class Base:
    """def class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries"""
        if list_dictionaries is not None and len(list_dictionaries) > 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string
        representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Return the JSON string representation list_objs to a file"""
        json_file = cls.__name__+".json"
        new_list = []
        if list_objs is not None and len(list_objs) > 0:
            for item in list_objs:
                new_list.append(item.to_dictionary())
        with open(json_file, 'w') as f:
            f.write(cls.to_json_string(new_list))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        my_list = list()
        try:
            with open(cls.__name__ + '.json', 'r') as file:
                file_string = file.read()
                instance_list = Base.from_json_string(file_string)
                for element in instance_list:
                    my_list.append(cls.create(**element))
                return my_list
        except FileNotFoundError:
            return []
