#!/ust/bin/python3
"""
    FileStorage model:
    serializes instances to a JSON file and deserializes JSON file to instances
"""
from models.base_model import BaseModel
from models.user import User
from json import dumps, loads


class FileStorage:
    """ Defines FileStorage class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in objects the obj with key <obj class name>.id """
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """ Serializes objects to the JSON file """
        objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, encoding="utf-8", mode="w") as file:
            file.write(dumps(objects))

    def reload(self):
        """ deserializes the JSON file to onjects """
        try:
            with open(self.__file_path, encoding="utf-8", mode="r") as file:
                objects = loads(file.read())
                for key, kwargs in objects.items():
                    if key.startswith("BaseModel"):
                        self.__objects[key] = BaseModel(**kwargs)
                    if key.startswith("User"):
                        self.__objects[key] = User(**kwargs)
        except FileNotFoundError:
            pass
