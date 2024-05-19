#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
import os


class FileStorage:
    """A class that serializes instances to a JSON file and deserializes JSON file to instances"""
    CLASSES = {'BaseModel': BaseModel}
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """A method that returns the __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """A method that adds new objects to the __object dictionary"""

        key = f"{obj.__class__.__name__}.(obj.id)"
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""

        serialized_obj = {}

        for k, v in self.__objects.items():
            serialized_obj[k] = v.to_dict()


        with open(self.__file_path, 'w') as file:
            json.dump(serialized_obj, file, indent=2)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""

        with open(self.__file_path, 'r') as file:
            obj_dict = json.load(file)

            for k, v in content.items():
                obj_dict = v['__class__']

                if obj_dict in self.CLASSES:
                    instance = self.CLASSES[obj_dict](**v)