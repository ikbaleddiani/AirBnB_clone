#!/usr/bin/python3
"""*** Amenity class tests cases model ***"""

import unittest
from models.amenity import Amenity


class AmenityTests(unittest.TestCase):
    """*** Defines Amenity tests cases class ***"""

    def test_initialization(self):
        """*** test case of initialization ***"""

        self.assertEqual(Amenity().name, "")
