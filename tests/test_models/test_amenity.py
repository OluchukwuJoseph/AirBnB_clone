#!/usr/bin/python3
"""
This module provides unit tests for the Amenity class.
"""
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """
    TestAmenity class provides unit tests for the Amenity class.
    """
    def setUp(self):
        """
        setUp method initializes an Amenity instance for each test.
        """
        self.instance = Amenity()

    def test_types(self):
        """
        Test the types of all attributes
        """
        self.assertEqual(type(self.instance.name), str)
        self.assertEqual(type(self.instance), Amenity)

    def test_default_value(self):
        """
        Tests the default value of all attributes
        """
        self.assertEqual(self.instance.name, "")

    def test_custom_values(self):
        """
        Change the default value and Test
        """
        self.instance.name = "Table"
        self.assertEqual(self.instance.name, "Table")
