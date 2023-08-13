#!/usr/bin/python3
"""
    User class tests cases model
"""
import unittest
from models.user import User


class UserTests(unittest.TestCase):
    """ Defines User tests cases class """
    def test_instance(self):
        """ tests cases for User model """
        self.assertEqual(User().email, "")
        self.assertEqual(User().password, "")
        self.assertEqual(User().first_name, "")
        self.assertEqual(User().last_name, "")
