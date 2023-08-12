#!/usr/bin/python3
"""
    Place class tests cases model
"""
import unittest
from models.place import Place


class PlaceTests(unittest.TestCase):
    """ Defines Place tests cases class """
    def test_initialization(self):
        """ test case of initialization """
        self.assertEqual(Place().city_id, "")
        self.assertEqual(Place().user_id, "")
        self.assertEqual(Place().name, "")
        self.assertEqual(Place().description, "")
        self.assertEqual(Place().number_rooms, 0)
        self.assertEqual(Place().number_bathrooms, 0)
        self.assertEqual(Place().max_guest, 0)
        self.assertEqual(Place().price_by_night, 0)
        self.assertEqual(Place().latitude, 0.0)
        self.assertEqual(Place().longitude, 0.0)
        self.assertEqual(Place().amenity_ids, [])
