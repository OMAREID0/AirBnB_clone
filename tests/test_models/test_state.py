

import unittest
import models
import uuid
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
from models.state import State
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    """
    Unit tests for the State class.
    """

    def test_state_attributes(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_state_name_type(self):
        state = State()
        self.assertIsInstance(state.name, str)

    def test_state_name_assignment(self):
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")


class TestState_instantiation(unittest.TestCase):
    '''Unittest for User class'''

    def test_instantiations(self):
        '''
        Test if the instantiation of State class is successful.
        '''
        self.assertEqual(State, type(State()))

    def test_att_string(self):
        '''
        Test if the attributes of State class are of type string.
        '''
        instant = State()
        self.assertEqual(str, type(instant.name))
        self.assertEqual(str, type(instant.id))

    def test_created_at_is_public_datetime(self):
        '''
        Test if the created_at attribute of State class is of type datetime.
        '''
        self.assertEqual(datetime, type(State().created_at))


def test_id_notequal(self):
    id1 = BaseModel()
    id2 = BaseModel()
    self.assertNotEqual(id1.id, id2.id)


# ============ test to_dict ===============
class TestState_to_dict(unittest.TestCase):
    """
    This class contains unit tests for the `to_dict` method of the `State` class.
    """

    def test_type(self):
        """
        Test the type of the returned value from the `to_dict` method.
        """
        instant = State()
        self.assertTrue(dict, type(instant.to_dict))

    def test_keys(self):
        """
        Test if the required keys are present in the returned dictionary from the `to_dict` method.
        """
        instant = State()
        self.assertIn("id", instant.to_dict())
        self.assertIn("created_at", instant.to_dict())
        self.assertIn("updated_at", instant.to_dict())
        self.assertIn("__class__", instant.to_dict())

    def test_datetime_string(self):
        """
        Test if the values of "created_at" and "updated_at" keys in the returned dictionary are strings.
        """
        instant = State()
        inst_dict = instant.to_dict()
        self.assertTrue(str, type(inst_dict["created_at"]))
        self.assertTrue(str, type(inst_dict["updated_at"]))

    def test_save(self):
        """
        Test if the `save` method updates the "updated_at" attribute of the `State` instance.
        """
        instant = State()
        sleep(0.05)
        first_updated_at = instant.updated_at
        instant.save()
        self.assertLess(first_updated_at, instant.updated_at)


if __name__ == '__main__':
    unittest.main()
