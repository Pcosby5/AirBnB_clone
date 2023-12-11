#!/usr/bin/python3
"""Defines the HBNB console"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


def tokenizer(arg):
    curl_tokens = re.search(r"\{(.*?)\}", arg)
    bracket_tokens = re.search(r"\[(.*?)\]", arg)
    if curl_tokens is None:
        if bracket_tokens is None:
            return [idx.strip(",") for idx in split(arg)]
        else:
            lexicon = split(arg[:bracket_tokens.span()[0]])
            toks = [idx.strip(",") for idx in lexicon]
            toks.append(bracket_tokens.group())
            return toks
    else:
        lexicon = split(arg[:curl_tokens.span()[0]])
        toks = [idx.strip(",") for idx in lexicon]
        toks.append(curl_tokens.group())
        return toks


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
        command = parse(arg)
        if len(command) > 0 and command[0] not in HBNBCommand.n_classes:
            print("** class doesn't exist **")
        else:
            n_obj = []
            for obj in storage.all().values():
                if len(command) > 0 and command[0] == obj.__class__.__name__:
                    n_obj.append(obj.__str__())
                elif len(command) == 0:
                    n_obj.append(obj.__str__())
            print(n_obj)

    def do_update(self, arg):
        """Updates instance by adding or updating attribute

        Usage: update <class_name> <id> <attribute_name> <attribute value>
        """
        command = parse(arg)
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