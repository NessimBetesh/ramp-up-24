import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ConvertMinutesintoSeconds_veryeasy import convert

class TestConvert(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(convert(1), 60)
        self.assertEqual(convert(5), 300)
        self.assertEqual(convert(10), 600)
        self.assertEqual(convert(0), 0)

if __name__ == '__main__':
    unittest.main()