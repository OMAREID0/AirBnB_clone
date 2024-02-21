import unittest
from unittest.mock import patch
from io import StringIO
import console
import inspect
import pep8
import unittest

HBNBCommand = console.HBNBCommand

class TestCodeUnderTest(unittest.TestCase):
    """
    This class contains unit tests for the code under test.
    """

    def setUp(self):
        """
        Set up the test environment before each test case.
        """
        self.hbnb_command = HBNBCommand()

    def assertErrorMessage(self, output, expected):
        """
        Asserts that the output matches the expected error message.
        """
        self.assertEqual(output, expected)

    def test_emptyline(self):
        """
        Test the emptyline method of HBNBCommand.
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.hbnb_command.emptyline()
            self.assertEqual(fake_out.getvalue().strip(), "")

    def test_do_quit(self):
        """
        Test the do_quit method of HBNBCommand.
        """
        self.assertTrue(self.hbnb_command.do_quit(""))

    def test_do_EOF(self):
        self.assertTrue(self.hbnb_command.do_EOF(""))

    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")

if __name__ == '__main__':
    unittest.main()
