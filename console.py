#!/usr/bin/python3
"""
console model: enter point to the program
"""
import cmd
from models.base_model import BaseModel
from models.user import User
import models


def cast_type(attribute, value):
    integers = (
                "number_rooms", "number_bathrooms", "max_guest",
                "price_by_night")
    floats = ("latitude", "longitude")

    if attribute in integers:
        try:
            value = int(value)
        except TypeError:
            raise TypeError("value must be integer")
    elif attribute in floats:
        try:
            value = float(value)
        except TypeError:
            raise TypeError("Value must be float")
    elif attribute == "amenity_ids":
        try:
            value = value.split(",")
        except TypeError:
            raise TypeError("Value must be a list of string")


class HBNBCommand(cmd.Cmd):
    """ Defines class """
    prompt = "(hbnb) "

    def do_quit(self, line):
        return True

    def emptyline(self):
        pass

    def do_EOF(self, line):
        return True

    def do_create(self, line):
        if line:
            args = line.split(" ")
            if args[0] in models.classes:
                instance = models.classes[args[0]]()
                instance.save()
                print(instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        if line:
            args = line.split(" ")
            if args[0] in models.classes:
                classname = models.classes[args[0]].__name__
                try:
                    id = args[1]
                    obj = models.storage.all()
                    try:
                        obj = obj[classname + "." + id]
                        print(str(obj))
                    except Exception:
                        print("** no instance found **")
                except Exception:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        if line:
            args = line.split(" ")
            if args[0] in models.classes:
                classname = models.classes[args[0]].__name__
                try:
                    id = args[1]
                    obj = models.storage.all()
                    try:
                        del obj[classname + "." + id]
                    except Exception:
                        print("** no instance found **")
                except Exception:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        objects = models.storage.all()
        if line:
            args = line.split(" ")
            if args[0] in models.classes:
                print(
                        list(
                            str(value) for key, value in objects.items() if
                            key.startswith(args[0])))
            else:
                print("** class doesn't exist **")
        else:
            print(list(str(value) for key, value in objects.items()))

    def do_update(self, line):
        if line:
            args = line.split(" ")
            if args[0] in models.classes:
                classname = models.classes[args[0]].__name__
                try:
                    id = args[1]
                    obj = models.storage.all()
                    try:
                        obj = obj[classname + "." + id]
                        try:
                            attribute = args[2]
                            try:
                                if args[3].startswith("\""):
                                    value = line.split("\"")[1]
                                else:
                                    value = line.split(" ")[3]
                                if classname == "Place":
                                    cast_type(attribute, value)
                                setattr(obj, attribute, value)
                                obj.save()
                            except Exception:
                                print("** value missing **")
                        except Exception:
                            print("** attribute name missing **")
                    except Exception:
                        print("** no instance found **")
                except Exception:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
