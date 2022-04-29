from ast import Str
from io import StringIO
from unittest import TestCase
import unittest
from unittest.mock import patch
from dice_functions import dices

#read_file patchen
#function_decision.combine patchen

#@patch("dice_functions.input", create=True)
#@patch("function_decision.combine", create=True)
class Test_dices_functions(TestCase):
    def test_dices(self):
        with patch('sys.stdout', new = StringIO()):
            self.assertRaises(Exception, dices(0))
        
        
        
        """with patch('sys.stdin', new = StringIO('1\n')):
            with self.assertRaises(IndexError):
                dices(3)
    def test_dices_simulated_input(self, mocked_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('sys.stdin', new=StringIO("'0'")) as fake_in:
                dices(0)
                fake_out.seek(0)
                self.asserEqual
        mocked_input.side_effect = ['1 2 3', '4', '5']
        self.assertEqual(dices(1), '1 2 3')"""




        


if __name__ == '__main__':
    unittest.main()