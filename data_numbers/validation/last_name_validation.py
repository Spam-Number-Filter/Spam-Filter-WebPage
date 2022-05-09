import re
from typing import List

from django.core.exceptions import ValidationError

FIRST_NAME_REGEX = "/^[a-z ,.'-]+$/i"
SPACES_REGEX = r"\s"


def valid_last_name(last_name: str) -> bool:
    if _is_a_single_word(last_name):
        return True
    if _are_two_words_separated_by_space(last_name):
        return True
    raise ValidationError("Last name must be alphabetic")


def _is_a_single_word(string: str):
    return not _contains_spaces(string) and string.isalpha()


def _contains_spaces(string: str):
    return re.match(SPACES_REGEX, string) is not None


def _are_two_words_separated_by_space(last_name) -> bool:
    words: List[str] = last_name.split(" ")
    if len(words) != 2:
        return False
    for word in words:
        if not _is_a_single_word(word):
            return False
    return True
