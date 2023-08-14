#!/usr/bin/python3
"""City class tests cases model"""

import unittest
from models.city import City


class CityTests(unittest.TestCase):
    """ Defines City tests cases class """

    def test_initialization(self):
        """ test case of initialization """

        self.assertEqual(City().state_id, "")
        self.assertEqual(City().name, "")
