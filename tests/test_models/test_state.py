#!/usr/bin/python3
"""
    State class tests cases model
"""
import unittest
from models.state import State


class StateTests(unittest.TestCase):
    """ Defines State tests cases class """
    def test_initialization(self):
        """ test case of initialization """
        self.assertEqual(State().name, "")
