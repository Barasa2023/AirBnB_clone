#!/usr/bin/python3
'''Users class'''

from models.base_model import BaseModel

class User(BaseModel):
    """Base class for creating users"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
