from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def valid_username(username: str) -> bool:
    if not username.isalnum():
        raise ValidationError("Username must be alphanumeric")
    if User.objects.filter(username=username).exists():
        raise ValidationError("Username already exists")
    return True


# Define a valid password
