#!/usr/bin/python3
"""Defines Review sub-class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines Review sub-class inheriting from BaseModel class

    Attributes:
        place_id (string): place id
        user_id (string): user id
        text (string): text of review
    """

    place_id = " "
    user_id = " "
    text = " "
