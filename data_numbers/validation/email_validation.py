import re

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

EMAIL_REGEX = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"


def valid_email(email: str) -> bool:
    if User.objects.filter(email=email).exists():
        raise ValidationError("Email already exists")
    elif re.fullmatch(EMAIL_REGEX, email) is None:
        raise ValidationError("Email isn't correct")
    return True
