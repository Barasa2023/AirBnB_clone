#!/usr/bin/python3
'''Console interpreter'''

import cmd
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()

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
        '''Creates a new instance of BaseModel, saves it\
            and prints the id'''
        if arg is None:
            print("** class name missing **")
            return
        try:
            obj = globals()[arg]()
            obj.save
            print(obj.id)
        
        except KeyError:
            print("** class doesn't exist **")


    def do_show(self, arg):
        """ Prints the string representation of an instance based\
            on the class name and id"""

        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
        key = args[1] + '.' + args[2]
        if key not in storage.all():
            print("** no instance found **")
            return
    
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and \
            id (save the change into the JSON file"""
        
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[1] + '.' + args[2]
        if key not in storage.allz():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()
    

    def do_all(self, arg):
        """ Prints all string representation of all instances \
            based or not on the class name"""
        
        if arg and arg not in classes:
            print("** class doesn't exist **")
            return
        if arg:
            objects = [str(obj) for obj in storage.all().values()\
                       if type(obj.__name__) == arg]
            print(objects)
        else:
            objects = [str(obj) for obj in storage.all().values()]
            print(objects)
        
        return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
