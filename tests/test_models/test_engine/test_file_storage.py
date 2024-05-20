#!/usr/bin/python
"""
This module provides unit tests for the FileStorage class in the
engine.file_storage module.
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest
import models


class TestFileStorage(unittest.TestCase):
    """
    TestFileStorage class provides unit tests for the FileStorage class.
    """
    def setUp(self):
        """
        setUp method initializes a FileStorage instance for each test.
        """
        self.storage = FileStorage()

    def test_all(self):
        """
        Test if the all() method returns a dictionary.
        """
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """
        Test if the new object is correctly saved in the storage.
        """
        obj = BaseModel()
        self.storage.new(obj)
        obj_key = "BaseModel.{}".format(obj.id)
        self.assertIn(obj_key, self.storage.all())

    def test_save_and_reload(self):
        """
        Test if an object can be saved and reloaded from the storage.
        """
        obj = BaseModel()
        obj.name = 'My name'
        obj.save()
        self.storage.reload()
        key = f"BaseModel.{obj.id}"
        objs = self.storage.all()
        self.assertIn(key, objs)
        obj_dict = objs[key]
        new_obj = BaseModel(**obj_dict)
        self.assertFalse(new_obj is obj)

    def test_storage_instance(self):
        """
        Test if the storage instance in models module is an
        instance of FileStorage.
        """
        self.assertIsInstance(models.storage, FileStorage)
