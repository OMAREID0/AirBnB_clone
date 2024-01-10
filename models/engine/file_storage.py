#/usr/bin/python3

import json

class FileStorage:
    __file_path = open("file.json", "w")
    __objects = {}

def all(self):
    return self.__objects

def new(self, obj):
    key = f"{obj.__class__.__name__}.{obj.id}"
    self.__objects[key] = obj

def save(self):
    json.dump(self.__objects, self.__file_path)

def reload(self):
    try:
        with open(self.__file_path, "r") as f:
            self.__objects = json.load(f)
    except:
        pass