#!/usr/bin/python3
"""
    BaseModel that defines all common attributes/methods for other classes
"""
import models
from datetime import datetime
import uuid


FORMAT = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ Defines BaseModel class """

    def __init__(self, *args, **kwargs):
        """ Initialises BaseModel instance and subclasses instances """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        setattr(self, key, datetime.strptime(value, FORMAT))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Returns a string representation for current instance """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                str(self.__dict__)
                )

    def save(self):
        """ Updates the public instance attribute 'updated_at' """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of '__dict__' """
        dic = {"__class__": self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                dic[key] = value.isoformat()
            else:
                dic[key] = value
        return dic
