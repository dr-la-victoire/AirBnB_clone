#!/usr/bin/python3
"""The magic __init__ file that turns this to a package"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
