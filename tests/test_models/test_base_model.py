#!/usr/bin/python3
"""
This module provides unit tests for the BaseModel class.
"""
import unittest
from models.base_model import BaseModel
import datetime
import time


class TestBaseClass(unittest.TestCase):
    """
    TestBaseModel class provides unit tests for the BaseModel class.
    """
    def setUp(self):
        """
        setUp method initializes a BaseModel instance for each test.
        """
        self.instance = BaseModel()
        self.instance.name = 'My name'
        self.instance.number = 89

    def test_types(self):
        """
        Test the types of the instance attribute
        """
        self.assertIsInstance(self.instance.id, str)
        self.assertIsInstance(self.instance.created_at, datetime.datetime)
        self.assertIsInstance(self.instance.updated_at, datetime.datetime)
        self.assertIsInstance(self.instance.number, int)

    def test_values(self):
        """
        Test the values of the instance attributes
        """
        self.assertEqual(self.instance.name, 'My name')
        self.assertEqual(self.instance.number, 89)

    def test_str(self):
        """
        Test if the __str__() method returns the expected string representation
        """
        string = f"[BaseModel] ({self.instance.id}) {self.instance.__dict__}"
        self.assertEqual(self.instance.__str__(), string)

    def test_save(self):
        """
        Test if the save() method updates the updated_at attribute correctly.
        """
        updated_at_value = self.instance.updated_at
        time.sleep(10)
        new_time = updated_at_value + datetime.timedelta(seconds=10)
        self.instance.save()
        self.assertEqual(new_time.replace(microsecond=0),
                         self.instance.updated_at.replace(microsecond=0))

    def test_to_dict(self):
        """
        Test if the to_dict() method returns a dictionary
        with expected keys and values
        """
        instance_dict = self.instance.to_dict()
        self.assertIn('__class__', instance_dict)
        self.assertIn('id', instance_dict)
        self.assertIn('created_at', instance_dict)
        self.assertIn('updated_at', instance_dict)
        self.assertIn('number', instance_dict)
        self.assertIsInstance(instance_dict['id'], str)
        self.assertIsInstance(instance_dict['created_at'], str)
        self.assertIsInstance(instance_dict['updated_at'], str)
        self.assertIsInstance(instance_dict['__class__'], str)
        self.assertIsInstance(instance_dict['number'], int)
        # Genreate class with dictionary
        new_instance = BaseModel(**instance_dict)
        self.assertEqual(self.instance.number, new_instance.number)
        self.assertEqual(self.instance.name, new_instance.name)
        self.assertFalse(self.instance is new_instance)
