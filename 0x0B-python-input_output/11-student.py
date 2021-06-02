#!/usr/bin/python3
"""class Student"""


class Student:
    """"define student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dict = {}

        if attrs is None:
            return self.__dict__

        for i in attrs:
            if type(i) is not str:
                continue
            if hasattr(self, i):
                dict[i] = getattr(self, i)

        return dict

    def reload_from_json(self, json):
        self.__dict__ = json
