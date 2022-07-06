#!/usr/bin/python3
'''Unittest for place class'''
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestUserClass(unittest.TestCase):

	def setUp(self):
		"""Sets up user instance"""
		self.User_1 = Place()

	def test_type(self):
		"""test to check type of instance"""
		self.assertEqual(type(self.User_1), Place)

	def test_place_id(self):
				'''Tests if has id attribute'''
				p1 = Place()
				self.assertEqual(type(p1.id), str)
				self.assertTrue(hasattr(p1, "city_id"))

	def test_place_user_id(self):
			'''Tests if has user_id attribute'''
			p1 = Place()
			self.assertEqual(type(p1.id), str)
			self.assertTrue(hasattr(p1, "user_id"))

	def test_place_created(self):
			'''Tests created_at for place'''
			p1 = Place()
			self.assertEqual(type(p1.created_at), type(datetime.now()))
			self.assertTrue(hasattr(self.place1, "created_at"))

	def test_place_updated(self):
			'''Tests updated_at for place'''
			p1 = Place()
			self.assertEqual(type(p1.updated_at), type(datetime.now()))
			self.assertTrue(hasattr(p1, "updated_at"))

	def test_place_description(self):
			'''Tests description for place'''
			p1 = Place()
			self.assertTrue(hasattr(p1, "description"))
			self.assertEqual(type(p1.description), str)

	def test_place_number_rooms(self):
			'''Tests number of rooms for place'''
			p1 = Place()
			self.assertTrue(hasattr(p1, "number_rooms"))
			self.assertEqual(type(p1.number_rooms), int)

	def test_place_number_bathrooms(self):
			'''Tests number of bathrooms for place'''
			p1 = Place()
			self.assertTrue(hasattr(p1, "number_bathrooms"))
			self.assertEqual(type(p1.number_bathrooms), int)

	def test_place_max_guest(self):
			'''Tests max number of guests'''
			p1 = Place()
			self.assertTrue(hasattr(p1, "max_guest"))
			self.assertEqual(type(p1.max_guest), int)

	def test_price_by_night(self):
			'''Tests price by night'''
			p1 = Place()
			self.assertTrue(hasattr(p1, "price_by_night"))
			self.assertEqual(type(p1.price_by_night), int)

	def test_latitude(self):
			'''Tests latitude'''
			p1 = Place()
			self.assertTrue(hasattr(p1, "latitude"))
			self.assertEqual(type(p1.latitude), float)

	def test_longitude(self):
			'''Tests longitude'''
			p1 = Place()
			self.assertTrue(hasattr(p1, "longitude"))
			self.assertEqual(type(p1.longitude), float)

	def test_amenity_ids(self):
			'''Tests amenity ids'''
			p1 = Place()
			self.assertTrue(hasattr(p1, "amenity_ids"))
			self.assertEqual(type(p1.amenity_ids), list)

	def test_strmethod(self):
			'''Tests str method'''
			p1 = Place()
			self.assertEqual(type(str(p1)), str)

	def test_strmethod_clsname(self):
			'''Tests if class name in str'''
			p1 = Place()
			self.assertEqual('[Place]' in str(p1), True)

	def test_strmethod_id(self):
			'''Tests if id is in str representation'''
			p1 = Place()
			self.assertEqual('id' in str(p1), True)

	def test_str_created_place(self):
			'''Tests if created_at is in str'''
			p1 = Place()
			self.assertEqual('created_at' in str(p1), True)

	def test_str_updated_place(self):
			'''Tests if updated_at is in str'''
			p1 = Place()
			self.assertEqual('updated_at' in str(p1), True)

	def test_str_output_user(self):
		'''Tests for expected output'''
		u1 = Place()
		output = f"[{u1.__class__.__name__}] ({u1.id}) {u1.__dict__}"
		self.assertEqual(output, str(u1))


if __name__ == "__main__":
    unittest.main()
