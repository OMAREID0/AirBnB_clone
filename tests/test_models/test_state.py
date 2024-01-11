#/usr/bin/python3

import unittest
from models.state import state

class TestState(unittest.TestCase):
    def test_state_attributes(self):
        s = state()
        self.assertEqual(s.name, "")

if __name__ == '__main__':
    unittest.main()
