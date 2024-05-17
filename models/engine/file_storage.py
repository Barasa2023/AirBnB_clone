#!/usr/bin/python3
"""Contains files functions to handle serialization"""

import json
import os


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""

        return self.__objects
    
    def new(self, obj):
        """Set in __object the object with key (object classname.id)"""

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects["key"] = obj


    def save(self):
        """Serializes objects to Json file"""

        serialized_items = {}
        
        for key, item in self.__objects.items():
            serialized_items[key] = item.to_dict()
        
        #TODO: Research more on the above

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_items, file)
    

    def reload(self):
        """Deserializes Json file to __objects"""

        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split(".")
                    obj = globals[class_name](**value)
                    self.__objects = obj