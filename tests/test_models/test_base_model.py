#!/usr/bin/python3


""""Module test for base model class"""

"""from datetime import datetime
import unittest
import uuid
from models.base_model import BaseModel

class TestBase(unittest.TestCase):

	Test cases for the base model class
	b1 = BaseModel()

	def test_id_exist(self):
		self.assertEqual(type(self.b1.id), str)
		self.assertTrue(self.b1.id)

	#def test_created_at(self):
		
		#self.assertTrue(self.b1.updated_at)
		#self.assertEqual(type(b1.updated_at), datetime)
   


if __name__ == '__main__':
	unittest.main()"""

#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)


"""my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
	print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))"""