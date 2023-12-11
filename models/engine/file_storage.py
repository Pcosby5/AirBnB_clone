from models.base_model import BaseModel
import json
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from os.path import exists


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_obj = {
            key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_obj, file)

    def reload(self):
        try:
            if exists(self.__file_path):
                with open(self.__file_path, 'r') as file:
                    data = json.load(file)
                    for key, value in data.items():
                        class_name, obj_id = key.split('.')
                        class_module = globals().get(class_name)
                        if class_module:
                            self.__objects[key] = class_module(**value)
        except FileNotFoundError:
            pass
