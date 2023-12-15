#!/usr/bin/python3
"""Defines the HBNB console"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def tokenizer(arg):
    curl_tokens = re.search(r"\{(.*?)\}", arg)
    bracket_tokens = re.search(r"\[(.*?)\]", arg)
    if curl_tokens is None:
        if bracket_tokens is None:
            return [idx.strip(",") for idx in split(arg)]
        else:
            lexicon = split(arg[:bracket_tokens.span()[0]])
            tok = [idx.strip(",") for idx in lexicon]
            tok.append(bracket_tokens.group())
            return tok
    else:
        lexicon = split(arg[:curl_tokens.span()[0]])
        tok = [idx.strip(",") for idx in lexicon]
        tok.append(curl_tokens.group())
        return tok


class HBNBCommand(cmd.Cmd):
    """Defines the HBNB requirement interpreter

    Attributes:
        prompt (str): custom command prompt
    """
    prompt = "(hbnb) "
    n_classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            }

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

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            command = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", command[1])
            if match is not None:
                commands = [command[1][:match.span()[0]], match.group()[1:-1]]
                if commands[0] in arg_dict.keys():
                    call = "{} {}".format(command[0], commands[1])
                    return arg_dict[commands[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_create(self, arg):
        """Creates instance of BaseModel and saves to JSON file

        Usage: create <class>
        """
        command = tokenizer(arg)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in HBNBCommand.n_classes:
            print("** class doesn't exist **")
        else:
            print(eval(command[0])().id)
            storage.save()

    def do_show(self, arg):
        """Set outs string repr of an instance

        Usage: Displays <class_name> <id>
        """
        command = tokenizer(arg)
        obj_dict = storage.all()
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in HBNBCommand.n_classes:
            print("** class doesn't exist **")
        elif len(command) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(command[0], command[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(command[0], command[1])])

    def do_destroy(self, arg):
        """Deletes class instances based on class_name and id

        Usage: Destroys <class_name> and <id>
        """
        command = tokenizer(arg)
        obj_dict = storage.all()
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in HBNBCommand.n_classes:
            print("** class doesn't exist **")
        elif len(command) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(command[0], command[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(command[0], command[1])]
            storage.save()

    def do_all(self, arg):
        """Prints string repr of all instances or specific classes

        Usage: all[class_name]
        """
        command = tokenizer(arg)
        if len(command) > 0 and command[0] not in HBNBCommand.n_classes:
            print("** class doesn't exist **")
        else:
            new_obj = []
            for obj in storage.all().values():
                if len(command) > 0 and command[0] == obj.__class__.__name__:
                    new_obj.append(obj.__str__())
                elif len(command) == 0:
                    new_obj.append(obj.__str__())
            print(new_obj)

    def do_count(self, arg):
        """Fetch and count the number of instances of a class
        Usage: count <class>
        """
        command = tokenizer(arg)
        count = 0
        for obj in storage.all().values():
            if command[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Updates instance by adding or updating attribute

        Usage: update <class_name> <id> <attribute_name> <attribute value>
        """
        command = tokenizer(arg)
        obj_dict = storage.all()

        if len(command) == 0:
            print("** class name missing **")
            return False
        if command[0] not in HBNBCommand.n_classes:
            print("** class doesn't exist **")
            return False
        if len(command) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(command[0], command[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(command) == 2:
            print("** attribute name missing **")
            return False
        if len(command) == 3:
            try:
                type(eval(command[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(command) == 4:
            obj = obj_dict["{}.{}".format(command[0], command[1])]
            if command[2] in obj.__class__.__dict__.keys():
                val_type = type(obj.__class__.__dict__[command[2]])
                obj.__dict__[command[2]] = val_type(command[3])
            else:
                obj.__dict__[command[2]] = command[3]
        elif type(eval(command[2])) == dict:
            obj = obj_dict["{}.{}".format(command[0], command[1])]
            for key, val in eval(command[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in
                        {str, int, float}):
                    val_type = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = val_type(val)
                else:
                    obj.__dict__[key] = val
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
