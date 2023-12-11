#!/usr/bin/python3
"""Defines the City sub-class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines City sub-class inheriting from BaseModel class

    Attributes:
        state_id (string): state id
        name (string): name of city
    """
    state_id = " "
    name = " "
