#!/usr/bin/python3

"""Console"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class_models = ["BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]


class HBNBCommand(cmd.Cmd):
    """Class for console"""

    prompt = "(hbnb) "
    file = None

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit(0)

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return(True)

    def do_create(self, arg):

        if arg == "":
            print("** class name missing **")
            return
        ARG = arg.split()
        try:
            INST = eval(ARG[0])()
            INST.save()
            print(INST.id)
        except ARG[0].DoesNotExist:
            print("** class doesn't exist **")
            return

    def do_show(self, arg):
        ARG = arg.split()
        if len(ARG) < 1:
            print("** class name missing **")
            return

        if ARG[0] not in class_models:
            print("** class doesn't exist **")
            return

        if len(ARG) < 2:
            print("** instance id missing **")
            return

        dict = storage.all()
        for key, value in dict.items():
            if f"{ARG[0]}.{ARG[1]}" == key:
                print(value)
                return

        print("** no instance found **")

    def do_destroy(self, arg):
        ARG = arg.split()
        if len(ARG) <= 1:
            print("** class name missing **")
            return

        if ARG[0] not in class_models:
            print("** class doesn't exist **")
            return

        if len(ARG) < 2:
            print("** instance id missing **")
            return

        dict = storage.all()
        for key, value in dict.items():
            if f"{ARG[0]}.{ARG[1]}" == key:
                del dict[key]
                storage.save()
                return

        print("** no instance found **")
        return

    def do_all(self, arg):
        ARG = arg.split()
        str_list = []
        obj_dict = storage.all()

        if len(ARG) == 0:
            for key, value in obj_dict.items():
                str_list.append(str(value))
            print(str_list)
            return

        if ARG[0] in class_models:
            for key, value in obj_dict.items():
                if ARG[0] in key:
                    str_list.append(str(value))
            print(str_list)
        else:
            print("** class doesn't exist **")
            return

    def do_update(self, arg):
        ARG = arg.split()

        if len(ARG) == 0:
            print("** class name missing **")
            return

        try:
            model = eval(ARG[0])
        except Exception as e:
            print("** class doesn't exist **")
            return

        if len(ARG) < 2:
            print("** instance id missing **")
            return

        dict = storage.all()
        not_found = 1
        for key, value in dict.items():
            if f"{ARG[0]}.{ARG[1]}" == key:
                not_found = 0
                continue
        if not_found == 1:
            print("** no instance found **")
            return

        if len(ARG) < 3:
            print("** attribute name missing **")
            return

        if len(ARG) < 4:
            print("** value missing **")
            return

        if len(ARG) > 4:
            ARG = ARG[:3]

        dict = storage.all()
        for key, value in dict.items():
            if f"{ARG[0]}.{ARG[1]}" == key:
                if type(ARG[3]) is int:
                    setattr(value, ARG[2], int(ARG[3]))
                elif type(ARG[3]) is float:
                    setattr(value, ARG[2], float(ARG[3]))
                else:
                    setattr(value, ARG[2], ARG[3].strip('"'))
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
