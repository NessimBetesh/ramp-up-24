import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Fridaythe13th_hard import has_friday_13

class TestHasFriday13(unittest.TestCase):
    def test_has_friday_13(self):
        # Test a month with Friday the 13th
        self.assertTrue(has_friday_13(3, 2020))  # March 2020 had Friday the 13th

        # Test a month without Friday the 13th
        self.assertFalse(has_friday_13(6, 2022))  # June 2022 did not have Friday the 13th

        # Test a leap year with February 29th falling on Friday
        self.assertFalse(has_friday_13(2, 2008))  # February 2008 had Friday the 29th

        # Test a non-leap year with February 29th not falling on Friday
        self.assertFalse(has_friday_13(2, 2021))  # February 2021 did not have Friday the 13th

        self.assertTrue (has_friday_13(10, 2023))
        # Test with an invalid month (month < 1 or month > 12)
        with self.assertRaises(ValueError):
            has_friday_13(13, 2023)

if __name__ == '__main__':
    unittest.main()
