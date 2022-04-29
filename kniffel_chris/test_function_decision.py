import unittest
from io import StringIO
from unittest.mock import patch
import function_decision

class Table(unittest.TestCase):

    #mit patch schnappt man sich die jeweiligen Funktionen um sie zu testen
    @patch('bottom_table_function.pasch_three')
    @patch('bottom_table_function.pasch_four')
    @patch('bottom_table_function.full_house')
    @patch('bottom_table_function.small_straight')
    @patch('bottom_table_function.large_straight')
    @patch('bottom_table_function.kniffel')
    @patch('bottom_table_function.chance')

    #der erste patch muss am Ende in den Argumenten stehen
    def test_bottom_table(self, chance, kniffel, large_s, small_s, full_h, pasch_4, pasch_3):
        
        pasch_3.return_value = 1
        pasch_4.return_value = 2
        full_h.return_value = 5
        small_s.return_value = 3
        large_s.return_value = 4
        kniffel.return_value = 6
        chance.return_value = 7

        #inputs: action_combine, active_user

        #pasch_three
        self.assertEqual(function_decision.bottom_table(7, 0), 1)
        #pasch_four
        self.assertEqual(function_decision.bottom_table(8, 0), 2)
        #full_house
        self.assertEqual(function_decision.bottom_table(9, 0), 5)
    	#small_straight
        self.assertEqual(function_decision.bottom_table(10, 0), 3)
        #large_straight
        self.assertEqual(function_decision.bottom_table(11, 0), 4)
        #kniffel
        self.assertEqual(function_decision.bottom_table(12, 0), 6)
        #chance
        self.assertEqual(function_decision.bottom_table(13, 0), 7)

    def test_write_file_dice(self):
        with patch('sys.stdout', new = StringIO()):
            self.assertRaises(Exception, function_decision.upper_table_function(0, 2))
    
    #fehler: eof reading a line bei input der wahl
    #def test_combine(self):
    #    with patch('sys.stdin', new = StringIO('10')):
    #        self.assertRaises(Exception, function_decision.combine(0))
    
    #@patch('combine_function.upper_table_function')
    #@patch('combine_function.bottom_table')
    #@patch('combine_function.strikeout')
    #def test_combine(self, strikeout, bottom_table, upper_table_function):
    #    strikeout.return_value = 0
    #    bottom_table.return_value = 0
    #    upper_table_function.return_value = 0
    #    self.assertEqual(function_decision.combine(0), 0)
    #    self.assertEqual(function_decision.combine(0), 0)
    #    self.assertEqual(function_decision.combine(0), 0)