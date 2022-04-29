from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import print_table_change_user

class TestURLPrint(TestCase):
	
	def test_act_user_success(self):
		active_user = 1
		expected_output = 0
		loop_control = 1
		with patch('sys.stdout', new = StringIO()):
			self.assertEqual(print_table_change_user.act_user(active_user, loop_control), expected_output)
	
	def test_act_user_error(self):
		active_user = 0
		expected_output = 0
		loop_control = 1
		with patch('sys.stdout', new = StringIO()):
			self.assertNotEqual(print_table_change_user.act_user(active_user, loop_control), expected_output)

	def test_ausgabe(self):
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, print_table_change_user.ausgabe())