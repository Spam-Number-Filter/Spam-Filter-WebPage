from django.core.exceptions import ValidationError


def valid_first_name(first_name: str) -> bool:
    if not first_name.isalnum():
        raise ValidationError("First name must be alphabetic")
    return True
