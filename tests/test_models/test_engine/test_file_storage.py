#!/usr/bin/python3
"""Test for FileStorage class
"""
import unittest
import pep8
import os
import json
from models.base_model import BaseModel
from models.__init__ import storage
from models import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test for the FileStorage class
    """
    def test_FileStorage_pep8(self):
        """Test PEP8 style
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["./models/engine/file_storage.py"])
        self.assertEqual(result.total_errors, 0)
    def test_User_pep8(self):
        """Test PEP8 style
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["tests/test_models/test_engine/test_file_storage.py"]
        )
        self.assertEqual(result.total_errors, 0)
if __name__ == "__main__":
    unittest.main()
