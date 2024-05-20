#!/usr/bin/python3
"""This script is the base model"""

from uuid import uuid4
from datetime import datetime
from models import storage



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
            storage.new(self)
            

    def __str__(self):
        """Returns a human readable string representation of an instance"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"


    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()

        return new_dict
