#!/usr/bin/python3
"""This module holds the class FileStorage
    that handle all serialization-deserialization,
    to a JSON file for a persistent model
    """
import json
class FileStorage:
    """Class FileStorage, class tos instance a unique
    object storage that will process all saving and loading
    information from the JSON file
    """
    __file_path = "file.json"
    __objects = {}
    def all(self):
        """Public Instance Method that return the dictionary
        with all the current elements on the private field
        called __objects
        Returns:
            [dic]: All the objects, saved from the classes of
            the project with the structure
            Class-Name.id(key): obj(value)
        """
        return FileStorage.__objects
    def new(self, obj):
        """Public Instance Method that sets the dictionary
        objects with the information of a new instance
        Args:
            obj ([obj]): Objects previusly created from
            a specify class
        """
        FileStorage.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj