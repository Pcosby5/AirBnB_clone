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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
