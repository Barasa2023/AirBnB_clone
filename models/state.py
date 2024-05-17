#!/bin/env/python3
"""This module is used to create the State class"""

from models.base_model import BaseModel

class State(BaseModel):
    """This class creates instances for states"""

    name = ""

    # def __init__(self, *args, **kwargs):
    #     """Initializes State attributes"""
    #     super().__init__(*args, **kwargs)