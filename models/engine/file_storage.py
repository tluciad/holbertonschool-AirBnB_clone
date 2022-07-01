#!/usr/bin/python3

"""Module for FileStorage"""
import json
from os import path


class FileStorage:
    """Class FileStorage
    To serialize and deserialize files into and from Json
    """

    __file_path = "__name__ + .json"
    __objects = {}


    def __init__(self):
        """Class constructor"""


    def all(self):
        return self.__objects


    def new(self, obj):



    def save(self):
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
        with open(self.__file_path, "w") as write:
            json.dump(self.__objects, write)

    def reload(self):
        if path.exists(self.__name__ + ".json"):
            data = json.loads(self.__name__ + ".json")
        return (data)
