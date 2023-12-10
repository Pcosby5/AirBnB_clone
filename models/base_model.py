#!/usr/bin/python3
"""This script is the base model
It has the parent class of all other classes"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Class from which other classes will inherit"""

    def __init__(self, *args, **kwargs):
        """creates an instance of all attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)

            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns official string representation"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary of key/value pairs of __dict__"""
        ret_dict = self.__dict__.copy()
        ret_dict["__class__"] = self.class__.__name__
        ret_dict["created_at"] = ret_dict["created_at"].isoformat()
        ret_dict["updated_at"] = ret_dict["updated_at"].isoformat()
        return ret_dict
