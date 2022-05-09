from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from data_numbers.validation.email_validation import valid_email


class EmailValidatorTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="test", email="pablofraile@gmail.com")

    def test_empty_email_returns_error(self):
        with self.assertRaises(ValidationError):
            valid_email("")

    def test_already_created_email(self):
        with self.assertRaises(ValidationError):
            valid_email("pablofraile@gmail.com")

    def test_good_case_email(self):
        self.assertTrue(valid_email("fakeaccount@gmail.com"))
