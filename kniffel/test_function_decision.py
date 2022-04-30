import unittest
from io import StringIO
from unittest.mock import patch
from function_decision import *

class test_function_decision(unittest.TestCase):

    #Funktionen simulieren
    @patch('bottom_table_function.pasch_three')
    @patch('bottom_table_function.pasch_four')
    @patch('bottom_table_function.full_house')
    @patch('bottom_table_function.small_straight')
    @patch('bottom_table_function.large_straight')
    @patch('bottom_table_function.kniffel')
    @patch('bottom_table_function.chance')

    def test_bottom_table(self, chance, kniffel, large_s, small_s, full_h, pasch_4, pasch_3):
        
        #return-values der Funktionen simulieren
        pasch_3.return_value = 1
        pasch_4.return_value = 2
        full_h.return_value = 5
        small_s.return_value = 3
        large_s.return_value = 4
        kniffel.return_value = 6
        chance.return_value = 7

            #pasch_three
        with patch('sys.stdout', new = StringIO()):
            self.assertEqual(bottom_table(7, 0), 1)
            #pasch_four
        with patch('sys.stdout', new = StringIO()):
            self.assertEqual(bottom_table(8, 0), 2)
            #full_house
        with patch('sys.stdout', new = StringIO()):
            self.assertEqual(bottom_table(9, 0), 5)
            #small_straight
        with patch('sys.stdout', new = StringIO()):
            self.assertEqual(bottom_table(10, 0), 3)
            #large_straight
        with patch('sys.stdout', new = StringIO()):
            self.assertEqual(bottom_table(11, 0), 4)
            #kniffel
        with patch('sys.stdout', new = StringIO()):
            self.assertEqual(bottom_table(12, 0), 6)
            #chance
            self.assertEqual(bottom_table(13, 0), 7)

    def upper_table_function(self):
        with patch('sys.stdout', new = StringIO()):
            self.assertRaises(Exception, upper_table_function(0, 2))
    