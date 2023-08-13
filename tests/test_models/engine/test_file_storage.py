#!/usr/bin/python3
"""
    FileStorage tests cases model
"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from Review import Review
from models.engine.file_storage import FileStorage


class FileStorageTests(unittest.TestCase):
    """ Defines BaseModel tests cases class """
    def test_instance(self):
        B = BaseModel()
        U = User()
        S = State()
        C = City()
        A = Amenity()
        P = Place()
        R = Review()
        B.save()
        U.save()
        S.save()
        C.save()
        A.save()
        P.save()
        R.save()
        self.assertTrue(FileStorage.all() != {})
        FileStorage.save()
        objects = FileStorage.reload()
        self.assertEqual(objects["BaseModel." + B.id], B)
        self.assertEqual(objects["User." + U.id], U)
        self.assertEqual(objects["State." + S.id], S)
        self.assertEqual(objects["City." + C.id], C)
        self.assertEqual(objects["Amenity." + A.id], A)
        self.assertEqual(objects["Place." + P.id], P)
        self.assertEqual(objects["Review." + R.id], R)
