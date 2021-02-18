#!/usr/bin/python3
"""This module holds the class FileStorage
    that handle all serialization-deserialization,
    to a JSON file for a persistent model
    """
import json


class FileStorage():
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

    def save(self):
        """Public Instance Method that Serialize
        elements from __objects to a JSON string
        and save all of those in a JSON file
        """
        temp_dict = {}
        for key, value in FileStorage.__objects.items():
            temp_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as work_file:
            json.dump(temp_dict, work_file)

    def reload(self):
        """Public instance Method that Deserializes
        the JSON strings from the JSON file if it exist
        and add the elements to the __objects dictionary
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.state import State
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as work_file:
                data = json.load(work_file)
                for key, value in data.items():
                    class_name = key.split(".")
                    FileStorage.__objects[key] = eval(class_name[0])(**value)
        except FileNotFoundError:
            pass
