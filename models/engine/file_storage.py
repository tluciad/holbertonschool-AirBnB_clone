#!/usr/bin/python3

"""Module for FileStorage"""
import json
from models import base_model, user, state, city, amenity, place, review


class FileStorage:
    """Class FileStorage
    To serialize and deserialize files into and from Json
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Class constructor"""

    def all(self):
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects dictionary to the JSON file"""
        with open(self.__file_path, "w", encoding='utf-8') as file:
            STR = json.dumps(self.__objects, sort_keys=True, default=str)
            file.write(STR)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as r:
                self.__objects = json.loads(r.read())
        except:
            pass
