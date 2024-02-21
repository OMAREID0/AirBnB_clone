
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    This class contains unit tests for the Amenity class.
    """

    def test_name_initialization(self):
        """
        Test case to verify that the name attribute is initialized as an empty string.
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_name_assignment(self):
        """
        Test case to verify that the name attribute can be assigned a value.
        """
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    def test_name_type(self):
        """
        Test case to verify that the name attribute is of type str.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)

    def test_name_length(self):
        """
        Test case to verify that the name attribute has a length greater than 0.
        """
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertGreater(len(amenity.name), 0)

    def test_name_whitespace(self):
        """
        Test case to verify that leading and trailing whitespaces are stripped from the name attribute.
        """
        amenity = Amenity()
        amenity.name = "  Spa  "
        self.assertEqual(amenity.name.strip(), "Spa")

    def test_name_case(self):
        """
        Test case to verify that the name attribute is case-insensitive.
        """
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name.lower(), "swimming pool")

    def test_name_special_characters(self):
        amenity = Amenity()
        amenity.name = "Gym & Spa"
        self.assertEqual(amenity.name, "Gym & Spa")

    def test_name_unicode(self):
        amenity = Amenity()
        amenity.name = "Sauna \u2665"
        self.assertEqual(amenity.name, "Sauna \u2665")


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_no_args_instantiates(self):
        """Test that Amenity can be instantiated with no arguments."""
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        """Test that a new instance of Amenity is stored in objects."""
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test that the id attribute of Amenity is of type str."""
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        """Test that the created_at attribute of Amenity is of type datetime."""
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test that the updated_at attribute of Amenity is of type datetime."""
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        """Test that the name attribute of Amenity is a public class attribute."""
        am = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", am.__dict__)

    def test_two_amenities_unique_ids(self):
        """Test that two instances of Amenity have unique ids."""
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_two_amenities_different_created_at(self):
        """Test that two instances of Amenity have different created_at timestamps."""
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.created_at, am2.created_at)

    def test_two_amenities_different_updated_at(self):
        """Test that two instances of Amenity have different updated_at timestamps."""
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.updated_at, am2.updated_at)

    def test_str_representation(self):
        """Test the string representation of Amenity."""
        dt = datetime.today()
        dt_repr = repr(dt)
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        amstr = am.__str__()
        self.assertIn("[Amenity] (123456)", amstr)
        self.assertIn("'id': '123456'", amstr)
        self.assertIn("'created_at': " + dt_repr, amstr)
        self.assertIn("'updated_at': " + dt_repr, amstr)

    def test_args_unused(self):
        """Test that passing None as an argument to Amenity does not affect the instance."""
        am = Amenity(None)
        self.assertNotIn(None, am.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test instantiation of Amenity with keyword arguments."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        am = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(am.id, "345")
        self.assertEqual(am.created_at, dt)
        self.assertEqual(am.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test instantiation of Amenity with None as keyword arguments."""
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        """Test if the return type of to_dict() is a dictionary."""
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test if the dictionary returned by to_dict() contains the correct keys."""
        am = Amenity()
        self.assertIn("id", am.to_dict())
        self.assertIn("created_at", am.to_dict())
        self.assertIn("updated_at", am.to_dict())
        self.assertIn("__class__", am.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test if the dictionary returned by to_dict() contains the added attributes."""
        am = Amenity()
        am.middle_name = "Holberton"
        am.my_number = 98
        self.assertEqual("Holberton", am.middle_name)
        self.assertIn("my_number", am.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test if the datetime attributes in the dictionary returned by to_dict() are strings."""
        am = Amenity()
        am_dict = am.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test the output of to_dict() with specific attribute values."""
        dt = datetime.today()
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        tdict = {
            "id": "123456",
            "__class__": "Amenity",
            "created_at": dt.isoformat(),
            "updated_at": dt.isoformat(),
        }
        self.assertDictEqual(am.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test if the dictionary returned by to_dict() is different from the __dict__ attribute."""
        am = Amenity()
        self.assertNotEqual(am.to_dict(), am.__dict__)

    def test_to_dict_with_arg(self):
        """Test if to_dict() raises a TypeError when called with an argument."""
        am = Amenity()
        with self.assertRaises(TypeError):
            am.to_dict(None)


if __name__ == '__main__':
    unittest.main()
