from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import os
import file_handling

class test_file_handling(TestCase):

#Testen der Exceptions der Dateilesefunktionen
	def test_read_file_kniffel_player(self):
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, file_handling.read_file_kniffel_player())
	
	def test_read_file_dice(self):
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, file_handling.read_file_dice())
	
	#File dice.json ist nicht vorhanden
	def test_read_file_dice_exception(self):
		os.rename(r'dice.json', r'dic.json')
		with patch('sys.stdout', new = StringIO()):
			with self.assertRaises(SystemExit):
				file_handling.read_file_dice()
		os.rename(r'dic.json', r'dice.json')

	#File kniffel_player.json ist nicht vorhanden
	def test_read_file_kniffel_player_exception(self):
		os.rename(r'kniffel_player.json', r'kniffel.json')
		with patch('sys.stdout', new = StringIO()):
			with self.assertRaises(SystemExit):
				file_handling.read_file_kniffel_player()
		os.rename(r'kniffel.json', r'kniffel_player.json')
	
#Testen der Exceptions der Dateischreibfunktionen
	def test_write_file_player(self):
		player = [["Caro",0,"-",6,0,5,18,"-","-","-","-","-","-","-","-","-","-","-","-"],["Nico",1,"-","-","-",10,12,"-","-","-","-","-","-",30,40,"-","-","-","-"]]
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, file_handling.write_file_player(player))
	
	def test_write_file_dice(self):
		dice_all = [5,4,1,6,4]
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, file_handling.write_file_dice(dice_all))
	
	

	
