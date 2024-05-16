#!/usr/bin/python3
"""
This module contains the definition of the Amenity class, which represents
an amenity in the Airbnb clone project.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
	"""
    	A class representing an amenity in an Airbnb clone project.
    	"""
	name = ""

	def __str__(self):
		"""
		Return a string representation of the Amenity object.
		"""
		return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
