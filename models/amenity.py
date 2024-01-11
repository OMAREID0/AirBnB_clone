#!/usr/bin/python3

from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class defines an amenity with various attributes.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""