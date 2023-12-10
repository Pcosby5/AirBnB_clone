#!/usr/bin/python3
"""Module for FileStorage class"""
import datetime
import json
import os


class FileStorage:

    """private class attributes for storing and getting data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary's __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to JSON file"""
        with open(FileStorage.__file_path, "w") as file:
            serialized_obj = {
                    key: obj.to_dict() for key,
                    obj in FileStorage.__objects.items()
                    }
            json.dump(serialized_obj, file)

    def classes(self):
        """Returns a dictionary of valid classes"""
        from models.base_model import BaseModel, User, State, City, Amenity, Place, Review

        classes = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
                }
        return classes

    def reload(self):
        """Reloads the object or data that has been stored
        other words, deserializes the json file to object
        only if it exists"""
        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r") as file:

            deserialized_file = json.load(file)
            # from models.engine.file_storage import storage
            deserialized_file = {
                    key: self.classes()[obj["__class__"]](**obj)
                    for key, obj in deserialized_file.items()
                    }
            FileStorage.__objects = deserialized_file

    def attributes(self):
        """Returns the valid attribute and their types for classname"""
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
                    "text": str},
        }
        return attributes
