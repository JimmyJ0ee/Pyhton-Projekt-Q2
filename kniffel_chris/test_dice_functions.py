from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import dice_functions

class TestDiceFunctions (TestCase):

    def test_dice_new(self):
        action_numbers = [1,2,3]
        with patch('sys.stdin', new = StringIO()):
            self.assertRaises(Exception, dice_functions.dice_new(action_numbers))

    #klappt nicht: eof line read bei sys.stdin
    #def test_dices(self):
    #    with patch('sys.stdin', new = StringIO('1\n')):
    #        self.assertRaises(Exception, dice_functions.dices(0))

    def test_dices(self):
        with patch('sys.stdin', new = StringIO('1\n2\n3')):
            with self.assertRaises(IndexError):
                dice_functions.dices(3)
        with patch('sys.stdin', new = StringIO('1\n2\n3')):
            with self.assertRaises(TypeError):
                dice_functions.dices('ABC')
        with patch('sys.stdin', new = StringIO('1\n2\n3')):
            with self.assertRaises(TypeError):
                dice_functions.dices(0.5458558)        
            #Programm läuft bei korrekter Eingabe durch     
        with patch('sys.stdin', new = StringIO('1\n2\n3')):
            self.assertRaises(Exception, dice_functions.dices(0))
            #Falscheingabe wird abgefangen - Programm läuft zum Ende
        with patch('sys.stdin', new = StringIO('A\n1\n2\n3')):
            with self.assertRaises(Exception):
                dice_functions.dices(0)