from django.core.exceptions import ValidationError
from django.test import TestCase

from data_numbers.validation.first_name_validation import valid_first_name


class FirstNameValidationTestCase(TestCase):
    def test_empty_first_name_returns_error(self):
        with self.assertRaises(ValidationError):
            valid_first_name("")

    def test_name_with_space_return_error(self):
        with self.assertRaises(ValidationError):
            valid_first_name("pablo ")

    def test_correct_case(self):
        self.assertTrue(valid_first_name("Pablo"))
