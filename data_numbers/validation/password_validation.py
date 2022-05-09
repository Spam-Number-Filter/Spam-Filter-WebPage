from django.core.exceptions import ValidationError

MIN_LENGTH_PASSWORD = 6


def valid_password(password: str) -> bool:
    if len(password) < MIN_LENGTH_PASSWORD:
        raise ValidationError("Password must be at least 6 characters long")
    if not any(char.isdigit() for char in password):
        raise ValidationError("Password must contain at least 1 digit")
    return True
