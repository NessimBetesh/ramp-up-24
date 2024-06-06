import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from findthediscount_easy import dis

class TestDiscount(unittest.TestCase):
    def test_discount(self):
        # Test with a discount of 10% on a price of $100
        self.assertAlmostEqual(dis(100, 10), 90.00)

        # Test with a discount of 25% on a price of $80
        self.assertAlmostEqual(dis(80, 25), 60.00)

        # Test with a discount of 50% on a price of $50
        self.assertAlmostEqual(dis(50, 50), 25.00)

        # Test with a discount of 0% on a price of $200
        self.assertAlmostEqual(dis(200, 0), 200.00)

if __name__ == '__main__':
    unittest.main()