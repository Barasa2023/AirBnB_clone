#!/usr/bin/python3
"""The city module creates Cities"""

from models.base_model import BaseModel


class City(BaseModel):
    """Creates and Manages Cities"""

    state_id = ""
    name = ""
    