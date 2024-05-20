#!/usr/bin/python3
"""
This module contains the definition of the State class, which represents
a state in the Airbnb clone project.
"""
from models.base_model import BaseModel


class State(BaseModel):
	"""
  	A class representing a state in the Airbnb clone project.
  	"""

	name = ""
	
	def __str__(self):
		"""
    	Return a string representation of the State object.
		"""
		return f"[{self.__class__.__name__} ({self.id}) {self.__dict__}]"
