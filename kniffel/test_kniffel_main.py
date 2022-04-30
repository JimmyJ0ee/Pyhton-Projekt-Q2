from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from kniffel_main import main
from file_handling import write_file_player


class test_kniffel_main(TestCase):
    #Falscheingaben werden mit Exceptions abgefangen + Durchlauf funktioniert bei richtigen Eingaben
    def test_main(self):
        player = [["Caro",0,0,"-",0,5,18,"-","-","-",0,15,0,0,0,0,0,15,"-"],["Nico",1,0,"-",5,10,12,"-","-","-",0,0,0,30,40,0,0,70,"-"]]
        write_file_player(player)
        with patch('sys.stdout', new = StringIO()):
                with patch('sys.stdin', new = StringIO('ABC\nj\n0\n3\n0\n3\n')):
                    self.assertRaises(Exception, main())