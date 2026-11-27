#!/usr/bin/python3
"""Defines the Base class."""
import json


class Base:
    """Base class that manages the id of all other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Set the id, or assign the next automatic one."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string of a list of dictionaries."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string of a list of instances to a file."""
        dictionaries = [obj.to_dictionary() for obj in list_objs or []]
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string."""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with the attributes in dictionary."""
        if cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from the class JSON file."""
        try:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as f:
                dictionaries = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []
        return [cls.create(**dictionary) for dictionary in dictionaries]
