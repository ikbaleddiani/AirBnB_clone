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
        b1= BaseModel()
        b_dict = b.to_dict()
        b2 = BaseModel(b_dict)
        self.assertEqual(b1, b2)

    def test_save(self):
        """ test save method """
        b1 = BaseModel()
        b2 = b1
        b2.save()
        self.assertNotEqual(b2.updated_at ,b1.updated_at)
