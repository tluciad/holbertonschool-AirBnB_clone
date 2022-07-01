#!/usr/bin/python3


""""Module test for base model class"""

import unittest
import uuid
from models.base_model import base_model

class TestBase(unittest.TestCase):

	"""Test cases for the base model class"""
	

	def test_id_exist(self):
		b1 = base_model()
		self.assertTrue(self.b1.id)

	def test_created_at(self):
		b1 = base_model()
		self.assertTrue(self.b1.updated_at)
		self.assertEqual(type(b1.updated_at), datetime)
   

	def test_types(self):
		b1 = base_model()
		self.assertEqual(type(b1.id), str)
		


if __name__ == '__main__':
	unittest.main()