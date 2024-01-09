from unittest import TestCase

from palindrome_checker import check_if_palindrome


class Test(TestCase):
    def test_check_if_palindrome_basic(self):
        result = check_if_palindrome("kajak")
        return self.assertEqual(result, True)

    def test_check_if_palindrome_spaces(self):
        result = check_if_palindrome("k aj a k")
        return self.assertEqual(result, True)

    def test_check_if_palindrome_mixed_case(self):
        result = check_if_palindrome("kAJaK")
        return self.assertEqual(result, True)

    def test_check_if_palindrome_punctuation(self):
        result = check_if_palindrome(".,!ka.,,ja,.k")
        return self.assertEqual(result, True)

    def test_check_if_palindrome_failing(self):
        result = check_if_palindrome("kot")
        return self.assertEqual(result, False)

    def test_check_if_palindrome_empty(self):
        result = check_if_palindrome("")
        return self.assertEqual(result, True)