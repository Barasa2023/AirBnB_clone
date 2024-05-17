#!/usr/bin/python3
"""This module contains the Amenity class"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """Class manages amenity instances"""

    name = ""

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)