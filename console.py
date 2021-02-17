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
