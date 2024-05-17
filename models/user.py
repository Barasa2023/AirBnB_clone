#!/usr/bin/python3
'''Users class'''

from base_model import BaseModel

class Users(BaseModel):
    """Base class for creating users"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
