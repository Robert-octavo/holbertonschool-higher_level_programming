#!/usr/bin/python3
"""Create a Class Base: """


from encodings import utf_8
import json


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
        pass