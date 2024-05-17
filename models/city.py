#!/usr/bin/python3
"""The city module creates Cities"""

from base_model import BaseModel

class City(BaseModel):
    """Creates and Manages Cities"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize attrbutes for city instances"""
        super().__init__(*args, **kwargs)