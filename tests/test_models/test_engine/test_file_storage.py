#/usr/bin/python3

import unittest
from models.engine.file_storage import FileStorage
SomeObject = __import__('tests.test_engine.test_file_storage.SomeObject').SomeObject

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def test_all(self):
        # Test if all() method returns the __objects dictionary
        self.assertEqual(self.storage.all(), self.storage._FileStorage__objects)

    def test_new(self):
        # Test if new() method adds an object to the __objects dictionary
        obj = SomeObject()
        self.storage.new(obj)
        self.assertIn(obj, self.storage._FileStorage__objects.values())

    def test_save(self):
        # Test if save() method saves the __objects dictionary to file
        obj = SomeObject()
        self.storage.new(obj)
        self.storage.save()

        # Reload the storage to check if the object was saved
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn(obj, new_storage._FileStorage__objects.values())

    def test_reload(self):
        # Test if reload() method loads objects from file to __objects dictionary
        obj = SomeObject()
        self.storage.new(obj)
        self.storage.save()

        # Clear the __objects dictionary and reload from file
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertIn(obj, self.storage._FileStorage__objects.values())

if __name__ == '__main__':
    unittest.main()
