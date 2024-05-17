#!/usr/bin/python3
'''Console interpreter'''

import cmd

class HBNBCommand(cmd.Cmd):
    '''Contains the entry point of the command interpreter'''

    prompt = "(hbnb)"

    def do_quit(self, arg: str):
        '''Method to exit the interpreter'''

        return True

    # def do_help(self, arg: str):
    #     '''Print help topic'''
        

    def do_EOF(self):
        '''Exit the interpreter'''

        print()
        return True

    def do_create(self, arg):
        '''Creates a new instance of BaseModel, saves it, and prints the id'''
        if arg is None:
            print("** class name missing **")
            return
        try:
            obj = globals()[arg]()
            obj.save
            print(obj.id)
        
        except KeyError:
            print("** class doesn't exist **")    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
