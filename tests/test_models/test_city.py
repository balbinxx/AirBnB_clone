#!/usr/bin/python3
"""Test for City class
"""

import unittest
import pep8
import os
from datetime import datetime
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Tests for the City class
    """
    def test_City_pep8(self):
        """Test PEP8 style
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["./models/city.py"])
        self.assertEqual(result.total_errors, 0)

    def test_City_pep8(self):
        """Test PEP8 style
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_city.py"])
        self.assertEqual(result.total_errors, 0)


if __name__ == "__main__":
    unittest.main()
