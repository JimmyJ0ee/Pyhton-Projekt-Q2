from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import kniffel_main

#class TestURLPrint(TestCase):

    #fehler bei stdin: eof read line
    #def test_main(self):
    #    with patch('sys.stdout', new = StringIO()):
    #        with patch('sys.stdin', new = StringIO('j\n')):
    #            self.assertRaises(Exception, kniffel_main.main())
