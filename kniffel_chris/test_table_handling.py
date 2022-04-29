from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import json
import table_handling

class TestTableHandling (TestCase):

    def test_bonus(self):
        with patch('sys.stdout', new = StringIO()):
            self.assertRaises(Exception, table_handling.bonus(0))

    def test_sum_bottom_table(self):
        with patch('sys.stdout', new = StringIO()):
            self.assertRaises(Exception, table_handling.sum_bottom_table(0))
    
    def test_winner(self):
        #json bereinigen
        with open ('kniffel_player.json', 'r', encoding='utf8') as kniffel_player:
            player=json.load(kniffel_player)
        count_reset_player_one = 1
        count_reset_player_two = 1
        while count_reset_player_one <= 18:
            player[0][count_reset_player_one] = '-'
            count_reset_player_one = count_reset_player_one + 1
        while count_reset_player_two <= 18:
            player[1][count_reset_player_two] = '-'
            count_reset_player_two = count_reset_player_two + 1
        player[0][9] = player[0][17] = player[1][9] = player[1][17] = 0
        with open ('kniffel_player.json', 'w', encoding='utf8') as kniffel_player:
            json.dump(player, kniffel_player, indent=4)
        with patch('sys.stdout', new = StringIO()):
            self.assertRaises(Exception, table_handling.winner())
