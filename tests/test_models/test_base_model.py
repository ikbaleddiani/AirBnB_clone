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
        id = b.id
        self.assertEqual(b.id, id)
        date_time = b.created_at
        b.save()
        self.assertEqual(date_time, b.created_at)
        dic = b.to_dict()
        self.assertEqual(dic, b.to_dict())
        s = str(b)
        self.assertEqual(s, str(b))
        b2 = BaseModel(dic)
        self.assertIsInstance(b2, BaseModel)
