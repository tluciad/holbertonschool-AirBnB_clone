#!/usr/bin/python3

"""Module for FileStorage"""
import json
from os import path


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
        Dict = {}
        for key, value in self.__objects.items():
            Dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as write:
            json.dump(Dict, write)

    def reload(self):
        """deserializes the JSON file to __objects"""
        dictionaryofdictionaries = {}
        try:
            with open(self.__file_path, "r") as r:
                dictionaryofdictionaries = json.load(r)
        except:
            pass
