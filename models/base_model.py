#!/usr/bin/python3
'''Base model file'''

from datetime import datetime

class BaseModel:
    '''defines all common attributes/methods for other classes'''

    def __init__(self, *args, **kwargs):
        '''Initialize intances'''

        if kwargs is not None and kwargs != {}:
            if kwargs["created_at"] == "created_at":
                self.created_at = datetime.now()
            elif kwargs["updated_at"] == "updated_at":
                self.updated_at = datetime.now()
            else:
                pass
        else:        
            self.id = id
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        '''Print the string representation of object'''
        pass

    def to_dict(self):
        '''Returns a dictionary containing all the key/values of __dict__'''

        self.__dict__["__class__"] = self.__dict__[self.__class__.__name__]
        return self.__dict__
    
    def save(self):
        '''updates the public instance attribute updated at'''

        self.updated_at = datetime.now()
    