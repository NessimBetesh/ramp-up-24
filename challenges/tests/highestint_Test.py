import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from FindtheHighestIntegerintheListUsingRecursion_medium import find_highest

class TestFindHighest(unittest.TestCase):
    def test_find_highest(self):
        # Test with a list of positive integers
        self.assertEqual(find_highest([1, 5, 3, 9, 2]), 9)

        # Test with a list of negative integers
        self.assertEqual(find_highest([-1, -5, -3, -9, -2]), -1)

        # Test with a list of mixed positive and negative integers
        self.assertEqual(find_highest([-1, 5, -3, 9, 2]), 9)

        # Test with an empty list
        self.assertIsNone(find_highest([]))

        # Test with a list containing a single element
        self.assertEqual(find_highest([42]), 42)

        # Test with a list containing duplicate elements
        self.assertEqual(find_highest([3, 3, 3, 3]), 3)

if __name__ == '__main__':
    unittest.main()
