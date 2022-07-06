'''Unittest for Amenity class'''
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestUserClass(unittest.TestCase):

	def setUp(self):
		"""Sets up user instance"""
		self.User_1 = Amenity()

	def test_type(self):
		"""test to check type of instance"""
		self.assertEqual(type(self.User_1), Amenity)

	def test_user_id(self):
		"""test to check user id"""
		User_1 = Amenity()
		self.assertEqual(type(User_1.id), str)
		self.assertTrue(hasattr(User_1, "id"))

	def test_user_created(self):
		"""test to check user created_at"""
		User_1 = Amenity()
		self.assertEqual(type(User_1.created_at), type(datetime.now()))
		self.assertTrue(hasattr(User_1, "created_at"))

	def test_user_updated(self):
		"""test to check user updated_at"""
		User_1 = Amenity()
		self.assertEqual(type(User_1.updated_at), type(datetime.now()))
		self.assertTrue(hasattr(User_1, "updated_at"))

	def test_user_name(self):
		"""test to check user name"""
		User_1 = City()
		self.assertEqual(type(User_1.id), str)
		self.assertTrue(hasattr(User_1, "name"))

	def test_str_output_user(self):
		'''Tests for expected output'''
		u1 = Amenity()
		output = f"[{u1.__class__.__name__}] ({u1.id}) {u1.__dict__}"
		self.assertEqual(output, str(u1))


if __name__ == "__main__":
    unittest.main()
