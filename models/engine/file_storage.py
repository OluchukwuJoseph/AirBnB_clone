#!/usr/bin/python3
"""This script is the base model"""

from uuid import uuid4
from datetime import datetime
import time
import json
import os



class BaseModel:
    """A class of BaseModel that defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Instantiation of a base instance"""

        if kwargs:
            for k, v in kwargs.items():
                if k in ('created_at', 'updated_at'):
                    date_format = "%Y-%m-%dT%H:%M:%S.%f"
                    v = datetime.strptime(v, date_format)

                if k != '__class__':
                    setattr(self, k, v)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            

    def __str__(self):
        """Returns a human readable string representation of an instance"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"


    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        
        new_dict = self.__dict__
        new_dict["__class__"] = self.__class__.__name__
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()

        return new_dict


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


storage = FileStorage()
storage.new(model)
all_obj = storage.all()
storage.reload()
storage.save()
