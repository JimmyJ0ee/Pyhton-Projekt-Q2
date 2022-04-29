from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import file_handling

class TestURLPrint(TestCase):
	def test_read_file_kniffel_player(self):
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, file_handling.read_file_kniffel_player())
	
	def test_read_file_dice(self):
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, file_handling.read_file_dice())
	
	def test_write_file_player(self):
		player = [["Caro",0,"-",6,0,5,18,"-","-","-","-","-","-","-","-","-","-","-","-"],["Nico",1,"-","-","-",10,12,"-","-","-","-","-","-",30,40,"-","-","-","-"]]
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, file_handling.write_file_player(player))
	
	def test_write_file_dice(self):
		dice_all = [5,4,1,6,4]
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, file_handling.write_file_dice(dice_all))
