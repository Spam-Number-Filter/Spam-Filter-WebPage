from django.core.exceptions import ValidationError
from django.test import TestCase

from data_numbers.validation.password_validation import valid_password


class PasswordTestCase(TestCase):
    def test_empty_password_returns_error(self):
        with self.assertRaises(ValidationError):
            valid_password("")

    def test_less_than_6_chars_password_returns_error(self):
        with self.assertRaises(ValidationError):
            valid_password("1a3b4")

    def test_no_number_password_returns_error(self):
        with self.assertRaises(ValidationError):
            valid_password("oscarguapo")

    def test_valid_password(self):
        self.assertTrue(valid_password("1a3b4c5d6e"))
