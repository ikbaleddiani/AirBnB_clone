#!/usr/bin/python3
"""
    Console test cases model
"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.user import User
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """ HBNBCommand test cases """

    def test_commands(self):
        """ Tests cases for all Console command """
        commands = ["create", "show", "update", "destroy", "all", "count"]

        self.assertEqual(True, HBNBCommand().onecmd("quit"))
        self.assertEqual(True, HBNBCommand().onecmd("EOF"))
        self.assertEqual(None, HBNBCommand().onecmd(""))
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)
        s = ""
        s += "Documented commands (type help <topic>):\n"
        s += "========================================\n"
        s += "EOF  all  count  create  destroy  help  quit  show  update"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertEqual(f.getvalue().strip(), s)

        for cmd in commands:
            with patch('sys.stdout', new=StringIO()) as f:
                if cmd == "all":
                    continue
                HBNBCommand().onecmd(cmd)
                output = "** class name missing **"
                self.assertEqual(f.getvalue().strip(), output)

        for cmd in commands:
            with patch('sys.stdout', new=StringIO()) as f:
                if cmd == "count":
                    continue
                HBNBCommand().onecmd(cmd + " user")
                output = "** class doesn't exist **"
                self.assertEqual(f.getvalue().strip(), output)

        for cmd in commands:
            cmds = ["create", "all", "count"]
            with patch('sys.stdout', new=StringIO()) as f:
                if cmd in cmds:
                    continue
                HBNBCommand().onecmd("{} User".format(cmd))
                output = "** instance id missing **"
                self.assertEqual(f.getvalue().strip(), output)

        for cmd in commands:
            cmds = ["create", "all", "count"]
            with patch('sys.stdout', new=StringIO()) as f:
                if cmd in cmds:
                    continue
                HBNBCommand().onecmd("{} User xxxx".format(cmd))
                output = "** no instance found **"
                self.assertEqual(f.getvalue().strip(), output)

        with patch('sys.stdout', new=StringIO()) as f:
            id = User().id
            HBNBCommand().onecmd("update User {}".format(id))
            output = "** attribute name missing **"
            self.assertEqual(f.getvalue().strip(), output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User {} name".format(id))
            output = "** value missing **"
            self.assertEqual(f.getvalue().strip(), output)
