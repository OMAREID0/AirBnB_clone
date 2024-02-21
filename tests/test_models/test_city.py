

import unittest
from models.city import City
import models
import uuid
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
    """
    Unit tests for the City class.
    """

    def test_city_attributes(self):
        """
        Test case to verify the initial attributes of a City instance.
        """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_state_id(self):
        """
        Test case to verify the state_id attribute of a City instance.
        """
        city = City()
        city.state_id = "CA"
        self.assertEqual(city.state_id, "CA")

    def test_city_name(self):
        """
        Test case to verify the name attribute of a City instance.
        """
        city = City()
        city.name = "San Francisco"
        self.assertEqual(city.name, "San Francisco")

    def test_city_attributes_initialization(self):
        city = City(state_id="NY", name="New York")
        self.assertEqual(city.state_id, "NY")
        self.assertEqual(city.name, "New York")


class TestCity_instantiation(unittest.TestCase):
    '''Unittest for User class'''

    def test_instantiations(self):
        self.assertEqual(City, type(City()))

    # test for attributes
    def test_att_string(self):
        instant = City()
        self.assertEqual(str, type(instant.name))
        self.assertEqual(str, type(instant.state_id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_id_notequal(self):
        id1 = City()
        id2 = City()
        self.assertNotEqual(id1.id, id2.id)


# ============ test to_dict ===============
class TestCity_to_dict(unittest.TestCase):
    """
    This class contains unit tests for the `to_dict` method of the `City` class.
    """

    def test_type(self):
        """
        Test the type of the returned value from the `to_dict` method.
        """
        instant = City()
        self.assertTrue(dict, type(instant.to_dict))

    def test_keys(self):
        """
        Test if the required keys are present in the dictionary returned by the `to_dict` method.
        """
        instant = City()
        self.assertIn("id", instant.to_dict())
        self.assertIn("created_at", instant.to_dict())
        self.assertIn("updated_at", instant.to_dict())
        self.assertIn("__class__", instant.to_dict())

    def test_datetime_string(self):
        """
        Test if the values of "created_at" and "updated_at" keys are of type string in the dictionary returned by the `to_dict` method.
        """
        instant = City()
        inst_dict = instant.to_dict()
        self.assertTrue(str, type(inst_dict["created_at"]))
        self.assertTrue(str, type(inst_dict["updated_at"]))

    def test_save(self):
        """
        Test if the `save` method updates the value of "updated_at" attribute.
        """
        instant = City()
        sleep(0.05)
        first_updated_at = instant.updated_at
        instant.save()
        self.assertLess(first_updated_at, instant.updated_at)


if __name__ == '__main__':
    unittest.main()
