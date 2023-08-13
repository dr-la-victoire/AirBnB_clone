#!/usr/bin/python3
"""This module has the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
