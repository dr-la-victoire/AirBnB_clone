#!/usr/bin/python3
"""This module contains the class that handles storing data"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State


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
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State
            }

        try:
            if not os.path.exists(FileStorage.__file_path):
                return
            with open(FileStorage.__file_path, encoding="utf-8") as j_str:
                the_dict = json.load(j_str)
            # Getting the values of the keys in the the_dict dictionary
            for value in the_dict.values():
                class_name = value["__class__"]
                class_obj = classes[class_name]
                self.new(class_obj(**value))
        except FileNotFoundError:
            pass
