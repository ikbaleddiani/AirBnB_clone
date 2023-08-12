#!/usr/bin/python3
"""
    City model inherits from BaseModel class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Defines City class """
    state_id = ""
    name = ""
