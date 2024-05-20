#!/usr/bin/python3
"""
This module provides unit tests for the City class.
"""
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """
    TestCity class provides unit tests for the CIty class.
    """
    def setUp(self):
        """
        setUp method initializes a City instance for each test.
        """
        self.instance = City()

    def test_types(self):
        """
        Test the types of all attributes
        """
        self.assertEqual(type(self.instance.state_id), str)
        self.assertEqual(type(self.instance.name), str)
        self.assertEqual(type(self.instance), City)

    def test_default_value(self):
        """
        Tests the default value of all attributes
        """
        self.assertEqual(self.instance.name, "")
        self.assertEqual(self.instance.state_id, "")

    def test_custom_values(self):
        """
        Change the default value and Test
        """
        self.instance.name = "Ikeja"
        self.assertEqual(self.instance.name, "Ikeja")
