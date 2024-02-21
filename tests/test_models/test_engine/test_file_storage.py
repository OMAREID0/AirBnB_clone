
import unittest
import models
import json
import uuid
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
import os
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

class TestFileStorage(unittest.TestCase):
    """Unittests for testing the FileStorage class."""

    def setUp(self):
        """Set up the test environment."""
        self.file_storage = FileStorage()

    def test_all_returns_dictionary(self):
        """Test if the 'all' method returns a dictionary."""
        result = self.file_storage.all()
        self.assertIsInstance(result, dict)

    def test_new_adds_object_to_dictionary(self):
        """Test if the 'new' method adds an object to the dictionary."""
        class MockObject:
            def __init__(self, id):
                self.id = id
        obj = MockObject("1")
        self.file_storage.new(obj)
        result = self.file_storage.all()
        self.assertIn("MockObject.1", result)

    def test_save_writes_to_file(self):
        """Test if the 'save' method writes to a file."""
        class MockObject:
            def __init__(self, id):
                self.id = id

            def to_dict(self):
                return {"id": self.id}
        obj = MockObject("1")
        self.file_storage.new(obj)
        self.file_storage.save()
        # Check if file exists and contains the object
        # You can add assertions based on your specific implementation

    def test_reload_loads_objects_from_file(self):
        """Test if the 'reload' method loads objects from a file."""
        class MockObject:
            def __init__(self, id):
                self.id = id

            def to_dict(self):
                return {"id": self.id}
        obj = MockObject("1")
        self.file_storage.new(obj)
        self.file_storage.save()
        # Modify the object in memory
        obj.id = "2"
        self.file_storage.reload()
        result = self.file_storage.all()
        self.assertIn("MockObject.1", result)
        self.assertNotIn("MockObject.2", result)

    class TestFileStorage_instantiation(unittest.TestCase):
        """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        """Test if FileStorage can be instantiated with no arguments."""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        """Test if FileStorage raises TypeError when instantiated with an argument."""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        """Test if the file_path attribute of FileStorage is a private string."""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        """Test if the objects attribute of FileStorage is a private dictionary."""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        """Test if models.storage is an instance of FileStorage."""
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        """Set up method to be executed before each test case."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """Tear down method to be executed after each test case."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """Test the 'all' method of the FileStorage class."""
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        """Test the 'all' method of the FileStorage class with an argument."""
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        """Test the 'new' method of the FileStorage class."""
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("User." + us.id, models.storage.all().keys())
        self.assertIn(us, models.storage.all().values())
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn(pl, models.storage.all().values())
        self.assertIn("City." + cy.id, models.storage.all().keys())
        self.assertIn(cy, models.storage.all().values())
        self.assertIn("Amenity." + am.id, models.storage.all().keys())
        self.assertIn(am, models.storage.all().values())
        self.assertIn("Review." + rv.id, models.storage.all().keys())
        self.assertIn(rv, models.storage.all().values())

    def test_new_with_args(self):
        """Test the 'new' method of the FileStorage class with arguments."""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save_with_arg(self):
        """Test the 'save' method of the FileStorage class with an argument."""
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        """Test the 'reload' method of the FileStorage class."""
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.reload()
        objs = FileStorage._FileStorage__objects

    def test_reload_with_arg(self):
        """Test the 'reload' method of the FileStorage class with an argument."""
        with self.assertRaises(TypeError):
            models.storage.reload(None)


class TestFileStorage_instantiation(unittest.TestCase):
    '''Unittest for FileStorage class'''

    def test_instantiations(self):
        '''Test if FileStorage class can be instantiated'''
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_file_path(self):
        '''Test the type of __file_path attribute'''
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_obj_dict(self):
        '''Test the type of __objects attribute'''
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_var(self):
        '''Test if models.storage is an instance of FileStorage'''
        self.assertEqual(FileStorage, type(models.storage))


class TestFileStorage_methods(unittest.TestCase):
    '''unittest for FileStorage methods'''

    # Unittest for all()
    def test_dict_type(self):
        instant = FileStorage
        self.assertEqual(dict, type(models.storage.all()))

    # Unittest for new()
    def test_new_method(self):
        instant = BaseModel()
        models.storage.new(instant)
        self.assertIn("BaseModel." + instant.id, models.storage.all().keys())


if __name__ == '__main__':
    unittest.main()
