#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
	"""A class that defines the HBNB command interpreter"""

	prompt = '(hbnb) '

	# Mapping of supported class names to their corresponding class objects.
	SUPPORTED_CLASSES = {
		'BaseModel': BaseModel,
		'User': User,
		'Amenity': Amenity,
		'City': City,
		'Place': Place,
		'Review': Review,
		'State': State
	}

	def do_create(self, line):
		"""
    	Create a new instance of a specified class.

    	Args:
      		line (str): The input command line containing the class name.

    	Returns:
			None
    	"""
		# Check if a class name was passed
		if not line:
			print("** class name missing **")
			return
		
		# checks if class name exists
		if line in self.SUPPORTED_CLASSES:
			# Create a new instance of the class
			new_instance = self.SUPPORTED_CLASSES[line]()
			print(new_instance.id)
			storage.save()
		else:
			print("** class doesn't exist **")
	
	def help_create(self):
		"""Create Help Method"""
		print(f"Create a new instance of a supported class.\n"
              "\nUsage: create <class name>\n"
              "\nExample:"
              "\ncreate BaseModel")
	
	def do_show(self, line):
		"""
        This method Displays details of a specific instance.

        Args:
            line (str): The input command line containing the class name
            and instance ID.

        Returns:
            None
        """
		# Do this if nothing was passed
		if not line:
			print("** class name missing **")
			return
		args = shlex.split(line)
		# Do this if only the classname was passed
		if len(args) == 1:
			if args[0] in self.SUPPORTED_CLASSES:
				print("** instance id missing **")
				return
			else:
				print("** class doesn't exist **")
				return
		
		# Do this if the classname and id was passed
		if args[0] in self.SUPPORTED_CLASSES:
			instance_id = args[1]
			instance_key = f"{args[0]}.{args[1]}"
			objs = storage.all()
			
			# check if key exists or not
			if instance_key in objs:
				# Regenerate new instance
				instance = self.SUPPORTED_CLASSES[args[0]](**objs[instance_key])
				print(instance)
				return
			else:
				print("** no instance found **")
				return
		else:
			print("** class doesn't exist **")
			return
	
	def help_show(self):
		"""help method of Show"""
		print(f"Display details of a specific instance.\n"
              "\nUsage: show <class name> <instance id>\n"
              "\nExample:"
              "\nshow BaseModel 1234-5678-9012")
		
	def do_destroy(self, line):
		"""
        This method deletes an instance based on the class name and instance id.

        Args:
            line (str): The input command line containing class name and
            instance id.

        Returns:
            None
        """
		# Do this if nothing was passed
		if not line:
			print(f"** class name missing **")
			return
		args = shlex.split(line)
		# Do this if only the classname was passed
		if len(args) == 1:
			if args[0] in self.SUPPORTED_CLASSES:
				print(f"** instance id missing **")
				return
			else:
				print(f"** class doesn't exist **")
				return
		
		# Do this if the classname and id was passed
		if args[0] in self.SUPPORTED_CLASSES:
			instance_id = args[1]
			instance_key = f"{args[0]}.{instance_id}"
			objs = storage.all()
			if instance_key in objs:
				del storage.all()[instance_key]
				storage.save()
				return
			else:
				print(f"** no instance found **")
				return
		else:
			print(f"** class doesn't exist **")
			return

	def help_destroy(self):
		"""Help Method of Destroy"""
		print(f"Delete an instance based on the class name and instance id.\n"
              "\nUsage: destroy <class name> <instance id>"
              "\nExample:"
              "\ndestroy BaseModel 1234-5678-9012")

	def do_all(self, line):
		"""
        Display details of all instances or instances of a specific class.

        Args:
            line (str): The input command line containing optional
            class name.

        Returns:
            None
        """
		objs = storage.all()
		instances = []
		# What to do when nothing was passed
		if not line:
			for key, value in objs.items():
				instance = (self.SUPPORTED_CLASSES[objs[key]
                            ['__class__']](**value))
				instances.append(instance.__str__())
			print(instances)
			return
		
		# what to do when a classname was passed
		args = shlex.split(line)
		if args[0] in self.SUPPORTED_CLASSES:
			for key, value in objs.items():
				if value['__class__'] == args[0]:
					instance = (self.SUPPORTED_CLASSES[objs[key]
                                ['__class__']](**value))
					instances.append(instance.__str__())
			print(instances)
			return
		else:
			print(f"** class doesn't exist **")
			return

	def help_all(self):
		"""Help method of all)"""
		print(f"Display all instances or instances of a specified class.\n"
              "\nUsage: all [<class name>]\n"
              "\nIf no class name is provided, all instances "
              "will be displayed\n"
              "\nExample:"
              "\nall"
              "\nall BaseModel")
	
	def do_update(self, line):
		"""
        Update attributes of an instance.

        Args:
            line (str): The input command line containing class name,
            instance id, attribute name, and new value.

        Returns:
            None
        """
		# Do this if nothing was passed
		if not line:
			print("** class name missing **")
			return

		args = shlex.split(line)
		# Do this if only the classname was passed
		if len(args) < 2:
			if args[0] in self.SUPPORTED_CLASSES:
				print("** instance id missing **")
				return
			else:
				print("** class doesn't exist **")
				return
		
		# Do this if more than 2 arguments was passed
		class_name = args[0]
		instance_id = args[1]
		instance_key = f"{args[0]}.{instance_id}"
		objs = storage.all()

		if class_name not in self.SUPPORTED_CLASSES:
			print("** class doesn't exist **")
			return

		if instance_key not in objs:
			print("** no instance found **")
			return
		
		if len(args) < 3:
			print("** attribute name missing **")
			return

		attribute_name = args[2]
		if len(args) < 4:
			print("** value missing **")
			return

		attribute_value = args[3]
		# Update the attribute value
		objs[instance_key].update({attribute_name: eval('attribute_value')})
		storage.save()

	def help_update(self):
		"""Help method for update"""
		print(f"Update attributes of an instance.\n"
              "\nUsage: update <class name> <instance id> <attribute name>"
              "<new value>\n"
              "\nExample:"
              "\nupdate BaseModel 1234-5678-9012 name 'New Name'")

	def do_quit(self, arg):
		"""Quit command to exit the program."""
		return True

	def help_quit(self):
		"""help method for quit"""
		print(f"Exit the command-line interpreter.\n"
              "\nUsage: quit\n"
              "\nExample:"
              "\nquit")
	
	def do_EOF(self, line):
		"""
        Exit the command-line interpreter when encountering EOF (Ctrl+D).

        Args:
            line (str): Unused. Represents the input command line.

        Returns:
            bool: True to exit the interpreter.
        """
		return True

	def help_EOF(self):
		"""help method for EOF"""
		print(f"Exit the command-line interpreter when encountering"
              " EOF (Ctrl+D).\n"
              "\nUsage: Press Ctrl+D\n"
              "\nExample:"
              "\nPress Ctrl+D to exit")

	def emptyline(self):
		"""Do nothing upon receiving an empty line."""
		pass


if __name__ == "__main__":
	HBNBCommand().cmdloop()
