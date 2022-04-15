from django import forms
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label="username")
    first_name = forms.CharField(label="first_name", max_length=30)
    last_name = forms.CharField(label="last_name", max_length=30)
    email = forms.EmailField(label="email")

    def clean_email(self):
        email = self.cleaned_data["email"]
        print("Email cleaned")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email

    def clean_username(self):
        username = self.cleaned_data["username"]
        if not username.isalnum():
            raise ValidationError("Username must be alphanumeric")
        return username

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if not first_name.isalpha():
            raise ValidationError("First name must be alphabetic")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if not last_name.isalpha():
            raise ValidationError("Last name must be alphabetic")
        return last_name

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        if len(password) < 6:
            raise ValidationError("Password must be at least 6 characters long")
        if not any(char.isdigit() for char in password):
            raise ValidationError("Password must contain at least 1 digit")
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
