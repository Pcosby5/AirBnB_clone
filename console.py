#!/usr/bin/python3
"""Defines the HBNB console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the HBNB requirement interpreter

    Attributes:
        cprompt (str): custom command prompt
    """
    cprompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to close program"""
        return True

    def do_EOF(self, arg):
        """EOF to signal and exit the program"""
        print("")
        return True

    def help_quit(self, arg):
        """Quit command to exit the program"""
        print("Quit command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
