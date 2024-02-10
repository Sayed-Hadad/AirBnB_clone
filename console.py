#!/usr/bin/python3

import cmd
import sys
import json
import os.path
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for the HBNB project.
    """

    prompt = '(hbnb) '  # Set the custom prompt

    __models = {
        "BaseModel": BaseModel
    }
    __file_path = "file.json"

    def emptyline(self):
        """Do nothing when receiving an empty line"""
        pass

    def do_EOF(self, line):
        """
        Exiting the program when reaching End of file
        """
        print("")
        return True

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_create(self, arg):
        """
        Creates a new instance of a specified class, saves it, and prints its ID.

        Usage: create <class_name>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.__models:
            print("** class doesn't exist **")
            return
        instance = self.__models[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """
        Shows the string representation of an instance based on the class name and ID.

        Usage: show <class_name> <instance_id>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if args[0] not in self.__models:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        objects = FileStorage().all()
        if key in objects:
            print(objects[key])
            return
        else:
            print("** no instance found **")
            return

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and ID.

        Usage: destroy <class_name> <instance_id>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.__models:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        objects = FileStorage().all()
        if key in objects:
            del objects[key]
            FileStorage().save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints string representations of all instances based on the class name or all instances if no class name is specified.

        Usage: all [<class_name>]
        """
        args = arg.split()
        objects = FileStorage().all()
        if len(args) == 0:
            print([str(obj) for obj in objects.values()])
        else:
            class_name = args[0]
            if class_name not in self.__models:
                print("** class doesn't exist **")
                return
            instances = [str(obj) for key, obj in objects.items() if key.startswith(class_name + ".")]
            print(instances)

    def do_update(self, arg):
        """
        Updates an instance based on the class name, ID, attribute name, and attribute value.

        Usage: update <class_name> <instance_id> <attribute_name> "<attribute_value>"
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.__models:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        objects = FileStorage().all()
        if key not in objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]
        instance = objects[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
