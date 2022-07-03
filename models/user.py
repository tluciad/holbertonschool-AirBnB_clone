#!/usr/bin/python3
"""a class User that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """Public class attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initiliazes an instance"""
        super().__init__(*args, **kwargs)
