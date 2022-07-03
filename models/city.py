#!/usr/bin/python3
"""a class State that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Public class attributes"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initiliazes an instance"""
        super().__init__(*args, **kwargs)