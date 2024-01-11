#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class defines a review by various attributes.

    Attributes:
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who wrote the review.
        text (str): The content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""