#!/usr/bin/python3
"""
This module contains the definition of the Review class, which represents
a review in an Airbnb clone project.
"""
from models.base_model import BaseModel


class Review(BaseModel):
	"""
    	A class representing a review in an Airbnb clone project.
    	"""
	place_id = ""
	user_id = ""
	text = ""

	def __str__(self):
		"""
		Return a string representation of the Review object.
		"""
		return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
