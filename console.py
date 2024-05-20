#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import shlex

class HBNBCommand(cmd.Cmd):
	"""A class that defines the HBNB command interpreter"""

	prompt = '(hbnb) '

	def do_create(self, line):
		if not line:
            		print("** class name missing **")
            		return
        
        	if line in self.SUPPORTED_CLASSES:
            		new_instance = self.SUPPORTED_CLASSES[line]()
            		print(new_instance.id)

        	else:
            		print("** class doesn't exist **")
		

	def do_quit(self, arg):
        	"""Quit command to exit the program."""
		return True

	def emptyline(self):
		"""Do nothing upon receiving an empty line."""
		pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
