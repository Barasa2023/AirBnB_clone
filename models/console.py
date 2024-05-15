#!/usr/bin/python3
'''Console interpreter'''

import cmd

class HBNBCommand(cmd.Cmd):
    '''Contains the entry point of the command interpreter'''

    prompt = "(hbnb)"

    def do_quit(self):
        '''Method to exit the interpreter'''

        pass

    def do_help(self, arg: str) -> bool | None:
        '''Print help topic'''
        return super().do_help(arg)
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
    
