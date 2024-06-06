import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ReturntheSumofTwoNumbers_veryeasy import sum

class TestSumFunction(unittest.TestCase):
    def test_sum(self):
        # Test with positive integers
        self.assertEqual(sum(3, 5), 8)

        # Test with negative integers
        self.assertEqual(sum(-3, -5), -8)

        # Test with one positive and one negative integer
        self.assertEqual(sum(-3, 5), 2)

        # Test with zero
        self.assertEqual(sum(0, 5), 5)

        # Test with one zero and one non-zero integer
        self.assertEqual(sum(0, -5), -5)

        # Test with both arguments being zero
        self.assertEqual(sum(0, 0), 0)
        
if __name__ == '__main__':
    unittest.main()
