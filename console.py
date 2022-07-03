#!/usr/bin/python3

"""Console"""

import cmd
import models


class HBNBCommand(cmd.Cmd):
	"""Class for console"""

	prompt = "(hbnb) "

	def emptyline(self):
		pass

	def do_quit(self, arg):
		"""Quit command to exit the program"""
		exit(0)

	def do_EOF(self, arg):
		"""EOF command to exit the program"""
		return(True)


if __name__ == '__main__':
    HBNBCommand().cmdloop()