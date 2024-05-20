#!/usr/bin/python3
from .engine.file_storage import FileStorage
"""
    initializes models
"""


storage = FileStorage()
storage.reload()
