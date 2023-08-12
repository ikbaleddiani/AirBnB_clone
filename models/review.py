#!/usr/bin/python3
"""
    Review model inherits from BaseModel class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Defines Review class """
    place_id = ""
    user_id = ""
    text = ""
