#!/usr/bin/python3
"""Test for Amenity class
"""

import unittest
import pep8
import os
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests for the Amenity class
    """

    def test_Amenity_pep8(self):
        """Test PEP8 style.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["./models/amenity.py"])
        self.assertEqual(result.total_errors, 0)

    def test_Amenity_pep8(self):
        """Test PEP8 style
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_amenity.py"])
        self.assertEqual(result.total_errors, 0)


if __name__ == "__main__":
    unittest.main()
