#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """This class defines a city by various attributes"""

    state_id = ""
    name = ""