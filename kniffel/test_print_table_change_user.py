from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from print_table_change_user import *

class test_print_table_change_user(TestCase):
	
	def test_act_user_success(self):
		with patch('sys.stdout', new = StringIO()):
			self.assertEqual(act_user(1, 1), 0)
	
	def test_act_user_error(self):
		with patch('sys.stdout', new = StringIO()):
			self.assertNotEqual(act_user(0, 1), 0)

	def test_ausgabe(self):
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, ausgabe())