#!/usr/bin/python3
"""This module is the console for Airbnb"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This class creates the console"""
    prompt = "(hbnb) "

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
