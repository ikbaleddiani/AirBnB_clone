#!/ust/bin/python3
"""
    FileStorage model:
    serializes instances to a JSON file and deserializes JSON file to instances
"""
import models
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
                    cls = key.split(".")[0]
                    if cls in models.classes:
                        self.__objects[key] = models.classes[cls](**kwargs)
        except FileNotFoundError:
            pass
