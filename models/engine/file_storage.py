#!/usr/bin/python3
"""Module for FileStorage class."""
import json


class FileStorage:
    """A class that serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """A method that returns the __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """A method that adds new objects to the __object dictionary"""

        key = f"{obj.__class__.__name__}.{obj.id}"
        value = obj.to_dict()
        self.__objects[key] = value

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""

        if self.__objects:
            with open(self.__file_path, 'w') as file:
                json.dump(self.__objects, file, indent=2)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""

        try:
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
        except (FileExistsError, FileNotFoundError):
            pass
