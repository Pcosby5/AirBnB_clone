#!/usr/bin/python3
"""This script is the base model
It has the parent class of all other classes"""

import uuid
from datetime import datetime


class BaseModel:

    """Class from which other classes will inherit"""

    def __init__(self):
        """creates an instance of all attributes"""

        self.id = str(uuid.uuid())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Returns official string representation"""

        return "[{}] ({}) {}".\
                format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary of key/value pairs of __dict__"""

        ret_dict = self.__dict__.copy()
        ret_dict["__class__"] = type(self).__name__
        ret_dict["created_at"] = ret_dict["created_at"].isoformat()
        ret_dict["updated_at"] = ret_dict["updated_at"].isoformat()
        return ret_dict






