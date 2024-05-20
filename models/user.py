#!/usr/bin/python3
"""
Defines User Class
"""
from models.base_model import BaseModel


class User(BaseModel):
	"""
  	A class User.

  	Attributes:
    		email (str): The user's email.
    		password (str): The user's password
    		first_name (str): The first name of the user
    		last_name (str): The last name of the user
  	"""

	email = ""
	password = ""
	first_name = ""
	last_name = ""

	def __str__(self):
		"""
        Return a string representation of the State object.
    	"""
		return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
