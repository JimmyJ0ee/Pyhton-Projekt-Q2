from unittest import TestCase
from dice_functions import dices, dice_new
from unittest.mock import patch
from io import StringIO

class test_dices_functions(TestCase):
    
    #dice_new läuft durch bei richtiger Eingabe
    def test_dice_new(self):
        action_numbers = [1,2,3]
        with patch('sys.stdout', new = StringIO()):
            with patch('sys.stdin', new = StringIO()):
                self.assertRaises(Exception, dice_new(action_numbers))

    #dices läuft weiter, auch wenn Funktionsvariable andere Werte als 1 oder 2 annimmt
    def test_dices(self):
        with patch('sys.stdout', new = StringIO()):
            with patch('sys.stdin', new = StringIO('1\n2\n3')):
                with self.assertRaises(IndexError):
                    dices(3)
        with patch('sys.stdout', new = StringIO()):
            with patch('sys.stdin', new = StringIO('1\n2\n3')):
                with self.assertRaises(TypeError):
                    dices('ABC')
        with patch('sys.stdout', new = StringIO()):
            with patch('sys.stdin', new = StringIO('1\n2\n3')):
                with self.assertRaises(TypeError):
                    dices(0.5458558)        
    #dices läuft bei korrekter Eingabe durch 
        with patch('sys.stdout', new = StringIO()):    
            with patch('sys.stdin', new = StringIO('1\n2\n3')):
                self.assertRaises(Exception, dices(0))
    #Falscheingabe Zeichenkette, Float, außerhalb der zugelassen range - Programm läuft normal weiter
        with patch('sys.stdout', new = StringIO()):
            with patch('sys.stdin', new = StringIO('_as\n1.5\n80\n-1\n3\n4\n0')):
                with self.assertRaises(Exception):
                    dices(0)