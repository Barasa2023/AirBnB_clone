#!/usr/bin/python3
'''Initializes the package'''
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()