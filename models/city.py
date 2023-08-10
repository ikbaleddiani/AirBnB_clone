#!/usr/bin/python3
"""
    City model inherits from BaseModel class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Defines class City """
    state_id = ""
    name = ""
