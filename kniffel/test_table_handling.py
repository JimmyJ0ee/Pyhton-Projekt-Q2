from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from file_handling import write_file_player
from table_handling import *

class test_table_handling(TestCase):

    def test_bonus(self):
        with patch('sys.stdout', new = StringIO()):
            self.assertRaises(Exception, bonus(0))

    def test_sum_bottom_table(self):
        with patch('sys.stdout', new = StringIO()):
            self.assertRaises(Exception, sum_bottom_table(0))
    
    def test_winner(self):
        player = [["Caro",0,0,0,0,5,18,0,0,0,0,15,0,0,0,0,0,15,0],["Nico",1,0,0,5,10,12,0,0,0,0,0,0,30,40,0,0,70,0]]
        write_file_player(player)
        with patch('sys.stdout', new = StringIO()):
            self.assertRaises(Exception, winner())
