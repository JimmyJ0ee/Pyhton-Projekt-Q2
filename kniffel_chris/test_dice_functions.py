from unittest import TestCase
from dice_functions import dices
from unittest.mock import patch
from io import StringIO

class Test_dices_functions(TestCase):
    def test_dices(self):
        with patch('sys.stdin', new = StringIO('1\n2\n3')):
            with self.assertRaises(IndexError):
                dices(3)
        with patch('sys.stdin', new = StringIO('1\n2\n3')):
            with self.assertRaises(TypeError):
                dices('ABC')
        with patch('sys.stdin', new = StringIO('1\n2\n3')):
            with self.assertRaises(TypeError):
                dices(0.5458558)        
            #Programm läuft bei korrekter Eingabe durch     
        with patch('sys.stdin', new = StringIO('1\n2\n3')):
            self.assertRaises(Exception, dices(0))
            #Falscheingabe wird abgefangen - Programm läuft zum Ende
        with patch('sys.stdin', new = StringIO('A\n1\n2\n3')):
            with self.assertRaises(Exception):
                dices(0)