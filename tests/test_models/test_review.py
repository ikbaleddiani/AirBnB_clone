#!/usr/bin/python3
"""
    Review class tests cases model
"""
import unittest
from models.review import Review


class ReviewTests(unittest.TestCase):
    """ Defines review tests cases class """
    def test_initialization(self):
        """ test case of initialization """
        self.assertEqual(Review().place_id, "")
        self.assertEqual(Review().user_id, "")
        self.assertEqual(Review().text, "")
