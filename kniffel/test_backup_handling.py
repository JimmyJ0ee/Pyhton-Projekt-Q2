from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from backup_handling import *

class test_backup_handling(TestCase):
	
	def test_delete_backup_success(self):
		with patch('sys.stdout', new = StringIO()):
			with patch('sys.stdin', new = StringIO('name\nname_zwei')):
				self.assertRaises(Exception, delete_backup())

	def test_analyse_backup_error(self):
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, analyse_backup())
