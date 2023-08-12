#!/usr/bin/python3
"""
    BaseModel tests cases model
"""
import unittest
from models.base_model import BaseModel


class BaseModelTests(unittest.TestCase):
    """ Defines BaseModel tests cases class """

    def test_instance(self):
        """ test initialization """
        b = BaseModel()
        self.assertIsInstance(b.id, str)

    def test_to_dict(self):
        """ test initialization """
        b1 = BaseModel()
        b1_dict = b1.to_dict()
        self.assertIsInstance(b1_dict, dict)

    def test_str(self):
        """ test cases """
        b = BaseModel
        self.assertIsInstance(str(b), str)

    def test_save(self):
        """ test save method """
        b1 = BaseModel()
        date = b1.updated_at
        b1.save()
        self.assertNotEqual(date, b1.updated_at)
