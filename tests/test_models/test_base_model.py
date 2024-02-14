#!/usr/bin/python3

"""
This module is for testing BaseModel class
using unittest
"""
import datetime
from models.base_model import BaseModel
import unittest
import uuid


class TestBaseModel(unittest.TestCase):
    """
    Testing the BaseMode class
    """

    def setUp(self):
        """
        Default test setup
        """
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def test_object_type(self):
        """ testing object type"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_str(self):
        """
        test __str__ method
        """
        expected_output = "[BaseModel] ({}) {}".format(
            self.my_model.id, self.my_model.__dict__)
        self.assertEqual(str(self.my_model), expected_output)

    def test_save(self):
        """
        test __save__method
        """
        previous_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(previous_updated_at, self.my_model.updated_at)

    def test_to_dict(self):
        """
        test to_dict method
        """
        my_model_json = self.my_model.to_dict()
        self.assertEqual(my_model_json['name'], "My First Model")
        self.assertEqual(my_model_json['my_number'], 89)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertEqual(my_model_json['updated_at'],
                         self.my_model.updated_at.isoformat())
        self.assertEqual(my_model_json['created_at'],
                         self.my_model.created_at.isoformat())

    def test_id_creation(self):
        """
        test that the created id is generated via
        the uuid4 method
        """
        self.assertEqual(len(self.my_model.id),
                         len(str(uuid.uuid4())))

    def test_created_at(self):
        """
        test that the created_at attribute is
        behaving correctly
        """
        temp_obj = BaseModel()
        current_time = datetime.datetime.now()
        self.assertIsInstance(temp_obj.created_at, datetime.datetime)
        acceptable_range = datetime.timedelta(minutes=1)
        self.assertLessEqual(current_time - temp_obj.created_at,
                             acceptable_range)

    def test_updated_at(self):
        """
        test that the updated_at attribute is
        behaving correctly
        """
        temp_obj = BaseModel()
        current_time = datetime.datetime.now()
        self.assertIsInstance(temp_obj.updated_at, datetime.datetime)
        acceptable_range = datetime.timedelta(minutes=1)
        self.assertLessEqual(current_time - temp_obj.updated_at,
                             acceptable_range)

    def test_init_with_kwargs(self):
        """
        Test the __init method with kwargs
        """
        base_model_dict = {
            'id': str(uuid.uuid4()),
            'created_at': '2022-01-01T00:00:00.000000',
            'updated_at': '2022-01-02T00:00:00.000000',
            'name': 'Base Model'
        }

        base_model = BaseModel(**base_model_dict)
        self.assertEqual(base_model.id, base_model_dict['id'])
        self.assertEqual(base_model.created_at,
                         datetime.datetime.strptime
                         (base_model_dict['created_at'],
                          '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(base_model.updated_at,
                         datetime.datetime.strptime
                         (base_model_dict['updated_at'],
                          '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(base_model.name, base_model_dict['name'])


if __name__ == '__main__':
    unittest.main()
