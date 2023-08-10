#!/usr/bin/python3
"""
    Review model inherits from BaseModel class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Defines class Review """
    place_id = ""
    user_id = ""
    text = ""
