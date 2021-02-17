#!/usr/bin/python3
"""constructor for the
    models Package """
    
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
