#!/usr/bin/python3
"""Module for the entry point, the command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):
    """Class for command interpreter"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on entering empty line"""
        pass

    def do_quit(self, arg):
        """Exit the console"""
        return True

    def do_EOF(self, arg):
        """Exit the console using EOF (Ctrl+D)"""
        print("")  # Print a newline for better console output
        return True

    def do_create(self, arg):
        """creates a new instance"""
        if arg is None or arg == "":
            print("** class name is missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes()[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """prints the string representation of an instance"""
        if arg is None or arg == "":
            print("** class name missing **")
        else:
            args = arg.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                obj_key = "{}.{}".format(args[0], args[1])
                if obj_key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[obj_key])




if __name__ == "__main__":
    HBNBCommand().cmdloop()
