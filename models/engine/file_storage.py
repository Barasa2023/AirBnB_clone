#!/usr/bin/python3
"""Contains files functions to handle serialization"""
import datetime
import json
import os


class FileStorage:
    """Serializes instances to a JSON file and\
        deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """Set in __object the object with key (object classname.id)"""

        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj
    
    def save(self):
        """Serializes objects to Json file"""
        # serialized_items = {}
        # for key, item in self.__objects.items():
        #     serialized_items[key] = item.to_dict()
        # with open(self.__file_path, 'w') as file:
        #     json.dump(serialized_items, file)
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dict_obj = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dict_obj, f)      
    
    
    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """Deserializes Json file to __objects"""

        # if os.path.exists(self.__file_path):
        #     with open(FileStorage.__file_path, "r") as file:
        #         #obj_dict = json.load(file)
        #         # for key, value in obj_dict.items():
        #         #     class_name, obj_id = key.split(".")
        #         #     obj = self.classes()[class_name["__class__"]](**value)
        #         obj_dict = json.load(file)
        #         obj_dict = {k: self.classes()[v["__class__"]](**v)
        #                 for k, v in obj_dict.items()}
        #         self.__objects = obj_dict
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict