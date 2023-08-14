#!/usr/bin/python3
"""BaseModel tests cases model"""

import unittest
from models.base_model import BaseModel


class BaseModelTests(unittest.TestCase):
    """ Defines BaseModel tests cases class """

    def test_instance(self):
        """*** test initialization ***"""

        b = BaseModel()
        id = b.id
        self.assertEqual(b.id, id)
        date_time = b.created_at
        b.save()
        self.assertEqual(date_time, b.created_at)
        dic = b.to_dict()
        self.assertEqual(dic, b.to_dict()
        self.assertEqual(dic["__class__"], b.__class__.__name__)
        self.assertEqual(dic["id"], b.id)
        self.assertEqual(dic["created_at"], b.created_at.isoformat())
        self.assertEqual(dic["updated_at"], b.updated_at.isoformat())
        s = str(b)
        self.assertEqual(s, str(b))
        b2 = BaseModel(dic)
        self.assertIsInstance(b2, BaseModel)
