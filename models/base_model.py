#!/usr/bin/python3

"""Module for base model class"""

class BaseModel:
	"""Class BaseModel
    Attr:
    __nb_objects: number of instances
    """

	def __init__(self, id=None):
		""""Initiliazes an instance"""
		if id is None:
			