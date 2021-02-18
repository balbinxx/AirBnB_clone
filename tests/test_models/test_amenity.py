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
        self.assertEqual(result.total_errors, 0, "Found style errors")

    def test_class(self):
        amenity1 = Amenity()
        self.assertEqual(amenity1.__class__.__name__, "Amenity")


if __name__ == "__main__":
    unittest.main()
