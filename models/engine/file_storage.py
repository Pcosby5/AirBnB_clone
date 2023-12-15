#!/usr/bin/python3
"""Defines FileStorage class."""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.user import User
from models.city import City


class FileStorage:
    """Defines the  storage

    Attributes:
        __file_path (str): name of the file to save objects to.
        __objects (dict): dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        new_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(new_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        n_dict = FileStorage.__objects
        obj_dict = {obj: n_dict[obj].to_dict() for obj in ndict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for p in obj_dict.values():
                    class_name = p["__class__"]
                    del p["__class__"]
                    self.new(eval(class_name)(**p))
        except FileNotFoundError:
            return
