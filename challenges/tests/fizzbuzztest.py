import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from FizzBuzzInterviewQuestion_medium import fizz_buzz

class fizzbuzztest(unittest.TestCase):
    def test_fizz_buzz(self):
       # self.assertEqual((1), "1")
        self.assertEqual(fizz_buzz(2), "2")
        self.assertEqual(fizz_buzz(3), "Fizz")
        self.assertEqual(fizz_buzz(4), "4")
        self.assertEqual(fizz_buzz(5), "Buzz")
        self.assertEqual(fizz_buzz(6), "Fizz")
        self.assertEqual(fizz_buzz(10), "Buzz")
        self.assertEqual(fizz_buzz(15), "FizzBuzz")
        self.assertEqual(fizz_buzz(30), "FizzBuzz")
        self.assertEqual(fizz_buzz(13), "13")

if __name__ == '__main__':
    unittest.main()
