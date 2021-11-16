#!/usr/bin/python3
'''Console Module'''
import cmd
import sys
from turtle import *
from models.base_model import BaseModel
classes = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    '''AirBNB command line interpreter'''
    prompt = '(hbnb) '
    file = None

    def do_create(self, line_args_obj):
        """
        Creates a new instance of BaseModel,
        saves it to the JSON file and prints its id.
        Ex: $ create BaseModel
        """
        if line_args_obj == "" or line_args_obj is None:
            print('** class name missing **')
        elif line_args_obj not in classes:
            print("** class doesn't exist **")
        else:
            string_class = ("{}()".format(line_args_obj))
            new_instance = eval(string_class)
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line_args_obj):
        """
        Prints the string representation of an instance
        based on the class name and id
        Ex: $ show BaseModel 1234-1234-1234
        """
        args = line_args_obj.split()
        if line_args_obj == "" or line_args_obj is None:
            print("** class name missing **")
        elif args[0] not in classes.keys():
            print("** class doesn't exist **")
            return False
        if len(args) < 2:
            print("** instance id missing **")
            return False
        instance = args[0] + "." + args[1]
        if instance in models.storage.all():
            print(models.storage.all()[instance])
        else:
            print("** no instance found **")

    def do_destroy(self, line_args_obj):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        Ex: destroy BaseModel 1234-1234-1234
        """
        args = line_args_obj.split()
        if len(line_args_obj) == 0:
            print("** class name missing **")
        elif args[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objects = models.storage.all()
            for i in all_objects:
                if i == "{}.{}".format(args[0], args[1]):
                    # del models.storage.all()[args[0] + "." +args[1]]
                    del all_objects[str(i)]
                    models.storage.save()
                    return False
            print("** no instance found **")

    def do_all(self, line_args_obj):
        """
         Prints all string representation of all instances
         based or not on the class name.
         Ex: $ all BaseModel or $ all
        """
        args = line_args_obj.split()
        "Printing list of objects in strings format"
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
            print("** class doesn't exist **")
        elif line_args_obj in classes:
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
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com". """
        args = line_args_obj.split()
        invalid_update = ["id", "created_at", "updated_at"]
        if len(line_args_obj) < 1:
            print("** class name missing **")
        elif args[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")

        key_first = "{}.{}".format(args[0], args[1])
        if key_first not in models.storage.all():
            print("** no instance found **")

        if len(args) < 3:
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

    def do_quit(self, arg):
        '''Quit command to exit the program\n'''
        self.close()
        # bye()
        return True

    def do_EOF(self, arg):
        '''Quit command to exit the program\n'''
        self.close()
        return True

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

    def precmd(self, line):
        if self.file and 'playback' not in line:
            print(line, file=self.file)
            print("hey")
        return line

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt.

        If this method is not overridden, it repeats the last nonempty
        command entered.
        """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')


def parse(arg):
    '''Convert a series of zero or more numbers to an argument tuple'''
    return tuple(map(int, arg.split()))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
