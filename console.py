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

    def do_EOF(self):
        '''Exit the interpreter'''

        print()
        return True

    def do_create(self, arg):
        '''Creates a new instance of BaseModel, saves it\
            and prints the id'''
        
        
        # if not arg:
        #     print(" ** class name missing **")
        #     return
        # try:
        #     obj = storage.classes()[arg]()
        #     obj.save()
        #     print(obj.id)
        
        # except KeyError:
        #     print("** class doesn't exist")
        if arg == "" or arg is None:
                print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[arg]()
            b.save()
            print(b.id)
            
 
    def do_show(self, arg):
        """ Prints the string representation of an instance based\
            on the class name and id"""

        if not arg:
            print("** class name missing **")
        else:
            args = arg.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + '.' + args[1]
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])
                    
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and \
            id (save the change into the JSON file"""
        
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()
    

    def do_all(self, arg):
        """ Prints all string representation of all instances
            based or not on the class name"""
        
        if arg != "":
            args = arg.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                objects = [str(obj) for obj in storage.all().values()\
                    if type(obj).__name__ == args[0]]
                print(objects)
        else:
            objects = [str(obj) for obj in storage.all().values()]
            print(objects)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by
             adding or updating attribute (save the change into the JSON file)"""
        
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        try:
            value = eval(args[3])
        except:
            value = args[3]
        setattr(storage.all()[key], args[2], value )
        storage.save()
        
    def do_count(self, arg):
        """Count the instances of a class"""
        
        args = arg.split(' ')
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            instances = [
                obj for obj in storage.all()\
                if obj.startswith(args[0] + '.')]
            print(len(instances))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
