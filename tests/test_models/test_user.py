
import unittest
import models
import uuid
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
from models.user import User
from models.engine.file_storage import FileStorage
from datetime import datetime
import inspect
import models
from models import user
from models.base_model import BaseModel
import pep8
import unittest
from models.user import User
from models.engine.file_storage import FileStorage
import inspect
import models
import unittest
User = user.User

class TestUser(unittest.TestCase):
    def test_user_attributes(self):
        """
        Test case to verify that the User object has the correct initial attribute values.
        """
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
        cls.user_f = inspect.getmembers(User, inspect.isfunction)

    def test_set_email(self):
        """
        Test case to verify that the email attribute of the User object can be set correctly.
        """
        user = User()
        user.email = "test@example.com"
        self.assertEqual(user.email, "test@example.com")

    def test_set_password(self):
        """
        Test case to verify that the password attribute of the User object can be set correctly.
        """
        user = User()
        user.password = "password123"
        self.assertEqual(user.password, "password123")

    def test_set_first_name(self):
        """
        Test case to verify that the first_name attribute of the User object can be set correctly.
        """
        user = User()
        user.first_name = "John"
        self.assertEqual(user.first_name, "John")

    def test_set_last_name(self):
        """
        Test case to verify that the last_name attribute of the User object can be set correctly.
        """
        user = User()
        user.last_name = "Doe"
        self.assertEqual(user.last_name, "Doe")'

    def test_instantiations(self):
        '''
        Test case to check if User instance is created successfully.
        '''
        self.assertEqual(User, type(User()))

    def test_att_string(self):
        '''
        Test case to check the data types of User attributes.
        '''
        instant = User()
        self.assertEqual(str, type(instant.email))
        self.assertEqual(str, type(instant.password))
        self.assertEqual(str, type(instant.first_name))
        self.assertEqual(str, type(instant.last_name))
        self.assertEqual(str, type(instant.id))

    def test_created_at_is_public_datetime(self):
        '''
        Test case to check if created_at attribute is of type datetime.
        '''
        self.assertEqual(datetime, type(User().created_at))

    def test_id_notequal(self):
        '''
        Test case to check if the ids of two BaseModel instances are not equal.
        '''
        id1 = BaseModel()
        id2 = BaseModel()
        self.assertNotEqual(id1.id, id2.id)

    def test_type(self):
        """
        Test the type of the returned value from the `to_dict` method.
        """
        instant = User()
        self.assertTrue(dict, type(instant.to_dict))

    def test_keys(self):
        """
        Test if the required keys are present in the dictionary returned by the `to_dict` method.
        """
        instant = User()
        self.assertIn("id", instant.to_dict())
        self.assertIn("created_at", instant.to_dict())
        self.assertIn("updated_at", instant.to_dict())
        self.assertIn("__class__", instant.to_dict())

    def test_datetime_string(self):
        """
        Test if the values of "created_at" and "updated_at" keys are of type string in the dictionary returned by the `to_dict` method.
        """
        instant = User()
        inst_dict = instant.to_dict()
        self.assertTrue(str, type(inst_dict["created_at"]))
        self.assertTrue(str, type(inst_dict["updated_at"]))

    def test_save(self):
        """
        Test if the `save` method updates the value of "updated_at" attribute.
        """
        instant = User()
        sleep(0.05)
        first_updated_at = instant.updated_at
        instant.save()
        self.assertLess(first_updated_at, instant.updated_at)

    def test_pep8_conformance_user(self):
        """Test that models/user.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_user(self):
        """Test that tests/test_models/test_user.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_user_module_docstring(self):
        """Test for the user.py module docstring"""
        self.assertIsNot(user.__doc__, None,
                         "user.py needs a docstring")
        self.assertTrue(len(user.__doc__) >= 1,
                        "user.py needs a docstring")

    def test_user_class_docstring(self):
        """Test for the City class docstring"""
        self.assertIsNot(User.__doc__, None,
                         "User class needs a docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class needs a docstring")

    def test_user_func_docstrings(self):
        """Test for the presence of docstrings in User methods"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_is_subclass(self):
        """Test that User is a subclass of BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_email_attr(self):
        """Test that User has attr email, and it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        if models.storage_t == 'db':
            self.assertEqual(user.email, None)
        else:
            self.assertEqual(user.email, "")

    def test_password_attr(self):
        """Test that User has attr password, and it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "password"))
        if models.storage_t == 'db':
            self.assertEqual(user.password, None)
        else:
            self.assertEqual(user.password, "")

    def test_first_name_attr(self):
        """Test that User has attr first_name, and it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        if models.storage_t == 'db':
            self.assertEqual(user.first_name, None)
        else:
            self.assertEqual(user.first_name, "")

    def test_last_name_attr(self):
        """Test that User has attr last_name, and it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        if models.storage_t == 'db':
            self.assertEqual(user.last_name, None)
        else:
            self.assertEqual(user.last_name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = User()
        new_d = u.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in u.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = User()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "User")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))


if __name__ == '__main__':
    unittest.main()
