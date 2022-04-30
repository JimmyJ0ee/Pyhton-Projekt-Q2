import imp
from importlib.resources import path
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import json
from bottom_table_function import *
from file_handling import *


class test_bottom_table_function(TestCase):

	def test_pasch_three(self):
		#Fall - 3er Pasch möglich
		dice_all = [1,1,2,1,3]
		write_file_dice(dice_all)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, pasch_three(0))

		#Fall - Pasch 3 Feld schon beschrieben
		dice_all = [2,2,2,1,3]
		write_file_dice(dice_all)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, pasch_three(0))

		#Fall - Pasch 3 nicht möglich
		player = [["Caro","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],["Nico","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]]
		write_file_player(player)
		dice_all = [2,5,2,1,3]
		write_file_dice(dice_all)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, pasch_three(0))
		
		
	
	def test_pasch_four(self):
		#Fall - 4er Pasch möglich
		dice_all = [2,2,2,2,3]
		write_file_dice(dice_all)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, pasch_four(0))

		#Fall - 4er Pasch Feld schon beschrieben
		dice_all = [2,2,2,2,3]
		write_file_dice(dice_all)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, pasch_four(0))

		#Fall - 4er Pasch nicht möglich
		player = [["Caro","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],["Nico","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]]
		write_file_player(player)
		dice_all = [5,2,2,2,3]
		write_file_dice(dice_all)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, pasch_four(0))
	
	def test_full_house(self):
		#Fall 1 - Full House moeglich
		dice_all = [5,2,5,5,2]
		write_file_dice(dice_all)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, full_house(0))

		#Fall 2 - Full House moeglich
		player = [["Caro","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],["Nico","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]]
		write_file_player(player)
		dice_all = [5,2,5,2,2]
		write_file_dice(dice_all)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, full_house(0))

		#Fall 3 - Full House Feld schon beschrieben
		dice_all = [5,2,5,2,2]
		write_file_dice(dice_all)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, full_house(0))

		#Fall 4 - Full House nicht moeglich
		player = [["Caro","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],["Nico","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]]
		write_file_player(player)
		dice_all = [5,2,3,2,2]
		write_file_dice(dice_all)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, full_house(0))
	
	
	def test_small_straight(self):
		#Fall 1 - kleine Straße
		dice_all = [1, 2, 3, 4, 1]
		write_file_dice(dice_all)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, small_straight(0))		
			
		#Fall 2 - kleine Straße
		player = [["Caro","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],["Nico","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]]
		write_file_player(player)
		dice_all = [2, 3, 4, 5, 2]
		write_file_dice(dice_all)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, small_straight(0))

		#Fall 3 - kleine Straße
		player = [["Caro","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],["Nico","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]]
		write_file_player(player)
		dice_all = [3, 4, 5, 6, 3]
		write_file_dice(dice_all)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, small_straight(0))

		#Fall - Feld bereits gefüllt
		dice_all = [2, 3, 4, 5, 2]
		write_file_dice(dice_all)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, small_straight(0))

		#Fall - kleine Straße nicht möglich
		player = [["Caro","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],["Nico","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]]
		write_file_player(player)
		dice_all = [2, 3, 2, 5, 2]
		write_file_dice(dice_all)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, small_straight(0))

		
	
	def test_large_straight_case_one(self):
		#Fall 1
		dice_all = [1, 2, 3, 4, 5]
		write_file_dice(dice_all)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, large_straight(0))

		#Fall 2
		player = [["Caro","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],["Nico","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]]
		write_file_player(player)
		dice_all = [2, 3, 4, 5, 6]
		write_file_dice(dice_all)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, large_straight(0))

		#Fall 3 - Feld bereits belegt
		dice_all = [2, 2, 4, 5, 6]
		write_file_dice(dice_all)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, large_straight(0))
		
		#Fall 4 - große Straße nicht möglich
		player = [["Caro","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],["Nico","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]]
		write_file_player(player)
		dice_all = [2, 2, 4, 5, 6]
		write_file_dice(dice_all)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, large_straight(0))
	
	def test_kniffel(self):
		#Fall - Kniffel moeglich
		dice_all=[5, 5, 5, 5, 5]
		write_file_dice(dice_all)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, kniffel(0))

		#Fall - Kniffel Feld bereits besetzt
		dice_all=[5, 5, 5, 5, 5]
		write_file_dice(dice_all)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, kniffel(0))
		
		#Fall - Kniffel nicht moeglich
		player = [["Caro","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],["Nico","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]]
		write_file_player(player)
		dice_all=[5, 4, 5, 5, 5]
		write_file_dice(dice_all)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, kniffel(0))
		

	
	def test_bonus_kniffel(self):
		#Fall - Bonus erreicht
		check=2
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, bonus_kniffel(0, check))
		
		#Fall - Feld bereits besetzt
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, bonus_kniffel(0, check))
	
	def test_chance(self):
		#Fall - Chance moeglich
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, chance(0))

		#Fall - Feld bereits besetzt
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, chance(0))
	
	def test_strikeout(self):
        #Fall - Feld streichen moeglich + Falscheingaben abgefangen
		player = [["Caro","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],["Nico","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]]
		write_file_player(player)
		with patch('sys.stdout', new = StringIO()):
			with patch('sys.stdin', new = StringIO('A\n20\n3\n12\n')):
				self.assertRaises(Exception, strikeout(0))
	
		#Fall - kein Feld wird gestrichen
		player = [["Caro","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],["Nico","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]]
		write_file_player(player)
		with patch('sys.stdout', new = StringIO()):
			with patch('sys.stdin', new = StringIO('14\n')):
				self.assertRaises(Exception, strikeout(0))

