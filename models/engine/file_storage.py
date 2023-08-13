#!/usr/bin/python3
"""This module contains the class that handles storing data"""
import json
import os
from models.base_model import BaseModel


class FileStorage():
    """Serializes & Deserializes data"""
    # Private class attributes
    __file_path = "file.json"
    __objects = {}

    # Public Instance methods
    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets __objects with a key"""
        # Key[__class__.__name__.obj.id]
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes the __objects to a JSON file"""
        # Create an empty dictionary for storage
        new_dict = {}
        # Turn the values of the __objects to another dictionary
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        # Open a file for writing
        with open(FileStorage.__file_path, "w", encoding="utf-8") as doc:
            # Serialize
            json.dump(new_dict, doc)

    def reload(self):
        """Deserializes the JSON file to a dictionary"""
        # Check if the file exists
        if not os.path.isfile(FileStorage.__file_path):
            return
        # Open the file for reading
        with open(FileStorage.__file_path, "r", encoding="utf-8") as doc:
            # Deserialize
            the_dict = json.load(doc)
        # Get the values of the dictionary
        for value in the_dict.values():
            # Get the __class__ name attached to the dictionary
            clsname = value["__class__"]
            del value["__class__"]
            # Link to its corresponding instance
            self.new(eval(clsname)(**value))
