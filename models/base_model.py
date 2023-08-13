#!/usr/bin/python3
"""This module is the base model for the Airbnb project"""
import uuid
from datetime import datetime


class BaseModel():
    """This class contains the common attributes and methods"""

    def __init__(self, id, created_at, updated_at):
        """Initializes the class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns a str representation of an instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the attribute 'updated_at'"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary of the instance"""
        the_dict = self.__dict__
        the_dict["__class__"] = self.__class__.__name__
        the_dict["created_at"] = the_dict["created_at"].isoformat()
        the_dict["updated_at"] = the_dict["updated_at"].isoformat()
        return the_dict
