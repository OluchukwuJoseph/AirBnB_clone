#!/usr/bin/python3
"""
This module contains the definition of the City class, which represents
a city in the Airbnb clone project.
"""
from models.base_model import BaseModel


class City(BaseModel):
	"""
    	A class representing a city in the Airbnb clone project.
    	"""
	state_id = ""
	name = ""

	def __str__(self):
		"""
        	Return a string representation of the City object.
        	"""
		return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
