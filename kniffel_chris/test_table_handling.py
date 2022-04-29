from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import table_handling

class TestTableHandling (TestCase):

    def test_bonus(self):
        with patch('sys.stdout', new = StringIO()):
            self.assertRaises(Exception, table_handling.bonus(0))

    def test_sum_bottom_table(self):
        with patch('sys.stdout', new = StringIO()):
            self.assertRaises(Exception, table_handling.sum_bottom_table(0))
    
    def test_winner(self):
        with patch('sys.stdout', new = StringIO()):
            self.assertRaises(Exception, table_handling.winner())
