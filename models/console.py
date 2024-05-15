#!/usr/bin/python3
'''Console interpreter'''

import cmd

class HBNBCommand(cmd.Cmd):
    '''Contains the entry point of the command interpreter'''

    prompt = "(hbnb)"

    def do_quit(self, arg: str):
        '''Method to exit the interpreter'''

        pass

    def do_help(self, arg: str):
        '''Print help topic'''
        
        pass

    def do_create(self, arg):
        '''Creates a new instance of BaseModel'''
        if arg is None:
            print("** class name missing **")
        else:
            print("New instance created")
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
