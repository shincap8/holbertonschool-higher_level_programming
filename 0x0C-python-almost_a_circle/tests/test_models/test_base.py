#!/usr/bin/python3
""" """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Testbase(unittest.TestCase):
    """ """

    def test_dictionary(self):
        re1 = Rectangle(10, 7, 2, 8, 70)
        dictionary = re1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), str)
