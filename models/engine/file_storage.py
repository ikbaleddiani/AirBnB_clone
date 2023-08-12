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
        """ Returns dictionary of all objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in objects the new object with the key <class name>.id """
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """ Serializes all objects to the JSON file """
        objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(
                FileStorage.__file_path, encoding="utf-8", mode="w"
                ) as file:
            file.write(dumps(objects))

    def reload(self):
        """ Deserializes the JSON file to instances """
        try:
            with open(
                    FileStorage.__file_path, encoding="utf-8", mode="r"
                    ) as file:
                objects = loads(file.read())
                for key, kwargs in objects.items():
                    cls = key.split(".")[0]
                    if cls in models.classes:
                        cls = models.classes[cls]
                        FileStorage.__objects[key] = cls(**kwargs)
        except FileNotFoundError:
            pass
