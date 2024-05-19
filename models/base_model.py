#!/usr/bin/python3
'''Base model file'''

import uuid
from datetime import datetime

from models import storage


class BaseModel:
    '''defines all common attributes/methods for other classes'''

    def __init__(self, *args, **kwargs):
        '''Initialize intances'''


        if kwargs:
            for key, value in kwargs.items():
            #     if key == "created_at" or key == "updated_at":
            #         value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
            #     setattr(self, key, value)
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                        self.__dict__[key] = kwargs[key]
        else:        
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''Print the string representation of object'''
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        '''Returns a dictionary containing all the keys/values of __dict__'''

        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy["__class__"] = type(self).__name__

        return dict_copy
    
    def save(self):
        '''updates the public instance attribute updated at'''

        self.updated_at = datetime.now()
        storage.save()
    