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

    def do_destroy(self, arg):
        """Deletes an instance of a class name and id"""
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
                    del storage.all()[obj_key]
                    storage.save()

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        if arg != "":
            args = arg.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                string_rep = [str(obj) for obj_key, obj in storage.all().items()
                        if type(obj).__name__ == args[0]]
                print(string_rep)

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return

        try:
            classname = args[0]
            att_name = args[2]
            att_value = args[3]

            if classname not in storage.all():
                print("** class doesn't exist **")
                return

            if len(args) < 2:
                print("** instance id missing **")
                return

            obj_key = "{}.{}".format(classname, args[1])
            if obj_key not in storage.all()[classname]:
                print("** no instance found **")
                return

            if len(args) < 3:
                print("** attribute name missing **")
                return

            new_instance = storage.all()[classname][obj_key]

            if hasattr(new_instance, att_name):
               att_type = type(getattr(new_instance, att_name))
               setattr(new_instance, att_name, att_type(att_value))
               storage.save()
        except IndexError:
            print("** attribute name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
