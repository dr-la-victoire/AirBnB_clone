#!/usr/bin/python3
"""This module is the console for Airbnb"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """This class creates the console"""
    prompt = "(hbnb) "
    # A list of classes
    __classes = ["BaseModel"]

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
        if not line:
            print("** class name missing **")
        else:
            line = line.split(' ')
            if line[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            elif len(line) < 2:
                print("** instance id missing **")

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
