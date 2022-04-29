from io import StringIO
from tokenize import String
from unittest import TestCase
from unittest.mock import patch
import dice_functions

class TestDiceFunctions (TestCase):

    def test_dice_new(self):
        action_numbers = [1,2,3]
        with patch('sys.stdin', new = StringIO()):
            self.assertRaises(Exception, dice_functions.dice_new(action_numbers))
