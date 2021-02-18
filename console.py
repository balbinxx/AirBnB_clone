#!/usr/bin/python3
"""This module holds a console that contains
    the entry point of the command interpreter
    """
import cmd
import models
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """HBNBCommand, BNB Console
    """
    prompt = "(hbnb) "
    __bnb_classes = {"BaseModel": BaseModel,
                     "User": User,
                     "City": City, "Amenity": Amenity,
                     "Place": Place, "Review": Review,
                     "State": State}

    def emptyline(self):
        """Empty line + ENTER shouldn't execute anything
        """
        return

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Exit the program with Ctrl + D
        """
        return True

    def do_create(self, arg):
        """Creates a new instance of Class-Name, saves
        it (to the JSON file) and prints the id
        Usage: create <ClassName>
        """
        if not arg:
            print("** class name missing **")
            return
        if arg in HBNBCommand.__bnb_classes:
            new_instance = HBNBCommand.__bnb_classes[arg]()
            new_instance.save()
            print(new_instance.id)
            return
        else:
            print("** class doesn't exist **")
            return

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id
        Usage: show <ClassName> <id>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__bnb_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        aux_key = "{}.{}".format(args[0], args[1])
        if aux_key in storage.all():
            print(storage.all()[aux_key])
            return
        else:
            print("** no instance found **")
            return

    def do_destroy(self, arg):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file).
        Usage: destroy <ClassName> <id>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__bnb_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        aux_key = "{}.{}".format(args[0], args[1].replace('"', ''))
        if aux_key in storage.all():
            del storage.all()[aux_key]
            storage.save()
            return
        else:
            print("** no instance found **")
            return

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name.
        Usage: all, all <ClassName>
        """
        if not arg:
            all_list = []
            for key, value in storage.all().items():
                all_list.append(str(value))
            print(all_list)
            return
        if arg in HBNBCommand.__bnb_classes:
            all_list = []
            for key, value in storage.all().items():
                if type(value).__name__ == arg:
                    all_list.append(str(value))
            print(all_list)
            return
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute (save
        the change into the JSON file).
        Usage: update <ClassName> <id> <key> <value>
        """
        args = arg.split()
        if arg == "":
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__bnb_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        aux_key = "{}.{}".format(args[0], args[1].replace('"', ''))
        if aux_key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        if args[3][0] == '"':
            temp_value = " ".join(aux_arg for aux_arg in args[3:])
            temp_value = temp_value.split('"')[1]
        else:
            temp_value = args[3]
        if "." in temp_value:
            try:
                temp_value = float(temp_value)
            except ValueError:
                pass
        else:
            try:
                temp_value = int(temp_value)
            except ValueError:
                pass
        setattr(storage.all()[aux_key], args[2], temp_value)
        storage.all()[aux_key].save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
