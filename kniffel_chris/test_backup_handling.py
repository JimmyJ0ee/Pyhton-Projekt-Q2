from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import backup_handling

class TestURLPrint(TestCase):
	
	def test_delete_backup_success(self):
		with patch('sys.stdin', new = StringIO('name\nname_zwei')):
			self.assertRaises(Exception, backup_handling.delete_backup())

	def test_analyse_backup_error(self):
		with patch('sys.stdout', new = StringIO()):
			self.assertRaises(Exception, backup_handling.analyse_backup())
