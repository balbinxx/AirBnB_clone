#!/usr/bin/python3
"""Test for State class
"""

import unittest
import pep8
import os
from datetime import datetime
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Tests for the State class
    """

    def test_State_pep8(self):
        """Test PEP8 style
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["./models/state.py"])
        self.assertEqual(result.total_errors, 0)

    def test_State_pep8(self):
        """Test PEP8 style
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_state.py"])
        self.assertEqual(result.total_errors, 0)


if __name__ == "__main__":
    unittest.main()
