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
        b1_dict = b1.to_dict()
        b2 = BaseModel(b1_dict)
        self.assertNotEqual(b1.id, b2.id)

    def test_save(self):
        """ test save method """
        b1 = BaseModel()
        b2 = b1
        b1.save()
        self.assertEqual(b2.created_at ,b1.created_at)
        self.assertEqual(b2.updated_at, b1.updated_at)
