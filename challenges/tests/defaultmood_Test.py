import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from defaultmood_easy import mood_today

class TestMoodToday(unittest.TestCase):
    def test_mood_today_default(self):
        self.assertEqual(mood_today(), "Today, I am feeling neutral")

    def test_mood_today_happy(self):
        self.assertEqual(mood_today("happy"), "Today, I am feeling happy")

    def test_mood_today_sad(self):
        self.assertEqual(mood_today("sad"), "Today, I am feeling sad")

    # Add more test cases for other moods if needed

if __name__ == '__main__':
    unittest.main()
