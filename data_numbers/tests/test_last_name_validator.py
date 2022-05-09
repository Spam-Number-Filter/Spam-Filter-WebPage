from django.core.exceptions import ValidationError
from django.test import TestCase

from data_numbers.validation.last_name_validation import valid_last_name


class LastNameValidationTestCase(TestCase):
    def test_valid_two_last_names_returns_true(self):
        self.assertTrue(valid_last_name("Oscar Guapo"))

    def test_valid_two_last_names_with_final_space_returns_error(self):
        with self.assertRaises(ValidationError):
            valid_last_name("Oscar Guapo ")

    def test_correct_case_one_last_name_returns_true(self):
        self.assertTrue(valid_last_name("Smith"))

    def test_empty_last_name_returns_error(self):
        with self.assertRaises(ValidationError):
            valid_last_name("")

    def test_three_last_names_returns_error(self):
        with self.assertRaises(ValidationError):
            valid_last_name("Oscar Guapo Guapissim")
