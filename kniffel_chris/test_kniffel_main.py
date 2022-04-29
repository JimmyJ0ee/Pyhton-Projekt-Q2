from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import kniffel_main

#@patch("kniffel_main.input", create=True)

#class test_main(TestCase):
    #fehler bei stdin: eof read line
#    def test_main(self, mocked_input):
#        mocked_input.side_effect = ['j']
#        self.assertRaises(Exception, kniffel_main.main())



        #"""with patch('sys.stdout', new = StringIO()):
        #        with patch('sys.stdin', new = StringIO('j\n')):
        #            self.assertRaises(Exception, kniffel_main.main())"""