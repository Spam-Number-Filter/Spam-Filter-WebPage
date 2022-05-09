from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

from data_numbers.validation.email_validation import valid_email
from data_numbers.validation.first_name_validation import valid_first_name
from data_numbers.validation.last_name_validation import valid_last_name
from data_numbers.validation.password_validation import valid_password
from data_numbers.validation.username_validation import valid_username


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label="username")
    first_name = forms.CharField(label="first_name", max_length=30)
    last_name = forms.CharField(label="last_name", max_length=30)
    email = forms.EmailField(label="email")

    def clean_email(self):
        email = self.cleaned_data["email"]
        if valid_email(email):
            return email

    def clean_username(self):
        username = self.cleaned_data["username"]
        if valid_username(username):
            return username

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if valid_first_name(first_name):
            return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if valid_last_name(last_name):
            return last_name

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        if valid_password(password):
            return password

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]


class ModifyUsernameForm(UserChangeForm):
    username = forms.CharField(label="username")

    def modify_username(self):
        username = self.cleaned_data["username"]
        if valid_username(username):
            return username

    class Meta:
        model = User
        fields = [
            "username",
        ]
