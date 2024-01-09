from unittest import TestCase

from prime_numbers_finder import find_prime_numbers


class Test(TestCase):
    def test_find_prime_numbers_with_positive_target(self):
        result = find_prime_numbers(10)
        self.assertEqual(result, [2, 3, 5, 7])

    def test_find_prime_numbers_with_zero_target(self):
        result = find_prime_numbers(0)
        self.assertEqual(result, [])

    def test_find_prime_numbers_with_negative_target(self):
        with self.assertRaises(ValueError):
            find_prime_numbers(-5)

    def test_find_prime_numbers_with_one_as_target(self):
        result = find_prime_numbers(1)
        self.assertEqual(result, [])

    def test_find_prime_numbers_with_large_target(self):
        result = find_prime_numbers(100)
        expected_result = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
            31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
            73, 79, 83, 89, 97
        ]
        self.assertEqual(result, expected_result)
