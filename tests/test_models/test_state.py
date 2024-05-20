#!/usr/bin/python3
"""
This module contain test cases for State Class in models/state.py module
"""
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """
    TestState class provides unit tests for the State class.
    """
    def setUp(self):
        """
        setUp method initializes a State instance for each test.
        """
        self.instance = State()

    def test_types(self):
        """
        Test the types of all attributes
        """
        self.assertEqual(type(self.instance.name), str)
        self.assertEqual(type(self.instance), State)

    def test_default_value(self):
        """
        Tests the default value of all attributes
        """
        self.assertEqual(self.instance.name, "")

    def test_custom_values(self):
        """
        Change the default value and Test
        """
        self.instance.name = "Lagos"
        self.assertEqual(self.instance.name, "Lagos")
