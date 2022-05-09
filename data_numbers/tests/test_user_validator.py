from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from data_numbers.validation.username_validation import valid_username


class UserNameValidatorTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="my_user", email="pablofraile@gmail.com")

    def test_empty_username_returns_error(self):
        with self.assertRaises(ValidationError):
            valid_username("")

    def test_already_saved_username_returns_error(self):
        with self.assertRaises(ValidationError):
            valid_username("my_user")

    def test_with_two_name_and_spaces_returns_error(self):
        with self.assertRaises(ValidationError):
            valid_username("pablo fraile")

    def test_with_spaces_returns_error(self):
        with self.assertRaises(ValidationError):
            valid_username("pablo ")

    def test_good_username_returns_true(self):
        self.assertTrue(valid_username("pablito2020"))
