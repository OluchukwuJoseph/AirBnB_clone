#!/usr/bin/python3
"""
This module provides unit tests for the Review class.
"""
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """
     TestReview class provides unit tests for the Review class.
     """
    def setUp(self):
        """
        setUp method initializes a Review instance for each test.
        """
        self.instance = Review()

    def test_types(self):
        """
        Test the types of all attributes
        """
        self.assertEqual(type(self.instance.user_id), str)
        self.assertEqual(type(self.instance.place_id), str)
        self.assertEqual(type(self.instance.text), str)
        self.assertEqual(type(self.instance), Review)

    def test_default_value(self):
        """
        Test the types of all attributes
        """
        self.assertEqual(self.instance.place_id, "")
        self.assertEqual(self.instance.user_id, "")
        self.assertEqual(self.instance.text, "")

    def test_custom_values(self):
        """
        Change the default value and Test
        """
        self.instance.text = "Nice Place"
        self.assertEqual(self.instance.text, "Nice Place")
