#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


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
        new instance of BaseModel and assigning attributes to it.
        """
        self.my_model = BaseModel()
        self.my_model.name = "My_First_Model"
        self.my_model.my_number = 89

    def test_new_instance_added(self):
        """
        Test whether a new instance is correctly added to __objects.
        It creates a new instance of BaseModel, assigns attributes to it,
        saves the instance using storage.save(), and checks if the instance
        is present in the __objects dictionary.
        """
        new_instance_key = f"{self.my_model.__class__.__name__}.{self.my_model.id}"
        storage.save()
        self.assertIn(new_instance_key, storage.all())

    def test_save_and_reload(self):
        """
        Test saving and reloading of instances from storage.
        It creates a new instance, assigns attributes, saves and reloads it,
        and checks if the instance is present in the __objects dictionary
        after reloading. Additionally, it confirms that the reloaded object
        is an instance of BaseModel.
        """
        new_instance_key = f"{self.my_model.__class__.__name__}.{self.my_model.id}"
        storage.save()
        storage.reload()
        self.assertIn(new_instance_key, storage.all())
        self.assertIsInstance(storage.all()[new_instance_key], BaseModel)


if __name__ == '__main__':
    unittest.main()
