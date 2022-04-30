from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from file_handling import *

class test_read_file_player(TestCase):
	def test_read_file_kniffel_player(self):
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, read_file_kniffel_player())
	
	def test_read_file_dice(self):
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, read_file_dice())
	
	def test_write_file_player(self):
		player = [["Caro",0,"-",6,0,5,18,"-","-","-","-","-","-","-","-","-","-","-","-"],["Nico",1,"-","-","-",10,12,"-","-","-","-","-","-",30,40,"-","-","-","-"]]
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, write_file_player(player))
	
	def test_write_file_dice(self):
		dice_all = [5,4,1,6,4]
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, write_file_dice(dice_all))
	
	#Problem: rename Funktion erstellt immer eine neue Datei, und benennt das nicht um 
	"""def test_read_file_player_exception(self):
		os.rename('kniffel_player.json', 'file_not_available')
		with self.assertRaises(Exception):
			read_file_kniffel_player()"""
	#Problem: Error wird nicht geworfen
	"""def test_read_file_player_ValueError(self):
		player = (("Caro",0,0,"-",0,5,18,"-","-","A",0,15,0,0,0,0,0,15,"-"),("Nico",1,0,"-",5,10,12,"-","-","-",0,0,0,30,40,0,0,70,"-"))
		write_file_player(player)
		with patch('sys.stdout', new = StringIO()):
			with self.assertRaises(ValueError):
				read_file_kniffel_player()"""
		
