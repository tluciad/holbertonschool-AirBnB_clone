#!/usr/bin/python3

"""Module for base model class"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """Class BaseModel
Attr:
__nb_objects: number of instances
"""
    name = ""
    my_number = 0

    def __init__(self, *args, **kwargs):
        """"Initiliazes an instance"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    dt_obj = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, dt_obj)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """should print as a string"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """method to return a dictionary"""
        Base_dict = self.__dict__.copy()
        Base_dict["__class__"] = self.__class__.__name__
        Base_dict["created_at"] = self.created_at.isoformat()
        Base_dict["updated_at"] = self.updated_at.isoformat()
        return (Base_dict)
