#!/usr/bin/python3
"""Defines the State sub-class"""
from models.base_model import BaseModel


class State(BaseModel):
    """Defines State sub-class inheriting from BaseModel class

    Attributes:
    name (string): name of state
    """

    name = ""
