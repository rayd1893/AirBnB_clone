#!/usr/bin/python3
"""modulo cmd"""
import cmd
from models.engine.file_storage import FileStorage
import json
from datetime import datetime
import sys
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User
import models


classes = {"BaseModel": BaseModel, "User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """Airbnb's command interpreter"""
    prompt = '(hbnb) '

    def do_create(self, line_args_obj):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        if line_args_obj == "" or line_args_obj is None:
            print('** class name missing **')
            return
        elif line_args_obj not in classes:
            print("** class doesn't exist **")
            return
        try:
            string_class = ("{}()".format(line_args_obj))
            new_instance = eval(string_class)
            new_instance.save()
            print(new_instance.id)
        except Exception as fail:
            print("** class doesn't exist**'")

    def do_show(self, line_args_obj):
        """
        Prints the string representation of an instance
        based on the class name and id
        Ex: $ show BaseModel 1234-1234-1234
        """
        args = line_args_obj.split()
        if line_args_obj == "" or line_args_obj is None:
            print("** class name missing **")
            return
        elif args[0] not in classes.keys():
            print("** class doesn't exist **")
            return False
        if len(args) < 2:
            print("** instance id missing **")
            return False
        instance = args[0] + "." + args[1]
        for instance in models.storage.all():
            print(models.storage.all()[instance])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file).
        """
        if line:
            args = line.split(" ")
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = args[0] + "." + args[1]
            obje = storage.all()
            if key not in obje:
                print("** no instance found **")
                return
            del obje[key]
            storage.save()
        else:
            print('** class name missing **')

    def do_all(self, line_args_obj):
        """
         Prints all string representation of all instances
         based or not on the class name.
         Ex: $ all BaseModel or $ all
        """
        args = line_args_obj.split()
        "COMMENT: impresion de un lista de cadena de los objetos almacenados"
        if len(args) == 0:
            print('["', end="")
            flag = 0
            all_objects = models.storage.all()
            for i in all_objects.keys():
                if flag == 1:
                    print('", "', end="")
                obj = all_objects[i]
                print(obj, end="")
                flag = 1
            print('"]')
        elif args[0] not in classes.keys():
            "COMMENT: si es nombre de la clase no esta"
            print("** class doesn't exist **")
        elif line_args_obj in classes:
            """
            COMMENT: imprimiremos la representacion en cadena de todos
            los objetos(incluido los que estan ingresando(comparando
            el valor inicial del objeto ingresado)) basados o no en
            el nombre de la clase"
            """
            print('["', end="")
            flag = 0
            all_objects = models.storage.all()
            for i in all_objects.keys():
                if i.startswith(args[0]):
                    if flag == 1:
                        print('", "', end="")
                    obj = all_objects[i]
                    print(obj, end="")
                    flag = 1
            print('"]')

    def do_update(self, line_args_obj):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file)
        """
        args = line_args_obj.split()
        invalid_update = ["id", "created_at", "updated_at"]
        if len(line_args_obj) < 1:
            print("** class name missing **")
            return
        elif args[0] not in classes.keys():
            "COMMENT: si es nombre de la clase no esta"
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        "Si este nombre y id no estan dentro de nuestro obj(almacenamiento)"
        key_first = "{}.{}".format(args[0], args[1])
        if key_first not in models.storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        elif args[2] not in invalid_update:
            obj = models.storage.all()[key_first]
            print(obj.__dict__)
            obj.__dict__[args[2]] = args[3]
            print(obj.__dict__[args[2]])
            obj.updated_at = datetime.now()
            obj.save()

    def do_count(self, line_args_obj):
        args = line_args_obj.split()
        if args[0] not in classes:
            return
        else:
            count = 0
            keys = models.storage.all().keys()
            for key in keys:
                lenght = len(args[0])
                if key[:lenght] == args[0]:
                    count += 1
            print(count)

    def emptyline(self):
        "method that is called when an empty line is entered"
        pass

    def do_help(self, args):
        """define help options"""
        cmd.Cmd.do_help(self, args)

    def do_EOF(self, args):
        "End-of-file command to exit the console"
        print()
        return True

    def do_quit(self, args):
        "Quit command to exit the program"
        return True

    def help_quit(self):
        """help_quit"""
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """help_EOF"""
        print("End of File command: exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
