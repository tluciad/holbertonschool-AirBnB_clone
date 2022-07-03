#!/usr/bin/python3
"""a class State that inherits from BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """Public class attributes"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initiliazes an instance"""
        super().__init__(*args, **kwargs)
