#!/usr/bin/python3
"""Defines the HBNB console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the HBNB requirement interpreter

    Attributes:
        cprompt (str): custom command prompt
    """
    prompt = "(hbnb)"

    def emptyline(self):
        """ """
        pass

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

    def do_create(self, arg):
        """Creates instance of BaseModel and saves to JSON file

        Usage: create <class>
        """
        pass

    def do_show(self, arg):
        """Set outs string repr of an instance

        Usage: Displays <class_name> <id>
        """
        pass

    def do_destroy(self, arg):
        """Deletes class instances based on class_name and id

        Usage: Destroys <class_name> and <id>
        """
        pass

    def do_all(self, arg):
        """Prints string repr of all instances or specific classes

        Usage: all[class_name]
        """
        pass

    def do_update(self, arg):
        """Updates instance by adding or updating attribute

        Usage: update <class_name> <id> <attribute_name> <attribute value>
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
