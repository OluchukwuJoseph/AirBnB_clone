#!/usr/bin/python3
"""
This module contains the definition of the Place class, which represents
a place in the AirBnB clone project.
"""
from models.base_model import BaseModel


class Place(BaseModel):
	"""
	A class representing a place. It inherits from BaseModel and adds
	attributes specific to a place such as city_id, name, description, etc.
	"""
	city_id = ""
	user_id = ""
	name = ""
	description = ""
	number_rooms = 0
	number_bathrooms = 0
	max_guest = 0
	price_by_night = 0
	latitude = 0.0
	longitude = 0.0
	amenity_ids = []

	def __str__(self):
		"""
		Return a string representation of the Place object.
		"""
		return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
