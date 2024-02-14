import unittest
import cmd
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage


class TestConsoleMethods(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f'show User {obj_id}')
            output = f.getvalue().strip()
            self.assertIn(f"[User] ({obj_id})", output)
            self.assertIn("'id': '" + obj_id + "'", output)

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertIsNone(self.console.emptyline())


if __name__ == '__main__':
    unittest.main()
