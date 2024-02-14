#!/usr/bin/python3
"""
Unit tests for Review class
"""

import unittest
from models.review import Review
from tests.test_models.test_base_model import TestBaseModel
import datetime
from models import storage


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def test_attributes(self):
        """Test default attributes of Review class"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))


class TestReviewMethods(unittest.TestCase):
    """
    Test methods of the Review class
    """

    def test_str(self):
        """
        Test the __str__ method of the Review class
        """
        review = Review()
        expected_output = "[Review] ({}) {}".format(
            review.id, review.__dict__)
        self.assertEqual(str(review), expected_output)


class TestReviewStorage(unittest.TestCase):
    """
    Test storage-related functionality of the Review class
    """

    def test_new_instance_stored(self):
        """
        Test if a new instance of Review is stored in the storage
        """
        review = Review()
        storage.new(review)
        self.assertIn(review, storage.all().values())


if __name__ == '__main__':
    unittest.main()
