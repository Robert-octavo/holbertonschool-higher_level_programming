#!/usr/bin/python3
"""Create a Class Base: """


import json
import os



class Base():
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that returns the JSON string representation of
        list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that writes the JSON string representation of
        list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf_8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list = [object.to_dictionary() for object in list_objs]
                file.write(Base.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """static method that returns the list of the JSON string
        representation json_string"""
        empty_list = []
        if json_string is None or json_string == "[]":
            return empty_list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """class method that returns an instance with all attributes
        already set"""
        if dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            if cls.__name__ == "Square":
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """class method that returns a list of instances:"""
        empty_list = []
        filename = cls.__name__ + ".json"
        if os.path.exists(filename):
            with open(filename, "r") as file:
                list = cls.from_json_string(file.read())
                return [cls.create(**dct) for dct in list]
        return empty_list
