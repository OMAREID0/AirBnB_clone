

import unittest
from models.place import Place
import models
import uuid
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
from models.engine.file_storage import FileStorage


class TestPlace(unittest.TestCase):
    """
    Unit tests for the Place class.
    """

    def setUp(self):
        """
        Set up the test fixture. This method is called before each test method.
        """
        self.place = Place()

    def test_city_id(self):
        """
        Test the city_id property of the Place class.
        """
        self.assertEqual(self.place.city_id, "")

    def test_user_id(self):
        """
        Test the user_id property of the Place class.
        """
        self.assertEqual(self.place.user_id, "")

    def test_name(self):
        """
        Test the name property of the Place class.
        """
        self.assertEqual(self.place.name, "")

    def test_description(self):
        """
        Test the description property of the Place class.
        """
        self.assertEqual(self.place.description, "")

    def test_number_rooms(self):
        """
        Test the number_rooms property of the Place class.
        """
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms(self):
        """
        Test the number_bathrooms property of the Place class.
        """
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest(self):
        """
        Test the max_guest property of the Place class.
        """
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night(self):
        """
        Test the price_by_night property of the Place class.
        """
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude(self):
        """
        Test the latitude property of the Place class.
        """
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude(self):
        """
        Test the longitude property of the Place class.
        """
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids(self):
        """
        Test the amenity_ids property of the Place class.
        """
        self.assertEqual(self.place.amenity_ids, [])

    def test_set_city_id(self):
        """
        Test the set_city_id method of the Place class.
        """
        self.place.city_id = "123"
        self.assertEqual(self.place.city_id, "123")

    def test_set_user_id(self):
        """
        Test the set_user_id method of the Place class.
        """
        self.place.user_id = "456"
        self.assertEqual(self.place.user_id, "456")

    def test_set_name(self):
        """
        Test the set_name method of the Place class.
        """
        self.place.name = "Test Place"
        self.assertEqual(self.place.name, "Test Place")

    def test_set_description(self):
        """
        Test the set_description method of the Place class.
        """
        self.place.description = "This is a test place"
        self.assertEqual(self.place.description, "This is a test place")

    def test_set_number_rooms(self):
        """
        Test the set_number_rooms method of the Place class.
        """
        self.place.number_rooms = 5
        self.assertEqual(self.place.number_rooms, 5)

    def test_set_number_bathrooms(self):
        """
        Test the set_number_bathrooms method of the Place class.
        """
        self.place.number_bathrooms = 2
        self.assertEqual(self.place.number_bathrooms, 2)

    def test_set_max_guest(self):
        """
        Test the set_max_guest method of the Place class.
        """
        self.place.max_guest = 10
        self.assertEqual(self.place.max_guest, 10)

    def test_set_price_by_night(self):
        """
        Test the set_price_by_night method of the Place class.
        """
        self.place.price_by_night = 100
        self.assertEqual(self.place.price_by_night, 100)

    def test_set_latitude(self):
        """
        Test the set_latitude method of the Place class.
        """
        self.place.latitude = 37.7749
        self.assertEqual(self.place.latitude, 37.7749)

    def test_set_longitude(self):
        self.place.longitude = -122.4194
        self.assertEqual(self.place.longitude, -122.4194)

    def test_set_amenity_ids(self):
        self.place.amenity_ids = ["1", "2", "3"]
        self.assertEqual(self.place.amenity_ids, ["1", "2", "3"])


class TestPlace_instantiation(unittest.TestCase):
    '''Unittest for Place class'''

    def test_instantiations(self):
        '''Test if Place instance is created correctly'''
        self.assertEqual(Place, type(Place()))

    def test_att_type(self):
        '''Test the types of attributes in Place instance'''
        instant = Place()
        self.assertEqual(str, type(instant.name))
        self.assertEqual(str, type(instant.city_id))
        self.assertEqual(str, type(instant.user_id))
        self.assertEqual(str, type(instant.description))
        self.assertEqual(int, type(instant.number_rooms))
        self.assertEqual(int, type(instant.number_bathrooms))
        self.assertEqual(int, type(instant.number_bathrooms))
        self.assertEqual(int, type(instant.max_guest))
        self.assertEqual(int, type(instant.price_by_night))
        self.assertEqual(float, type(instant.latitude))
        self.assertEqual(float, type(instant.longitude))
        self.assertEqual(list, type(instant.amenity_ids))

    def test_created_at_is_public_datetime(self):
        '''Test if created_at attribute is of type datetime'''
        self.assertEqual(datetime, type(Place().created_at))

    def test_id_notequal(self):
        '''Test if the ids of two Place instances are not equal'''
        id1 = Place()
        id2 = Place()
        self.assertNotEqual(id1.id, id2.id)


# ============ test to_dict ===============
class TestPlace_to_dict(unittest.TestCase):
    """
    A test case for the `to_dict` method of the `Place` class.
    """

    def test_type(self):
        instant = Place()
        self.assertTrue(dict, type(instant.to_dict))

    def test_keys(self):
        instant = Place()
        self.assertIn("id", instant.to_dict())
        self.assertIn("created_at", instant.to_dict())
        self.assertIn("updated_at", instant.to_dict())
        self.assertIn("__class__", instant.to_dict())

    def test_datetime_string(self):
        instant = Place()
        inst_dict = instant.to_dict()
        self.assertTrue(str, type(inst_dict["created_at"]))
        self.assertTrue(str, type(inst_dict["updated_at"]))

    def test_save(self):
        instant = Place()
        sleep(0.05)
        first_updated_at = instant.updated_at
        instant.save()
        self.assertLess(first_updated_at, instant.updated_at)


if __name__ == '__main__':
    unittest.main()
