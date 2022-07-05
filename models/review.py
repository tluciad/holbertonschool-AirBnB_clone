#!/usr/bin/python3
"""a class Review that inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Public class attributes"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initiliazes an instance"""
        super().__init__(*args, **kwargs)
