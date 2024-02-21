
import unittest
from datetime import datetime
from models.base_model import BaseModel
from time import sleep


class TestBaseModelInitialization(unittest.TestCase):
    def test_initialize_base_model_with_no_arguments(self):
        """
        Test case to verify the initialization of BaseModel with no arguments.
        """
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)
        self.assertEqual(base_model.created_at, base_model.updated_at)
        self.assertEqual(base_model.__class__.__name__, "BaseModel")

    def test_to_dict_base_model(self):
        """
        Test case to verify the to_dict method of BaseModel.
        """
        base_model = BaseModel()
        obj_dict = base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(obj_dict["id"], base_model.id)

    def test_str_base_model(self):
        """
        Test case to verify the string representation of BaseModel.
        """
        base_model = BaseModel()
        obj_str = str(base_model)
        expected_str = f"[BaseModel] ({base_model.id}) {base_model.__dict__}"
        self.assertEqual(obj_str, expected_str)

    def test_initialize_base_model_with_invalid_time_format(self):
        """
        Test case to verify that BaseModel raises a ValueError when initialized with an invalid time format.
        """
        with self.assertRaises(ValueError):
            BaseModel(created_at="2022-01-01")

    def test_base_model_attributes(self):
        """
        Test case to verify the presence of attributes in BaseModel.
        """
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, "id"))
        self.assertTrue(hasattr(base_model, "created_at"))
        self.assertTrue(hasattr(base_model, "updated_at"))

    def test_base_model_class_attribute(self):
        """
        Test case to verify the presence of the __class__ attribute in BaseModel.
        """
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, "__class__"))


class TestBaseModel(unittest.TestCase):
    '''Unittest for Base_model'''
    def test_instantiations(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_notequal(self):
        id1 = BaseModel()
        id2 = BaseModel()
        self.assertNotEqual(id1.id, id2.id)


class TestBaseModel_to_dict(unittest.TestCase):
    ''' unittest for to_dict method'''

    def test_type(self):
        '''Test if the type of to_dict method is dict'''
        instant = BaseModel
        self.assertTrue(dict, type(instant.to_dict))

    def test_keys(self):
        '''Test if the necessary keys are present in the dictionary returned by to_dict method'''
        instant = BaseModel()
        self.assertIn("id", instant.to_dict())
        self.assertIn("created_at", instant.to_dict())
        self.assertIn("updated_at", instant.to_dict())
        self.assertIn("__class__", instant.to_dict())

    def test_datetime_string(self):
        '''Test if the values of "created_at" and "updated_at" keys are of type string'''
        instant = BaseModel()
        inst_dict = instant.to_dict()
        self.assertTrue(str, type(inst_dict["created_at"]))
        self.assertTrue(str, type(inst_dict["updated_at"]))


if __name__ == '__main__':
    unittest.main()
