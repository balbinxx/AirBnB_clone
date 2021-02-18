#!/usr/bin/python3
"""Test for User class
"""

import unittest
import pep8
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Tests for the User class
    """

    def test_User_pep8(self):
        """Test PEP8 style
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["./models/user.py"])
        self.assertEqual(result.total_errors, 0)

    def test_User_pep8(self):
        """Test PEP8 style
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_user.py"])
        self.assertEqual(result.total_errors, 0)


if __name__ == "__main__":
    unittest.main()
