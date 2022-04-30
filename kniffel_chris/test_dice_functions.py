from unittest import TestCase
from dice_functions import dices, dice_new
from unittest.mock import patch
from io import StringIO

class Test_dices_functions(TestCase):

    def test_dice_new(self):
        action_numbers = [1,2,3]
        with patch('sys.stdout', new = StringIO()):
            with patch('sys.stdin', new = StringIO()):
                self.assertRaises(Exception, dice_new(action_numbers))

    #klappt nicht: eof line read bei sys.stdin
    #def test_dices(self):
    #    with patch('sys.stdin', new = StringIO('1\n')):
    #        self.assertRaises(Exception, dice_functions.dices(0))


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
    #Programm läuft bei korrekter Eingabe durch 
        with patch('sys.stdout', new = StringIO()):    
            with patch('sys.stdin', new = StringIO('1\n2\n3')):
                self.assertRaises(Exception, dices(0))
    #Falscheingabe Zeichenkette, Float, außerhalb der zugelassen range - Programm läuft normal weiter
        with patch('sys.stdout', new = StringIO()):
            with patch('sys.stdin', new = StringIO('_as\n1.5\n80\n-1\n3\n4\n0')):
                with self.assertRaises(Exception):
                    dices(0)