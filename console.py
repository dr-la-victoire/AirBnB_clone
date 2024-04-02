#!/usr/bin/python3
"""This module is the console for Airbnb"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """This class creates the console"""
    prompt = "(hbnb) "
    # A list of classes
    __classes = ["BaseModel", "User", "Amenity", "City", "Place",
                 "Review", "State"]

    def do_create(self, line):
        """Creates a new instance and prints its id"""
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            print(new.id)

    def do_show(self, line):
        """Prints the str representation of an instance"""
        if not line:
            print("** class name missing **")
        else:
            new_line = line.split(' ')
            if new_line[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            elif len(new_line) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(new_line[0], new_line[1])
                # remember all is a dict of __objects
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance and saves the changes"""
        if not line:
            print("** class name missing **")
        else:
            new_line = line.split(' ')
            if new_line[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            elif len(new_line) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(new_line[0], new_line[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Prints all the str representations of an instance"""
        if not line:
            return
        if line not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            line = line.split(' ')
            # Create an empty list to store the instances
            insts = []
            # Loop through the dict values
            for value in storage.all().values():
                # If the classname matches line[0]
                if value.__class__.__name__ == line[0]:
                    # Add to the list
                    insts.append(value.__str__())
            # Print the list
            print(insts)

    def do_update(self, line):
        """Updates an instance based on class name and id"""
        args = line.split(" ")
        # Getting a dictionary of all the stored instances
        objdict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(args) == 4:
            obj = objdict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = objdict["{}.{}".format(args[0], args[1])]
            for k, v in eval(args[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF signal to exit the program"""
        return True

    def emptyline(self):
        """Does nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
