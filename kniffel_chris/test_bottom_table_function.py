from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import json
import bottom_table_function

class TestURLPrint(TestCase):

	def test_pasch_three(self):
		#json bereinigen
		with open('dice.json', 'r') as dice:
			dice_all=json.load(dice)
		count_reset_dices = 0
		while count_reset_dices <= 4:
			dice_all[count_reset_dices] = 0
			count_reset_dices = count_reset_dices + 1
		dice_all[0] = dice_all[1] = dice_all[2] = 2
		with open('dice.json', 'w') as dice:
			json.dump(dice_all, dice, indent=4)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, bottom_table_function.pasch_three(0))
	
	def test_pasch_four(self):
		#json bereinigen
		with open('dice.json', 'r') as dice:
			dice_all=json.load(dice)
		count_reset_dices = 0
		while count_reset_dices <= 4:
			dice_all[count_reset_dices] = 0
			count_reset_dices = count_reset_dices + 1
		dice_all[0] = dice_all[1] = dice_all[2] = dice_all[3] = 2
		with open('dice.json', 'w') as dice:
			json.dump(dice_all, dice, indent=4)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, bottom_table_function.pasch_four(0))
	
	def test_full_house(self):
		#json bereinigen
		with open('dice.json', 'r') as dice:
			dice_all=json.load(dice)
		count_reset_dices = 0
		while count_reset_dices <= 4:
			dice_all[count_reset_dices] = 0
			count_reset_dices = count_reset_dices + 1
		dice_all[0] = dice_all[1] = 2
		dice_all[2] = dice_all[3] = dice_all[4] = 3
		with open('dice.json', 'w') as dice:
			json.dump(dice_all, dice, indent=4)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, bottom_table_function.full_house(0))
		#json bereinigen
		with open('dice.json', 'r') as dice:
			dice_all=json.load(dice)
		count_reset_dices = 0
		while count_reset_dices <= 4:
			dice_all[count_reset_dices] = 0
			count_reset_dices = count_reset_dices + 1
		dice_all[0] = dice_all[1] = dice_all[2] = 2
		dice_all[3] = dice_all[4] = 3
		with open('dice.json', 'w') as dice:
			json.dump(dice_all, dice, indent=4)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, bottom_table_function.full_house(0))
	
	def test_full_house_two(self):
		#json bereinigen
		with open('dice.json', 'r') as dice:
			dice_all=json.load(dice)
		count_reset_dices = 0
		while count_reset_dices <= 4:
			dice_all[count_reset_dices] = 0
			count_reset_dices = count_reset_dices + 1
		dice_all[0] = dice_all[1] = dice_all[2] = 2
		dice_all[3] = dice_all[4] = 3
		with open('dice.json', 'w') as dice:
			json.dump(dice_all, dice, indent=4)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, bottom_table_function.full_house(0))
	
	def test_small_straight(self):
		#fall 1
		with open('dice.json', 'r') as dice:
			dice_all=json.load(dice)
		count_reset_dices = 0
		while count_reset_dices <= 4:
			dice_all[count_reset_dices] = 0
			count_reset_dices = count_reset_dices + 1
		dice_all[0] = 1
		dice_all[1] = 2
		dice_all[2] = 3
		dice_all[3] = 4
		dice_all[4] = 1
		with open('dice.json', 'w') as dice:
			json.dump(dice_all, dice, indent=4)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, bottom_table_function.small_straight(0))
		
		#fall 1
		with open('dice.json', 'r') as dice:
			dice_all=json.load(dice)
		count_reset_dices = 0
		while count_reset_dices <= 4:
			dice_all[count_reset_dices] = 0
			count_reset_dices = count_reset_dices + 1
		dice_all[0] = 2
		dice_all[1] = 3
		dice_all[2] = 4
		dice_all[3] = 5
		dice_all[4] = 1
		with open('dice.json', 'w') as dice:
			json.dump(dice_all, dice, indent=4)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, bottom_table_function.small_straight(0))
		
		#fall 1
		with open('dice.json', 'r') as dice:
			dice_all=json.load(dice)
		count_reset_dices = 0
		while count_reset_dices <= 4:
			dice_all[count_reset_dices] = 0
			count_reset_dices = count_reset_dices + 1
		dice_all[0] = 3
		dice_all[1] = 4
		dice_all[2] = 5
		dice_all[3] = 6
		dice_all[4] = 1
		with open('dice.json', 'w') as dice:
			json.dump(dice_all, dice, indent=4)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, bottom_table_function.small_straight(0))
	
	def test_large_straight_case_one(self):
		#fall 1
		with open('dice.json', 'r') as dice:
			dice_all=json.load(dice)
		count_reset_dices = 0
		while count_reset_dices <= 4:
			dice_all[count_reset_dices] = 0
			count_reset_dices = count_reset_dices + 1
		dice_all[0] = 1
		dice_all[1] = 2
		dice_all[2] = 3
		dice_all[3] = 4
		dice_all[4] = 5
		with open('dice.json', 'w') as dice:
			json.dump(dice_all, dice, indent=4)

		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, bottom_table_function.large_straight(0))
		
	def test_large_straight_case_two(self):
		#fall 2
		with open('dice.json', 'r') as dice:
			dice_all=json.load(dice)
		count_reset_dices = 0
		while count_reset_dices <= 4:
			dice_all[count_reset_dices] = 0
			count_reset_dices = count_reset_dices + 1
		dice_all[0] = 2
		dice_all[1] = 3
		dice_all[2] = 4
		dice_all[3] = 5
		dice_all[4] = 6
		with open('dice.json', 'w') as dice:
			json.dump(dice_all, dice, indent=4)
		
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, bottom_table_function.large_straight(0))
	
	def test_kniffel(self):
		#json bereinigen
		with open('dice.json', 'r') as dice:
			dice_all=json.load(dice)
		count_reset_dices = 0
		while count_reset_dices <= 4:
			dice_all[count_reset_dices] = 3
			count_reset_dices = count_reset_dices + 1
		with open('dice.json', 'w') as dice:
			json.dump(dice_all, dice, indent=4)
		        #json bereinigen
		with open('kniffel_player.json', 'r', encoding='utf8') as kniffel_player:
			player=json.load(kniffel_player)
		count_reset_player_one = 1
		count_reset_player_two = 1
		while count_reset_player_one <= 18:
			player[0][count_reset_player_one] = '-'
			count_reset_player_one = count_reset_player_one + 1
		while count_reset_player_two <= 18:
			player[1][count_reset_player_two] = '-'
			count_reset_player_two = count_reset_player_two + 1
		with open ('kniffel_player.json', 'w', encoding='utf8') as kniffel_player:
			json.dump(player, kniffel_player, indent=4)
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, bottom_table_function.kniffel(0))
	
	def test_bonus_kniffel(self):
		check=2
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, bottom_table_function.bonus_kniffel(0, check))
	
	def test_chance(self):
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, bottom_table_function.chance(0))
	
    #gleicher Fehler für stdin: eof reading line
	def test_strikeout(self):
        #json bereinigen
		with open('kniffel_player.json', 'r', encoding='utf8') as kniffel_player:
			player=json.load(kniffel_player)
		count_reset_player_one = 1
		count_reset_player_two = 1
		while count_reset_player_one <= 18:
			player[0][count_reset_player_one] = '-'
			count_reset_player_one = count_reset_player_one + 1
		while count_reset_player_two <= 18:
			player[1][count_reset_player_two] = '-'
			count_reset_player_two = count_reset_player_two + 1
		with open ('kniffel_player.json', 'w', encoding='utf8') as kniffel_player:
			json.dump(player, kniffel_player, indent=4)
		with patch('sys.stdin', new = StringIO('12\n')):
			self.assertRaises(Exception, bottom_table_function.strikeout(0))
