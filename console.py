#!/usr/bin/python3
"""
    console model: command interpreter
"""
import models
import cmd
from re import fullmatch, search


def cast_value(value):
    try:
        value = int(value)
    except Exception:
        try:
            value = float(value)
        except Exception:
            pass
    return value


class HBNBCommand(cmd.Cmd):
    """** Defines HBNBCommand class, the enter point to the program **"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """**quit command to exit program **
        """
        return True

    def emptyline(self):
        """** Do anything **"""
        pass

    def do_EOF(self, line):
        """**EOF and exit **
        """
        return True

    def do_create(self, line):
        """Instantiate a given model"""

        if line:
            args = line.split()
            if args[0] in models.classes:
                instance = models.classes[args[0]]()
                instance.save()
                print(instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
            ** Prints the string representation of the instance **
            syntax:
                - show <class name> <id>
                or
                - <class name>.show(<id>)
        """
        if line:
            args = line.split()
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
        """
            ** Deletes the instance **
            syntax:
                - destroy <class name> <id>
                or
                - <class name>.destroy(<id>)
        """
        if line:
            args = line.split()
            if args[0] in models.classes:
                classname = models.classes[args[0]].__name__
                try:
                    id = args[1]
                    obj = models.storage.all()
                    try:
                        del obj[classname + "." + id]
                        models.storage.save()
                    except Exception:
                        print("** no instance found **")
                except Exception:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """
            ** Prints all string representation of all instances **
            syntax:
                - all [<class name>]
                or
                - <class name>.all()
        """
        objects = models.storage.all()
        if line:
            args = line.split()
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
        """
            ** Updates or add new attributes to the instance **
            syntax:
                - update <class name> <id> <attribute name> <attribute value>
                or
                - <class name>.update(<id>, [dict])
            -------------------------------------------------------------------
            Note: attribute value with a space must be between double quote
        """
        if line:
            args = line.split()
            if args[0] in models.classes:
                classname = models.classes[args[0]].__name__
                try:
                    id = args[1]
                    obj = models.storage.all()
                    try:
                        obj = obj[classname + "." + id]
                        for i in range(2, len(args) - 1, 2):
                            try:
                                attribute = args[i]
                                try:
                                    if ">$<" in args[i + 1]:
                                        value = args[i + 1].replace(">$<", " ")
                                    elif args[i + 1].startswith("\""):
                                        value = line.split("\"")[1]
                                        i += 2
                                    else:
                                        value = args[i + 1]
                                    value = cast_value(value)
                                    setattr(obj, attribute, value)
                                    obj.save()
                                except IndexError:
                                    print("** value missing **")
                            except IndexError:
                                print("** attribute name missing **")
                    except IndexError:
                        print("** no instance found **")
                except IndexError:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def precmd(self, line):
        """
            ** Preprocess the command line **
            syntax: <class name>.<command>(<id>,[dict])
        """
        pattern = "^[BUSCAPR]{1}[a-z]*.[a-z]{3,7}(.*)?"
        pattern = fullmatch(pattern, line)
        if pattern:
            classname = line.split(".")[0]
            command = line.split("(")[0].split(".")[1]
            if command in ("all", "count"):
                return command + " " + classname
            args = search(r"\(.*\)+", line).group()[1: -1]
            id = args.split(", ")[0].translate({34: 0})
            if "," in args:
                if "{" in args:
                    kwargs = search("{.*}+", args).group()[1: -1]
                    kwargs = kwargs.split(", ")
                    list1 = []
                    for item in kwargs:
                        list1.append(item.split(": ")[0].translate(
                            {34: "", 39: ""}))
                        list1.append(item.split(": ")[1].translate(
                            {39: "", 34: "", 32: ">$<"}))
                    return " ".join([command, classname, id] + list1)
                attribute = args.split(", ")[1]
                value = args.split(", ")[2].translate(
                        {39: "", 34: "", 32: ">$<"})
                return " ".join([command, classname, id, attribute, value])
            else:
                return " ".join([command, classname, args])
        else:
            return line

    def do_count(self, line):
        """
            ** Prints the instances number of a class **
            syntax: <class name>.count()
        """
        try:
            classname = line.split()[0]
            if classname in models.classes:
                count = 0
                objects = models.storage.all()
                for key in objects:
                    if classname in key:
                        count += 1
                        print(count)
                    else:
                        print("** class doesn't exist **")
        except Exception:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
