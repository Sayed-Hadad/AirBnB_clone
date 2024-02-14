#!/usr/bin/python3
"""
Unit tests for Place class
"""

import unittest
from models.place import Place
from tests.test_models.test_base_model import TestBaseModel
import datetime
from models import storage


class TestPlace(unittest.TestCase):
    """Test cases for Place class"""

    def test_attributes(self):
        """Test default attributes of Place class"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))


class TestPlaceAttributes(unittest.TestCase):
    """
    Test attributes of the Place class
    """

    def test_name_type(self):
        """
        Test if the 'name' attribute is of type str
        """
        place = Place()
        self.assertEqual(type(place.name), str)


class TestPlaceMethods(unittest.TestCase):
    """
    Test methods of the Place class
    """

    def test_str(self):
        """
        Test the __str__ method of the Place class
        """
        place = Place()
        expected_output = "[Place] ({}) {}".format(
            place.id, place.__dict__)
        self.assertEqual(str(place), expected_output)


class TestPlaceStorage(unittest.TestCase):
    """
    Test storage-related functionality of the Place class
    """

    def test_new_instance_stored(self):
        """
        Test if a new instance of Place is stored in the storage
        """
        place = Place()
        storage.new(place)
        self.assertIn(place, storage.all().values())


if __name__ == '__main__':
    unittest.main()
