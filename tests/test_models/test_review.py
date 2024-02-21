

import unittest
import models
import uuid
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
from models.review import Review
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """
    This class contains unit tests for the Review class.
    """

    def setUp(self):
        """
        Set up the test fixture. This method is called before each test method.
        """
        self.review = Review()

    def test_place_id(self):
        """
        Test the initial value of place_id attribute.
        """
        self.assertEqual(self.review.place_id, "")

    def test_user_id(self):
        """
        Test the initial value of user_id attribute.
        """
        self.assertEqual(self.review.user_id, "")

    def test_text(self):
        """
        Test the initial value of text attribute.
        """
        self.assertEqual(self.review.text, "")

    def test_set_place_id(self):
        """
        Test setting the place_id attribute.
        """
        self.review.place_id = "123"
        self.assertEqual(self.review.place_id, "123")

    def test_set_user_id(self):
        """
        Test setting the user_id attribute.
        """
        self.review.user_id = "456"
        self.assertEqual(self.review.user_id, "456")

    def test_set_text(self):
        self.review.text = "This is a review"
        self.assertEqual(self.review.text, "This is a review")


class TestReview_instantiation(unittest.TestCase):
    '''Unittest for User class'''

    def test_instantiations(self):
        self.assertEqual(Review, type(Review()))

    # test for attributes
    def test_att_string(self):
        instant = Review()
        self.assertEqual(str, type(instant.place_id))
        self.assertEqual(str, type(instant.user_id))
        self.assertEqual(str, type(instant.text))
        self.assertEqual(str, type(instant.id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_id_notequal(self):
        id1 = Review()
        id2 = Review()
        self.assertNotEqual(id1.id, id2.id)


# ============ test to_dict ===============
class TestReview_to_dict(unittest.TestCase):
    """
    This class contains unit tests for the `to_dict` method of the `Review` class.
    """

    def test_type(self):
        instant = Review()
        self.assertTrue(dict, type(instant.to_dict))

    def test_keys(self):
        instant = Review()
        self.assertIn("id", instant.to_dict())
        self.assertIn("created_at", instant.to_dict())
        self.assertIn("updated_at", instant.to_dict())
        self.assertIn("__class__", instant.to_dict())

    def test_datetime_string(self):
        instant = Review()
        inst_dict = instant.to_dict()
        self.assertTrue(str, type(inst_dict["created_at"]))
        self.assertTrue(str, type(inst_dict["updated_at"]))

    def test_save(self):
        instant = Review()
        sleep(0.05)
        first_updated_at = instant.updated_at
        instant.save()
        self.assertLess(first_updated_at, instant.updated_at)


if __name__ == '__main__':
    unittest.main()
