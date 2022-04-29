from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import bottom_table_function

class TestURLPrint(TestCase):

	def test_pasch_three(self):
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, bottom_table_function.pasch_three(0))
	
	def test_pasch_four(self):
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, bottom_table_function.pasch_four(0))
	
	def test_full_house(self):
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, bottom_table_function.full_house(0))
	
	def test_small_straight(self):
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, bottom_table_function.small_straight(0))
	
	def test_large_straight(self):
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, bottom_table_function.large_straight(0))
	
	def test_kniffel(self):
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, bottom_table_function.kniffel(0))
	
	def test_bonus_kniffel(self):
		check=2
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, bottom_table_function.bonus_kniffel(0, check))
	
	def test_chance(self):
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, bottom_table_function.chance(0))
	
	def test_strikeout(self):
		with patch('sys.stdin', new = StringIO('8\n')):
			self.assertRaises(Exception, bottom_table_function.strikeout(0))
