#!/usr/bin/python3

"""
This module contains a class User,
which inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class User inherits from BaseModel
    class, and contains these public attr:

    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
