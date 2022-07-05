#!/usr/bin/python3


""""Module test for base model class"""

from datetime import datetime
import unittest
import uuid
from models.base_model import BaseModel

class TestBase(unittest.TestCase):

	"""Test cases for the base model class"""

	b1 = BaseModel()

	def test_id_exist(self):
		self.assertEqual(type(self.b1.id), str)
		self.assertTrue(self.b1.id)   


if __name__ == '__main__':
	unittest.main()