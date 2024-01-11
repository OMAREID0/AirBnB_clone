#/usr/bin/python3

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        # Test initialization of BaseModel instance
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_str(self):
        # Test string representation of BaseModel instance
        model = BaseModel()
        string = str(model)
        self.assertEqual(string, "[BaseModel] ({}) {}".format(model.id, model.__dict__))

    def test_save(self):
        # Test saving BaseModel instance
        model = BaseModel()
        prev_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(prev_updated_at, model.updated_at)

    def test_to_dict(self):
        # Test conversion of BaseModel instance to dictionary
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], model.id)
        self.assertEqual(model_dict["created_at"], model.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(model_dict["updated_at"], model.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))

if __name__ == '__main__':
    unittest.main()
