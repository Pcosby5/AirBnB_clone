#!/usr/bin/python3
"""Defines FileStorage class"""
from models.base_model import BaseModel
import json
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from os.path import exists
import datetime


class FileStorage:
    """Defines abstracted storage engine.

    Attributes:
        __file_path (str): file path to save objects to.
        __objects (dict): dictionary of instance objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dict of instances based on class names"""
        if cls is None:
            return self.__objects
        else:
            obj_dict = {}
            for key, obj in self.__objects.items():
                class_name = key.split('.')[0]
                if class_name == cls.__name__:
                    obj_dict[key] = obj
            return obj_dict

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        new_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(new_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def classes(self):
        classes = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review}
        return classes

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

    def attributes(self):
        """Returns the valid attributes and their types for classname"""
        attributes = {
                "BaseModel":
                {"id": str,
                    "created_at": datetime.datetime,
                    "updated_at": datetime.datetime},
                "User":
                {"email": str,
                    "password": str,
                    "first_name": str,
                    "last_name": str},
                "State":
                {"name": str},
                "City":
                {"state_id": str,
                    "name": str},
                "Amenity":
                {"name": str},
                "Place":
                {"city_id": str,
                    "user_id": str,
                    "name": str,
                    "description": str,
                    "number_rooms": int,
                    "number_bathrooms": int,
                    "max_guest": int,
                    "price_by_night": int,
                    "latitude": float,
                    "longitude": float,
                    "amenity_ids": list},
                "Review":
                {"place_id": str,
                    "user_id": str,
                    "text": str}
                }
        return attributes
