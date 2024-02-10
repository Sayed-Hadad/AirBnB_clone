#!/usr/bin/python3

"""
This module is for testing the file_storage
module.
"""
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User
import os


class TestFileStorage(unittest.TestCase):
    """
    This class contains unit tests for the FileStorage class,
    which is responsible for serializing and deserializing instances
    to and from a JSON file.
    """

    def setUp(self):
        """
        This method is executed before each test case.
        It sets up a clean environment for testing by creating a
        new instances of different classes and assigning attributes to it.
        """
        self.obj_base = BaseModel()
        self.obj_usr = User()
        self.obj_city = City()
        self.obj_place = Place()
        self.obj_state = State()
        self.obj_review = Review()
        self.obj_amenity = Amenity()

    def test_type_file_path(self):
        """ Tests the type of the file path """
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_type_obj_dict(self):
        """ Tests the type of __objects"""
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_all_return_type(self):
        """ Tests the all method"""
        self.assertEqual(type(storage.all()), dict)

    def test_new(self):
        """
        Test whether a new instance is correctly added to __objects.
        It creates a new instance of BaseModel, assigns attributes to it,
        saves the instance using storage.new(object), and checks if the
        instance is present in the __objects dictionary.
        """
        self.assertIn("BaseModel." + self.obj_base.id, storage.all().keys())
        self.assertIn(self.obj_base, storage.all().values())
        self.assertIn("User." + self.obj_usr.id, storage.all().keys())
        self.assertIn(self.obj_usr, storage.all().values())
        self.assertIn("City." + self.obj_city.id, storage.all().keys())
        self.assertIn(self.obj_city, storage.all().values())
        self.assertIn("Place." + self.obj_place.id, storage.all().keys())
        self.assertIn(self.obj_place, storage.all().values())
        self.assertIn("State." + self.obj_state.id, storage.all().keys())
        self.assertIn(self.obj_state, storage.all().values())
        self.assertIn("Review." + self.obj_review.id, storage.all().keys())
        self.assertIn(self.obj_review, storage.all().values())
        self.assertIn("Amenity." + self.obj_amenity.id, storage.all().keys())
        self.assertIn(self.obj_amenity, storage.all().values())

    def test_save(self):
        """
        Test saving instance to the storage.
        It creates a new instance, assigns attributes, saves and reloads it,
        and checks if the instance is present in the file.json file.
        """
        storage.save()
        json_read = ""
        with open("file.json", "r") as f:
            json_read = f.read()
            self.assertIn("BaseModel." + self.obj_base.id, json_read)
            self.assertIn("User." + self.obj_usr.id, json_read)
            self.assertIn("City." + self.obj_city.id, json_read)
            self.assertIn("Place." + self.obj_place.id, json_read)
            self.assertIn("State." + self.obj_state.id, json_read)
            self.assertIn("Review." + self.obj_review.id, json_read)
            self.assertIn("Amenity." + self.obj_amenity.id, json_read)
        os.remove('file.json')

    def test_reload(self):
        """
        Test reloading instance from the storage
        (from "file.json")
        """
        storage.save()
        storage.reload()
        all_objs = storage.all()
        self.assertIn("BaseModel." + self.obj_base.id, all_objs)
        self.assertIn("User." + self.obj_usr.id, all_objs)
        self.assertIn("City." + self.obj_city.id, all_objs)
        self.assertIn("Place." + self.obj_place.id, all_objs)
        self.assertIn("State." + self.obj_state.id, all_objs)
        self.assertIn("Review." + self.obj_review.id, all_objs)
        self.assertIn("Amenity." + self.obj_amenity.id, all_objs)

    def test_no_file(self):
        """
        Testing what happens when there's no file called (file.json)
        """
        if os.path.exists('file.json'):
            os.remove('file.json')
        try:
            storage.reload()
        except Exception:
            self.assertTrue(False)
        else:
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()