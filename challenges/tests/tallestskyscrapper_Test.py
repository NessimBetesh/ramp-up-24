import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tallestskyscraper_hard import tallest_skyscraper

class TestTallestSkyscraper(unittest.TestCase):
    def test_tallest_skyscraper(self):
        # Test case with one skyscraper
        city1 = [
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [1, 1, 1, 1]
        ]
        self.assertEqual(tallest_skyscraper(city1), 3)

        # Test case with multiple skyscrapers of different heights
        city2 = [
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [1, 1, 1, 1]
        ]
        self.assertEqual(tallest_skyscraper(city2), 4)

        # Test case with no skyscrapers
        city3 = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 1, 0],
            [1, 1, 1, 1]
        ]
        self.assertEqual(tallest_skyscraper(city3), 2)

if __name__ == '__main__':
    unittest.main()
