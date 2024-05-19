#!/usr/bin/python3
"""This module creates the Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class for creating and managing review instances"""

    place_id = ""
    user_id = ""
    text = ""
