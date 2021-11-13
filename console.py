#!/usr/bin/python3


import cmd, sys
from turtle import *

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    file = None

    def do_quit(self, arg):
        '''Quit command to exit the program\n'''
        self.close()
        #bye()
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
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
