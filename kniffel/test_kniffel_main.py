from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from kniffel_main import main
from file_handling import write_file_player

#@patch("kniffel_main.input", create=True)

class test_main(TestCase):
    def test_main(self):
        player = [["Caro",0,0,"-",0,5,18,"-","-","-",0,15,0,0,0,0,0,15,"-"],["Nico",1,0,"-",5,10,12,"-","-","-",0,0,0,30,40,0,0,70,"-"]]
        write_file_player(player)
        with patch('sys.stdout', new = StringIO()):
            with patch('sys.stdin', new = StringIO('ABC\nj\n\n0\n3\n0\n3')):
                self.assertIsNone(main())
    #fehler bei stdin: eof read line
#    def test_main(self, mocked_input):
#        mocked_input.side_effect = ['j']
#        self.assertRaises(Exception, main())



        #"""with patch('sys.stdout', new = StringIO()):
        #        with patch('sys.stdin', new = StringIO('j\n\n0\n13')):
        #            self.assertRaises(Exception, main())"""