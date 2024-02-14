#!/usr/bin/python3
"""
Unit tests for State class
"""

import unittest
from models.state import State
from tests.test_models.test_base_model import TestBaseModel
import datetime
from models import storage


class TestStateAttributes(unittest.TestCase):
    """
    Test attributes of the State class
    """
    def test_name_type(self):
        """
        Test if the 'name' attribute is of type str
        """
        state = State()
        self.assertEqual(type(state.name), str)


class TestStateMethods(unittest.TestCase):
    """
    Test methods of the State class
    """

    def test_str(self):
        """
        Test the __str__ method of the State class
        """
        state = State()
        expected_output = "[State] ({}) {}".format(
            state.id, state.__dict__)
        self.assertEqual(str(state), expected_output)


class TestStateStorage(unittest.TestCase):
    """
    Test storage-related functionality of the State class
    """

    def test_new_instance_stored(self):
        """
        Test if a new instance of State is stored in the storage
        """
        state = State()
        storage.new(state)
        self.assertIn(state, storage.all().values())


class TestState(unittest.TestCase):
    """Test cases for State class"""

    def test_attributes(self):
        """Test default attributes of State class"""
        state = State()
        self.assertEqual(state.name, "")
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))


if __name__ == '__main__':
    unittest.main()
