import unittest
from main import robot


class FizzBuzzTest(unittest.TestCase):
    def test_not_multiples(self):
        nums = [1, 2, 4, 7, 8]
        for num in nums:
            with self.subTest():
                self.assertEqual(robot(num), str(num))

    def test_multiples_of_three(self):
        nums = [3,6,9,12]
        for num in nums:
            with self.subTest():
                self.assertEqual(robot(num), 'Fizz')

    def test_multiples_of_five(self):
        nums = [5,10,20,25]
        for num in nums:
            with self.subTest():
                self.assertEqual(robot(num), 'Buzz')

    def test_multiples_of_three_and_five(self):
        nums = [15, 30, 45, 60]
        for num in nums:
            with self.subTest():
                self.assertEqual(robot(num), 'FizzBuzz')

