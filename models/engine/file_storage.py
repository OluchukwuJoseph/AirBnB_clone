"""
Module for handling storage of objects in a JSON file.

This module contains the FileStorage class, which provides methods
for managing the storage of objects in a JSON file. It allows for
adding, retrieving, saving, and reloading objects to and from the
JSON file.

Classes:
        FileStorage: A class to handle storage of objects in a JSON file.

"""
import json
from ..base_model import BaseModel
from ..user import User
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..place import Place
from ..review import Review

class FileStorage:
    """
         Class to handle storage of objects in a JSON file.

         Attributes:
            __file_path (str): The path to the JSON file used for storage.
            __objects (dict): A dictionary to store objects in memory.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            Retrieve all objects stored in memory.

            Returns:
                dict: A dictionary containing all stored objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
            Add a new object to storage.

            Args:
                obj: The object to be added to storage.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        value = obj.to_dict()
        FileStorage.__objects.update({key: value})

    def save(self):
        """
                Save objects (FileStorage.__objects) in memory to the JSON file
        """
        if FileStorage.__objects:
            with open(FileStorage.__file_path, 'w') as file:
                json.dump(FileStorage.__objects, file, indent=2)

    def reload(self):
        """
            Reload objects from the JSON file into memory.
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                FileStorage.__objects = json.load(file)
        except (FileExistsError, FileNotFoundError):
            pass
