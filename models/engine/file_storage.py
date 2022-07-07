#!/usr/bin/python3
"""
This module contains the class FileStorage
that serializes instances to a JSON file and
deserializes JSON file to instances
"""
import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Class FileStorage
    To serialize and deserialize files into and from Json
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Class constructor"""

    def all(self):
        """ return dictionary"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj"""
        KEY_obj = f"{type(obj).__name__}.{obj.id}"
        self.__objects[KEY_obj] = obj

    def save(self):
        """Serializes __objects to JSON file (path:__file_path)"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects
        if __file_path doesn't exist, nothing is done
        """
        try:
            with open(self.__file_path, 'r') as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except Exception as e:
            pass
