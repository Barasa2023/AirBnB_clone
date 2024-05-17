#!/usr/bin/python3
'''Base model file'''

from datetime import datetime
import uuid
from models import storage


class BaseModel:
    '''defines all common attributes/methods for other classes'''

    def __init__(self, *args, **kwargs):
        '''Initialize intances'''

        #if kwargs is not None and kwargs != {}:
            # if kwargs["created_at"] == "created_at":
            #     self.created_at = datetime.now()
            # elif kwargs["updated_at"] == "updated_at":
            #     self.updated_at = datetime.now()
            # else:
            #     pass
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:        
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        '''Print the string representation of object'''
        return f"[(self.__class__.__name__)] ({self.id}) {self.__dict__}"

    def to_dict(self):
        '''Returns a dictionary containing all the keys/values of __dict__'''

        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy["__class__"] = self.__class__.__name__

        return dict_copy
    
    def save(self):
        '''updates the public instance attribute updated at'''
        storage.save()

        self.updated_at = datetime.now()
    