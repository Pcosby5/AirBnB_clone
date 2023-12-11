#!/usr/bin/python3
"""Creates a class User with it attributes"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from class BaseModel"""


    email = ""
    password = ""
    first_name = ""
    last_name = ""
