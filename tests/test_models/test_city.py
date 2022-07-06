#!/usr/bin/python3
'''Unittest for City class'''
from models.city import City
from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestUserClass(unittest.TestCase):

	def setUp(self):
		"""Sets up user instance"""
		self.User_1 = City()

	def test_type(self):
		"""test to check type of instance"""
		self.assertEqual(type(self.User_1), City)

	def test_user_id(self):
		"""test to check user id"""
		User_1 = City()
		self.assertEqual(type(User_1.id), str)
		self.assertTrue(hasattr(User_1, "id"))

	def test_user_created(self):
		"""test to check user created_at"""
		User_1 = City()
		self.assertEqual(type(User_1.created_at), type(datetime.now()))
		self.assertTrue(hasattr(User_1, "created_at"))

	def test_user_updated(self):
		"""test to check user updated_at"""
		User_1 = City()
		self.assertEqual(type(User_1.updated_at), type(datetime.now()))
		self.assertTrue(hasattr(User_1, "updated_at"))

	def test_user_name(self):
		"""test to check user name"""
		User_1 = City()
		self.assertEqual(type(User_1.id), str)
		self.assertTrue(hasattr(User_1, "name"))

	def test_str_output_user(self):
		'''Tests for expected output'''
		u1 = City()
		output = f"[{u1.__class__.__name__}] ({u1.id}) {u1.__dict__}"
		self.assertEqual(output, str(u1))

	def test_City_state_id(self):
		'''Tests state_id for City'''
		c1 = City()
		self.assertTrue(hasattr(c1, "state_id"))
		self.assertEqual(type(c1.state_id), str)


if __name__ == "__main__":
    unittest.main()
