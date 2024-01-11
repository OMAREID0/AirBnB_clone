#/usr/bin/python3

import json
import models.base_model as base_model
import models.user as user
import models.state as state
import models.city as city
import models.amenity as amenity
import models.place as place
import models.review as review


class FileStorage:
    """Class for file storage."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of all objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to the dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Save the objects to a JSON file."""
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Reload the objects from a JSON file."""
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except:
            pass
